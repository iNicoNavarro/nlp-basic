from nlp_logic.core import *


def test_get_phrases():
    assert 'golden state' in get_phrases("Golden State Warriors")