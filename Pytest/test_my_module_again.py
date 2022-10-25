from my_module import square
import pytest
@pytest.fixture 
def input_value(): 
    return 4
def test_square_return_int(input_value):
    subject = square(input_value)
    assert isinstance(subject,int)