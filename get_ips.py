import requests as req
import json
import traceback
import time

# vhack_api url at time of development - could be changed
# this module calls api to get existing ips for users but you have to provide your access via username & password captured from your network while playing
# this url contains example -- not real user credintials
url = 'https://api.vhack.cc/v/8/vh_network.php?user=eyJnbG9iYWwiOiIwIiwidGltZSI6IjE0ODE2MzE2NzUiLCJ1c2VyIjoidW5pc56sdfLf4IiwicGFzcyI6ImdoYXp5MjAwMCIsInVoYXNoIjoiZDDFDFUEWTA3MWY3MzcwMmE5NmUxNDQ5NTk1MDYxMTRiODEzMTgxMWU5ZDBjNWJhODU1N2E1Mjk1NTQzNTViMCJ9&pass=62368d0099fg52rc192ca8efd012b7d7f'
output = 'false'
try:
    ips = open('ips.txt', 'w')
    for i in xrange(200):
        res = req.get(url)
        obj = json.loads(res.text)
        lst = obj['data']
        for item in lst:
            ips.write(item['ip'] + '\n')
        time.sleep(1)
    output = 'true'
except:
    traceback.print_exc()
finally:
    print output
    ips.close()
