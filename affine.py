#!/usr/bin/env python3

import sys
import tools
import getopt

def generate_possible_a_keys(mod):
   a_keys = list()
   for element in range(mod):
      if tools.are_coprime(element, mod):
         a_keys.append(element)
   return a_keys

def affine_encrypt(plain_list, a_key, b_key, mod):
   if not tools.are_coprime(a_key, mod):
      raise tools.NotCoprimeError
   if b_key > mod:
      raise "Invalid b key"
   cipher_list = [((a_key*char + b_key) % mod) for char in plain_list]
   return cipher_list

def affine_decrypt(cipher_list, a_key, b_key, mod):
   a_inverse = tools.mod_inverse(a_key,mod)
   plain_list = [((a_inverse * (char - b_key)) % mod) for char in cipher_list]
   return plain_list

def affine_encrypt_text(plaintext, a_key, b_key):
   # printable ascii range 20 - 126
   # so we need 126 - 20 + 1 = mod 107
   # 107 is prime, don't worry about inverse existence
   mod = 107
   plaintext = tools.string_to_numcode(plaintext)
   ciphertext = affine_encrypt(plaintext, a_key, b_key, mod)
   return tools.numcode_to_string(ciphertext)

def affine_decrypt_text(ciphertext, a_key, b_key):
   ciphertext = tools.string_to_numcode(ciphertext)
   mod = 107
   plaintext = affine_decrypt(ciphertext, a_key, b_key, mod)
   return tools.numcode_to_string(plaintext)

# TODO: file or stdin inputs, using getopt for clear
# TODO: encrypt/decrypt binary

if __name__ == "__main__":
   if len(sys.argv) < 4:
      print("Usage: {} encrypt|decrypt a_key b_key string".format(sys.argv[0]))
      exit()

   if sys.argv[1] == "encrypt":
      print(affine_encrypt_text(sys.argv[3], int(sys.argv[1]), int(sys.argv[2])))
   elif sys.argv[1] == "decrypt":
      print(affine_decrypt_text(sys.argv[3], int(sys.argv[1]), int(sys.argv[2])))
   else:
      print("Undefined")