# pytrackr
Python3 interface to the TrackR API.

**NOTE** TrackR has no official API therefore this library could stop working at any time, without warning.

```python
from pytrackr.api import trackrApiInterface

trackr_api = trackrApiInterface("YOUR EMAIL", "YOUR PASSWORD")

# This will dump the state from the API
state = str(trackr_api.dump_state())
print(state)

device = trackr_api.get_trackrs()[0]

print("Custom name: " + str(device.name()))
print("Location: " + str(device.last_known_location()))
print("Last time seen: " + str(device.last_time_seen()))
print("Tracker ID: " + str(device.tracker_id()))
print("ID: " + str(device.id()))
print("Type: " + str(device.trackr_type()))
print("Last upadted: " + str(device.last_updated()))
print("Battery level: " + str(device.battery_level()))
print("Icon: " + str(device.icon()))
print("Time updated diff: " + str(device.time_updated_diff()))
print("Group item: " + str(device.group_item()))
print("Lost: " + str(device.lost()))
print("\n")

# This will update the api interfaces dictionary
trackr_api.update_state_from_api()

# This will update the devices state from the api dictionary
# and call the api update if needed.
device.update_state()
```
