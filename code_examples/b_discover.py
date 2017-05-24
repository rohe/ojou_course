#!/usr/bin/env python
"""
Shows off how you can do OpenID Connect dynamic configuration discovery
"""
import json
import requests

from oic.oic import Client
from oic.oic import OIDCONF_PATTERN
from oic.utils.webfinger import WebFinger
from oic.utils.webfinger import OIC_ISSUER

from requests.packages import urllib3
urllib3.disable_warnings()

__author__ = 'roland'

# =============================================================================

wf = WebFinger()
ACCOUNT = "carol@localhost:8040"
#ACCOUNT = "carol@op1.test.inacademia.org"
RESOURCE = "acct:{}".format(ACCOUNT)

query = wf.query(RESOURCE, rel=OIC_ISSUER)

r = requests.request("GET", query, verify=False)

jwt = json.loads(r.text)
url = jwt["links"][0]["href"]

print("Issuer URL from webfinger:", url)

# Construct the URL used to get the provider configuration
url = OIDCONF_PATTERN % url

print("Provider configuration url:", url)

r = requests.request("GET", url, verify=False)

jwt = json.loads(r.text)
print("----  provider configuration info ----")
print(json.dumps(jwt, sort_keys=True, indent=4, separators=(',', ': ')))

# =============================================================================
# A bit more higher level :-)

cli = Client()
cli.verify_ssl = False

issuer = cli.discover("carol@op1.test.inacademia.org")

# pcr is an instance of oic.oic.message.ProviderConfigurationResponse
pcr = cli.provider_config(issuer)
print(pcr.to_dict())