def sort_numbers(numbers):
    """
    Sorts a list of numbers.

    Parameters:
        numbers (list): List of numbers.

    Returns:
        list: Sorted list of numbers or a message if sorting isn't possible.

    Examples:
    >>> sort_numbers([3, 1, 2])
    [1, 2, 3]
    >>> sort_numbers([4.5, 15.4, 6, 7, 2])
    [2, 4.5, 6, 7, 15.4]
    >>> sort_numbers([3.14159, 1.618, 2.718])
    [1.618, 2.718, 3.14159]
    >>> sort_numbers([4.5, 15.4, 6, 7, 2, 'text'])
    "Isn't possible to sort"
    >>> sort_numbers([1.1, 2, 3.5, 4.0])
    [1.1, 2, 3.5, 4.0]
    """

    if all(isinstance(num, (int, float)) for num in numbers):
        return sorted(numbers)
    else:
        return "Isn't possible to sort"


# Console interaction
def console_sort():
    input_numbers = input("Enter numbers separated by commas: ")
    try:
        numbers = [float(num) for num in input_numbers.split(",")]
        result = sort_numbers(numbers)
        print(result)
    except ValueError:
        print("Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    console_sort()
