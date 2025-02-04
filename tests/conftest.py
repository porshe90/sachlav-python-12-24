import pytest
from source.accum import Accumulator

@pytest.fixture
def global_accum():
    return Accumulator()