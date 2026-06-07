# Basic knowledge of program systemctl

## systemctl

#### Start, stop, restart, reload and check status for service
`systemctl start/stop/restart/reload/status nginx.service`

#### Enable and disable a service
`systemctl enable/disable nginx.service`

#### Check if service is active, enabled or failed
`systemctl is-active/is-enabled/is-failed nginx.service`

#### Cat service config file
```bash
systemctl cat nginx.service
``` 

#### Show service all info including generated
```bash
systemctl show nginx.service
``` 

#### Show specific parameter in a config file
```bash
systemctl show nginx.service -p Description
``` 

#### Edit service file
Edited data goes to /path/to/original/service/service-name.d/override.conf
```bash
systemctl edit nginx.service
``` 


#### Overwrite service file and send to /etc/systemd/system/service-name.service
```bash
systemctl edit --full nginx.service
``` 

#### Mask a service to prevent from running even mannually or unmask to allow 
`systemctl mask/unmask nginx.service`

#### Reload systemctl daemon to update all changed services
```bash
systemctl daemon-reload
``` 

#### Set default target to load a system
```bash
systemctl set-default multi-user.target
``` 

#### Isolate target to run in it instantly
```bash
systemctl isolate rescue.target
``` 

#### Some isolation targets built it with short-carts
`systemctl reboot/rescue/poweroff` <br/><br/>
For reboot and poweroff there're just the commands

#### List all active/loaded units
```bash
systemctl list-units
``` 

#### List all units
```bash
systemctl list-units --all
``` 

#### Filter units by state
It wiil filter by 3 colums: LOAD, ACTIVE and SUB
```bash
systemctl list-units --all --state=inactive
``` 

#### Filter units by type
```bash
systemctl list-units --all --type=target
``` 

#### Show unit configuration files
Also can be filtered by type
```bash
systemctl list-unit-files
``` 
