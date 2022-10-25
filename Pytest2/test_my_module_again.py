from my_module import square
import pytest

@pytest.mark.parametrize('inputs',[2,3,4])
def test_square_return_int(inputs):
    subject=square(inputs)
    assert isinstance(subject,int)