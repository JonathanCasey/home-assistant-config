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
list.  From there, it can be moved into another file and configured.  It will
also add all other existing devices, too, so these will need to be deleted; but
the bottom most should be the newest paired device.

It might be best to "configure" the mqtt integration in Home Assistant to
re-configure and, on the second step, uncheck "enable discovery" before
pairing and configuring in zigbee2mqtt, at least until the device is named.
Home Assistant will need to be restarted for the device to show up (probably).


### Remove Zigbee devices
See [this section](https://www.zigbee2mqtt.io/information/mqtt_topics_and_message_structure.html#zigbee2mqttbridgerequestdeviceremove)
of the zigbee2mqtt docs.  The easy way to do this is to drop an inject node
into node-red and add the json data as the payload, then connect this to an
mqtt out node that uses the topic `zigbee2mqtt/bridge/request/device/remove`.
