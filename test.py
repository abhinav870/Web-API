import requests
# we will be sending requests to our API from here

BASE= "http://127.0.0.1:5000/"
# location of the server where we are running the API

data = [{"likes":10,"views": 100000,"name": "Abhinav"},
        {"likes":35,"views": 50000,"name": "Avi"},
        {"likes":75,"views": 22569,"name": "Tim"}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i),data[i])
    print(response.json())

response_delete = requests.delete(BASE + "video/0")
print(response_delete)
# since the video_id is deleted we no longer send the json response we return an empty string and 204
# so as no json serializable obj is returned, we don't write .json()

# response_get = requests.get(BASE + "video/0")
# print(response_get.json())

response = requests.get(BASE + "video/2")
print(response.json())
