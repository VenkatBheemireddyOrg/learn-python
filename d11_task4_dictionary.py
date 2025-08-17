import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_detail = response.json()

print(response.json())