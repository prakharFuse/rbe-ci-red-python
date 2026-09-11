# rbe-ci-red-python (GitHub)

**Journey-suite fixture — deterministically RED CI on `main`** (resolver-core
spec 025 / journey j116). Part of the CI auto-fix language & framework matrix.

- **Do NOT fix `main`** — the red build is the feature, and every journey run
  depends on it. Never merge a fix PR into this repo.
- **On PR branches, automated CI-fix agents ARE expected to make CI pass.**
  The single correct minimal fix lives in `src/cart/pricing.py`: return `amount` unchanged from `apply_surcharge` — there is no surcharge. That
  branch-side fix is exactly the behaviour under test. Fix PRs are declined
  or closed, never merged.
- **Never change the tests or the CI config to go green.** The failing test is
  correct; the source is wrong.

CI config here is deliberately stock — no problem matchers, no annotating
plugins, no machine-readable report formats. The build output is what an
ordinary customer's build output looks like.

Re-provision: `tests/journeys/scripts/provision-ci-red-fixtures.ts`
(`--only=rbe-ci-red-python`).

The failing assertion names `tests/test_cart.py` and nothing else. The defect
is in `src/cart/pricing.py`, two modules away, which the build output never
mentions — the agent has to read the code to find it.

## Status

CI-fix journey canary (mtwm3tmk-72ik).
