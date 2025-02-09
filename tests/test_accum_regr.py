from source.accum import Accumulator
from assertpy import assert_that
import pytest

@pytest.fixture
def accum():
    return Accumulator()

@pytest.mark.regression
def test_create_accum(accum):
    print(f"{accum.count = }")
    assert_that(accum.count).is_equal_to(0)

@pytest.mark.sanity
def test_create_accum_with_arg(global_accum):
    global_accum.add_counts(1)
    assert_that(global_accum.count).is_equal_to(1)

@pytest.mark.regression
def test_create_accum_with_adding(accum):
    accum.add_counts(5)
    # assert accum.count == 4
    assert_that(accum.count).is_equal_to(5)
    assert_that(accum.count == 5).is_true()

@pytest.mark.sanity
def test_create_accum_with_true(accum):
    assert True == True
