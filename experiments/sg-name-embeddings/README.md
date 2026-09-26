# SG name embeddings

Side project spun off from karparthy's zero to hero leson 4  (`04-makemore-batchnorm`). I present a small makemore-style MLP trained on Singaporean first names, with 3D character embeddings so the results can be looked at directly:

1. **P(name)** — log-probability the model assigns to my and my friends' names.
2. **Name vectors** — sum each name's character embeddings, normalise onto the unit sphere, compare with cosine similarity, and trace the path each name takes as its characters are added (interactive plotly view). It dosent mean anything but its just nice to think that ur name is close to someone elses ()

## Files

| File | What it is |
|---|---|
| `sg-name-embeddings.ipynb` | The experiment notebook (kernel: `makemore-mlp`, needs `torch`, `matplotlib`, `plotly`). |
| `sg-firstnames.txt` | 7,172 Singaporean first names, lowercase, one per line, most popular first. Vocab: `a-z` + `-` (+ `.` as start/end token = 28). |
| `build_sg_firstnames.py` | Script that produced `sg-firstnames.txt`. |

## How `sg-firstnames.txt` was built

Source: the aggregated first/last-name statistics shipped with [philipperemy/name-dataset](https://github.com/philipperemy/name-dataset) (`names_dataset/v3/first_names.pkl.gz` and `last_names.pkl.gz`). Note that dataset was derived from the 2021 Facebook leak; only its per-name aggregate statistics (country share, gender share, popularity rank) are used here, not individual records.

Filters, in order:

1. Names with a Singapore (`SG`) popularity rank — 14,096.
2. Latin letters only (a-z, words separated by a space or dash).
3. Drop South Asian names: share in IN/BD/MV ≥ 0.2, or share in IN/BD/MV + Gulf states (AE/SA/KW/OM/QA/BH) ≥ 0.5.
4. Drop names that rank higher as an SG **surname** than as an SG first name (Tan, Lim, Lee, …), since many people entered names surname-first.
5. Lowercase, spaces → `-` (`wei jie` → `wei-jie`), dedupe, sort by SG first-name rank.

Both filters are statistical, so a few names are misclassified either way (e.g. `yi`, `ying`, `hui` were dropped as surnames).

To rebuild just run:

```bash
curl -sLO https://github.com/philipperemy/name-dataset/raw/master/names_dataset/v3/first_names.pkl.gz
curl -sLO https://github.com/philipperemy/name-dataset/raw/master/names_dataset/v3/last_names.pkl.gz
python3 build_sg_firstnames.py sg-firstnames.txt
```
