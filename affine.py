#!/usr/bin/env python3
# Affine Cipher: Encrypting and Decrypting
# Sid

import sys
import tools 

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
   import argparse
   
   FUNCTION_MAP = {"encrypt": encrypt_text, "decrypt": decrypt_text}

   parser = argparse.ArgumentParser()

   # group = parser.add_mutually_exclusive_group(required=True)
   # group.add_argument("func", choices=FUNCTION_MAP.keys())
   parser.add_argument("func", choices=FUNCTION_MAP.keys())

   parser.add_argument("-a", "--a_key", type=int, required=True, help="'a' key of affine cipher (integer 0-106)")
   parser.add_argument("-b", "--b_key", type=int, required=True, help="'b' key of affine cipher (integer 0-106)")
   parser.add_argument("-if", "--input_file", required=True, help="file to encrypt or decrypt")
   parser.add_argument("-of", "--output_file", required=True, help="output file")

   args = parser.parse_args()

   func = FUNCTION_MAP[args.func]
   a_key, b_key = args.a_key, args.b_key
   infile = args.input_file
   outfile = args.output_file
   filebuffer = list()

   with open(infile, "r") as reader:
      for line in reader:
         processed_line = func(line.rstrip('\n'), a_key, b_key)
         print(processed_line)
         filebuffer.append(processed_line + '\n')

   with open(outfile, "x") as writer:
       writer.writelines(filebuffer)


         
   

