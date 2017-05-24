#!/usr/bin/env python3
"""
Show how to do compact signing and verification of JWTs.
"""
import os

from jwkest import jws

from jwkest.jwk import import_rsa_key_from_file
from jwkest.jwk import RSAKey
from jwkest.jws import JWS
from oic.utils.keyio import create_and_store_rsa_key_pair

from oic.utils.time_util import utc_time_sans_frac

__author__ = 'roland'

payload = {"iss": "joe",
           "exp": utc_time_sans_frac()+3600,
           "http://example.com/is_root": True}

if not os.path.isfile('foo'):
    key = create_and_store_rsa_key_pair("foo", size=2048)

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

_jw = jws.factory(_jwt)
print("jwt headers:", _jw.jwt.headers)

# Part 0 is the headers
# Part 1 is the payload message
print("jwt part 1:", _jw.jwt.part[1])
print()

# If everything is OK the verify_compact method will return the payload message
info = _jw.verify_compact(_jwt, keys)

print("Verified info:", info)
