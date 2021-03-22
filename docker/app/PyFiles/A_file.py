import requests

response = requests.get("http://localhost:5001")

f = "A"
print("file {} - apicall".format(f))
print(response.json())