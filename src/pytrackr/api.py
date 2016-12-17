import json
import requests

from pytrackr.device import trackrDevice

BASE_URL = "https://phonehalocloud.appspot.com"
EMAIL = None
PASSWORD = None
TOKEN = None
LAST_JSON_STATE = None
API_INTERFACE = None


class trackrApiInterface(object):

    def update_state_from_api(self):
        global LAST_JSON_STATE
        url = BASE_URL + "/rest/item"
        payload = {'usertoken': TOKEN}
        r = requests.get(url, params=payload)
        if r.status_code == 401:
            print("Token expired? Trying to get a new one.")
            authenticate(EMAIL, PASSWORD)
            r = requests.get(url, params=payload)
        LAST_JSON_STATE = r.json()
        return LAST_JSON_STATE
        

def authenticate(email, password):
    """
    Get a token.
    """
    global TOKEN, EMAIL, PASSWORD, API_INTERFACE
    EMAIL = email
    PASSWORD = password
    auth_url = BASE_URL + "/rest/user"
    payload = {'email': email, 'password': password}
    r = requests.get(auth_url, params=payload)
    token = r.json().get('usertoken')
    if token is not None:
        TOKEN = r.json().get('usertoken')
        API_INTERFACE = trackrApiInterface()
        API_INTERFACE.update_state_from_api()
    else:
        print("Failed to get token")

def get_trackrs():
    return _create_devices_from_response_dict(LAST_JSON_STATE)

def _create_devices_from_response_dict(response_dict):

    trackrs = []
    for trackr in response_dict:
        trackrs.append(trackrDevice(trackr, API_INTERFACE))
    return trackrs
