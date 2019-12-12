import tools

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