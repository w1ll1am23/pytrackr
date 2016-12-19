# pytrackr
Python3 interface to the TrackR API.

**NOTE** TrackR has no official API therefore this library could stop working at any time, without warning.

```python
from pytrackr.api import trackrApiInterface

trackr_api = trackrApiInterface("YOUR EMAIL", "YOUR PASSWORD")
device = trackr_api.get_trackrs()[0]

print("Custom name: " + device.name())
print("Location: " + str(device.last_known_location()))
print("Last time seen: " + str(device.last_time_seen()))
print("Tracker ID: " + str(device.tracker_id()))
print("Type: " + str(device.type()))
print("Last upadted: " + str(device.last_updated()))
print("Battery level: " + str(device.battery_level()))
print("\n")

# This will update the api interfaces dictionary
trackr_api.update_state_from_api()

# This will update the devices state from the api dictionary
# and call the api update if needed.
device.update_state_from_api()
```
