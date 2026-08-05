"""Integration test for #106: run the restored sample profile fixture through
the real ingestion pipeline.

Loads `tests/fixtures/sample_profiles/basic_profile.json` and feeds its resume
text and two repositories through `IngestionPipeline`, confirming they're
parsed, chunked, and embedded without errors.
"""

import json
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from ingestion.embeddings.provider import MockEmbeddingProvider
from ingestion.pipeline import IngestionPipeline

FIXTURE_PATH = (
    Path(__file__).resolve().parent.parent / "fixtures" / "sample_profiles" / "basic_profile.json"
)


@pytest.fixture
def profile_fixture() -> dict:
    return json.loads(FIXTURE_PATH.read_text())


@pytest.fixture
def pipeline() -> IngestionPipeline:
    db_session = MagicMock()
    # Ensure the pipeline's "already ingested?" check treats everything as new.
    db_session.query.return_value.filter_by.return_value.first.return_value = None

    return IngestionPipeline(
        vector_db=MagicMock(),
        db_session=db_session,
        embedding_provider=MockEmbeddingProvider(),
    )


def _stored_documents(pipeline: IngestionPipeline) -> str:
    """Concatenate every document string the pipeline stored in the vector DB."""
    return "\n".join(call.kwargs["documents"][0] for call in pipeline.vector_db.add.call_args_list)


@pytest.mark.integration
def test_ingest_resume_from_fixture(pipeline, profile_fixture):
    result = pipeline.ingest_resume(
        profile_id="profile-106",
        content=profile_fixture["resume_text"],
        filename=profile_fixture["resume_filename"],
    )

    assert not result.skipped
    assert result.chunk_count > 0

    stored = _stored_documents(pipeline)
    assert "Jane Doe" in stored
    assert "Northwind Systems" in stored


@pytest.mark.integration
def test_ingest_repositories_from_fixture(pipeline, profile_fixture):
    repos = profile_fixture["repositories"]
    assert len(repos) == 2

    results = [
        pipeline.ingest_repo_metadata(profile_id="profile-106", repo_data=repo) for repo in repos
    ]

    for result in results:
        assert not result.skipped
        assert result.chunk_count > 0

    stored = _stored_documents(pipeline)
    for repo in repos:
        assert f"Repository: {repo['name']}" in stored
        assert f"Language: {repo['language']}" in stored
