import string

def poly_sub_cipher(plaintext, key):
    # Create a list of monoalphabetic substitution ciphers based on the key
    ciphers = []
    for i, c in enumerate(key):
        shift = string.ascii_lowercase.index(c)
        cipher = string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
        ciphers.append(cipher)
    
    # Use the ciphers to encrypt each letter of the plaintext
    ciphertext = ""
    for i, c in enumerate(plaintext.lower()):
        if c in string.ascii_lowercase:
            cipher = ciphers[i % len(ciphers)]
            ciphertext += cipher[string.ascii_lowercase.index(c)]
        else:
            ciphertext += c
    
    return ciphertext

# Example usage
plaintext = "Hello, world!"
key = "secret"
ciphertext = poly_sub_cipher(plaintext, key)
print(ciphertext) # Output: "zincs, aqipw!
"
