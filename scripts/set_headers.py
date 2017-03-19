import requests
from mitmproxy import http
from mitmproxy import ctx

# TODO authenticate user
def getProxyauth(flow):
    if 'proxyauth' in flow.metadata: # TODO and user != None
        return flow.metadata['proxyauth']
    else:
        return ""

def request(flow):
    payload = { 'username': getProxyauth(flow)[0], 'password': getProxyauth(flow)[1], 'url': flow.request.pretty_host }
    r = requests.get("http://localhost:3000/idea", params=payload)
    # TODO check if auth'd
    if r.status_code == 401:
        flow.response = http.HTTPResponse.make(
            401,  # (optional) status code
            b"You need to authenticate properly, buddy",  # (optional) content
            {"Content-Type": "text/html"}  # (optional) headers
        )
        return
    flow.request.headers["x-idea-id"] = r.text
