---
name: architecture
description: Module and CI dependency graph for this fixture — how tests, cart package, and CI actually connect
type: knowledge
scope: global
updated: '2026-09-11'
captured_sha: e7234c1e984276e0afb5786b17a7d796171b3726
sources:
  - src/cart/__init__.py
  - src/cart/core.py
  - src/cart/pricing.py
  - tests/test_cart.py
  - .github/workflows/ci.yml
  - pyproject.toml
sources_sha256:
  .github/workflows/ci.yml: b60b74a3c6111b22741cb48d2a47aa6b904472b65ad4fda5c3796c21ffd491e1
  pyproject.toml: 0dee78f7369ffd565221bf9323b3a6d083e754b0324ce2cd9e81cc5aa6710164
  src/cart/__init__.py: a34255c0902ee1e2ce5d2d35d67a6de3f9bd5df39bbad8b6fd7c11de12974209
  src/cart/core.py: 7371f66b2a2eda310f4b7d6c3457e5573e9760fd4e77fb024f989bfdee39f476
  src/cart/pricing.py: 73b4c1129c4fbeff550403c5eabdfccd6529058b3f92dc7f7c60374738425c73
  tests/test_cart.py: 727aa0bf1f67c21946acc54b501691d08b0bc1aaa14cae60f1f103b9fd570de1
---

```mermaid
flowchart TD
    CI["ci.yml: pytest job"] -->|pip install pytest; run pytest| PT["pytest\n(pyproject.toml: pythonpath=src, testpaths=tests)"]
    PT --> TEST["tests/test_cart.py"]
    TEST -->|"from cart import total"| INIT["src/cart/__init__.py"]
    INIT -->|re-exports| CORE["src/cart/core.py: total()"]
    CORE -->|"from .pricing import apply_surcharge"| PRICE["src/cart/pricing.py: apply_surcharge()"]
```

Only two runtime modules exist (`core.py`, `pricing.py`); there is no web
server, database, or external service in this repo — it is a single flat
package exercised entirely through `pytest`. The CI workflow
(`.github/workflows/ci.yml`) is deliberately minimal: checkout, set up
Python 3.12, `pip install pytest`, `pytest` — no linting, coverage, or
report-annotation steps, matching the "deliberately stock" claim in
../../README.md.
