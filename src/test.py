import time
from pytrackr.api import trackrApiInterface

def output_device_states():
    for device in devices:
        print("Custom name: " + device.name())
        print("Location: " + str(device.last_known_location()))
        print("Last time seen: " + str(device.last_time_seen()))
        print("Tracker ID: " + str(device.tracker_id()))
        print("Type: " + str(device.type()))
        print("Last upadted: " + str(device.last_updated()))
        print("Battery level: " + str(device.battery_level()))
        print("\n")

def update_states():
    # calling update on one device will update the api interface
    # dictionary which stores all devices states.
    devices[0].update_state_from_api()

email = input("Enter your trackr email: ")
password = input("Enter your trackr password: ")
trackr_api = trackrApiInterface(email, password)
devices = trackr_api.get_trackrs()
output_device_states()
print("\n\nMove your phone/trackr so the location can change.")
print("Sleeping for 2 minutes for a device update. Not sure how long it takes.")
print("Try force closing the app and re-opening it, that should force a location update.")
time.sleep(120)
update_states()
output_device_states()



