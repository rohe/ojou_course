#!/usr/bin/env python
"""
Creating and reading JWKs and JWKS
"""
import json
import os

from oic.utils.keyio import create_and_store_rsa_key_pair
from oic.utils.keyio import build_keyjar
from jwkest.jwk import import_rsa_key_from_file
from jwkest.jwk import RSAKey
from jwkest.jwk import KEYS

# Will create 2 files on disc if not there already
# 'foo' will contain the private key
# 'foo.pub' will contain the public key
if not os.path.isfile('foo'):
    key = create_and_store_rsa_key_pair("foo", size=2048)
    rsa = RSAKey().load_key(key)
else:
    rsa = RSAKey(key=import_rsa_key_from_file("foo"))
    key = rsa.key

# by default this will be the public part of the key
ser_rsa = rsa.serialize()

print("--- JWK (public) ----")
print(json.dumps(ser_rsa, sort_keys=True, indent=4, separators=(',', ': ')))
print()

# and this will give you the serialization of the private key
ser_rsa = rsa.serialize(private=True)

print("--- JWK (private) ----")
print(json.dumps(ser_rsa, sort_keys=True, indent=4, separators=(',', ': ')))
print()

# ============================================================================
# And now for the JWKS

keys = KEYS()
keys.wrap_add(key, use="sig", kid="rsa1")

print("--- JWKS ----")
print(keys.dump_jwks())

# Build a number of keys from a specification and place them in a keyjar
key_conf = [
    {"type": "RSA", "name": "rsa_key", "use": ["enc", "sig"]},
    {"type": "EC", "crv": "P-256", "use": ["sig"]},
    {"type": "EC", "crv": "P-256", "use": ["enc"]}
]

# The function return a set of representations of the keys that was
# created.
# jwks: a JWKS representation
# keyjar: a oic.utils.keyio.KeyJar instance with the keys added
# kdd: a simple dictionary enumerating which key ids that can be used for
# which key operations.
jwks, keyjar, kdd = build_keyjar(key_conf, "m%d", None, None)

print()
print("---- JWKS from specification ----")
print(jwks)