#!/usr/bin/env python3
# Vignere Cipher
# Sid

import tools
from itertools import cycle, islice

class Vigenere:
    def __init__(self, passphrase="fuck",mod=107):
        self.passphrase = passphrase
        self.mod = mod
    
    def __repeatto(self, n):
        # repeat passphrase to desired length
        # "fuck" become ['f', 'u', 'c', 'k', 'f', 'u'] if wanted length is 6
        return list(islice(cycle(self.passphrase),n))

    def __pass_to_num(self, n):
        return tools.string_to_numcode(self.__repeatto(n))

    def __encrypt(self, plain_list):
        return [(plain_char+pass_char)%self.mod for plain_char, pass_char in list(zip(plain_list, self.__pass_to_num(len(plain_list))))]

    def encrypt(self, plain_list):
        return [(plain_char+pass_char)%self.mod for plain_char, pass_char in list(zip(plain_list, self.__pass_to_num(len(plain_list))))]
    
    def __decrypt(self, cipher_list):
        return [(cipher_char-pass_char)%self.mod for cipher_char, pass_char in list(zip(cipher_list, self.__pass_to_num(len(cipher_list))))]

    def decrypt(self, cipher_list):
        return [(cipher_char-pass_char)%self.mod for cipher_char, pass_char in list(zip(cipher_list, self.__pass_to_num(len(cipher_list))))]

    def encrypt_text(self, plaintext):
        plaintext = tools.string_to_numcode(plaintext)
        ciphertext = self.__encrypt(plaintext)
        return tools.numcode_to_string(ciphertext)

    def decrypt_text(self, ciphertext):
        ciphertext = tools.string_to_numcode(ciphertext)
        plaintext = self.__decrypt(ciphertext)
        return tools.numcode_to_string(plaintext)
    
if __name__ == "__main__":
    import argparse
    
    vigenere = Vigenere()

    FUNCTION_MAP = {"encrypt": vigenere.encrypt_text, "decrypt": vigenere.decrypt_text}

    parser = argparse.ArgumentParser()
    parser.add_argument("func", choices=FUNCTION_MAP.keys())
    parser.add_argument("-p", "--passphrase", required=True, help="Passphrase(string)")
    parser.add_argument("-if", "--input_file", required=True, help="file to encrypt or decrypt")
    parser.add_argument("-of", "--output_file", required=True, help="output file")

    args = parser.parse_args()

    func = FUNCTION_MAP[args.func]
    vigenere.passphrase = args.passphrase
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
