
class trackrDevice(object):

    def __init__(self, device_state_as_json, api_interface):
        self.api_interface = api_interface
        self.json_state = device_state_as_json

    def name(self):
        return self.json_state.get('customName', None)

    def tracker_id(self):
        return self.json_state.get('trackerId', None)

    def last_time_seen(self):
        return self.json_state.get('lastTimeSeen', None)

    def type(self):
        return self.json_state.get('type', None)

    def last_updated(self):
        return self.json_state.get('lastUpdated', None)

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
