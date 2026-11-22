# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

A study project for learning the Python constructs needed for AI work (basics first: data types, collections, loops, functions). It is learning material, not a deployable application — there is no build system, test suite, linter, or package manifest.

## Layout

- Numbered topic folders (e.g. `01_data_types_functions/`) each hold Jupyter notebooks. Add new topics as the next number (`02_...`).
- Notebooks are self-contained and progressive: each cell introduces one construct, using the same running example (revenue/expense → profit/margin) re-expressed with different structures (variables → lists → dicts → tuples). Keep that style when adding cells: a short markdown-style heading, then minimal runnable code.
- Note: in the existing notebook, the heading lines (`## ...`) are inside *code* cells, not markdown cells. Prefer real markdown cells for new content.

## Environment

- `.venv/` at the repo root (Python 3.14) with Jupyter/ipykernel installed. It is untracked-by-intent tooling; don't edit it.
- Activate and launch:
  ```
  source .venv/bin/activate
  jupyter lab        # or open notebooks in VS Code using the .venv kernel
  ```
- Run a notebook headlessly: `jupyter nbconvert --to notebook --execute <path>.ipynb --output-dir <tmpdir>` (avoids writing outputs back into the tracked file).
- No dependencies file exists yet; if you install new packages (numpy, pandas, etc.), record them in a `requirements.txt`.
