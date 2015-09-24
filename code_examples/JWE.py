#!/usr/bin/env python
from Crypto.PublicKey import RSA
from jwkest.jwe import JWE_RSA

__author__ = 'roland'

rsa = RSA.generate(2048)
plain = "Now is the time for all good men to come to the aid of their country."

_rsa15_enc = JWE_RSA(plain, alg="RSA1_5", enc="A128CBC-HS256")
jwt1 = _rsa15_enc.encrypt(rsa)

print "(1)"
for p in jwt1.split('.'):
    print "-", p

_rsa15_dec = JWE_RSA()
msg = _rsa15_dec.decrypt(jwt1, rsa)
print
print msg

jwt2 = JWE_RSA(plain, alg="RSA-OAEP", enc="A256GCM").encrypt(rsa)
print "(2)"
for p in jwt2.split("."):
    print "-", p
msg = JWE_RSA().decrypt(jwt2, rsa)
print
print msg