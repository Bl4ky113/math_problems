# Made By Bl4ky

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
    factors_arr = [7, 5, 3, 2]
    multiples_factors = multiples

    for factor in factors_arr:
        add_factor = False

        for i in range(len(multiples_factors)):
            if multiples_factors[i] % factor == 0:
                multiples_factors[i] /= factor
                add_factor = True

        if add_factor:
            used_factors.append(factor)

    if sum(multiples_factors) == len(multiples_factors):
        iterations = 1
        for factor in used_factors:
            iterations *= factor
        return iterations

    return least_common_multiple_factors(multiples_factors, used_factors)
