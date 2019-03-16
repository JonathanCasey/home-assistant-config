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


### Rsync
Hassio is very limited in capabilities, and working remotely does make life
easier.

After installing the
[SSH & Web Terminal addon](https://github.com/hassio-addons/addon-ssh),
rsync can be used to push/pull from the machine where dev will be done since it
still will not be installed on the hassio image.

The easiest way to do this is to make the following scripts for easy push/pull
from the dev machine:

`rsync-pull.sh`:
```
#!/bin/bash

rsync -tlpuhrv -e 'ssh -p <port>' <hassio-user>@<hassio-hostname/ip>:/config/ ./ --exclude={.git/*,.storage/*,.cloud/*,*.google.token/*,*__pycache__*,*.db,*.db-shm,*.db-wal,.HA_VERSION} --no-links
```

`rsync-push.sh`:
```
#!/bin/bash

rsync -tlpuhrv ./ -e 'ssh -p <port>' <hassio-user>@<hassio-hostname/ip>:/config/ --exclude={.git/*,.storage/*,.cloud/*,*.google.token/*,*__pycache__*,*.db,*.db-shm,*.db-wal,.HA_VERSION}
--no-links
```

Note that the excludes should generally follow the contents of `.gitignore`,
but are really only critical when it is undesirable to pull data that will
add excess time for transfer for no good reason, and for data that should not
be overwritten when pushing (e.g. the `.db`).
