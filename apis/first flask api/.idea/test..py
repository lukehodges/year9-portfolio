import requests
base = "http://127.0.0.1:5000/"
y = requests.post(base+"helloworld")
print(y.json())