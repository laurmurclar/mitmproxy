# Running
`cd ~/Code/mitmproxy`
`. venv/bin/activate`
`pip3 install mysql.connector`
`python scripts/setup_db.py`
`mitmproxy -s scripts/set_headers.py`

# TODO
- Add new id to table from proxy
- Sign in for proxy
- Figure out protocol for sites to be added to host
- Easy setup on another machine (change startup script of mitmproxy)
