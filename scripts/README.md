# Running
`cd ~/Code/mitmproxy`
`. venv/bin/activate`
`pip3 install mysql.connector`
`python scripts/setup_db.py`
`mitmproxy -s scripts/set_headers.py`

# TODO
- Read id for relevant site from table
- Add new id to table from proxy
- Sign in for proxy
- Easy setup on another machine (change startup script of mitmproxy)
