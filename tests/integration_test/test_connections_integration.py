import pytest
import os

from services.memer_service import test_all_connections
from repos.r2_service import test_connection as r2_test_connection
from repos.firebase_service import test_connection as fs_test_connection

# ---------------------------
# Optional Integration Tests (real API calls)
# Run only if env var ENABLE_INTEGRATION_TESTS is set
# ---------------------------
@pytest.mark.asyncio
@pytest.mark.skipif(
  not os.getenv("ENABLE_INTEGRATION_TESTS"),
  reason="Integration tests disabled. Set ENABLE_INTEGRATION_TESTS=1 to run.",
)
async def test_r2_connection_real():
  result = await r2_test_connection()
  assert result is True

@pytest.mark.asyncio
@pytest.mark.skipif(
  not os.getenv("ENABLE_INTEGRATION_TESTS"),
  reason="Integration tests disabled. Set ENABLE_INTEGRATION_TESTS=1 to run.",
)
async def test_firestore_connection_real():
  result = await fs_test_connection()
  assert result is True

@pytest.mark.asyncio
@pytest.mark.skipif(
  not os.getenv("ENABLE_INTEGRATION_TESTS"),
  reason="Integration tests disabled. Set ENABLE_INTEGRATION_TESTS=1 to run.",
)
async def test_all_connections_real():
  result = await test_all_connections()
  assert result is True
