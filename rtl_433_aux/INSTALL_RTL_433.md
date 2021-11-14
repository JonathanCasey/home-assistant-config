# Installation of RTL_433

### RTL_433 build and install on Ubuntu/Linux

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