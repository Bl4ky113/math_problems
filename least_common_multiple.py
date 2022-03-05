# Made By Bl4ky

from number_factors import get_prime_numbers, get_factors

def least_common_multiple_multiples(multiples=[]):
    iterations = 0
    arr_multiples = multiples.copy()

    while True:
        break_loop = True
        iteration_is_multiple = [False for i in range(len(multiples))]
        iterations += 1

        for i in range(len(arr_multiples)):
            if iterations % arr_multiples[i] == 0:
                iteration_is_multiple[i] = True

        for iteration_multiple in iteration_is_multiple:
            if iteration_multiple == False:
                break_loop = False

        if break_loop:
            return iterations

def least_common_multiple_factors(multiples=[], used_factors=[]):
    primes_arr = get_prime_numbers(max(multiples))
    arr_multples = multiples.copy()
    factors = get_factors(arr_multples, primes_arr, [])
    iterations = 1

    for factor in factors:
        iterations *= factor

    return iterations

def main():
    mutiples_arr = [4, 5, 6]
    least_common_multiple = least_common_multiple_factors(mutiples_arr)

    print(mutiples_arr)
    print(least_common_multiple)

if __name__ == "__main__":
    main()
