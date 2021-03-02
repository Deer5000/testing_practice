import pytest
import extract_position as ex_pos



@pytest.fixture
def if_null():
    return None




@pytest.fixture
def if_average():
    return "the positron location is x:21.432"



@pytest.fixture
def if_error():
    return "|ERROR| could not calculate."



def test_ex_pos_null(if_null):
    assert ex_pos.extract_position(if_null) == None


def test_ex_pos_average(if_average):
    ex_pos.extract_position(if_average) == "21.432"


def test_ex_pos_error(if_error):
    ex_pos.extract_position(if_error) == None
