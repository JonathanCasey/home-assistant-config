#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "$0" )" && pwd )"

env_file="$SCRIPT_DIR/.secrets.env"
source $env_file

log=0

while getopts "l" opt; do
    case "$opt" in
    l) log=1 ;;
    esac
done

errLog="/tmp/ha-backup-stderr.log"

python="/usr/bin/python3"
script="$SCRIPT_DIR/backup.py"
script="$script"
tmpLog="1> /tmp/ha-backup-stdout.log 2> $errLog"

logStdout="logger -s -t '[HA-Backup]' -p local0.info < /tmp/ha-backup-stdout.log"
logStderr="logger -s -t '[HA-Backup]' -p local0.error < $errLog"

rmStdout="rm /tmp/ha-backup-stdout.log"
rmStderr="rm /tmp/ha-backup-stderr.log"

if [ $log -eq 1 ]; then
  eval $python $script $tmpLog
  eval $logStdout
  eval $logStderr

  if [ -s $errLog ]; then
    SENDEMAIL=/usr/bin/sendemail

    DATE=`date +"%B %-d, %Y"`
    SUBJECT="Error in Server HA Backup for $DATE"
    MESSAGE="___This is real.___<br \>"
    MESSAGE="$MESSAGE System report:<br \>"
    MESSAGE="$MESSAGE Everything is fine.  Nothing is ruined.<br \>"
    MESSAGE="$MESSAGE <br \><br \>...wait...<br \><br \>"
    MESSAGE="$MESSAGE ___Flagrant System Error___<br \>"
    MESSAGE="$MESSAGE The system is down.  I dunno what you did, moron,"
    MESSAGE="$MESSAGE but you sure screwed everything up.<br \>"
    MESSAGE="$MESSAGE<br \><br \>Error log:<br \><br \>"
    ERRMESSAGE=`cat $errLog |  sed ':a;s|^\([[:space:]]*\)[[:space:]]|\1\&nbsp\;|;ta' |  sed ':a;N;$!ba;s|\n|<br />|g'`
    MESSAGE="$MESSAGE $ERRMESSAGE"

    $SENDEMAIL -f "$EMAIL_SEND_NAME" \
               -t "$EMAIL_ADMIN_ADDR" \
               -s "$EMAIL_SERVER_HOST:$EMAIL_SERVER_PORT" \
               -o tls=yes \
               -xu "$EMAIL_USERNAME" \
               -xp "$EMAIL_PASSWORD" \
               -u "$SUBJECT" \
               -m "$MESSAGE" \
               -o message-content-type=html
  fi

  eval $rmStdout
  eval $rmStderr
else
  $python $script
fi
