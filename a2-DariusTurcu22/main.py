import random


def exponential_search(arr: list, elem: int) -> int:
    """
    Function that uses exponential search to find the index of a natural number elem
    :param arr: list of natural numbers
    :param elem: natural number
    :return: natural number (index)
    """
    size = len(arr)
    if size == 0:
        return -1
    bound = 1
    while bound < size and arr[bound] < elem:
        bound *= 2

    # binary search
    left = bound // 2
    right = min(bound, size - 1)
    while left <= right:
        middle = (left + right) // 2
        if elem == arr[middle]:
            return middle
        elif elem < arr[middle]:
            right = middle - 1
        elif elem > arr[middle]:
            left = middle + 1
    return -1


def ask_for_step() -> int:
    """
    Function that prompts the user to input the parameter step
    :return: natural number
    """
    print("Please enter the value of the parameter step:")
    return read_int()


def check_step(arr: list, step, step_ct, i: int) -> int:
    """
    Function that prints the list arr for every n steps, and increments step_ct otherwise
    :param arr: list of natural numbers
    :param step: natural number
    :param step_ct: natural number
    :param i: natural number
    :return: natural number
    """
    if step_ct != step:
        step_ct += 1
    if step_ct == step:
        print("Step", i, arr)
        step_ct = 0
    return step_ct


def cocktail_sort(arr: list, step: int) -> None:
    """
    Function that uses cocktail sort to sort the list arr in ascending order
    :param step: natural number
    :param arr: list of natural numbers
    :return: None
    """
    bgn = 0
    end = len(arr) - 1
    step_ct = 0
    k = 0
    while bgn <= end:
        new_bgn = end
        new_end = bgn
        for i in range(bgn, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                k += 1
                step_ct = check_step(arr, step, step_ct, k)
            new_end = i
        end = new_end
        for i in range(end, bgn, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                k += 1
                step_ct = check_step(arr, step, step_ct, k)
            new_bgn = i
        bgn = new_bgn


def comb_sort(arr: list, step: int) -> None:
    """
    Function that uses comb sort to sort the list arr in ascending order
    :param step: natural number
    :param arr: list of natural numbers
    :return: None
    """
    length = len(arr)
    gap = length
    shrink = 1.3
    srt = False
    step_ct = 0
    k = 0
    while not srt:
        gap = int(gap // shrink)
        if gap <= 1:
            gap = 1
            srt = True
        elif gap in (9, 10):
            gap = 11
        i = 0
        while i + gap < length:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                srt = False
                k += 1
                step_ct = check_step(arr, step, step_ct, k)
            i += 1


def gen_list_rand_n(arr: list, n: int) -> None:
    """
    Function that generates a list of n random natural numbers
    :param arr: list of natural numbers
    :param n: natural number
    :return: None
    """
    for i in range(n):
        arr.append(random.randint(0, 1000))
    print("The list has been generated successfully!")


def check_sort(arr: list) -> bool:
    """
    Function that checks is a list arr is sorted in ascending order
    :param arr: list of natural numbers
    :return: boolean
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def read_int() -> int:
    """
    Function that returns an input only if it is a natural number
    :return: natural number
    """
    while True:
        try:
            option = int(input(">>> "))
            if option < 0:
                raise ValueError()
            return option
        except ValueError:
            print("Invalid value! Please enter a natural number!")


def print_menu() -> None:
    """
    Function that displays the menu options
    :return: None
    """
    print("####################################################")
    print("Menu options:")
    print("[1] Display the list")
    print("[2] Generate a list of n random natural numbers")
    print("[3] Search for an item in the list")
    print("[4] Sort the list using cocktail sort")
    print("[5] Sort the list using comb sort")
    print("\n[0] Exit")
    print("####################################################")
    print("Choose an option:")


def menu(arr: list) -> None:
    """
    Function that prompts the user to input their desired option and calls that respective function
    :param arr: empty list that the function will work with
    :return: None
    """
    bad_command = False
    while True:
        if bad_command:
            print("Invalid option! Please enter a number between 0 and 5")
            bad_command = False
        else:
            print_menu()
        option = read_int()
        if option == 0:  # Exit
            break
        elif option == 1:  # Show list
            if not arr:
                print("The list is empty. Please consider generating a list!")
            else:
                print(arr)
        elif option == 2:  # Generate list
            print("Please enter the value of n:")
            n = read_int()
            gen_list_rand_n(arr, n)
        elif option == 3:  # Exponential search
            if check_sort(arr):
                print("Please enter the number you would like to search for:")
                nr = read_int()
                index = exponential_search(arr, nr)
                if index == -1:
                    print("The element", nr, "was not found in the list.")
                else:
                    print("The element", nr, "can be found at index", str(index) + ".")
            else:
                print(
                    "The list is not sorted! Please sort the list using option [4] or [5] before searching for an element.")
        elif option == 4:  # Cocktail sort
            step = ask_for_step()
            cocktail_sort(arr, step)
        elif option == 5:  # Comb sort
            step = ask_for_step()
            comb_sort(arr, step)
        else:
            bad_command = True


def main():
    numbers_list = []
    menu(numbers_list)


main()
