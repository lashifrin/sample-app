def print_array(data: typ.Iterable) -> None:
    """
    Loops through an iterable and prints each element.

    Args:
        data (typing.Iterable): The iterable to loop through and print.
    """

    if not isinstance(data, (list, tuple)):
        raise ValueError(ARRAY_ERROR_MSG)

    for element in data:
        print(element)

if __name__ == "__main__":
    # Example usage
    numbers = [1, 2, 3, 4, 5]
    print_array(numbers)