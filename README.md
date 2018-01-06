# RasberryWifi
Interface to support connect wifi in rasberry pi

## How to use:

```python
from wifi import RasberryWifi

wifi = RasberryWifi()
wifi.connect_wifi(ssid="AutonomousTech", wpa="autonomous123")   # connect wifi with password
wifi.connect_wifi(ssid="AutonomousTech", wpa='')                # connect wifi which no password
wifi.active_network()                                           # it will return AutonomousTech
wifi.network_list()                                             # list all networks you have been connected before
```

If there is any issue with this. Feel free to contact me: trongdth@gmail.com
