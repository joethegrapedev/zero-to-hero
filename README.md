# Zero to Genius

Following Andrej Karpathy's [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) series, one lecture per folder.

## Lectures

- [`01-micrograd`](01-micrograd) — building a tiny autograd engine from scratch (Lecture 1)

## Setup (already done for 01-micrograd)

Each lecture folder is a self-contained project with its own virtual environment.

Prerequisites (installed once, machine-wide):

```bash
brew install python graphviz git
```

## Starting work on a lecture

```bash
cd 01-micrograd
source .venv/bin/activate
jupyter lab micrograd.ipynb
```

In VS Code: open the folder, open `micrograd.ipynb`, and select the **"Python 3 (micrograd)"** kernel in the top-right.

To confirm the environment is healthy:

```bash
dot -V              # Graphviz binary
python3 --version   # should match the venv's Python
jupyter --version
```

## Continuing work later

```bash
cd 01-micrograd
source .venv/bin/activate
jupyter lab
```

Your virtual environment (`.venv/`) persists between sessions — no need to reinstall packages unless `requirements.txt` changes.

## Adding a new lecture

```bash
mkdir 02-<lecture-name>
cd 02-<lecture-name>
python3 -m venv .venv
source .venv/bin/activate
pip install notebook jupyterlab graphviz matplotlib numpy
python3 -m ipykernel install --user --name=<lecture-name> --display-name "Python 3 (<lecture-name>)"
pip freeze > requirements.txt
```

## Recreating an environment from scratch

If `.venv/` is deleted or you're on a new machine:

```bash
cd 01-micrograd
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Notes

- `.venv/` is git-ignored — each project's dependencies are isolated and reproducible via `requirements.txt`, not committed as binaries.
- One virtual environment per lecture folder keeps dependencies from clashing as the series moves from micrograd to more complex projects.
