import requests
key='WIgF7DuwHlLmib_80PKl'
response=requests.get('https://the-one-api.dev/v2/book/',
params={"key":key})
print(response.status_code)