#!/usr/bin/env python
from jwkest import b64e
import json

header = {"alg": "none"}
htxt = json.dumps(header)
hdr = b64e(htxt)

claims_set = {"foo": "bar"}
txt = json.dumps(claims_set)
msg = b64e(txt)

jws = ".".join([hdr, msg, ""])

print "JWT={}".format(jws)

