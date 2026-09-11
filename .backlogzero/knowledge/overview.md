---
name: overview
description: What this repo is and why main is deliberately red — read before touching src/cart or tests
type: knowledge
scope: global
updated: '2026-09-11'
captured_sha: e7234c1e984276e0afb5786b17a7d796171b3726
sources:
  - README.md
  - pyproject.toml
  - src/cart/core.py
  - src/cart/pricing.py
  - tests/test_cart.py
sources_sha256:
  README.md: 85eb6952e7c17ada83da7e9520b3a457f570fff99b535157fff89e60b4340069
  pyproject.toml: 0dee78f7369ffd565221bf9323b3a6d083e754b0324ce2cd9e81cc5aa6710164
  src/cart/core.py: 7371f66b2a2eda310f4b7d6c3457e5573e9760fd4e77fb024f989bfdee39f476
  src/cart/pricing.py: 73b4c1129c4fbeff550403c5eabdfccd6529058b3f92dc7f7c60374738425c73
  tests/test_cart.py: 727aa0bf1f67c21946acc54b501691d08b0bc1aaa14cae60f1f103b9fd570de1
---

This repo is a **journey-test fixture**, not a product. Its purpose, the
non-fixable-on-main rule, and the intended branch-side fix are already stated
correctly in ../../README.md and in the module docstring at
`src/cart/pricing.py:1`. Read those first; this page only adds what they
don't spell out.

## Derived: the exact failure on `main`

`total()` (`src/cart/core.py:6`) sums items and pipes the result through
`apply_surcharge()` (`src/cart/pricing.py:11`), which adds a flat `+1`.
Given the fixture's tests (`tests/test_cart.py`):

- `total([1, 2, 3])` → `6 + 1 = 7`, but the test asserts `== 6` → fails.
- `total([])` → `0 + 1 = 1`, but the test asserts `== 0` → fails.

Both `pytest` cases fail on `main` for the same root cause (the `+1` in
`apply_surcharge`), not two independent defects.

## Package shape

- `src/` layout: `pyproject.toml` sets `pythonpath = ["src"]` and
  `testpaths = ["tests"]`, so tests import via the installed-on-path `cart`
  package, not a relative path.
- `src/cart/__init__.py` re-exports only `total` (`__all__ = ["total"]`).
  `apply_surcharge` is intentionally not part of the public package API —
  tests exercise it only indirectly through `total`.

## What NOT to modify here

- `tests/test_cart.py` and `.github/workflows/ci.yml` — the README and the
  `pricing.py` docstring both say these must never change to force green.
- `src/cart/pricing.py`'s docstring language — it's part of the fixture's
  self-documentation for CI-fix agents, not incidental commentary.
