"""Build sg-firstnames.txt from philipperemy/name-dataset first-name stats."""
import gzip
import pickle
import re
import sys

OUT = sys.argv[1]
LATIN = re.compile(r"[A-Za-z]+([ -][A-Za-z]+)*")
SOUTH_ASIA = ("IN", "BD", "MV")
GULF = ("AE", "SA", "KW", "OM", "QA", "BH")
SA_MAX, SA_GULF_MAX = 0.2, 0.5

fn = pickle.load(gzip.open("first_names.pkl.gz"))
ln = pickle.load(gzip.open("last_names.pkl.gz"))

def share(v, codes):
    return sum(v["country"].get(c, 0) for c in codes)

def sg_rank(d, name):
    return ((d.get(name) or {}).get("rank") or {}).get("SG")

stats = {"sg": 0, "non_latin": 0, "south_asian": 0, "surname": 0}
kept, dropped_surnames = [], []
for name, v in fn.items():
    f_rank = sg_rank(fn, name)
    if f_rank is None:
        continue
    stats["sg"] += 1
    if not LATIN.fullmatch(name):
        stats["non_latin"] += 1
        continue
    if share(v, SOUTH_ASIA) >= SA_MAX or share(v, SOUTH_ASIA + GULF) >= SA_GULF_MAX:
        stats["south_asian"] += 1
        continue
    l_rank = sg_rank(ln, name)
    if l_rank is not None and l_rank < f_rank:  # more common as an SG surname
        stats["surname"] += 1
        dropped_surnames.append((f_rank, name))
        continue
    kept.append((f_rank, name.lower().replace(" ", "-")))

seen, words = set(), []
for _, w in sorted(kept):  # most popular first
    if w not in seen:
        seen.add(w)
        words.append(w)

with open(OUT, "w") as fh:
    fh.write("\n".join(words) + "\n")

print(stats, "written:", len(words))
print("surnames dropped (top 60):", [n for _, n in sorted(dropped_surnames)[:60]])
print("vocab:", "".join(sorted(set("".join(words)))), len(set("".join(words))) + 1)
