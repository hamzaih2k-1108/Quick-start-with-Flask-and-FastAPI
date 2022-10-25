from my_module import square
#print(square(3))
def test_square_gives_correct_value():
    subject= square(2)
    assert subject == 4