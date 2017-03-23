import requests
from mitmproxy import http
from mitmproxy import ctx

id_url = "https://lmc-lightswitch.herokuapp.com/idea"

def getProxyauth(flow):
    if 'proxyauth' in flow.metadata: # TODO and user != None
        return flow.metadata['proxyauth']
    else:
        return ""

def request(flow):
    payload = { 'username': getProxyauth(flow)[0], 'password': getProxyauth(flow)[1], 'url': flow.request.pretty_host }
    # TODO handle bad requests
    r = requests.get(id_url, params=payload)

    if r.status_code == 401:
        flow.response = http.HTTPResponse.make(
            401,  # (optional) status code
            b"You need to authenticate properly, buddy",  # (optional) content
            {"Content-Type": "text/html"}  # (optional) headers
        )
        return

    flow.request.headers["x-idea-id"] = r.text
