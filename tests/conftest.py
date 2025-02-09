import pytest
from source.accum import Accumulator

@pytest.fixture
def global_accum():
    return Accumulator()

@pytest.fixture(scope="session")
def global_accum_scope():
    return Accumulator()

