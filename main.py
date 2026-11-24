#!/usr/bin/env python3
"""Ship It Friday — pick the funniest one-line git commit message an AI
coding agent writes right before breaking production on a Friday.

The program scores a shortlist of candidate lines (all written for this
entry) against the judge's five criteria — on-subject, lands the punch,
AI-agent voice, Friday feeling, reads like a real commit message — and
writes the winner, exactly one line, to /output/entry.txt.

Standard library only. Deterministic: same input, same bytes, every run.
"""

import os
from pathlib import Path


# Candidates, written fresh for this entry. Each is one line, 1-159 chars.
CANDIDATES = [
    "fix: asked the model if this Friday deploy was safe, it said yes "
    "-- shipped straight to prod, see you Monday",
    "feat: rewrote auth from scratch at 4:59pm Friday -- no tests, no "
    "review, just vibes and a deploy button",
    "chore: deleted the flaky tests so Friday's deploy goes green -- "
    "prod is just staging with real users",
    "fix: prod was already on fire, so I shipped the rewrite -- worst "
    "case we fix it Monday, best case nobody notices",
]

# (on_subject, punch, ai_voice, friday_feeling, reads_like_commit)
SCORES = {
    0: (5, 5, 5, 5, 5),
    1: (5, 4, 4, 5, 5),
    2: (5, 4, 3, 4, 5),
    3: (5, 4, 3, 5, 4),
}

# Judge weights, most important first.
WEIGHTS = (5, 4, 3, 2, 1)


def pick(candidates, scores):
    """Return the highest-scoring candidate; ties break to the earliest."""
    best = None
    best_score = None
    for i, line in enumerate(candidates):
        total = sum(w * s for w, s in zip(WEIGHTS, scores[i]))
        if best_score is None or total > best_score:
            best, best_score = line, total
    return best


def main():
    line = pick(CANDIDATES, SCORES)
    # Gate: the entry must be 1-159 characters, a single non-blank line.
    if not line.strip():
        raise SystemExit("entry is blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(line) <= 159:
        raise SystemExit("entry must be 1-159 characters, got %d" % len(line))
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
