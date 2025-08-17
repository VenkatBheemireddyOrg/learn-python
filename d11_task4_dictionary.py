import requests  #github api


# github url for integration
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

# converting json as dictionary
complete_detail = response.json()

print(complete_detail[0]["user"]["login"])

for i in range(len(complete_detail)):
    print(complete_detail[i]["user"]["login"])
