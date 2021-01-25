from main import add_background
from main import add_colour
from main import center_board_text
from main import sort_numerical_string
from main import password_decoder


def test_add_background():
    """Done by: Ethan Lam"""
    assert add_background("hi", "red") == "\033[0;37;41mhi\033[0;0;0m"
    assert add_background("code", "green") == "\033[0;30;42mcode\033[0;0;0m"
    assert add_background("", "orange") == "\033[0;37;43m\033[0;0;0m"
    assert add_background("Good Morning", "blue") == "\033[0;37;44mGood Morning\033[0;0;0m"
    assert add_background(" ", "red") == "\033[0;37;41m \033[0;0;0m"
    assert add_background("1234567890", "orange") == "\033[0;37;43m1234567890\033[0;0;0m"
    assert add_background("1 + 2", "green") == "\033[0;30;42m1 + 2\033[0;0;0m"
    assert add_background("a/s.d-12=3", "blue") == "\033[0;37;44ma/s.d-12=3\033[0;0;0m"
    assert add_background("a", "red") == "\033[0;37;41ma\033[0;0;0m"
    assert add_background("Green", "green") == "\033[0;30;42mGreen\033[0;0;0m"


def test_add_colour():
    """Done by: Ethan Lam"""
    assert add_colour("", "red", True) == "\033[1;31;1m\033[0;0;0m"
    assert add_colour("Coding_Fun", "green", True) == "\033[1;32;1mCoding_Fun\033[0;0;0m"
    assert add_colour(" ", "orange", True) == "\033[1;33;1m \033[0;0;0m"
    assert add_colour("a/s12-203=129;293", "blue", True) == "\033[1;34;1ma/s12-203=129;293\033[0;0;0m"
    assert add_colour("1", "none", True) == "\033[1;0;1m1\033[0;0;0m"
    assert add_colour("10m", "cyan", True) == "\033[1;36;1m10m\033[0;0;0m"
    assert add_colour("12345", "red", False) == "\033[0;31;1m12345\033[0;0;0m"
    assert add_colour(" test ", "green", False) == "\033[0;32;1m test \033[0;0;0m"
    assert add_colour("hello world", "orange", False) == "\033[0;33;1mhello world\033[0;0;0m"
    assert add_colour("blue", "blue", False) == "\033[0;34;1mblue\033[0;0;0m"
    assert add_colour("[0;0;1m[0;0;0m", "none", False) == "\033[0;0;1m[0;0;1m[0;0;0m\033[0;0;0m"
    assert add_colour("()[]{}<>", "cyan", False) == "\033[0;36;1m()[]{}<>\033[0;0;0m"


def test_center_board_text():
    """Done by: Ethan Lam"""
    assert center_board_text("") == "                                       "
    assert center_board_text("A") == "                   A                   "
    assert center_board_text("        ") == "                                       "
    assert center_board_text("1234567890") == "              1234567890               "
    assert center_board_text("You rolled a 10!") == "           You rolled a 10!            "
    assert center_board_text("'NAME' landed on ABC") == "         'NAME' landed on ABC          "
    assert center_board_text("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890()>") == "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890()>"
    assert center_board_text("->(){}[]<-=+*") == "             ->(){}[]<-=+*             "
    assert center_board_text("center_board_text") == "           center_board_text           "
    assert center_board_text("Ethan Lam") == "               Ethan Lam               "


def test_sort_numerical_string():
    """Done by: Ethan Lam"""
    assert sort_numerical_string("12345") == "12345"
    assert sort_numerical_string("2") == "2"
    assert sort_numerical_string("54321") == "12345"
    assert sort_numerical_string("993224051") == "012234599"
    assert sort_numerical_string("23549863") == "23345689"
    assert sort_numerical_string("12938407632045473808") == "00012233344456778889"


def test_password_decoder():
    """Done by: Ethan Lam"""
    assert password_decoder(12345) == "bcdef"
    assert password_decoder(0) == "a"
    assert password_decoder(265947509138) == "cgfjehfajbdi"
    assert password_decoder(100) == "baa"
    assert password_decoder(5555555555) == "ffffffffff"
    assert password_decoder(90) == "ja"
