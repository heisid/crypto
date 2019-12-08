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

def isprime(n):
   result = False
   if n and (n != 1):
       allfactors = factors(n)
       if len(allfactors) == 1:
           result = True
   return result

def error():
   print("freaking error")
   exit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: %s function_to_call argument(s)" % sys.argv[0])
        exit()
    if sys.argv[1] == "factors":
        try:
            print(factors(int(sys.argv[2])))
        except:
            error()
    elif sys.argv[1] == "isprime":
        try:
            print(isprime(int(sys.argv[2])))
        except:
            error()
    else:
        print("undefined function")
        exit()
