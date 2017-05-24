#!/usr/bin/env python
"""
Show of how to construct a simple unsigned JWT as outlined in
https://tools.ietf.org/html/rfc7519

1.  Create a JWT Claims Set containing the desired claims.  Note that
   whitespace is explicitly allowed in the representation and no
   canonicalization need be performed before encoding.

2.  Let the Message be the octets of the UTF-8 representation of the
   JWT Claims Set.

3.  Create a JOSE Header containing the desired set of Header
   Parameters.  The JWT MUST conform to either the [JWS] or [JWE]
   specification.  Note that whitespace is explicitly allowed in the
   representation and no canonicalization need be performed before
   encoding.

4.  Depending upon whether the JWT is a JWS or JWE, there are two
   cases:

   *  If the JWT is a JWS, create a JWS using the Message as the JWS
      Payload; all steps specified in [JWS] for creating a JWS MUST
      be followed.

   *  Else, if the JWT is a JWE, create a JWE using the Message as
      the plaintext for the JWE; all steps specified in [JWE] for
      creating a JWE MUST be followed.

5.  If a nested signing or encryption operation will be performed,
   let the Message be the JWS or JWE, and return to Step 3, using a
   "cty" (content type) value of "JWT" in the new JOSE Header
   created in that step.

6.  Otherwise, let the resulting JWT be the JWS or JWE
"""
from jwkest import b64e, as_bytes, as_unicode
import json

# 1
claims_set = {"foo": "bar"}
# 2
txt = json.dumps(claims_set)
msg = b64e(as_bytes(txt))

#3
header = {"alg": "none"}
htxt = json.dumps(header)
hdr = b64e(as_bytes(htxt))

# (4,5),6
jws = ".".join([as_unicode(hdr), as_unicode(msg), ""])

print("JWT={}".format(jws))

# ============================================================================
# Higher level

from jwkest import b64d
from jwkest.jws import JWS

# JWS is A class that can be used for signing and verifying signatures
jws = JWS({"foo": "bar"}, alg="none").sign_compact()

print("JWT={}".format(jws))
print("")

# decode and print the different parts. No verification is done.
for p in jws.split("."):
    p = p.encode("utf8")
    print(b64d(p))