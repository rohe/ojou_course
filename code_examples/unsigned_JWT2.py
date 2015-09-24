#!/usr/bin/env python

from jwkest import b64d
from jwkest.jws import JWS

jws = JWS({"foo": "bar"}, alg="none").sign_compact()

print "JWT={}".format(jws)
print ""

for p in jws.split("."):
    p = p.encode("utf8")
    print b64d(p)