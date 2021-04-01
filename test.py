import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 10, "name": "Joe", "views": 100000},
        {"likes": 10, "name": "How to make Rest Api", "views": 80000},
        {"likes": 10, "name": "Tim", "views": 4500}, ]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/6")
print(response.json())
