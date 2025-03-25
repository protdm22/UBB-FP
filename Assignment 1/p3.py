# Solve the problem from the third set here

"""
14. Determine the n-th element of the sequence 1,2,3,2,2,5,2,2,3,3,3,7,2,2,3,3,3,...
obtained from the sequence of natural numbers by replacing composed numbers with
their prime divisors, each divisor d being written d times, without memorizing
the elements of the sequence.
the elements of the sequence.
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


def seq_space(n) -> int:
    """
    Function that returns the space n occupies in the sequence
    :param n: natural number
    :return: natural number
    """
    if n <= 3:
        return 1
    d = 2
    ct = 0
    m = n
    while n != 1 and d <= m // 2:
        if n % d == 0:
            ct += d
            while n % d == 0:
                n /= d
        d += 1
    if ct == 0:
        ct = 1
    return ct


def check_nr(n) -> list:
    """
    Function that returns a composed/prime number,
    whose divisor is situated on the n-th position of the sequence
    :param n: natural number
    :return: list of two natural numbers
    """
    nr = 0
    prev_n = n
    while n > 0:
        nr += 1
        prev_n = n
        n -= seq_space(nr)
    return [nr, prev_n]


def prime(n) -> bool:
    """
    Function that evaluates if n is prime or not (1 is also considered a prime number in this case)
    :param n: natural number
    :return: boolean (true or false)
    """
    if n != 2 and n % 2 == 0:
        return False
    for i in range(3, n // 2 + 1, 2):
        if n % i == 0:
            return False
    return True


def nth_elem(nr, init_n) -> int:
    """
    Function that returns the n-th element of the sequence
    :param nr:
    :param init_n:
    :return:
    """
    if prime(nr):
        return nr
    d = 2
    aux = nr
    while nr != 1 and d <= aux // 2:
        if nr % d == 0:
            init_n -= d
            if init_n <= 0:
                return d
            while nr % d == 0:
                nr /= d
        d += 1


def show(n, x: int) -> None:
    """
    Function that displays the n-th element of the sequence
    :param n: natural number
    :param x: natural number
    :return: none
    """
    if n % 10 == 1 and n % 100 // 10 != 1:
        print("The", str(n) + "st element of the sequence is", x)
    elif n % 10 == 2 and n % 100 // 10 != 1:
        print("The", str(n) + "nd element of the sequence is", x)
    elif n % 10 == 3 and n % 100 // 10 != 1:
        print("The", str(n) + "rd element of the sequence is", x)
    else:
        print("The", str(n) + "th element of the sequence is", x)


def main():
    n = read_nr()
    tmp_list = check_nr(n)
    show(n, nth_elem(tmp_list[0], tmp_list[1]))


main()
