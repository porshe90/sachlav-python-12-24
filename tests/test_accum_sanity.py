from source.accum import Accumulator
from assertpy import assert_that
import pytest

@pytest.fixture
def accum():
    return Accumulator()

@pytest.fixture
def accum_1():
    return Accumulator(1)

def test_create_accum(accum):
    assert_that(accum.count).is_equal_to(0)

@pytest.mark.regression
def test_create_accum_with_arg(accum_1):
    assert_that(accum_1.count).is_equal_to(1)

@pytest.mark.sanity
@pytest.mark.regression
def test_create_accum_with_adding(accum):
    accum.add_counts(5)
    # assert accum.count == 4
    assert_that(accum.count).is_equal_to(5)
    assert_that(accum.count == 5).is_true()
