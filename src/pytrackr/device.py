import datetime


class trackrDevice(object):

    def __init__(self, device_state_as_json, api_interface):
        self.api_interface = api_interface
        self.json_state = device_state_as_json

    def name(self):
        return self.json_state.get('customName', None)

    def tracker_id(self):
        return self.json_state.get('trackerId', None)

    def ownership_order(self):
        return self.json_state.get('ownershipOrder', None)

    def id(self):
        return self.json_state.get('id', None)

    def icon(self):
        return self.json_state.get('icon', None)

    def time_updated_diff(self):
        # What format is this is?
        return self.json_state.get('timeUpdatedDiff', None)

    def owners_email(self):
        return self.json_state.get('ownersEmail', None)

    def group_item(self):
        # Is this trackr part of a group?
        return self.json_state.get('groupItem', False)

    def lost(self):
        # Was this trackr reported as lost?
        return self.json_state.get('lost', False)

    def last_time_seen(self):
        "ex. Mon Dec 19 17:57:06 UTC 2016"
        return self.json_state.get('lastTimeSeen', None)

    def last_updated(self):
        # This is in Epoch time * 1000. (milliseconds)
        # ex. 1482007969200
        # Converting to match format of last_time_seen.
        last_update = int(self.json_state.get('lastUpdated', None))
        dt = datetime.datetime.utcfromtimestamp(last_update/1000.)
        return dt.strftime('%a %b %d %H:%M:%S UTC %Y')

    def trackr_type(self):
        # Not sure what this is? TrackR Bravo responses with
        # a value of bluetooth.
        return self.json_state.get('type', None)

    def battery_level(self):
        return self.json_state.get('batteryLevel', None)

    def last_known_location(self):
        """
        Return last know location dictionary.
        """
        return self.json_state.get('lastKnownLocation', None)

    def update_state(self):
        self.api_interface.update_state_from_api()
        for device in self.api_interface.state:
            if device.get('trackerId') == self.tracker_id():
                self.json_state = device
