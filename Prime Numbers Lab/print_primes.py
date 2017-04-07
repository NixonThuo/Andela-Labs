def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for n in range(2, x):
            if x % n == 0:
                return False
        return True


def prime_numbers_in_range(max):
    while True:
        try:
            primes = []
            for num in range(max):
                if is_prime(num) is True:
                    primes.append(num)
            return primes
        except (AttributeError, ValueError, TypeError):
            return "invalid"


# print prime_numbers_in_range([])
