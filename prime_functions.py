import math


def is_prime(n: int) -> bool:
    """Check if integer n is prime."""
    prime_bool = True
    if not n <= 1:
        if not n == 2:
            for i in range(2, math.ceil(n/2)+1):
                if n % i == 0:
                    prime_bool = False
                    break
    else:
        prime_bool = False
    return prime_bool


def find_primes_below(n: int) -> list:
    """Find all primes less than or equal to a number n and return as a list."""
    # Sieve of Eratosthenes
    primes = [True]*n
    primes[0] = False

    for i, val in enumerate(primes, start=1):
        if val:
            for nval in range(i*i, n+1, i):
                primes[nval-1] = False
    primes = [i for i, val in enumerate(primes, start=1) if val]
    return primes


def find_prime_factors(n: int) -> list:
    """Find all prime factors of an integer n and return as a list."""
    factors = []
    if not n <= 1:
        while n % 2 == 0:
            if 2 not in factors:
                factors.append(2)
            n = int(n/2)
        for i in range(3, math.ceil(math.sqrt(n))+1, 2):
            # print(n,i)
            if n % i == 0:
                factors.append(i)
                n = n / i
    return factors

def generate_primes(n):
    """Generate and return list of n consecutive primes."""
    return primes