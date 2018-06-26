# lotto_ops

A work in progress lotto monitoring tool.

Note: currently requires they scripts to be copied into lotto.

### Monitoring Lotto Logs in GUI

- Install Flask

- Set up ssh tunneling:
	- Install FoxyProxy on browser
	- Configure Forxyproxy as shown in figure in repo.


- Login to server with
`ssh -D <serving-port-number> <username@serverip>`

example:

`ssh -D 8001 ubuntu@xx.xx.xx.xx`

### Converting Files

To convert files to html:

`python deploy.py -f <name-of-file>`

Files are stored in `templates/`

To deploy server:

`python serveapp.py`

This serve the files in `templates/`

View in browser:

`http://localhost:<serving-port-number>/`

example:

`http://0.0.0.0:8001/`

### Viewing files

At the moment searchable by time only
