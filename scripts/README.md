# Running
`cd ~/Code/mitmproxy`
`. venv/bin/activate`
`pip3 install mysql.connector`
`python scripts/setup_db.py`
`mitmproxy --nonanonymous -s scripts/set_headers.py`
# SET PROXY TO BYPASS LOCALHOST:3000

# TODO
- Sign in for proxy
- Figure out protocol for sites to be added to host
- Easy setup on another machine (change startup script of mitmproxy)
- Setup on phone
- Allow www.google.com and google.com etc to be considered the same when adding - but then heroku apps will all be considered the same. Hmmm, think about this more. I think we will just solve this with the host protocol
- Maybe create another heroku app for "different" server


networksetup -setwebproxy networkservice domain portnumber authenticated username password

networksetup -setwebproxy "Wi-Fi" localhost 8080 on laura pass


can get networksetup -listallnetworkservices as variables to pipe into the above command

networksetup -setwebproxystate "Wi-Fi" on

CAN PROBABLY GET BEFORE SET TO USE FOR APPEND
-setproxybypassdomains networkservice domain1 [domain2] [...]
Set the Bypass Domain Name Servers for <networkservice> to <domain1> [domain2] [...]. Any number of Domain Name servers can be specified. Specify "Empty" for <domain1> to
          clear all Domain Name entries.
