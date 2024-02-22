import pytest

from utils import arrs


@pytest.fixture
def tree_elements_array():
    return [1, 2, 3]


@pytest.fixture
def four_elements_array():
    return [1, 2, 3, 4]


@pytest.fixture
def empty_array():
    return []


def test_get(tree_elements_array, empty_array):
    assert arrs.get(tree_elements_array, 1, "test") == 2
    assert arrs.get(empty_array, 0, "test") == "test"


def test_slice(tree_elements_array, four_elements_array, empty_array):
    assert arrs.my_slice(four_elements_array, 1, 3) == [2, 3]
    assert arrs.my_slice(tree_elements_array, 1) == [2, 3]
    assert arrs.my_slice(tree_elements_array, end=2) == [1, 2]
    assert arrs.my_slice(empty_array, 1, 2) == []
