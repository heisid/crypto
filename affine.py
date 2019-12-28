#!/usr/bin/env python3
# Affine Cipher: Encrypting and Decrypting
# Sid

import sys
import tools 


class Affine:
   def __init__(self, a_key=1, b_key=1, mod=107):
      self.a_key = a_key
      self.b_key = b_key
      self.mod = mod

   def generate_possible_a_keys(self):
      return [element for element in range(self.mod) if tools.are_coprime(element, self.mod)]

   def __encrypt(self, plain_list):
      if not tools.are_coprime(self.a_key, self.mod):
         raise tools.NotCoprimeError
      if self.b_key > self.mod:
         raise "Invalid b key"
      return [((self.a_key*char + self.b_key) % self.mod) for char in plain_list]

   def __decrypt(self, cipher_list):
      a_inverse = tools.mod_inverse(self.a_key, self.mod)
      return [((a_inverse * (char - self.b_key)) % self.mod) for char in cipher_list]

   def encrypt_text(self, plaintext):
      plaintext = tools.string_to_numcode(plaintext)
      ciphertext = self.__encrypt(plaintext)
      return tools.numcode_to_string(ciphertext)

   def decrypt_text(self, ciphertext):
      ciphertext = tools.string_to_numcode(ciphertext)
      plaintext = self.__decrypt(ciphertext)
      return tools.numcode_to_string(plaintext)

# TODO: file or stdin inputs
# TODO: encrypt/decrypt binary

if __name__ == "__main__":
   import argparse
   
   affine = Affine()
   FUNCTION_MAP = {"encrypt": affine.encrypt_text, "decrypt": affine.decrypt_text}

   parser = argparse.ArgumentParser()

   parser.add_argument("func", choices=FUNCTION_MAP.keys())

   parser.add_argument("-a", "--a_key", type=int, required=True, help="'a' key of affine cipher (integer 0-106)")
   parser.add_argument("-b", "--b_key", type=int, required=True, help="'b' key of affine cipher (integer 0-106)")
   parser.add_argument("-if", "--input_file", required=True, help="file to encrypt or decrypt")
   parser.add_argument("-of", "--output_file", required=True, help="output file")

   args = parser.parse_args()

   func = FUNCTION_MAP[args.func]
   affine.a_key, affine.b_key = args.a_key, args.b_key
   infile = args.input_file
   outfile = args.output_file
   filebuffer = list()

   with open(infile, "r") as reader:
      for line in reader:
         processed_line = func(line.rstrip('\n'))
         print(processed_line)
         filebuffer.append(processed_line + '\n')

   with open(outfile, "x") as writer:
       writer.writelines(filebuffer)


         
   

