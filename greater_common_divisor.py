# Made By Bl4ky

from number_factors import get_factors, get_prime_numbers

def greater_common_divisor_factors(num_arr=[]):
    divisors_arr = []
    prime_numbers = get_prime_numbers(max(num_arr))
    greater_divisor_factors = {prime: [] for prime in prime_numbers}
    greater_divisor = 1

    for num in num_arr:
        num_factor = get_factors([num], prime_numbers, [])
        prime_count = {}

        for prime in prime_numbers:
            prime_count[prime] = 0

            for factor in num_factor:
                if factor == prime:
                    prime_count[prime] += 1

        divisors_arr.append(prime_count)

    for divisors in divisors_arr:
        for prime, count in divisors.items():
            greater_divisor_factors[prime].append(count)

    for factor, values in greater_divisor_factors.items():
        greater_divisor *= (factor ** min(values))

    return greater_divisor

def greater_common_divisor_euclid_sub(data_arr=[]):
    if len(data_arr) > 2:
        return 0

    num_arr = data_arr.copy()
    while num_arr[0] != num_arr[1]:
        num_arr.sort()
        num_arr[1] -= num_arr[0]
        print(num_arr)

    return num_arr[0]

def greater_common_divisor_euclid_mod(data_arr=[]):
    if len(data_arr) > 2:
        return 0

    num_arr = data_arr.copy()
    while num_arr[0] != 0:
        try:
            num_arr.sort()
            num_arr[1] %= num_arr[0]
            print(num_arr)
        except ZeroDivisionError:
            break

    return num_arr[1]

def main():
    nums = [48, 18]

    greater_divisor = greater_common_divisor_euclid_mod(nums)
    print(f"gcd({nums}) = {greater_divisor}")

if __name__ == "__main__":
    main()
