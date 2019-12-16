
"""
client app
"""
import os
from google.oauth2 import service_account
import google.auth.transport.requests

from gcloud import bigquery
import json
import base64
import requests

URL = "https://us-central1-polytech-lab.cloudfunctions.net/resize"

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/bc30138/.gcred/polytech-lab-f08acf9f2b3a.json'

def entry():
    id_token = requestIdentityToken('https://us-central1-polytech-lab.cloudfunctions.net/resize')

    if id_token is not None:
        print('ID Token', id_token)
        return f'SUCCESS'
    else:
        return f'FAILURE'

def requestIdentityToken(audience=None):
    host = 'http://metadata.google.internal'
    header = {'Metadata-Flavor': 'Google'}

    if audience is None:
        audience = 'http://example.com'

    url = '{}/computeMetadata/v1/instance/service-accounts/default/identity?audience={}'.format(host, audience)

    r = requests.get(url=url, headers=header)

    if r.status_code < 200 or r.status_code >= 300:
        print('Error:', r.reason)
        return None

    return r.text

entry()

# # def GetIDTokenFromServiceAccount():

# #     return creds.token

# def main():
#     # client = bigquery.Client.from_service_account_json('/Users/bc30138/.gcred/polytech-lab-f08acf9f2b3a.json')
#     credentials = service_account.IDTokenCredentials.from_service_account_file('/Users/bc30138/.gcred/polytech-lab-f08acf9f2b3a.json', target_audience='https://us-central1-polytech-lab.cloudfunctions.net/resize ')
#     request = google.auth.transport.requests.Request()
#     credentials.refresh(request)
#     token = credentials.token

#     # credentials = service_account.Credentials.from_service_account_file(
#     #     '/Users/bc30138/.gcred/polytech-lab-f08acf9f2b3a.json',
#     #     scopes=['https://www.googleapis.com/auth/cloud-platform'])
#     # auth_req = google.auth.transport.requests.Request()
#     # credentials.refresh(auth_req)

#     data = {}
#     with open('data/igor-nikolaev.jpg', mode='rb') as file:
#         img = file.read()
#     data['image'] = base64.encodebytes(img).decode("utf-8")
#     data['name'] = "John"

#     headers = {"Authorization": "Bearer {}".format(token)}
#     print(headers)
#     response = requests.post(URL, data=json.dumps(data), headers=headers)
#     data = response.text
#     # print(data['data'])
#     # for key in data:
#     #     print(key)
#     print(data)

# main()