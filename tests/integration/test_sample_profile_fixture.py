"""Reproduction for #106: shared sample profile fixture is missing.

This test documents the bug reported in issue #106 — integration tests that
exercise profile ingestion depend on `tests/fixtures/sample_profiles/basic_profile.json`,
but that fixture (and the `tests/fixtures/` directory itself) does not exist in the repo.
This test is expected to fail/error until the fixture is restored.
"""

import json
from pathlib import Path

import pytest

FIXTURE_PATH = (
    Path(__file__).resolve().parent.parent
    / "fixtures"
    / "sample_profiles"
    / "basic_profile.json"
)


@pytest.mark.integration
def test_basic_profile_fixture_exists():
    """The shared sample profile fixture should exist for profile-ingestion tests to use."""
    assert FIXTURE_PATH.exists(), (
        f"Missing fixture: {FIXTURE_PATH}. See issue #106 — this file needs to be "
        "restored with a realistic sample portfolio (GitHub username, resume, two repos)."
    )


@pytest.mark.integration
def test_basic_profile_fixture_has_expected_shape():
    """Once restored, the fixture should contain a username, resume, and two repos."""
    data = json.loads(FIXTURE_PATH.read_text())

    assert "github_username" in data
    assert "resume" in data
    assert "repositories" in data
    assert len(data["repositories"]) == 2
