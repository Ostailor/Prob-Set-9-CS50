from final_project import color_word, check_valid, answer_check


def test_color_word():
    # the answer to the unit test is cryptic because this is the return value but when you print it, it changes the
    # color of characters.
    assert color_word('Hello', 'Stall') == '\x1b[37mS \x1b[37mt \x1b[37ma \x1b[32ml \x1b[33ml '


def test_check_valid():
    assert check_valid('cccio') == 'Not a valid 5 letter word'


def test_answer_check():
    assert answer_check('Hello', 'Hello') == True
    assert answer_check('Stall', 'Hello') == False
