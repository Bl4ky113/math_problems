# Made By Bl4ky

from number_factors import get_prime_numbers, get_factors

def least_common_multiple_multiples(len_numbers=2, multiples=[]):
    iterations = 0

    while True:
        break_loop = True
        iteration_is_multiple = [False for i in range(len_numbers)]
        iterations += 1

        for i in range(len_numbers):
            if iterations % multiples[i] == 0:
                iteration_is_multiple[i] = True

        for iteration_multiple in iteration_is_multiple:
            if iteration_multiple == False:
                break_loop = False

        if iterations > 1000 or break_loop:
            return iterations

def least_common_multiple_factors(multiples=[], used_factors=[]):
    primes_arr = get_prime_numbers(max(multiples))
    factors = get_factors(multiples, primes_arr)
    iterations = 1

    for factor in factors:
        iterations *= factor

    return iterations
