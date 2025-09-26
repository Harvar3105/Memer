import pytest
from unittest.mock import AsyncMock, patch

from services.memer_service import test_all_connections
from repos.r2_service import test_connection as r2_test_connection
from repos.firebase_service import test_connection as fs_test_connection


# ---------------------------
# Mocked R2 Test
# ---------------------------
@pytest.mark.asyncio
async def test_r2_connection_mocked():
    with patch("aioboto3.Session.client", new_callable=AsyncMock) as mock_client:
        mock_client.return_value.__aenter__.return_value.list_buckets = AsyncMock(
            return_value={"Buckets": [{"Name": "test-bucket"}]}
        )
        result = await r2_test_connection()
        assert result is True


# ---------------------------
# Mocked Firestore Test
# ---------------------------
def test_firestore_connection_mocked():
    with patch("firebase_admin.firestore.client") as mock_fs:
        mock_doc = mock_fs.return_value.collection.return_value.document.return_value
        mock_doc.get.return_value.exists = True
        mock_doc.get.return_value.to_dict.return_value = {"ping": "pong"}

        result = fs_test_connection()
        assert result is True

# ---------------------------
# Mocked All Connections Test
# ---------------------------
def test_all_connections_mocked():
    with patch("firebase_admin.firestore.client") as mock_fs, patch(
        "aioboto3.Session.client", new_callable=AsyncMock
    ) as mock_client:
        # Mock Firestore
        mock_doc = mock_fs.return_value.collection.return_value.document.return_value
        mock_doc.get.return_value.exists = True
        mock_doc.get.return_value.to_dict.return_value = {"ping": "pong"}

        # Mock R2
        mock_client.return_value.__aenter__.return_value.list_buckets = AsyncMock(
            return_value={"Buckets": [{"Name": "test-bucket"}]}
        )

        result = test_all_connections()
        assert result is True