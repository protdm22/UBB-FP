# Solve the problem from the second set here

"""
9. Consider a given natural number n. Determine the product p
of all the proper factors of n.
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


def calc_prod(n) -> int:
    """
    Function that calculates the product of all proper factors of n
    :param n: natural number
    :return: natural number
    """
    p = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            p *= i
    return p


def show(p: int) -> None:
    """
    Function that displays the product of all the proper factors of n
    :param p: natural number
    :return: none
    """
    print("The product of all the proper factors of n is", p)


def main():
    show(calc_prod(read_nr()))


main()
