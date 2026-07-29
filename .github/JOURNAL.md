## Week 7 — Issue selection

**Issue link:** https://github.com/ascherj/pathreview/issues/106

**Issue title:** Shared test fixture for a sample user profile is missing from `tests/fixtures/`

**Tier:** [x] Tier 1  [ ] Tier 2  [ ] Tier 3

**Problem summary:**
Several integration tests are being skipped because they rely on a shared fixture file, `tests/fixtures/sample_profiles/basic_profile.json`, that no longer exists in the repo. Without it, the tests have no sample data to exercise the profile-parsing and portfolio-review code paths, so that coverage is effectively disabled. A successful fix restores the fixture with a realistic sample portfolio — a GitHub username, a resume, and two repositories — so the dependent integration tests can run again and actually validate the profile ingestion logic in `tests/integration/`.

**Branch name:** test/106-sample-user-profile-fixture

**Setup confirmation:** [x] App runs locally at localhost:5173

**Cohort ledger:** [x] Issue added to cohort ledger

## Week 8 — Reproduction & solution planning

**Reproduction commit link:** https://github.com/VSilva0806/pathreview/commit/f003caad0015b7baec669ff54867b70e7e62b894

**Reproduction summary:**
Ran `make setup` and confirmed `tests/fixtures/sample_profiles/basic_profile.json` (and the whole `tests/fixtures/` directory) does not exist in the repo, on this branch or on upstream `main`/`cohort/su26-start`. Added `tests/integration/test_sample_profile_fixture.py`, which fails with `FileNotFoundError` on the missing fixture path, documenting the reproduction.

**PLAN.md link:** https://github.com/VSilva0806/pathreview/blob/61309a693f56236555394c7a041cddb27d9883b2/PLAN.md

**Walkthrough video (recommended):** [link to your Loom video, ≤2 min — recommended, not graded]

**Blockers or open questions:**
[Anything you're still uncertain about going into Week 9, or leave blank]