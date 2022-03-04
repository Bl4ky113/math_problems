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

def greater_common_divisor_euclid_sub():
    pass

def greater_common_divisor_euclid_mod():
    pass

def main():
    nums = [18, 48]

    greater_divisor = greater_common_divisor_factors(nums)
    print(f"gcd({nums}) = {greater_divisor}")

if __name__ == "__main__":
    main()
