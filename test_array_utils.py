def test_print_array_with_list():
    """
    Test print_array function with a valid list input.
    """
    numbers = [1, 2, 3, 4, 5]
    print_array(numbers)
    assert numbers == [1, 2, 3, 4, 5]

def test_print_array_with_tuple():
    """
    Test print_array function with a valid tuple input.
    """
    numbers = (1, 2, 3, 4, 5)
    print_array(numbers)
    assert list(numbers) == [1, 2, 3, 4, 5]

def test_print_array_with_empty_list():
    """
    Test print_array function with an empty list input.
    """
    empty_list = []
    with pytest.raises(ValueError, match=ARRAY_ERROR_MSG):
        print_array(empty_list)

def test_print_array_with_string():
    """
    Test print_array function with a string input (non-iterable).
    """
    string = "This is a string."
    with pytest.raises(ValueError, match=ARRAY_ERROR_MSG):
        print_array(string)

def test_print_array_with_dict():
    """
    Test print_array function with a dictionary input (not an iterable).
    """
    data = {"a": 1, "b": 2}
    with pytest.raises(ValueError, match=ARRAY_ERROR_MSG):
        print_array(data)