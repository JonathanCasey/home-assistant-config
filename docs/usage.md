# Usage

### Checking configuration
Running `hassio homeassistant check` will allow the configuration to be checked
without having to wait for the entire server to restart if it passes.  It will
also show config issues more immediately.


### Restarting
After changing configuration files, the changes will need to be loaded.  Changes
are loaded by restarting the server, but sometimes partial restart can be done
if only certain modules were affected.

In the web UI, navigating to `Configuration` > `General` will bring up the right
page.  Here, certain reload options may make sense depending on what was
changed.  If not applicable, though, or when it doubt (and definitely if
`configuration.yaml` changed), the `Restart` at the bottom for the server
management will be required.


### Observing issues
In addition to checking the configuration, there is also a log file.  This can
be checked on the local fs within the `/config` dir with
`tail -f home-assistant.log`.  This can also be found on the web UI at
`Hass.io` > `System` tab.


### Git cred cache
More of a generic git usage item, but I always forget, and other methods don't
work as well due to the limited install nature of hassio.

Per [this section](https://help.github.com/en/enterprise/2.16/user/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent),
the following commands can be executed to start the agent and then add the key:
```
$ eval $(ssh-agent -s)
$ ssh-add ~/.ssh/id_rsa
```

This will cache for the remainder of the terminal session.  This can also be
setup to execute automatically when a terminal session is started so the
command itself does not need to be remembered -- only the password :)
