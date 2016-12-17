# pytrackr
Python3 interface to the Trackr API

```python
import time
import pytrackr

pytrackr.authenticate('email adress here', 'password here')
devices = pytrackr.get_trackrs()

for device in devices:
    print(device.name())
    print(str(device.last_known_location()))
    time.sleep(60)
    device.update_state_from_api()
    print(str(device.last_known_location()))

```
