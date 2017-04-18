# Too Doo
## a django application example

### start VM
```bash
$ vagrant up
```

### Connect to VM by SSH
```bash
$ vagrant ssh
```
Password - *vagrant*

###Run smtp server
```bash
$ python -m smtpd -n -c DebuggingServer localhost:1025
```
