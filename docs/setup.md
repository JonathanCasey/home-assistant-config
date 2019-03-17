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


### Remote development
Doing all development on the hassio platform is a bit cumbersome.  Not only is
the code editing not ideal, but the git installation is limited in functionality
as well.

The best solution to this is to install the
[Samba share addon](https://www.home-assistant.io/addons/samba/) and then mount
the `config` dir using samba.  Not only will this allow direct code editing,
but it will also allow git to be used on the dev machine.



## Secrets
These are in the root `/config` dir unless specified with a subpath in the
heading.

### `secrets.yaml`
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

# A test stringify push url
stringify_ha_test_url:
```

### `plex.conf`
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
