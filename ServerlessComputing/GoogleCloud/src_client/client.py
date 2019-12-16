import google.oauth2.credentials
from google.oauth2 import id_token
from google.oauth2 import service_account
import google.auth
import google.auth.transport.requests
from google.auth.transport.requests import AuthorizedSession

url = 'https://us-central1-polytech-lab.cloudfunctions.net/resize'
certs_url='https://www.googleapis.com/auth/cloud-platform'

svcAccountFile = '/Users/bc30138/.gcred/polytech-lab-f08acf9f2b3a.json'

def GetIDTokenFromServiceAccount(svcAccountFile):
    creds = service_account.IDTokenCredentials.from_service_account_file(svcAccountFile, target_audience='https://www.googleapis.com/auth/cloud-platform')
    request = google.auth.transport.requests.Request()
    creds.refresh(request)
    return creds.token

# def VerifyIDToken(token, certs_url,  audience=None):
#     request = google.auth.transport.requests.Request()
#     result = id_token.verify_token(token,request,certs_url=certs_url)
#     if audience in result['aud']:
#         return True
#     return False

def MakeAuthenticatedRequest(id_token, url):
    creds = google.oauth2.credentials.Credentials(id_token)
    authed_session = AuthorizedSession(creds)
    r = authed_session.get(url)
    print(r.status_code)
    print(r.text)

# For ServiceAccount
token = GetIDTokenFromServiceAccount(svcAccountFile)


print('Token: ' + token)
# if VerifyIDToken(token=token,certs_url=certs_url, audience=target_audience):
#     print('token Verified with aud: ' + target_audience)
print('Making Authenticated API call:')
MakeAuthenticatedRequest(token,url)