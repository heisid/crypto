import math
import sys

def prime_factors(n):
    result = []
    while n % 2 == 0:
        result.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            result.append(i)
            n = n / i

    if n > 2:
        result.append(n)

    return result


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(prime_factors(int(sys.argv[1])))
    else:
        print("argument invalid")

