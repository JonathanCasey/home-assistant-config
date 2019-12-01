# Debug
A lot of this is general stuff for my own cheat sheet :)

# General

### Tracing system calls
```
sudo -u USER strace CMD
```
where the `-u USER` is optional to see how command execute as a specific user,
and `CMD` is the full shell command being troubleshot.  This will output A LOT
of info, but when all other logs fail, this may give a hint...


### Testing network issues
```
curl -v ADDR:PORT
```
will try to connect and print any output from accessing that address and port.
If just need to check if an error, `curl -f ADDR:PORT` will give nothing on
success, and an error message on failure.

```
sudo tcpdump -i any port PORT
```
can monitor for traffic on a specific port indefinitely.

Listing ports that are listening have a few options:
```
sudo netstat --tcp --listening --programs --numeric
sudo ss -tulwn
sudo lsof -i -P -n | grep LISTEN
sudo netstat -tulpn | grep LISTEN
sudo nmap -sT -O localhost
sudo nmap -sU -O 192.168.1.x ##[ list open UDP ports ]##
sudo nmap -sT -O 192.168.1.x ##[ list open TCP ports ]##
sudo nmap -sTU -O 192.168.1.x
```


# Docker

### Restart single container
```
docker-compose restart CONTAINER_NAME
```

NOTE: If changes made to `docker-compose.yaml`, MUST run:
```
docker-compose up -d CONTAINER_NAME
```
as `restart` does NOT reload yaml.


### Logs
To get logs direct from container:

```
docker ps -a
docker container logs CONTAINER_ID
# where CONTAINER_ID was noted from the ps output
```


### Shell inside container
```
docker exec -it CONTAINER_NAME /bin/bash
```

In general, `/bin/bash` can be replaced with any command to execute inside of
the container.  Success of shell depends on whether the container image has a
shell installed.



# Home Assistant

### Test config file
```
docker exec homeassistant python -m homeassistant --script check_config --config /config
```
where the first `homeassistant` is the container name.

This will allow the configuration to be checked without having to wait for the
entire server to restart if it passes.  It will also show config issues more
immediately.


### Observing issues
In addition to checking the configuration, there is also a log file.  This can
be checked on the local fs within the `homeassistant` dir with
`tail -f home-assistant.log`.  This can also be found on the web UI of portainer
(or any docker log).
