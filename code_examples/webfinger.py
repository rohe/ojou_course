#!/usr/bin/env python
import json
from oic.oauth2 import PBase
import requests
from oic.utils.webfinger import WebFinger, OIC_ISSUER

__author__ = 'roland'

wf = WebFinger()
query = wf.query("acct:carol@op1.test.inacademia.org", rel=OIC_ISSUER)

print query

r = requests.request("GET", query, verify=False)

jwt = json.loads(r.text)
print json.dumps(jwt, sort_keys=True, indent=4, separators=(',', ': '))

# =====================================================================

wf = WebFinger()
wf.httpd = PBase(verify_ssl=False)
url = wf.discovery_query("acct:carol@op1.test.inacademia.org")
print url