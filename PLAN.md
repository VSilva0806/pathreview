# Solution plan

**Issue:** [Shared test fixture for a sample user profile is missing from `tests/fixtures/`](https://github.com/ascherj/pathreview/issues/106)

### Understand
The `tests/fixtures/sample_profiles/basic_profile.json` file (and the whole `fixtures/` folder) got deleted at some point, so any test that needs sample profile data has nothing to load. Expected: the file exists with realistic data and tests can read it. Actual: the file is missing, so profile-ingestion tests can't run.

### Map
Mainly a new file: `tests/fixtures/sample_profiles/basic_profile.json`. It'll be read by `tests/integration/test_sample_profile_fixture.py` (added during reproduction) and by whatever new integration test(s) exercise `core/services/profile_service.py` and `core/models/profile.py`, since those define what a profile actually looks like (github username, resume text, portfolio url).

### Plan
1. Create the `tests/fixtures/sample_profiles/` folder and add `basic_profile.json` with a realistic sample: a GitHub username, resume text, and two repositories.
2. Match the JSON shape to the real `Profile` model fields so it's actually usable (`github_username`, `resume_text`, etc.), not just arbitrary keys.
3. Update `tests/integration/test_sample_profile_fixture.py` so it checks the fixture's real shape instead of just "does it exist."
4. Write an integration test that loads the fixture and runs it through profile ingestion, confirming the two repos and resume are parsed correctly.
5. Run the full test suite to make sure nothing else was relying on the old fixture in a different shape.

### Inputs & outputs
Input: none at runtime — it's a static JSON fixture file used only by tests. Output: a valid `basic_profile.json` that tests can load and parse without errors, unblocking the previously-skipped integration coverage.

### Edge cases
Make sure the two repos have slightly different data (not just copy-pasted) so parsing logic that handles multiple repos actually gets exercised, and keep the resume text realistic enough to hit normal resume-parsing code paths (sections like Experience/Skills/Education).

### Risks & unknowns
Not fully sure yet what exact JSON shape the ingestion pipeline expects — need to check `ingestion/pipeline.py` and `core/services/profile_service.py` a bit closer before finalizing field names. Also unclear if this fixture should match an existing API schema (`api/schemas/review.py`) or just be a plain test fixture.
