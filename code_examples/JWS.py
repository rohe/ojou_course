#!/usr/bin/env python
"""
Show how to do compact signing and verification of JWTs.
"""
import json
from jwkest import b64d
from jwkest.jwk import import_rsa_key_from_file
from jwkest.jwk import RSAKey
from jwkest.jws import JWS
from jwkest.jwt import JWT

__author__ = 'roland'

payload = {"iss": "joe",
           "exp": 1300819380,
           "http://example.com/is_root": True}

# The JWS class can not work directly with rsa keys.
# In this case the rsa key is wrapped in a RSAKey
keys = [RSAKey(key=import_rsa_key_from_file("foo"))]

_jws = JWS(payload, alg="RS512")
_jwt = _jws.sign_compact(keys)

print("Signed jwt:",  _jwt)
print()

# The JWT class can be used to peek into a JWT, whether is is signed or
# encrypted. It will not do any verificiation or decryption just unpacking
# the JWT.

jwt = JWT()
jwt.unpack(_jwt)
print("jwt headers:", jwt.headers)

# Part 0 is the headers
# Part 1 is the payload message
print("jwt part 1:", jwt.part[1])
print()

# If you want to verify the signature you have to use the JWS class
_rj = JWS()

# If everything is OK the verify_compact method will return the payload message
info = _rj.verify_compact(_jwt, keys)

print("Verified info:", info)
