#!/usr/bin/env python3
# Various tools for this crypto toy
# Sid

from math import sqrt
import sys
from collections import Counter

def factors(n):
   result = list()
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

def string_to_ascii(text):
   return [ord(character) for character in text]

def ascii_to_string(ascii_list):
   return ''.join(chr(list_element) for list_element in ascii_list)

def string_to_numcode(text):
   text = string_to_ascii(text)
   # printable ascii range 20 - 126, shift to 0 - 106
   return list(map(lambda char: char - 20, text))

def numcode_to_string(numcode):
    # shift back to ascii code
    numcode = map(lambda char: char + 20, numcode)
    return ascii_to_string(numcode)

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

class NotPrime(Exception):
    def __init__(self, n):
        Exception.__init__(self, "{} is not a prime number".format(n))
        self.n = n

class NotCoprimeError(Exception):
    def __init__(self, n1, n2):
        Exception.__init__(self, "{} and {} are not coprime".format(n1, n2))
        self.n1, self.n2 = n1, n2

def mod_inverse(n, mod):
   if not are_coprime(n, mod):
      raise NotCoprimeError(n, mod)
   phi_of_mod = euler_phi(mod)
   return (n**(phi_of_mod - 1)) % mod

if __name__ == "__main__":
   import argparse
   
   parser = argparse.ArgumentParser(
      description="Various tools, can be imported or used directly"
   )
   subparsers = parser.add_subparsers(
      title="Subcommands"
   )
   subparsers.required = True
   subparsers.dest = "Subcommands"

   parser_factors = subparsers.add_parser("factors",
      help="Giving list of prime factors of a number"
   )
   parser_factors.add_argument("n", type=int, help="number(int)")
   parser_factors.set_defaults(func=factors)

   parser_isprime = subparsers.add_parser("isprime",
      help="Checking if a number is prime"
   )
   parser_isprime.add_argument("n", type=int, help="number(int)")
   parser_isprime.set_defaults(func=is_prime)

   parser_string2ascii = subparsers.add_parser("string_to_ascii",
      help="Converting string to ASCII codes"
   )
   parser_string2ascii.add_argument("text", type=str, 
      help="Text to convert (enclosed in quotes)"
   )
   parser_string2ascii.set_defaults(func=string_to_ascii)

   parser_ascii2string = subparsers.add_parser("ascii_to_string",
      help="Convert ASCII codes into a string"
   )
   parser_ascii2string.add_argument("ascii", type=int, nargs="+",
      help="ASCII codes to convert"
   )
   parser_ascii2string.set_defaults(func=ascii_to_string)

   parser_gcd = subparsers.add_parser("gcd",
      help="Computing GCD / Greater common divisor of two numbers"
   )
   parser_gcd.add_argument("n1", type=int, help="First number(int)")
   parser_gcd.add_argument("n2", type=int, help="Second number(int)")
   parser_gcd.set_defaults(func=gcd)

   parser_arecoprime = subparsers.add_parser("arecoprime",
      help="Check if two numbers are coprime"
   )
   parser_arecoprime.add_argument("n1", type=int, help="First number(int)")
   parser_arecoprime.add_argument("n2", type=int, help="Second number(int)")
   parser_arecoprime.set_defaults(func=are_coprime)

   parser_eulerphi = subparsers.add_parser("eulerphi",
      help="Computing Euler Phi Function of given number"
   )
   parser_eulerphi.add_argument("m", type=int, help="number(int)")
   parser_eulerphi.set_defaults(func=euler_phi)

   parser_modinverse = subparsers.add_parser("modinverse",
      help="Computing modular multiplicative inverse"
   )
   parser_modinverse.add_argument("n", type=int, help="number(int)")
   parser_modinverse.add_argument('mod', type=int, help="modular basis(int)")
   parser_modinverse.set_defaults(func=mod_inverse)

   args = vars(parser.parse_args())
   func = args.pop('func')
   print(func(**args))