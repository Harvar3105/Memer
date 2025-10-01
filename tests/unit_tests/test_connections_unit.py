import pytest
from unittest.mock import AsyncMock, Mock, patch, MagicMock

from services.memer_service import test_all_connections
from repos.r2_service import test_connection as r2_test_connection
from repos.firebase_service import test_connection as fs_test_connection


# ---------------------------
# Mocked R2 Test
# ---------------------------
@pytest.mark.asyncio
async def test_r2_connection_mocked():
  mock_s3 = MagicMock()
  mock_s3.__aenter__.return_value = AsyncMock()
  mock_s3.__aenter__.return_value.list_buckets.return_value = {
    "Buckets": [{"Name": "test-bucket"}]
  }
  with patch("aioboto3.Session.client", return_value=mock_s3):
    result = await r2_test_connection()
    assert result is True


# ---------------------------
# Mocked Firestore Test
# ---------------------------
@pytest.mark.asyncio
async def test_firestore_connection_mocked():
    mock_query = AsyncMock()
    mock_query.get.return_value = [AsyncMock()]

    mock_collection = Mock()
    mock_collection.limit.return_value = mock_query

    mock_client = Mock()
    mock_client.collection.return_value = mock_collection

    with patch("repos.firebase_service.db_client", mock_client):
        from repos.firebase_service import test_connection
        result = await test_connection()
        assert result is True

# ---------------------------
# Mocked All Connections Test
# ---------------------------
@pytest.mark.asyncio
async def test_all_connections_mocked():
  mock_query = AsyncMock()
  mock_query.get.return_value = [AsyncMock()]

  mock_collection = Mock()
  mock_collection.limit.return_value = mock_query

  mock_client = Mock()
  mock_client.collection.return_value = mock_collection

  # R2 mock
  mock_s3 = MagicMock()
  mock_s3.__aenter__.return_value = AsyncMock()
  mock_s3.__aenter__.return_value.list_buckets.return_value = {
    "Buckets": [{"Name": "test-bucket"}]
  }

  with patch("repos.firebase_service.db_client", mock_client), \
      patch("aioboto3.Session.client", return_value=mock_s3):
    result = await test_all_connections()
    assert result is True