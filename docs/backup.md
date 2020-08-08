# Backup

# System Setup
Python3.6 or later is required, and is expected to be mapped to `python3`.

For localized logging, the system logger must have `local0` configured in
`rsyslog`, as this is hardcoded at the moment.

The files in `/backup/stubs` must be copied to `/backup`, with the `.default`
suffix removed.  These files must be modified as specified.


# Execution
To manually backup, simply run `./backup.sh` from `/backup`, or directly run the
python script with `python3 backup.py`.

It is recommended to setup a cronjob, such as
```
0 2 1-15/14 * * /path/to/repo/backup/backup.sh
```
which will create a backup every 1st and 15th of the month at 2am.

Be sure to either add this to root's crontab, or chown the entire dir to ensure
the user's crontab has access to all files!
