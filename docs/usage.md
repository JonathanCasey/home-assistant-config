# Usage

### Checking configuration
Running `hassio homeassistant check` will allow the configuration to be checked
without having to wait for the entire server to restart if it passes.  It will
also show config issues more immediately.


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
