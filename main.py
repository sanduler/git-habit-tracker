# Name: Ruben Sanduleac
# Date: 2/22/22
# Description: The program is habit tracker for the user
# post every day their habits and then the program determines the intensity of the habit.
import requests
import os
from datetime import datetime

# create env variables for the required parameters need for the POST
pixela_api_key = os.environ["PIXELA_API"]
pixela_username = os.environ["PIXELA_USERNAME"]
pixela_api_endpoint = "https://pixe.la/v1/users"
graphID = "graph1"

# use a dictionary to keep track of the variables
user_pixel_parameters = {
    "token": pixela_api_key,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}
# use the endpoint to get the post response
response = requests.post(url=pixela_api_endpoint, json=user_pixel_parameters)
# call for the exception.
requests.RequestException(response)
# print(response.text)

graph_pixela_endpoint = f"{pixela_api_endpoint}/{pixela_username}/graphs"
graph_config = {
    "id": graphID,
    "name": "Commit Tracker",
    "unit": "commit",
    "type": "int",
    "color": "momiji",
    "timezone": "PST"
}

headers = {
    "X-USER-TOKEN": pixela_api_key
}
requests.post(url=graph_pixela_endpoint, json=graph_config, headers=headers)

pixel_pixela_endpoint = f"{pixela_api_endpoint}/{pixela_username}/graphs/{graphID}"
today = datetime.now()
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3",
}

requests.post(url=pixel_pixela_endpoint, json=pixel_config, headers=headers)

update_pixel_endpoint = f"{pixela_api_endpoint}/{pixela_username}/graphs/{graphID}/20220222"

update_pixel_config = {
    "quantity": "3",
}

requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)

delete_pixel_endpoint = f"{pixela_api_endpoint}/{pixela_username}/graphs/{graphID}/20220222"

requests.delete(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
