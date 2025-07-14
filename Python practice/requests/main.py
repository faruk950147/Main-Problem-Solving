import requests
# GET request
response = requests.get("https://api.github.com")
# print response status code
print(response.status_code)
# print response json and pretty print
print(response.json())

# POST request
# response = requests.post("https://api.github.com", json={"name": "John", "age": 30})
# # print response status code
# print(response.status_code)
# # print response json and pretty print
# print(response.json())
