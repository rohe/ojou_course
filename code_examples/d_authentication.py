from oic import rndstr
from oic.oic import Client
from requests.packages import urllib3

urllib3.disable_warnings()

cli = Client(verify_ssl=False)

issuer = cli.discover("diana@localhost:8040")

pcr = cli.provider_config(issuer)

registration_info = {'redirect_uris': ['https://example.com/rp']}

regresp = cli.register(pcr['registration_endpoint'], **registration_info)

_state = rndstr()
request_args = {
    'response_type': 'code',
    'scope': ['openid'],
    'redirect_uri': regresp['redirect_uris'],
    'client_id': regresp['client_id']
}

res = cli.do_authorization_request(request_args=request_args, state=_state)
print(res)
