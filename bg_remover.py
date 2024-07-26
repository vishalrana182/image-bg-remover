import requests

input = '/content/nameLogo.png'
api = '' #try with your own api
output = 'output.png'
with open(input, 'rb') as input:
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': input},
        data={'size': 'auto'},
        headers={'X-Api-Key': api},
    )
if response.status_code == requests.codes.ok:
    with open(output, 'wb') as output:
        output.write(response.content)
    print("success")
else:
    print("some error occured")