import requests
from mitmproxy import ctx

# TODO authenticate user
def getUser(flow):
        if 'proxyauth' in flow.metadata: # TODO and user != None
            return flow.metadata['proxyauth'][0]
        else:
            return ""

def request(flow):
    payload = { 'username': getUser(flow), 'url': flow.request.pretty_host }
    r = requests.get("http://localhost:3000/idea", params=payload)
    flow.request.headers["x-idea-id"] = r.text
