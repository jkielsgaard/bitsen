import requests
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
api_url = "http://{}:5001".format(ip_address)


response = requests.get(api_url)

f = "A"
print("file {} - apicall".format(f))
print(response.json())