# Usage


### Restarting
After changing configuration files, the changes will need to be loaded.  Changes
are loaded by restarting the server, but sometimes partial restart can be done
if only certain modules were affected.

In the web UI, navigating to `Configuration` > `General` will bring up the right
page.  Here, certain reload options may make sense depending on what was
changed.  If not applicable, though, or when it doubt (and definitely if
`configuration.yaml` changed), the `Restart` at the bottom for the server
management will be required.


### Pairing Zigbee devices
To pair Zigbee devices via zigbee2mqtt, the `zigbee2mqtt/configuration.yaml`
will need to be temporarily changed to set `permit_join: true` at the top.  This
should be undone immediately after completion to avoid the security risk of
other, outside devices gaining access.

The device will be added to `devices_new.yaml` since it is the first in the
list.  From there, it can be moved into another file and configured.

It might be best to turn off "enable newly discovered entities" in Home
Assistant until after the device is paired and its settings set, or at least its
name.  Home Assistant will need to be restarted for the device to show up
(probably).
