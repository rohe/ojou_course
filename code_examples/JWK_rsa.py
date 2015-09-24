#!/usr/bin/env python
import json
from oic.utils.keyio import create_and_store_rsa_key_pair, \
    build_keyjar
from jwkest.jwk import RSAKey, KEYS, keyitems2keyreps

key = create_and_store_rsa_key_pair("foo", size=2048)

rsa = RSAKey().load_key(key)
ser_rsa = rsa.serialize()

print "--- JWK ----"
print json.dumps(ser_rsa, sort_keys=True, indent=4, separators=(',', ': '))
print

k = keyitems2keyreps({"RSA": [key]})

print "--- JWKS ----"
keys = KEYS()
keys.wrap_add(key, use="sig", kid="rsa1")
print keys.dump_jwks()

key_conf = [
    {"type": "RSA", "name": "rsa_key", "use": ["enc", "sig"]},
    {"type": "EC", "crv": "P-256", "use": ["sig"]},
    {"type": "EC", "crv": "P-256", "use": ["enc"]}
]

jwks, keyjar, kdd = build_keyjar(key_conf, "m%d", None, None)

print "---- JWKS from keyjar ----"
print jwks