import numpy as np


# Testing
def perfect_numbers(n):
    """
    :param n: number of ordered prime numbers
    :return: list of prime numbers
    """
    # p_numbers = np.array([])
    # p_numbers = np.append(p_numbers, [1,2,3], )
    # print(p_numbers)
    p_numbers = []
    counter = 3
    while len(p_numbers) < n:
        current_factors = []
        for number in range(1, counter-1):
            if counter % number == 0:
                current_factors.append(number)
        if sum(current_factors) == counter:
            p_numbers.append(counter)
        counter += 1
    return p_numbers


print(perfect_numbers(4))


