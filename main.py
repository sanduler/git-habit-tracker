# Name: Ruben Sanduleac
# Date: 2/22/22
# Description: The program is habit tracker for the user
# post every day their habits and then the program determines the intensity of the habit.


import requests
import os

pixela_api_key = os.environ["PIXELA_API"]
pixela_username = os.environ["PIXELA_USERNAME"]
pixela_api_endpoint = "https://pixe.la/v1/users"
pixel_parameters = {
    "token": pixela_api_key,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}
response = requests.post(pixela_api_endpoint)
requests.RequestException(response)