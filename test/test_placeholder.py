from sqlmuggle import hello_word

def test_hello_world_should_return_hello_world():
    assert hello_word() == "hello word"
