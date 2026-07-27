## Week 7 — Issue selection

**Issue link:** https://github.com/ascherj/pathreview/issues/106

**Issue title:** Shared test fixture for a sample user profile is missing from `tests/fixtures/`

**Tier:** [x] Tier 1  [ ] Tier 2  [ ] Tier 3

**Problem summary:**
Several integration tests are being skipped because they rely on a shared fixture file, `tests/fixtures/sample_profiles/basic_profile.json`, that no longer exists in the repo. Without it, the tests have no sample data to exercise the profile-parsing and portfolio-review code paths, so that coverage is effectively disabled. A successful fix restores the fixture with a realistic sample portfolio — a GitHub username, a resume, and two repositories — so the dependent integration tests can run again and actually validate the profile ingestion logic in `tests/integration/`.

**Branch name:** test/106-sample-user-profile-fixture

**Setup confirmation:** [x] App runs locally at localhost:5173

**Cohort ledger:** [x] Issue added to cohort ledger
