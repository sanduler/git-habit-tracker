# Name: Ruben Sanduleac
# Date: 2/22/22
# Description: The program is habit tracker for the user
# post every day their habits and then the program determines the intensity of the habit.


import requests

pixela_api_endpoint = "https://pixe.la/v1/users"

pixel_parameters = {
    "token": "aafsdi2hf82mv73bzali2j",
    "username": "sanduler",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}
requests.post()