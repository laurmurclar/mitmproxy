# Running
`cd ~/Code/mitmproxy`
`. venv/bin/activate`
`pip3 install mysql.connector`
`python scripts/setup_db.py`
`mitmproxy -s scripts/set_headers.py`

# TODO
- Sign in for proxy
- Figure out protocol for sites to be added to host
- Easy setup on another machine (change startup script of mitmproxy)
- Setup on phone
- Allow www.google.com and google.com etc to be considered the same when adding - but then heroku apps will all be considered the same. Hmmm, think about this more. I think we will just solve this with the host protocol
- Maybe create another heroku app for "different" server
