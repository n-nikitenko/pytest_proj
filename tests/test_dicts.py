import pytest

from utils.dicts import get_val


@pytest.fixture
def collection():
    return {"one": 1, "two": 2, "three": 3}


def test_get_val(collection):
    assert get_val(collection, "one") == 1
    assert get_val(collection, "four", 4) == 4
