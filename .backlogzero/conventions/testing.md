---
name: testing
description: pytest layout and conventions used by tests/test_cart.py — read before adding or editing tests
type: convention
scope:
  - tests/**
  - src/**
updated: '2026-09-11'
captured_sha: e7234c1e984276e0afb5786b17a7d796171b3726
sources:
  - pyproject.toml
  - tests/test_cart.py
sources_sha256:
  pyproject.toml: 0dee78f7369ffd565221bf9323b3a6d083e754b0324ce2cd9e81cc5aa6710164
  tests/test_cart.py: 727aa0bf1f67c21946acc54b501691d08b0bc1aaa14cae60f1f103b9fd570de1
---

- Tests live under `tests/`, discovered via `testpaths = ["tests"]` in
  `pyproject.toml`; source is resolved via `pythonpath = ["src"]`, so tests
  import the package as `from cart import total`, never with a relative or
  `src.`-prefixed path.
- One behavior per test function, named `test_<behavior>` (see
  `test_total_sums_the_items`, `test_total_of_empty_cart_is_zero`) — each
  covers a distinct equivalence class (non-empty vs. empty input) rather than
  bundling multiple assertions into one function.
- Assertions are exact-value (`== 6`, `== 0`), not loose/containment checks.
- Per ../../README.md and the `src/cart/pricing.py` docstring: test files in
  this repo are fixed points — the failing assertions define correct
  behavior, so new tests should follow the same exact-value style rather than
  being loosened to pass against current (intentionally broken) source.
