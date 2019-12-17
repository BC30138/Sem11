
"""
client app
"""
import base64
import requests
import json
import subprocess

URL = "https://us-central1-polytech-lab.cloudfunctions.net/resize"


def main():
    proc = subprocess.Popen(['sudo', 'gcloud', 'auth' ,'print-identity-token'],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    token, _ = proc.communicate()
    token = str(token)[2:-3]

    data = {}
    files = {'image': open('data/igor-nikolaev.jpg', mode='rb')}

    headers = {"Authorization": "bearer {}".format(token.strip())}
    response = requests.post(URL, files=files, headers=headers)
    data = response.json()
    for index, image in enumerate(data['resized_images']):
        with open('data/' + str(index) + '.jpg', 'wb') as fl:
            fl.write(base64.b64decode(image))

main()