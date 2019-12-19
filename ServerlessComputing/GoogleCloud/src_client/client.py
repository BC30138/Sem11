
"""
client app
"""
import argparse
import subprocess
import base64
import requests

PROD_URL = "https://us-central1-polytech-lab.cloudfunctions.net/resize"
TEST_URL = "http://127.0.0.1:8888/resize"

class Client():
    def __init__(self):
        parser = argparse.ArgumentParser(
            description="Client to send requests to resize image")
        parser.add_argument("-i", "--input", action='store',
                            type=str,
                            help="Path to image to send",
                            required=False,
                            default='data/igor-nikolaev.jpg')
        parser.add_argument("-o", "--output", action='store',
                            type=str,
                            help="Path to response" +
                            "zip/extracted images directory",
                            required=False, default='data/data.zip')
        parser.add_argument("-e", "--extract",
                            help="Flag to extract response zip",
                            action='store_true', required=False)
        parser.add_argument("-l", "--local", help="Flag to local testing",
                            action='store_true', required=False)
        self.args = parser.parse_args()
        if self.args.local:
            self.url = TEST_URL
            self.headers = {}
        else:
            self.url = PROD_URL
            proc = subprocess.Popen(['sudo', 'gcloud',
                                     'auth', 'print-identity-token'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            token, _ = proc.communicate()
            token = str(token)[2:-3]
            self.headers = {"Authorization": "bearer {}".format(token.strip())}

    def post(self):
        with open(self.args.input, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read())

        response = requests.post(self.url, data=encoded_string,
                                 headers=self.headers)

        if self.args.extract:
            print("TBD")
        else:
            with open(self.args.output, 'wb') as output_file:
                output_file.write(base64.b64decode(response.text))

app = Client()
app.post()
