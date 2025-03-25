""""""
import texttable

"""
--- Dynamic Programming ---
5. Maximize the profit when selling a rod of length n. 
The rod can be cut into pieces of integer lengths and pieces can be sold 
individually. The prices are known for each possible length. 
For example, if rod length n = 7, and the price array is 
price = [1, 5, 8, 9, 10, 17, 17] (the price of a piece of length 3 is 8), 
the maximum profit is 18, and is obtained by cutting the rod into 3 pieces, 
two of length two and one of length 3. Display the profit and the length 
of rod sections sold to obtain it.
"""

ROW_OF_HASHES = "#####"


def read_rod_length():
    """
    Function that prompts the user to input the length of a rod
    :return: the length of the rod (natural number)
    """
    return int(input("Enter the length of the rod: "))


def read_list_of_prices_for_each_rod_length(rod_length: int) -> list:
    """
    Function that prompts the user to input the price for each length of the rod
    :param rod_length: the length of the rod (natural number)
    :return: a list of prices for every length of the rod
    """
    list_of_prices_for_each_rod_length = []
    for length in range(1, rod_length + 1):
        while True:
            try:
                price = int(input(f"Enter the price for a piece of rod of length {length}: "))
                list_of_prices_for_each_rod_length.append(price)
                break
            except ValueError:
                print("Please enter a valid value!")
    return list_of_prices_for_each_rod_length


def calculate_maximum_profit_when_selling_a_rod_of_a_given_length_naive_implementation(remaining_rod_length: int,
                                                                                       rod_length_to_sell: int,
                                                                                       list_of_prices_for_each_rod_length: list):
    """
    Function that calculates the maximum profit that can be obtained by selling a rod of a
    given length (recursive implementation)
    :param remaining_rod_length: the length of the rod in the current step of the recursion (natural number)
    :param rod_length_to_sell: the length of the rod currently being sold (natural number)
    :param list_of_prices_for_each_rod_length: a list of prices for each length of rod being sold (list of natural numbers)
    :return: the maximum profit that can be obtained (natural number)
    """
    if rod_length_to_sell == 0 or remaining_rod_length == 0:
        return 0, []
    elif rod_length_to_sell > remaining_rod_length:
        return calculate_maximum_profit_when_selling_a_rod_of_a_given_length_naive_implementation(remaining_rod_length,
                                                                                                  rod_length_to_sell - 1,
                                                                                                  list_of_prices_for_each_rod_length)
    else:
        profit_with_cut, rod_with_cut = calculate_maximum_profit_when_selling_a_rod_of_a_given_length_naive_implementation(
            remaining_rod_length - rod_length_to_sell, rod_length_to_sell - 1, list_of_prices_for_each_rod_length)
        profit_with_cut += list_of_prices_for_each_rod_length[rod_length_to_sell - 1]
        profit_without_cut, rod_without_cut = calculate_maximum_profit_when_selling_a_rod_of_a_given_length_naive_implementation(
            remaining_rod_length, rod_length_to_sell - 1, list_of_prices_for_each_rod_length)
        if profit_with_cut > profit_without_cut:
            return profit_with_cut, rod_with_cut + [rod_length_to_sell]
        else:
            return profit_without_cut, rod_without_cut


def calculate_maximum_profit_when_selling_a_rod_of_a_given_length_dynamic_programming_implementation(
        total_rod_length: int,
        W: list):
    """
    Function that calculates the maximum profit that can be obtained by selling a rod of a
    given length (dynamic programming implementation)
    :param total_rod_length: the initial length of the rod (natural number)
    :param W: a list of prices for each length of rod being sold (list of natural numbers)
    :return: the maximum profit that can be obtained (natural number)
    """
    dp = [[0 for i in range(total_rod_length + 1)] for i in range(total_rod_length + 1)]
    lengths_sold = [[[] for i in range(total_rod_length + 1)] for i in range(total_rod_length + 1)]
    for i in range(1, total_rod_length + 1):
        for j in range(total_rod_length + 1):
            if i <= j:
                if dp[i - 1][j] > dp[i - 1][j - i] + \
                        W[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                    lengths_sold[i][j] = lengths_sold[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - i] + \
                               W[i - 1]
                    lengths_sold[i][j] = lengths_sold[i][j - i] + [i]
            else:
                dp[i][j] = dp[i - 1][j]
                lengths_sold[i][j] = lengths_sold[i][j] = lengths_sold[i - 1][j]

    display_dynamic_programming_table_for_calculating_maximum_profit_when_selling_a_rod(total_rod_length,
                                                                                        dp)
    return dp[total_rod_length][total_rod_length], lengths_sold[total_rod_length][
        total_rod_length]


def display_dynamic_programming_table_for_calculating_maximum_profit_when_selling_a_rod(rod_length: int,
                                                                                        dynamic_programming_table):
    """
    Function that displays the dynamic programming table structure used to determine the
    maximum profit we can obtain by selling a rod with a given length
    :param rod_length: the length of the rod
    :param dynamic_programming_table: the dynamic programming table structure where we can
    find the maximum profit in its bottom-right corner
    :return:
    """
    import texttable
    dynamic_programming_table_to_print = texttable.Texttable()
    dynamic_programming_table_to_print.add_row(['*'] + list(range(rod_length + 1)))
    for i in range(rod_length + 1):
        dynamic_programming_table_to_print.add_row([i] + dynamic_programming_table[i])
    print(f"\n{ROW_OF_HASHES * 10}\nDynamic programming table structure:")
    print(dynamic_programming_table_to_print.draw())
    print(f"{ROW_OF_HASHES * (rod_length + 3)}")


def dynamic_programming_main():
    rod_length = read_rod_length()
    list_of_prices_for_each_rod_length = read_list_of_prices_for_each_rod_length(rod_length)
    maximum_profit_naive, lengths_sold_naive = calculate_maximum_profit_when_selling_a_rod_of_a_given_length_naive_implementation(
        rod_length,
        rod_length,
        list_of_prices_for_each_rod_length)
    maximum_profit_dynamic_programming, lengths_sold_dynamic_programming = calculate_maximum_profit_when_selling_a_rod_of_a_given_length_dynamic_programming_implementation(
        rod_length, list_of_prices_for_each_rod_length)
    print("Maximum profit (naive):", maximum_profit_naive)
    print("Lengths of rod sold (naive):", lengths_sold_naive)
    print("Maximum profit (dynamic):", maximum_profit_dynamic_programming)
    print("Lengths of rod sold (naive):", lengths_sold_dynamic_programming)


dynamic_programming_main()
