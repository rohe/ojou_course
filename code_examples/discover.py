#!/usr/bin/env python
import json
from oic.oic import OIDCONF_PATTERN
import requests
from oic.utils.webfinger import WebFinger
from oic.utils.webfinger import OIC_ISSUER

__author__ = 'roland'

wf = WebFinger()
query = wf.query("acct:carol@oictest.umdc.umu.se:8060", rel=OIC_ISSUER)

r = requests.request("GET", query, verify=False)

jwt = json.loads(r.text)
url = jwt["links"][0]["href"]

print "Provider:", url

url = OIDCONF_PATTERN % url[:-1]

print "Provider info url:", url

r = requests.request("GET", url, verify=False)

jwt = json.loads(r.text)
print "----  provider configuration info ----"
print json.dumps(jwt, sort_keys=True, indent=4, separators=(',', ': '))
