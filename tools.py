from math import sqrt
import sys
from collections import Counter

def factors(n):
    result = []
    while n % 2 == 0:
        result.append(2)
        n = n / 2

    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            result.append(i)
            n = n / i

    if n > 2:
        result.append(int(n))

    return result

def is_prime(n):
   result = False
   if n and (n != 1):
       allfactors = factors(n)
       if len(allfactors) == 1:
           result = True
   return result

def string_to_ascii(string_data):
   return [ord(character) for character in string_data]

def ascii_to_string(ascii_list):
    return ''.join(chr(list_element) for list_element in ascii_list)

def gcd(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1
    if (not n2) or (n1 == n2):
        return n1
    return gcd(n1-n2, n2)

def are_coprime(n1, n2):
    if gcd(n1, n2) == 1:
        return True
    else:
        return False

def euler_phi(m):
    prime_factors = factors(m)
    factors_counter = Counter(prime_factors)
    phi = 1
    for factor,counter in factors_counter.items():
        phi = phi * (factor**counter - factor**(counter-1))
    return phi
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: %s function_to_call argument(s)" % sys.argv[0])
        exit()

    function_todo = sys.argv[1]
    if len(sys.argv) > 2:
        args = sys.argv[2:]

    if function_todo == "factors":
        print(factors(int(args[0])))
    elif function_todo == "isprime":
        print(isprime(int(args[0])))
    elif function_todo == "string_to_ascii":
        print(string_to_ascii(args[0]))
    elif function_todo == "ascii_to_string":
        print(ascii_to_string(map(int, args)))
    elif function_todo == "gcd":
        print(gcd(int(args[0]), int(args[1])))
    elif function_todo == "are_coprime":
        print(are_coprime(int(args[0]), int(args[1])))
    elif function_todo == "euler_phi":
        print(euler_phi(int(args[0])))
            
    else:
        print("undefined function")
        exit()
