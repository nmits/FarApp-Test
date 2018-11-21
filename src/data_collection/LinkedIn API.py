import requests
import ConfigParser
# import selenium

def get_access_code():
    config_parser = ConfigParser.ConfigParser()
    config_parser.read("../../config.txt")
    client_id = config_parser.get('LinkedInAPI', 'client')
    client_secret = config_parser.get('LinkedInAPI', 'secret')

    OAuthBaseUrl = "https://www.linkedin.com/oauth/v2/authorization?"
    callback = "https://localhost/auth/linkedin/callback"

    OAuthUrl = OAuthBaseUrl
    OAuthUrl += "&response_type=code"
    OAuthUrl += "&client_id=" + client_id
    OAuthUrl += "&redirect_uri=" + callback

    print requests.get(OAuthUrl).url

    #Haven't done this before, not sure how to get URL to open in browser without using Selenium

    AccessCode = "" #Not sure

    AccessUrl = "https://www.linkedin.com/oauth/v2/accessToken?"
    AccessPayload = {}
    AccessPayload['grant_type'] = "authorization_code"
    AccessPayload['code'] = AccessCode
    AccessPayload['redirect_uri'] = callback
    AccessPayload['client_id'] = client_id
    AccessPayload['client_secret'] = client_secret

    AccessResponse = requests.post("https://www.linkedin.com/oauth/v2/accessToken", data=AccessPayload)

    return AccessResponse #Get Token from this response

def poll_users(max=100, access_code = None):
    return requests.get("https://api.linkedin.com/v1/people/~?format=json&code=" + access_code)

AccessResponse = get_access_code()
print poll_users(access_code=AccessResponse)