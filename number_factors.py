# Made By Bl4ky

def get_factors(numbers=[], prime_numbers=[], used_factors=[]):
    for prime in prime_numbers:
        add_factor = False

        for i in range(len(numbers)):
            if numbers[i] % prime == 0:
                numbers[i] /= prime 
                add_factor = True

        if add_factor:
            used_factors.append(prime)

    if sum(numbers) == len(numbers):
        return used_factors

    return get_factors(numbers, prime_numbers, used_factors)

def get_prime_numbers(range_numbers=100):
    initial_primes = [2, 3, 5, 7]
    prime_numbers = []

    for i in range(range_numbers + 1):
        is_prime = True

        for prime_number in initial_primes:
            if (i == 1 or i % prime_number == 0) and (i not in initial_primes):
                is_prime = False

        if is_prime:
            prime_numbers.append(i)

    return prime_numbers

def main():
    num = 8
    prime_numbers = get_prime_numbers(num)
    factors = get_factors([num], prime_numbers, [])
    print(prime_numbers)
    print(factors, num)

if __name__ == "__main__":
    main()
