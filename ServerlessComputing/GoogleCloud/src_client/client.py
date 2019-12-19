
"""
client app
"""
import argparse
import subprocess
import base64
import requests

PROD_URL = "https://us-central1-polytech-lab.cloudfunctions.net/resize"
TEST_URL = "http://127.0.0.1:8888/resize"
URL: str
INPUT_FILE_PATH: str


def argument_parser():
    parser = argparse.ArgumentParser(description = "Description for my parser"

def main():
    # url: str
    # headers: dict
    # input_path: str
    # output_path: str

    # if len(sys.argv) == 3:
    #     if sys.argv[1] == "local":
    #         url = TEST_URL
    #     else:
    #         raise Exception("Incorrect arguments.")
    #     headers = {}

    # elif len(sys.argv) == 1:
    #     url = PROD_URL
    #     proc = subprocess.Popen(['sudo', 'gcloud',
    #                              'auth', 'print-identity-token'],
    #                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #     token, _ = proc.communicate()
    #     token = str(token)[2:-3]
    #     headers = {"Authorization": "bearer {}".format(token.strip())}
    # else:
    #     raise Exception("Incorrect arguments.")

    with open('data/igor-nikolaev.jpg', 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())

    response = requests.post(url, data=encoded_string, headers=headers)

    with open('data/data.zip', 'wb') as output_file:
        output_file.write(base64.b64decode(response.text))

main()
