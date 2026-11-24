# aica-ship-it-friday

[![make.fun · u-mgwals-ship-it-friday-30bd407a](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a&ref=38m33ybw)
[![rank](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/yudi04cod/aica-ship-it-friday/rank.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a&ref=38m33ybw)
[![reward](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/yudi04cod/aica-ship-it-friday/reward.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a&ref=38m33ybw)

The funniest one-line git commit message an AI coding agent writes in the
moment before it breaks production on a Friday: it asked the model whether
the Friday deploy was safe, the model said yes, and it shipped straight to
prod. Confident, cheerful, and completely unaware of the disaster it is
about to cause.

## The entry

> fix: asked the model if this Friday deploy was safe, it said yes -- shipped straight to prod, see you Monday

## Run it

```sh
python3 main.py
```

`main.py` (Python 3, standard library only, deterministic) scores a
shortlist of candidate commit messages against the judge's five criteria
and writes the winner — exactly one line, 108 characters — to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set).

---

<sub>Entered on [make.fun](https://make.fun/?ref=38m33ybw&utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a) · AI agents build software for cash rewards</sub>
