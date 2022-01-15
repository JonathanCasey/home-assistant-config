# Installation of RTL_433

## RTL_433 build and install on Ubuntu/Linux

From this repo root (from
[merbanan/rtl_433](https://github.com/merbanan/rtl_433/blob/master/docs/BUILDING.md)):
```bash
cd rtl_433
mkdir build
cd build
cmake ..
make
make install
```

When testing a new build over and over, can do `cmake .. && make` to do in one
step.

When not installed, the `rtl_433` binary will be found at
`rtl_433/build/src/rtl_433`.

When installed, it will be found at `/usr/local/bin/rtl_433`.  Note that this is
different from the one that may be installed from apt-get, which is
`/usr/bin/rtl_433`!


## RTL_433 service

### Installation
The `rtl_433_mqtt.service` file must be copied to `/etc/systemd/system`.

If this repo is not cloned to `/opt/home-assistant` the path in the
`rtl_433.service` must be updated accordingly.

The `.secrets.env.stub` file in `rtl_aux` must be renamed to `.secrets.env` and
the credentials in there must be filled out.

Finally, the service must be installed and started:
```bash
sudo systemctl enable rtl_433_mqtt.service
```

### Updating
Any time the `.service` file is updated, it must be updated at
`/etc/systemd/system` (whether editing there or editing here then copying).

After each, the daemon must be reloaded and service restarted:
```bash
sudo systemctl daemon-reload
sudo systemctl restart rtl_433_mqtt.service
```

### Monitoring
To monitor how it is doing, it's as simple as:
```bash
journalctl -f -u rtl_433_mqtt.service
```

This is especially effective if the json flag has been enabled in the
`rtl_433_mqtt.sh` script.  Be warned this WILL flood syslog unless those lines
in the `.service` file are commented out!
