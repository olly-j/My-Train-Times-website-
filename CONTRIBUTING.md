# Contributing To TubeBoard Assets

Read `AGENTS.md` and `docs/README.md`. Select an owner-approved `TB-NNN` Issue
from `olly-j/My-Train-Times`, create a short-lived branch from `origin/main`,
and keep the change limited to that outcome.

Before opening a PR, run:

```sh
git submodule update --init --recursive
scripts/check-assets.sh
```

Visually inspect changed graphics and record dimensions, target surfaces,
product-copy evidence, and accessibility/legal checks in the PR. Link the
central work item with `Relates to olly-j/My-Train-Times#NN`.
