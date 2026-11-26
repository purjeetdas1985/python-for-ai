"""Streamlit app: generate a recipe from fridge ingredients via OpenRouter.

Run:  streamlit run 04_call_llm/recipe.py
"""
import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
CUISINES = ["Mediterranean", "Italian", "Indian", "Mexican", "Chinese", "Thai", "French", "American"]

PROMPT_TEMPLATE = """
You are a chef. I will give you a list of ingredients I have in my fridge and the cuisine I like,
and you will give me a recipe I can make with those ingredients.
You will not give me any other information other than the recipe.
The ingredients are: {ingredients}
Cuisine type is: {cuisine_type}
The recipe should be in the following format:

Recipe Name:
Ingredients:
Instructions:

If you understand, please respond with the recipe.
"""

st.set_page_config(page_title="Fridge Chef", page_icon="🍳")
st.title("🍳 Fridge Chef")
st.caption("Tell me what's in your fridge and I'll suggest a recipe.")

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    st.error("OPENROUTER_API_KEY is not set. Add it to your .env file.")
    st.stop()

with st.sidebar:
    st.header("Settings")
    model = st.text_input("Model", value="openrouter/auto")

ingredients = st.text_area(
    "Ingredients (comma separated)",
    value="chicken, garlic, olive oil, lemon, rosemary",
)
cuisine_type = st.selectbox("Cuisine", CUISINES)

if st.button("Get recipe", type="primary"):
    if not ingredients.strip():
        st.warning("Please enter at least one ingredient.")
    else:
        client = OpenAI(base_url=OPENROUTER_BASE_URL, api_key=api_key)
        prompt = PROMPT_TEMPLATE.format(ingredients=ingredients, cuisine_type=cuisine_type)
        try:
            with st.spinner("Cooking up something..."):
                resp = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                )
            if resp.choices and resp.choices[0].message:
                st.markdown(resp.choices[0].message.content)
            else:
                st.warning("The model returned no content.")
        except Exception as e:
            st.error(f"Error: {e}")
