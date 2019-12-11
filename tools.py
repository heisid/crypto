import math
import sys

def factors(n):
    result = []
    while n % 2 == 0:
        result.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
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
        return n1 # why does it always return None
    gcd(n1-n2, n2)


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
            
    else:
        print("undefined function")
        exit()
