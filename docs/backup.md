# Backup

# System Setup
Python3.6 or later is required, and is expected to be mapped to `python3`.

For localized logging, the system logger must have `local0` configured in
`rsyslog`, as this is hardcoded at the moment.

The files in `/backup/stubs` must be copied to `/backup`, with the `.default`
suffix removed.  These files must be modified as specified.
