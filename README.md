# Zero to Genius

A learning project. Working through Andrej Karpathy's
[Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) series, one lecture per
folder, reimplementing the main ideas from scratch rather than copying them down — including the
multilayer perceptron language model of Bengio et al. (2003) in
[`03-makemore-mlp`](03-makemore-mlp).

The notebooks are kept as written: repeated attempts, rebuilds from memory, and questions left in
the comments. That record is the point.

> Bengio, Y., Ducharme, R., Vincent, P., & Jauvin, C. (2003). A Neural Probabilistic Language
> Model. *Journal of Machine Learning Research*, 3, 1137–1155.
> [jmlr.org/papers/v3/bengio03a.html](https://www.jmlr.org/papers/v3/bengio03a.html) ·
> [PDF](https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf)

## Lectures

- [`01-micrograd`](01-micrograd) — building a tiny autograd engine from scratch (Lecture 1)
- [`02-makemore`](02-makemore) — bigram character-level language model, counting and neural net (Lecture 2)
- [`03-makemore-mlp`](03-makemore-mlp) — multilayer perceptron language model, Bengio et al. 2003 (Lecture 3)
- [`04-makemore-batchnorm`](04-makemore-batchnorm) — activations, gradients and batch normalisation (Lecture 4)

> `04-makemore-batchnorm` is the one exception to the one-venv-per-lecture rule below: it needs no
> packages beyond lecture 3's, so it shares the **"Python 3 (makemore-mlp)"** kernel rather than
> carrying its own ~1 GB copy of PyTorch.

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
