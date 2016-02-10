import json
from oic.oic import Client

from requests.packages import urllib3

urllib3.disable_warnings()

__author__ = 'roland'

rp = Client()

issuer = rp.discover("carol@oictest.umdc.umu.se:8092")

pcr = rp.provider_config(issuer)

registration_info = {'redirect_uris': ['https://example.com/rp']}

regresp = rp.register(pcr['registration_endpoint'],
                      **registration_info)

print(json.dumps(regresp.to_dict(), sort_keys=True, indent=4,
                 separators=(',', ': ')))
