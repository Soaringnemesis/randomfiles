from Crypto.Cipher import AES
import base64
import os
 
BLOCK_SIZE = 32
 
PADDING = '{'
 
# Encrypted text to decrypt
encrypted = "uqX82PBZ8pi1fvt4GLHYgLs50ht8OQlrR1KHL2teppQ="
 
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
 
secret = "password"
 
with open("words1.txt", "r") as file:
    for line in file:
        secret = line[:-1]
        print("OLD: " + secret)
        secret = secret[:31]
        print("NEW: " + secret)
        if (secret[-1:] == "\n"):
            print("Error, new line character at the end of the string. This will not match!")
        elif (len(secret) >= 32):
            print("Error, string too long. Must be less than 32 characters.")
        else:
            # create a cipher object using the secret
            cipher = AES.new(secret + (BLOCK_SIZE - len(secret) % BLOCK_SIZE) * PADDING)

            # decode the encoded string
            decoded = DecodeAES(cipher, encrypted)

            if (decoded.startswith('FLAG:')):
                print("\n")
                print("Success: "+secret+"\n")
                print(decoded+"\n")
                break
            else:
                print('Wrong password')