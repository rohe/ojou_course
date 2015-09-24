from oic.oauth2 import rndstr
from oic.oic import Client

cli = Client()

issuer = cli.discover("diana@oictest.umdc.umu.se:8060")

pcr = cli.provider_config(issuer)

_state = rndstr()
cli.do_authorization_request(state=_state)