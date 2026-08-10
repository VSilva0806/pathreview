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

**PR link:** https://github.com/VSilva0806/pathreview/pull/1

**Branch:** test/106-sample-user-profile-fixture

**What you built:**
Restored `tests/fixtures/sample_profiles/basic_profile.json`, shaped to match the real `Profile` model fields with a realistic GitHub username, markdown resume, and two distinct repositories. Added an integration test that runs the fixture through the actual `IngestionPipeline` to confirm the resume and both repos parse and embed correctly.

**Tests added or updated:**
Updated `tests/integration/test_sample_profile_fixture.py` to assert the fixture's real shape instead of just checking existence, and added `tests/integration/test_profile_ingestion.py` to exercise `ingest_resume` and `ingest_repo_metadata` against it.

**Self-review confirmation:** [x] make check passes  [x] make test-unit passes

**Draft PR feedback received from:** None

### Reflection

**What was harder than you expected?**
Figuring out the fixture's exact JSON shape was harder than expected — the issue referenced tests and fields that no longer existed, so I had to reverse-engineer the shape from the `Profile` model instead of copying an existing pattern.

**What did you learn about working in a large codebase?**
I learned to verify assumptions against the actual model/pipeline code rather than trusting what an issue description implies exists, since the "integration tests" it referenced turned out not to be there at all.

**How did AI tools help — and where did they fall short?**
AI was most useful for quickly tracing how fixture fields flow through the ingestion pipeline and drafting the fixture/tests; I still had to manually verify field names against the real model code before trusting the output.

**What would you do differently if you started over?**
I'd check `ingestion/pipeline.py` and the model definitions before writing the reproduction test, so the first version already targets the real fixture shape instead of needing a follow-up revision.

**What are you most proud of from this module?**
I am proud of contributing to a repo for the first time.
