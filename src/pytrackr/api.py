import logging
import datetime

import requests

from pytrackr.device import trackrDevice

BASE_URL = "https://platform.thetrackr.com"
_LOGGER = logging.getLogger(__name__)


class trackrApiInterface(object):
    """
    API interface object.
    """

    def __init__(self, email, password):
        """
        Create the Trackr API interface object.
        Args:
            email (str): Trackr account email address.
            password (str): Trackrr account password.
        """
        self.email = email
        self.password = password
        self.token = None
        self.last_api_call = None
        self.state = []
        # get a token
        self.authenticate()
        # get the latest state from the API
        self.update_state_from_api()

    def update_state_from_api(self):
        """
        Pull and update the current state from the API.
        """
        if self.last_api_call is not None:
            difference = (datetime.datetime.now() - self.last_api_call).seconds
        else:
            # This is the first run, so we need to get the lastest state.
            difference = 301
        if difference >= 300:
            url = BASE_URL + "/rest/item"
            payload = {'usertoken': self.token}
            arequest = requests.get(url, params=payload)
            status = str(arequest.status_code)
            if status == '401':
                _LOGGER.info("Token expired? Trying to get a new one.")
                self.authenticate(True)
                arequest = requests.get(url, params=payload)
                status = arequest.status_code
            elif status == '404':
                _LOGGER.error("No devices associated with this account.")
            elif status != '200':
                _LOGGER.error("API error not updating state. " + status)
            else:
                self.state = arequest.json()
            self.last_api_call = datetime.datetime.now()
            _LOGGER.info("Pulled latest state from API.")

    def authenticate(self, reauth=False):
        """
        Authenticate with the API and return an authentication token.
        """
        auth_url = BASE_URL + "/rest/user"
        payload = {'email': self.email, 'password': self.password}
        arequest = requests.get(auth_url, params=payload)
        status = arequest.status_code
        if status != 200:
            if reauth:
                _LOGGER.error("Reauthentication request failed. " + status)
            else:
                _LOGGER.error("Authentication request failed, please check credintials. " + status)
        self.token = arequest.json().get('usertoken')
        if reauth:
            _LOGGER.info("Reauthentication was successful, token updated.")
        else:
            _LOGGER.info("Authentication was successful, token set.")

    def get_trackrs(self):
        """
        Extract each Trackr device from the trackrApiInterface state.
        return a list of all Trackr objects from account.
        """
        trackrs = []
        for trackr in self.state:
            trackrs.append(trackrDevice(trackr, self))
        return trackrs

    def dump_state(self):
        """
        Return the JSON state from the last API poll.
        """
        return self.state
