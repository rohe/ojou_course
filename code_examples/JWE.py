#!/usr/bin/env python3
"""
Show of how to so encryption and decryption of JWTs
"""
from Crypto.PublicKey import RSA
from jwkest.jwe import JWE_RSA

__author__ = 'roland'

rsa = RSA.generate(2048)
# Usually the message is a JSON document but nothing prevents you from
# using any text as long as it's unicode.
plain = "Now is the time for all good men to come to the aid of their country."

# use one set of encryption algorithms.
# 'alg' is the cryptographic algorithm used
# to encrypt or determine the value of the Content Encryption Key.
# 'enc' is the content encryption algorithm used to perform authenticated
# encryption on the Plaintext to produce the Ciphertext and the Authentication
# Tag.

# If the instance is going to be used to encrypt the message has to be
# available at initialization.
# If you want you can give the message when initiating the class but it
# can also be done later (just-in-time).

_rsa15_jwe = JWE_RSA(msg=plain, alg="RSA1_5", enc="A128CBC-HS256")
jwt1 = _rsa15_jwe.encrypt(rsa)

print("Parts of the encrypted JWT (RSA1_5+A128CBC-HS256)")
for p in jwt1.split('.'):
    print("-", p)

# You don't have to instanciate a new JWE_RSA class when you want to do
# decryption. Using the one you already have is OK.
msg = _rsa15_jwe.decrypt(jwt1, rsa)
print()
print("After decryption (RSA 1.5+A128CBC-HS256): {}".format(msg))

print(60*'=')

# Test using other algorithms
jwt2 = JWE_RSA(plain, alg="RSA-OAEP", enc="A256GCM").encrypt(rsa)
print("Parts of the encrypted JWT (RSA-OAEP+A256GCM)")
for p in jwt2.split("."):
    print("-", p)
msg = JWE_RSA().decrypt(jwt2, rsa)
print()
print(("After decryption (RSA-OAEP+A256GCM): {}".format(msg)))
