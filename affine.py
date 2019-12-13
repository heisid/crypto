#!/usr/bin/env python3

import sys
import tools
import argparse 

def generate_possible_a_keys(mod):
   a_keys = list()
   for element in range(mod):
      if tools.are_coprime(element, mod):
         a_keys.append(element)
   return a_keys

def encrypt(plain_list, a_key, b_key, mod):
   if not tools.are_coprime(a_key, mod):
      raise tools.NotCoprimeError
   if b_key > mod:
      raise "Invalid b key"
   cipher_list = [((a_key*char + b_key) % mod) for char in plain_list]
   return cipher_list

def decrypt(cipher_list, a_key, b_key, mod):
   a_inverse = tools.mod_inverse(a_key,mod)
   plain_list = [((a_inverse * (char - b_key)) % mod) for char in cipher_list]
   return plain_list

def encrypt_text(plaintext, a_key, b_key):
   # printable ascii range 20 - 126
   # so we need 126 - 20 + 1 = mod 107
   # 107 is prime, don't worry about inverse existence
   mod = 107
   plaintext = tools.string_to_numcode(plaintext)
   ciphertext = encrypt(plaintext, a_key, b_key, mod)
   return tools.numcode_to_string(ciphertext)

def decrypt_text(ciphertext, a_key, b_key):
   ciphertext = tools.string_to_numcode(ciphertext)
   mod = 107
   plaintext = decrypt(ciphertext, a_key, b_key, mod)
   return tools.numcode_to_string(plaintext)

# TODO: file or stdin inputs
# TODO: encrypt/decrypt binary

if __name__ == "__main__":
   """
   This way is so sick
   if len(sys.argv) < 4:
      print("Usage: {} encrypt|decrypt a_key b_key string".format(sys.argv[0]))
      exit()

   if sys.argv[1] == "encrypt":
      print(encrypt_text(sys.argv[3], int(sys.argv[1]), int(sys.argv[2])))
   elif sys.argv[1] == "decrypt":
      print(decrypt_text(sys.argv[3], int(sys.argv[1]), int(sys.argv[2])))
   else:
      print("Undefined")
   """
   FUNCTION_MAP = {"encrypt": encrypt_text, "decrypt": decrypt_text}

   parser = argparse.ArgumentParser()

   # group = parser.add_mutually_exclusive_group(required=True)
   # group.add_argument("func", choices=FUNCTION_MAP.keys())
   parser.add_argument("func", choices=FUNCTION_MAP.keys())

   parser.add_argument("-a", type=int, required=True)
   parser.add_argument("-b", type=int, required=True)
   parser.add_argument("-t", required=True)

   args = parser.parse_args()

   func = FUNCTION_MAP[args.func]
   a_key, b_key = args.a, args.b
   text = args.t
   print(func(text, a_key, b_key))


