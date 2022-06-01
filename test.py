from urllib import response
import requests

BASE = "http://127.0.0.1:5000/"

data = [
        {'likes':78, 'name': "Joe", 'views': 100_000},
        {'likes':10_000, 'name': "How to make REST API", 'views': 80_000},
        {'likes':35, 'name': "Tim", 'views': 2_000}
        ]

for i in range(len(data)):
    
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

print("")
print("Press enter to continue.")
input()


response = requests.delete(BASE + 'video/0')
print(response)


print("Press enter to continue.")
input()


response = requests.get(BASE + "video/2")
print(response.json())