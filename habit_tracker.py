import requests
import datetime as dt

# post requests
# second arg in post func is json since its json youre sending to the external server
# this process is me creating an account on pixela
TOKEN = "ewnodpendiuwww"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": "sam22uel",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
# second step is to create the graph we will use to track the habit

graph_endpoint = f"{pixela_endpoint}/sam22uel/graphs"
# this the request body
graph_params = {
    "id": "graph1",
    "name": "Miles run",
    "unit": "km",
    "type": "float",
    "color": "sora"

}
# this the header
headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# posting a pixel
# will have same header as graph
post_value_endpoint = f"{pixela_endpoint}/sam22uel/graphs/graph1"
now = dt.datetime.now()
# it don have to be the time rn you can make your own custom time using the datetime class
value_params = {
    # reqs a date of form "20230822"
    # we cant hardcode this as this has to be the date user adds to the habit tracker
    # so we use the strftime
    "date": f"{now.strftime('%Y%m%d')}",

    "quantity": "30.96",

}
post_value = requests.post(url=post_value_endpoint, json=value_params, headers=headers)
print(post_value.text)

# to update a pixel
update_endpoint = f"{pixela_endpoint}/sam22uel/graphs/graph1/{now.strftime('%Y%m%d')}"

update_params = {
    "newToken": TOKEN,
    "color": "shibafu",
    "quantity": input("how many km have you run today"),
    "unit": "km"

}
# update_request = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(update_request.text)
# to delete  a pixel
delete_endpoint = f"{pixela_endpoint}/sam22uel/graphs/graph1/{now.strftime('%Y%m%d')}"
delete_request = requests.delete(url=delete_endpoint, headers=headers)
print(delete_request.text)