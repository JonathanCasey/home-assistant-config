# Setup


### Cloning with symlinks in Windows
In order to do this, support will need to be added.  First, git-scm must be
installed with the "Enable symbols links" option selected.

Then, execute the following to enable global support:
```
git config --global core.symlinks true
```

If global support is not desired, then this can be done on an individual repo
basis when cloning with:
```
git clone -c core.symlinks=true <url>
```

Note that administrator access may be necessary to clone and/or work with
symlink files.

See
[this post](https://stackoverflow.com/questions/5917249/git-symlinks-in-windows#answer-52097145)
for some additional info.

#### If showing pending changes...
Note that windows may struggle with "typechange" status.  In this case, it is
recommended to use:
```
git update-index --assume-unchanged <file1> <file2>
```
on all of the symlink files so they do not show as changed.

To undo this, simply run the same command, but with `--no-assume-unchanged`.


### Remote development
Doing all development on the hassio platform is a bit cumbersome.  Not only is
the code editing not ideal, but the git installation is limited in functionality
as well.

The best solution to this is to install the
[Samba share addon](https://www.home-assistant.io/addons/samba/) and then mount
the `config` dir using samba.  Not only will this allow direct code editing,
but it will also allow git to be used on the dev machine.



## Secrets
These are in the root dir unless specified with a subpath in the heading.

### `homeassistant/secrets.yaml`
In `secrets.yaml`, the following keys are expected to be included:
```
# Latitude / Longitude to 6 decimal places.
home_latitude:
home_longitude:

# Gmail creds used for where security will report info for parsing.
gmail_username:
gmail_password:

# Login creds for security system if it will be used.
security_username:
security_password:

# The password for the web login portion of the SSH addon.
ssh_addon_web_password:
```

### `homeassistant/plex.conf`
In `plex.conf`, the json structure will be provided by the addon when installed
as a template, but copying it here:
```
{
   "<server local address>:<server local port>": {
      "ssl": <true/false>,
      "token": "",
      "verify": <true/false>
   }
}
```

The `token` can be obtained as the `X-Plex-Token` as documented
[here](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/).


### Mosquitto `.passwd`
A password file is recommended for mosquitto.  First, get into the shell of the
container:
```
docker exec -it mosquitto /bin/sh
```

Then change to the config and make/append to the password file:
```
$ cd mosquitto/config/
# Create a password file and add the user with password to be specified after
$ mosquitto_passwd -c .passwd user1
# Add another user to the same password file
$ mosquitto_passwd .passwd user2
```

See full docs from mosquitto
[here](https://mosquitto.org/man/mosquitto_passwd-1.html).


### `zigbee2mqtt/secret.yaml`
After creating a user/pass with mosquitto, that will need to be added into this
secret file, along with the network key if `GENERATE` is not used:
```
user: <mosquitto-username>
password: <mosquitto-password>
network_key: <network-key>
```

A network key can be generated using `GENERATE`, though it will not be shown.
This will generate a new key on next start, which will require re-pairing all
devices!

Could also generate via:
```
dd if=/dev/urandom bs=1 count=16 2>/dev/null | od -A n -t x1 | awk '{printf "["} {for(i = 1; i< NF; i++) {printf "0x%s, ", $i}} {printf "0x%s]\n", $NF}'
```

Again, any time the network key is changed, all devices will need to be
re-paired.
