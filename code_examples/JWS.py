#!/usr/bin/env python
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


keys = [RSAKey(key=import_rsa_key_from_file("foo"))]

_jws = JWS(payload, alg="RS512")
_jwt = _jws.sign_compact(keys)

print "jwt:",  _jwt
print

jwt = JWT()
jwt.unpack(_jwt)
print "jwt headers:", jwt.headers
print "jwt part 1:", jwt.part[1]
print

_rj = JWS()
info = _rj.verify_compact(_jwt, keys)

print "Verified info:", info
