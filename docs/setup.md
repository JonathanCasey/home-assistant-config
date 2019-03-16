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
