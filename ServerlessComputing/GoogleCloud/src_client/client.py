
"""
client app
"""
import subprocess
import base64
import requests

URL = "https://us-central1-polytech-lab.cloudfunctions.net/resize"
TEST_URL = "http://127.0.0.1:8888/resize"

def main():
    proc = subprocess.Popen(['sudo', 'gcloud', 'auth' ,'print-identity-token'],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    token, _ = proc.communicate()
    token = str(token)[2:-3]

    with open('data/igor-nikolaev.jpg', 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())
    headers = {"Authorization": "bearer {}".format(token.strip())}

    response = requests.post(URL, data=encoded_string, headers=headers)

    with open('data/data.zip', 'wb') as f:
        f.write(base64.b64decode(response.text))

main()
