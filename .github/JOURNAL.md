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

**Blockers or open questions:**
Not 100% sure yet what exact JSON shape the ingestion code expects for the fixture — need to check `ingestion/pipeline.py` more closely before finalizing field names. Also, the original "integration tests" the issue refers to don't actually exist in the repo yet, so I'll be writing new ones alongside the fixture rather than just unskipping old ones.

## Week 9 — Solution building & PR submission

### Check-in 1 (mid-week)

**Current progress:**
Restored `basic_profile.json`, shaped to match the real `Profile` model fields (`github_username`, `resume_text`, etc.) rather than arbitrary keys, and updated the reproduction test to assert against that shape. Also wrote a new integration test that runs the fixture through the actual ingestion pipeline to confirm the resume and both repos parse correctly. That covers steps 1–4 from PLAN.md.

**Next steps:**
Run the full test suite and `make check` to confirm nothing else depended on the old fixture shape and that lint/format/typecheck stay clean, then write up and open the PR.

**Blockers:**
None on this issue specifically — `make check`/full suite turned up a pre-existing backlog of ~53 unrelated failing tests elsewhere in the repo, but confirmed those predate this branch and aren't caused by this change.

---

### Check-in 2 (end of week)

**PR link:** [link to your submitted pull request]

**Branch:** [the branch name you worked on, e.g. `fix/123-short-description`]

**What you built:**
[1–3 sentences summarizing what your fix does and how it works]

**Tests added or updated:**
[Which test files did you touch? What do they cover?]

**Self-review confirmation:** [ ] make check passes  [ ] make test-unit passes

**Draft PR feedback received from:** [name or Slack handle, or "none"]