---
name: fixture-invariant
description: The main-stays-red / PR-branch-fixes workflow rule for this repo — read before opening or merging any PR here
type: convention
scope: global
updated: '2026-09-11'
captured_sha: e7234c1e984276e0afb5786b17a7d796171b3726
sources:
  - README.md
  - src/cart/pricing.py
sources_sha256:
  README.md: 85eb6952e7c17ada83da7e9520b3a457f570fff99b535157fff89e60b4340069
  src/cart/pricing.py: 73b4c1129c4fbeff550403c5eabdfccd6529058b3f92dc7f7c60374738425c73
---

The core workflow rule is already stated correctly in ../../README.md and in
the docstring at `src/cart/pricing.py:1`: `main` must stay red, PR branches
are expected to fix `apply_surcharge()` to return `amount` unchanged, and fix
PRs are never merged back into `main`. This page only adds the parts those
sources leave implicit.

## What "the fix" concretely touches

The minimal fix is a one-line change inside the function body at
`src/cart/pricing.py:11-13`: change `return amount + 1` to `return amount`.
Nothing else in the repo needs to change for both tests in
`tests/test_cart.py` to pass — `core.py`, `__init__.py`, the test file, and
`.github/workflows/ci.yml` are all correct as-is and out of scope for the fix.

## Applying this rule

- On `main`: never apply the fix above, never edit tests or CI config to mask
  the red build.
- On any other branch/PR: applying the one-line fix is the expected,
  correct action for an automated CI-fix agent — it is not a violation of
  the "don't touch tests/CI" rule, since it only changes `pricing.py`.
