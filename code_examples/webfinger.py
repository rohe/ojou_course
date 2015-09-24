#!/usr/bin/env python
"""
Code to show how you can use WebFinger to aquire the issuer ID
of an OpenID Connect provider using an account id
"""
import json
from oic.oauth2 import PBase
import requests
from oic.utils.webfinger import WebFinger, OIC_ISSUER

__author__ = 'roland'

# =====================================================================
# Using only very basic functions and methods

# Initiate the WebFinger class
wf = WebFinger()

# contruct the webfinger query URL
query = wf.query("acct:carol@op1.test.inacademia.org", rel=OIC_ISSUER)

print(query)

r = requests.request("GET", query, verify=False)

# parse the JSON returned by the website and dump the content to
# standard out
jwt = json.loads(r.text)
print(json.dumps(jwt, sort_keys=True, indent=4, separators=(',', ': ')))

# =====================================================================
# A bit more high level

wf = WebFinger()

# PBase is a wrapper around requests
wf.httpd = PBase(verify_ssl=False)

# discover_query will follow webfinger redirects
url = wf.discovery_query("acct:carol@op1.test.inacademia.org")
print(url)