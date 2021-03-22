import requests

response = requests.get("http://localhost:5001")

f = "B"
print("file {} - apicall".format(f))
print(response.json())