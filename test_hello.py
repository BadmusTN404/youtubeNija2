from hello import more_hello, more_nothingham


def test_more_hello():
    assert "hi" == more_hello()


def test_more_nothingham():
    assert "nothing" == more_nothingham()
