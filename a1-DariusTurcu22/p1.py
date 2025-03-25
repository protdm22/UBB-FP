# Solve the problem from the first set here

"""
4. For a given natural number n find the largest natural number written
with the same digits. (e.g. n=3658, m=8653).
"""


def read_nr() -> int:
    """
    Function that prompts the user to enter a natural number n
    :return: natural number
    """
    while True:
        try:
            n = int(input("Enter the natural number n = "))
            if n < 0:
                raise ValueError()
            return n
        except ValueError:
            print("Please enter a natural number")


def to_list(n: int, digits_of_n: list) -> None:
    """
    Function that splits n into its digits and appends them to the list digits_of_n
    :param n: natural number
    :param digits_of_n: list of digits
    :return: none
    """
    while n != 0:
        digits_of_n.append(n % 10)
        n = n // 10


def sort_arr(digits_of_n: list) -> None:
    """
    Function that sorts the list digits_of_n in ascending order
    :param digits_of_n: list of digits
    :return: none
    """
    for i in range(len(digits_of_n) - 1):
        for j in range(i + 1, len(digits_of_n)):
            if digits_of_n[i] < digits_of_n[j]:
                aux = digits_of_n[i]
                digits_of_n[i] = digits_of_n[j]
                digits_of_n[j] = aux


def create_nr(digits_of_n: list) -> int:
    """
    Returns the largest natural number that can be written with the digits of n
    :param digits_of_n: list of digits
    :return: natural number
    """
    max_nr = 0
    for i in range(len(digits_of_n)):
        max_nr = max_nr * 10 + digits_of_n[i]
    return max_nr


def show(n: int) -> None:
    """
    Function that displays the largest natural number that can be written with the digits of n
    :param n: natural number
    :return: none
    """
    print("The largest natural number that can be written with the digits of n is", n)


def main():
    digits_of_n = []
    to_list(read_nr(), digits_of_n)
    sort_arr(digits_of_n)
    show(create_nr(digits_of_n))


main()
