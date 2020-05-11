Reading notes from [Ansible: Up and Running](https://books.google.com/books/about/Ansible_Up_and_Running.html?id=n0bKrQEACAAJ)


# Introduction
Ansible work steps:
1. Generate a Python script that execute a task
2. Copy the script to all hosts
3. Execute the script on all hosts
4. Wait for the script to complete execution on all hosts 

Ansible will then move to the next task in the list.
* Ansible runs each task in parallel across all hosts
* Ansible waits until all hosts have completed a task before moving to the next task
* Ansible runs the tasks in the order that you specify them


# Playbooks
*Example web-notls.yml*
```yaml
- name: Configure webserver with nginx
  hosts: webservers
  sudo: True
  tasks:
    - name: install nginx
      apt: name=nginx update_cache=yes
    
    - name: copy nginx config file
      copy: src=files/nginx.conf dest=/etc/nginx/sites-available/default
      
    - name: enable configuration
      file: >
        dest=/etc/nginx/sites-enabled/default
        src=/etc/nginx/sites-available/default
        state=link
    
    - name: copy index.html
      template: src=templates/index.html.j2 dest=/usr/share/nginx/html/index.html 
        mode=0644
      
    - name: restart nginx
      service: name=nginx state=restarted
```

**TIP** 
YAML truthy: true, True, TRUE, yes, Yes, YES, on, On, ON, y, Y
YAML falsey: false, False, FALSE, no, No, NO, off, Off, OFF, n, N

module arg truthy: yes, on, 1, true
module arg falsey: no, off, 0, false

*Example files/nginx.conf*
```
server {
        listen 80 default_server;
        listen [::]:80 default_server ipv6only=on;
        
        root /usr/share/nginx/html;
        index index.html index.htm;
        
        server_name localhost;
        
        location / {
          try_files $uri $uri/ =404;
        }
}
```

**TIP**
An Ansible convention is to keep files in a subdirectory named *files* and Jinja2 templates in a subdirectory named *templates*.

*Example playbooks/templates/index.html.j2*
```html
<html>
  <head>
    <title>Welcome to ansible</title>
  </head>
  <body>
  <h1>nginx, configured by Ansible</h1>
  <p>If you can see this, Ansible successfully installed nginx.</p>
  
  <p>{{ ansible_managed }}</p>
  </body>
</html>
```
*ansible_managed* : information about when the template file was generated.

## Creating a Webservers Group
Inventory files are in the *.ini* file format.

*Example playbooks/hosts*
```yaml
[webservers]
testserver ansible_ssh_host=127.0.0.1 ansible_ssh_port=2222

```
```shell
$ ansible webservers -m ping
```

## Running the Playbook
```shell
$ ansible-playbook web-notls.yml
```

**TIP**
If your playbook file is marked as executable and starts with a line:
```
#!/usr/bin/env ansible-playbook
```
then you can run it:
```shell
$ ./web-notls.yml
```

## YAML

**Start of File** YAML files are supposed to start with three dashes
```
---
```
However, if you forget to put it, Ansible won't complain.

**Comments**
```
# This is a YAML comment
```

**Strings**
this is a lovely sentence
The JSON equivalent is: 
"this is a lovely sentence"

**Booleans**
True
The JSON equivalent is:
true

**Lists**
```
- My Fair Lady
- Oklahoma
- The Pirates of Penzance
```

The JSON equivalent is:
[
  "My Fair Lady",
  "Oklahoma",
  "The Pirates of Penzance"
]

YAML also supports an inline format for lists
[My Fair Lady, Oklahoma, The Pirates of Penzance]

**Dictionaries**
```
address: 743 Evergreen Terrace
city: Springfield
state: North Takoma
```

The JSON equivalent is:
{
  "address": "742 Evergreeen Terrace",
  "city": "Springfield",
  "state": "North Takoma"
}

YAML also supports an inline format for dictionaries:
{address: 742 Evergreen Terrace, city: Springfield, state: North Takoma}

**Line Folding**

```yaml
address: >
  Department
city: co
state: mar
```

**TIP**
A valid JSON file is also a valid YAML file. 

## Plays
a playbook is a list of dictonaries

Every play must contain:
* A set of hosts to configure
* A list of tasks to be executed on those hosts

There are three common optional settings:
* name : A comment that describes what the play is about
* sudo : run tasks as the root user 
* vars : a list of variables and values

## Tasks

## Modules
```shell
$ ansible-doc service
```

## TLS Support Example

*example web-tls.yml*
```yaml
- name: Configure webserver with nginx and tls
  hosts: webservers
  sudo: True
  vars:
    key_file: /etc/nginx/ssl/nginx.key
    cert_file: /etc/nginx/ssl/nginx.crt
    conf_file: /etc/nginx/sites-available/default
    server_name: localhost
  tasks:
    - name: Install nginx
      apt: name=nginx update_cache=yes cache_valid_time=3600
      
    - name: create directories for ssl certificates
      file: path=/etc/nginx/ssl state=directory
    
    - name: copy TLS key
      copy: src=files/nginx.key dest={{ key_file }} owner=root mode=0600
      notify: restart nginx
      
    - name: copy TLS certificate
      copy: src=files/nginx.crt dest={{ cert_file }}
      notify: restart nginx
      
    - name: copy nginx config file
      template: src=templates/nginx.conf.j2 dest={{ conf_file }}
      notify: restart nginx
      
    - name: enable configuration
      file: dest=/etc/nginx/sites-enabled/default src={{ conf_file }} state=link
      notify: restart nginx
      
    - name: copy index.html
      template: src=templates/index.html.j2 dest=/usr/share/nginx/html/index.html mode=0644
      
    handlers:
      - name: restart nginx
        service: name=nginx state=restarted
```

### Generating TLS certificate
```shell
$ mkdir files
$ openssl req -x509 -nodes -days 3650 -newkey rsa:2048 \
    -subj /CN=localhost \
    -keyout files/nginx.key -out files/nginx.crt
```

**TIP**
**When Quoting is Necessary**
* When you reference a variable righ after specifying the module
```yaml
- name: perform some task
  command: "{{ myapp }} -a foo"
```

* your arguments contains a colon
* The debug module's *msg* argument requires a quoted string to capture the spaces
```yaml
- name: show a debug message
  debug: "msg='The debug module will print a message: neat, eh?'"
```

### Generating the Nginx Configuration Template
*templates/nginx.conf.j2*
```
server {
  listen 80 default_server;
  listen [::]:80 default_server ipv6only=on;
  
  listen 443 ssl;
  
  root /usr/share/nginx/html;
  index index.html index.htm;
  
  server_name {{ server_name }};
  ssl_certificate {{ cert_file }};
  ssl_certificate_key {{ key_file }};
  
  location / {
    try_files $uri $uri/ =404;
  }
}
```

### Handlers
A handler is similar to a task, but it runs only if it has been notified by a task.

Handlers only run after all of the tasks are run, and they only run once, even if they are notified multiple times. They always run in the order that they appear in the play, not the notification order.


# Inventory
**TIP**
There is one host that Ansible automatically adds to the inventory by default: *localhost*
Although Ansible adds the localhost to your inventory automatically, you have to have at least one other host in your inventory file.
In the case where you have no other hosts in your inventory file, you can explicitly add an entry for localhost like this:

localhost ansible_connection=local


*example ansible.cfg*
```
[defaults]
hostfile = inventory
remote_user = vagrant
private_key_file = ~/.vagrant.d/insecure_private_key
host_key_checking = False
```

*Table Behavioral inventory parameters*

| Name                         | Default         | Description                              |
| ---------------------------- | --------------- | ---------------------------------------- |
| ansible_ssh_host             | name of host    | Hostname or IP address to SSH to         |
| ansible_ssh_port             | 22              | Port to SSH to                           |
| ansible_ssh_user             | root            | User to SSH as                           |
| ansible_ssh_pass             | none            | Password to use for SSH authentication   |
| ansible_connection           | smart           | How Ansible will connect to host         |
| ansible_ssh_private_key_file | none            | SSH private key to use for SSH authentication |
| ansible_shell_type           | sh              | Shell to use for commands                |
| ansible_python_interpreter   | /usr/bin/python | Python interpreter on host               |
| ansible_*_interpreter        | none            | Like ansible_python_interpreter for other languages |

## Groups
*example Inventory file for Django app*
```ini
[production]
delaware.example.com
georgia.example.com
maryland.example.com
newhampshire.example.com
newjersey.example.com
newyork.example.com
northcarolina.example.com
pennsylvania.example.com
rhodeisland.example.com
virginia.example.com

[staging]
ontario.example.com
quebec.example.com

[vagrant]
vagrant1 ansible_ssh_host=127.0.0.1 ansible_ssh_port=2222
vagrant2 ansible_ssh_host=127.0.0.1 ansible_ssh_port=2200
vagrant3 ansible_ssh_host=127.0.0.1 ansible_ssh_port=2201

[lb]
delaware.example.com

[web]
georgia.example.com
newhampshire.example.com
newjersey.example.com
ontario.example.com
vagrant1

[task]
newyork.example.com
northcarolina.example.com
maryland.example.com
ontario.example.com
vagrant2

[rabbitmq]
pennsylvania.example.com
quebec.example.com
vagrant3

[db]
rhodeisland.example.com
virginia.example.com
quebec.example.com
vagrant3
```

### Groups of Groups
```
[django:children]
web
task
```

### Numbered Hosts
```ini
[web]
web[1:20].example.com
```
```ini
[web]
web-[a-t].example.com
```

### Hosts and Group Variables
```ini
a.example.com color=red
```

```
[all:vars]
ntp_server=ntp.ubuntu.com

[production:vars]
db_user=dbuser
db_password=pass
```
[<group name>:vars]

You can create a separate variable file for each host and each group

**TIP**
Ansible looks for host variable files in a directory called *host_vars* and group variable files in a directory called *group_vars*. Ansible expects these directories to be either in the directory that contains your playbooks or in the directory adjacent to your inventory file.

*eample groups_vars/production, with dictionaries*
```
db:
  db_user: dbuser
  db_password: pass
  primary:
    host: example.com
    port: 5432
```
{{ db.primary.host }}

*advance* dynamic inventory
$ sudo pip install paramiko
```python
import subprocess
import paramiko
cmd = "vagrant ssh-config vagrant2"
p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
config = paramiko.SSHConfig()
config.parse(p.stdout)
config.lookup("vagrant2")
```

*example vagrant.py*
```python
#!/usr/bin/env python
# Adapted from Mark Mandel's implementation
# https://github.com/ansible/ansible/blob/devel/plugins/inventory/vagrant.py
# License: GNU General Pulbic License, Version 3 <http://www.gnu.org/licenses/>

import argparse
import json
import paramiko
import subprocess
import sys

def parse_args():
	parser = argparse.ArgumentParser(description="Vagrant inventory script")
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('--list', action='store_true')
	group.add_argument('--host')
	return parser.parse_args()
	
def list_running_hosts():
	cmd = "vagrant status --machine-readable"
	status = subprocess.check_output(cmd.split()).rstrip()
	hosts = []
	for line in status.split('\n'):
		(_, host, key, value) = line.split(',')
		if key == 'state' and value == 'running':
			hosts.append(host)
	return hosts
	
def get_host_details(host):
	cmd = "vagrant ssh-config {}".format(host)
	p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
	config = paramiko.SSHConfig()
	config.parse(p.stdout)
	c = config.lookup(host)
	return {'ansible_ssh_host': c['hostname'],
			'ansible_ssh_port': c['port'],
			'ansbile_ssh_user': c['user'],
			'ansible_ssh_private_key_file': c['identityfile'][0]}
			

def main():
	args = parse_args()
	if args.list:
		hosts = list_running_hosts()
		json.dump({'vagrant': hosts}, sys.stdout)
	else:
		details = get_host_details(args.host)
		json.dump(details, sys.stdout)
		
if __name__ == '__main__':
	main()
```

config inventory file location
*ansible.cfg*
```
[defaults]
hostfile = inventory
```

### Adding Entries at Runtime
**add_host** module adds a host to the inventory.
```yaml
add_host name=hostname groups=web,staging myvar=myval
```
Specifying the list of groups and additional variables is optional.
**TIP**
The *add_host* module adds the host only for the duration of the execution of the playbook. It does not modify your inventory file.

**group_by** module creates a group based on a fact(see next Chapter) value.
```yaml
- name: create groups based on Linux distribution
  group_by: key={{ ansible_distribution }}
```

###Dynamic Inventory Script
dynamic.py
- --host=<hostname> for showing host details
- --list for listing groups



# Variables and Facts
The simplest way to define variables is to put a vars section in playbook.
```yaml
vars:
  key_file: /etc/nginx/ssl/nginx.key
  server_name: localhost
```
Ansible also allows you to put variables into one or more files.
```yaml
vars_files:
  - nginx.yml
```
nginx.yml
```yaml
key_file: /etc/nginx/ssl/nginx.key
server_name: localhost
```

Debug the value of Variables
```yaml
- debug: var=myvarname
```

Registering Variables
```yaml
- name: capture output of whoami command
  command: whoami
  register: login
```

*Example whoami.yml*
```yaml
- name: show return value of command module
  hosts: server1
  tasks:
    - name: capture output of id command
      command: id -un
      register: login
    - debug: var=login
```
```yaml
- name: capture output of id command
  command: id -un
  register: login
- debug: msg="Logged in as user {{ login.stdout }}"
```
```yaml
- name: Run myprog
  command: /opt/myprog
  register: result
  ignore_errors: True
- debug: var=result
```

Accessing Dictionary Keys in a Variable
you can access the keys of the dictionary using either a dot (.) or a subscript ([]).

TIP make sure you know the content of a variable, both for cases where the module changes the host's state and for when the module doesn't change the host's state.

## Facts

*Example print out operating system*

```yaml
- name: print out operating system
  hosts: all
  gather_facts: True
  tasks:
  - debug: var=ansible_distribution
```

View All Facts

```shell
$ ansible server1 -m setup
```

View a Subset of Facts

```shell
$ ansible server1 -m setup -a 'filter=ansible_eth*'
```

### Local Facts

Ansible also provides an additional mechanism for associating facts with a host. You can place one or more files on the hosts machine in the */etc/ansible/facts.d* directory.

Ansible will recognize the file if it is:

* .ini format
* JSON format
* An executable that takes no arguments and outputs JSON on standard out

These facts are available as keys of a speical variable : ansible_local

*Example /etc/ansible/facts.d/example.fact  .ini format*

```ini
[book]
title=Ansible: Up and Running
author=Lorin Hochstein
publisher=O'Reilly Media
```

we can access the contents:

```yaml
- name: print ansible_local
  debug: var=ansible_local
- name: print book title
  debug: msg="The title of the book is {{ ansible_local.example.book.title }}"
```



### Using set_fact to Define a New Variable
*Example Using set_fact to simplify variable reference*
```yaml
- name: get snapshot id
  shell: >
    aws ec2 describe-snapshots --filters
    Name=tag:Name,Values=my-snapshots
    | jq --raw-output ".Snapshots[].SnapshotId"
    register: snap_result
    
- set_fact: snap={{ snap_result.stdout }}

- name: delete old snapshot
  command: aws ec2 delete-snapshot --snapshot-id "{{ snap }}"
```

## Built-in Variables

| Parameter                | Description                              |
| ------------------------ | ---------------------------------------- |
| hostvars                 | A dict whose keys are Ansible host names and values are dicts that map variable names to values |
| inventory_hostname       | Name of the current host as known by Ansible |
| inventory_hostname_short | Name of the current host as known by Ansible, without domain name |
| group_names              | A list of all groups that the current host is a member of |
| groups                   | A dict whose keys are Ansible group names and values are a list of hostnames that are members of the group. Includes all and ungrouped groups: {"all": […], "web": […], "ungrouped": [...] } |
| ansible_check_mode       | A boolean that is true when running in check mode |
| ansible_play_hosts       | A list of all of the inventory hostnames that are active in the current play |
| ansible_play_batch       | A list of the inventory hostnames that are active in the current batch |
| play_hosts               | A list of inventory hostnames that are active in the current play |
| ansible_version          | A dict with Ansible version info         |


### hostvars
In Ansible, variables are scoped by host. If you define a variable in the vars section of a play, you are defining the variable for the set of hosts in the play. But what Ansible is really doing is creating a copy of that variable for each host in the group.

If Ansible has not yet gathered facts on a host, then you will not be able to access its facts using the hostvars variable, unless fact caching is enabled.

*hostvars example*

{{ hostvars['db.example.com'].ansible_eth1.ipv4.address }}

This would evaluate to the *ansible_eth1.ipv4.address* fact associated with the host named *db.example.com*

### inventory_hostname
you can output all of the variables associated with the current host:
```yaml
- debug: var=hostvars[inventory_hostname]
```

### Groups
Example, need the IP addresses of all of the servers in our web group:
```
backend web-backend
{% for host in groups.web %}
  server {{ host.inventory_hostname }} {{ host.ansible_default_ipv4.address }}:80
{% endfor %}
```

## Setting Variables on the Command Line
Variables set by passing -e var=value to ansible-playbook have the highest precedence.

*Example greet.yml*
```yaml
- name: pass a message on the command line
  hosts: localhost
  vars:
    greeting: "you didn't specify a message"
  tasks:
    - name: output a message
      debug: msg="{{ greeting }}"
```
```shell
# case 1
$ ansible-playbook greet.yml -e greeting=hiya
# case 2
$ ansible-playbook greet.yml -e 'greeting="hi there"'
# case 3
$ ansible-playbook greet.yml -e @greetvars.yml
```
*greetvars.yml*
```
greeting: hiya
```

## Precedence
The basic rules of precedence:
1. (Highest) ansible-playbook -e var=value
2. Task variables
3. Block variables
4. Role and include variable
5. set_fact
6. Registered variables
7. vars_files
8. vars_prompt
9. Play variables
10. Host facts
11. host_vars set on a playbook
12. group_vars set on a playbook
13. host_vars set in the inventory
14. group_vars set in the inventory
15. Inventory variables
16. In defaults/main.yml of a role




# Real Application Example

Listing Tasks in a Playbook
```
$ ansible-playbook --list-tasks xxx.yml
```

Using Iteration (with_items)
```yaml
- name: install apt packages
  apt: pkg={{ item }} update_cache=yes cache_valid_time=3600
  sudo: True
  with_items:
    - git
    - libjped-dev
    - nginx
    - python-dev
```

Specifying package names and version
```yaml
- name: python packages
  pip: name={{ item.name }} version={{ item.version }} virtualenv={{ venv_path }}
  with_items:
    - { name: mezzanine, version: 3.1.10 }
    - { name: gunicorn, version: 19.1.1 }
    - { name: setproctitle, version: 1.1.8 }
    - { name: south, version: 1.0.1 }
    - { name: psycopg2, version: 2.5.4 }
    - { name: django-compressor, version: 1.4 }
    - { name: python-memcached, version: 1.53 }
```
```yaml
- name: install package with pip
  pip: >
    name={{ item.name }}
    version={{ item.version }}
    virtualenv={{ venv_path }}
```
```yaml
- name: install package with pip
  pip:
    name: "{{ item.name }}"
    version: "{{ item.version }}"
    virtualenv: "{{ venv_path }}"
```

If you are specifying an octal value as a complex argument, it must either start the value with a  0 or quote it as a string
```yaml
- name: copy index.html
  copy:
    src: files/index.html
    dest: /usr/share/nginx/html/index.html
    mode: "0644"
```

create postgresql database and database user
```yaml
- name: create a user
  postgresql_user:
    name: "{{ database_user }}"
    password: "{{ db_pass }}"
  sudo: True
  sudo_user: postgres
  
- name: create the database
  postgresql_db:
    name: "{{ database_name }}"
    owner: "{{ database_user }}"
    encoding: UTF8
    lc_ctype: "{{ locale }}"
    lc_collate: "{{ locale }}"
    template: template0
  sudo: True
  sudo_user: postgres
```

Example local_settings.py.j2
```
from __future__ import unicode_literals

SECRET_KEY = "{{ secret_key }}"
NEVERCACHE_KEY = "{{ nevercache_key }}"
ALLOWED_HOSTS = [{% for domain in domains %}"{{ domain }}",{% endfor %}]

DATABASES = {
  "default": {
    # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
    "ENGINE": "django.db.backends.postgresql_psycopg2",
    # DB name or path to database file if using sqlite3
    "NAME": "{{ proj_name }}",
    # Not used with sqlite3
    "USER": "{{ proj_name }}",
    # Not used with sqlite3
    "PASSWORD": "{{ db_pass }}",
    # Set to empty string for localhost. Not used with sqlite3
    "HOST": "127.0.0.1",
    # Set to empty string for default. Not used with sqlite3
    "PORT": "",
  }
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")
CACHE_MIDDLEWARE_SECONDS = 60
CACHE_MIDDLEWARE_KEY_PREFIX = "{{ proj_name }}"

CACHES = {
  "default": {
    "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
    "LOCATION": "127.0.0.1:11211",
  }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
```

example
```yaml
- name: sync the database, apply migrations, collect static content
  django_manage:
    command: "{{ item }}"
    app_path: "{{ proj_path }}"
    virtualenv: "{{ venv_path }}"
  with_items:
    - syncdb
    - migrate
    - collectstatic
```

Example Using the script module to invoke custom Python code
```yaml
- name: set the site id
  script: scripts/setsite.py
  environment:
    PATH: "{{ venv_path }}/bin"
    PROJECT_DIR: "{{ proj_path }}"
    WEBSITE_DOMAIN: "{{ live_hostname }}"
    
- name: set the admin password
  script: scripts/setadmin.py
  environment:
    PATH: "{{ venv_path }}/bin"
    PROJECT_DIR: "{{ proj_path }}"
    ADMIN_PASSWORD: "{{ admin_pass }}"
```

Example scripts/setsite.py
```python
#!/usr/bin/env python
# A script to set the site domain
# Assumes two environment variables
#
# PROJECT_DIR: the project directory (e.g., ~/projname)
# WEBSITE_DOMAIN: the domain of the site (e.g., www.example.com)

import os
import sys

# Add the project directory to system path
proj_dir = os.path.expanduser(os.environ['PROJECT_DIR'])
sys.path.append(proj_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.conf import settings
from django.contrib.sites.models import Site

domain = os.environ['WEBSITE_DOMAIN']
Site.objects.filter(id=settings.SITE_ID).update(domain=domain)
Site.objects.get_or_create(domain=domain)
```

Example scripts/setadmin.py
```python
#!/usr/bin/env python
# A script to set the admin credentials
# Assumes two environment variables
#
# PROJECT_DIR: the project directory (e.g., ~/projname)
# ADMIN_PASSWORD: admin user's password

import os
import sys

# Add the project directory to system path
proj_dir = os.path.expanduser(os.environ['PROJECT_DIR'])
sys.path.append(proj_dir)

os.environ['DJANDO_SETTINGS_MODULE'] = 'settings'

from mezzanine.utils.models import get_user_model
User = get_user_model()
u, _ = User.objects.get_or_create(username='admin')
u.is_staff = u.is_superuser = True
u.set_password(os.environ['ADMIN_PASSWORD'])
u.save()
```

configuration file for Gunicorn, nginx and Supervisor
```yaml
- name: set the gunicorn config file
  template: src=templates/gunicorn.conf.py.j2 dest={{ proj_path }}/gunicorn.conf.py
  
- name: set the supervisor config file
  template: src=templates/supervisor.conf.j2 dest=/etc/supervisor/conf.d/mezzanine.conf
  sudo: True
  notify: restart supervisor
  
- name: set the nginx config file
  template: src=templates/nginx.conf.j2 dest=/etc/nginx/site-avaiable/mezzanine.conf
  notify: restart nginx
  sudo: True
  
handlers:
  - name: restart supervisor
    supervisorctl: name=gunicorn_mezzanine state=restarted
    sudo: True
    
  - name: restart nginx
    service: name=nginx state=restarted
    sudo: True
```

Example templates/gunicorn.conf.py.j2
```
from __future__ import unicode_literals
import multiprocessing

bind = "127.0.0.1:{{ gunicorn_port }}"
workers = multiprocessing.cpu_count() * 2 + 1
loglevel = "error"
proc_name = "{{ proj_name }}"
```
Example templates/supervisor.conf.j2
```
[group: {{ proj_name }}]
programs=gunicorn_{{ proj_name }}

[program:gunicorn_{{ proj_name }}]
command={{ venv_path }}/bin/gunicorn_django -c gunicorn.conf.py -p gunicorn.pid
directory={{ proj_path }}
user={{ user }}
autostart=true
autorestart=true
redirect_stderr=true
environment=LANG="{{ locale }}",LC_ALL="{{ locale }}",LC_LANG="{{ locale }}"
```
Example templates/nginx.conf.j2
```
upstream {{ proj_name }} {
  server 127.0.0.1:{{ gunicorn_port }};
}

server {
  listen 80;
  
  {% if tls_enabled %}
  listen 443 ssl;
  {% endif %}
  server_name {{ domains|join(", ") }};
  client_max_body_size 10M;
  keepalive_timeout    15;
  
  {% if tls_enabled %}
  ssl_certificate        conf/{{ proj_name }}.crt;
  ssl_certificate_key    conf/{{ proj_name }}.key;
  ssl_session_cache      shared:SSL:10m;
  ssl_session_timeout    10m;
  # ssl_ciphers entry is too long to show in this book
  ssl_prefer_server_ciphers on;
  {% endif %}
  
  location / {
    proxy_redirect       off;
    proxy_set_header     Host                   $host;
    proxy_set_header     X-Real-IP              $remote_addr;
    proxy_set_header     X-Forwarded-For    $proxy_add_x_forwarded_for;
    proxy_set_header     X-Forwarded-Protocol   $scheme;
    proxy_pass           http://{{ proj_name }};
  }
  
  location /static/ {
    root           {{ proj_path }};
    access_log     off;
    log_not_found  off;
  }
  
  location /robots.txt {
    root           {{ proj_path }}/static;
    access_log     off;
    log_not_found  off;
  }
  
  location/favicon.ico {
    root           {{ proj_path }}/static/img;
    access_log     off;
    log_not_found  off;
  }
}
```

The convention with nginx configuration files is to put your configuration files in /etc/nginx/site-available and enable them by symlinking them into /etc/nginx/sites-enabled

Example Enabling nginx configuration
```
- name: enable the nginx config file
  file:
    src: /etc/nginx/sites-available/mezzanine.conf
    dest: /etc/nginx/sites-enabled/mezzanine.conf
    state: link
  notify: restart nginx
  sudo: True
  
- name: remove the default nginx config file
  file: path=/etc/nginx/site-enabled/default state=absent
  notify: restart nginx
  sudo: True
```

Installing TLS Certificates
```yaml
- name: ensure config path exists
  file: path={{ conf_path }} state=directory
  sudo: True
  when: tls_enabled

- name: create self-signed tls certificates
  command: >
    openssl req -new -x509 -nodes -out {{ proj_name }}.crt
    -keyout {{ proj_name }}.key -subj '/CN={{ domains[0] }}' -days 3650
    chdir={{ conf_path }}
    creates={{ conf_path }}/{{ proj_name }}.crt
  sudo: True
  when: tls_enabled
  notify: restart nginx
```
The chdir parameter changes directory before running the command. The creates parameter implements idempotence. will check if the file exists , will skip this task.

Installing Twitter Cron Job
```yaml
- name: install poll twitter cron job
  cron: name="poll twitter" minute="*/5" user={{ user }} job="{{ manage }} poll_twitter" 
```
list cron job
```
$ crontab -l
```
```yaml
- name: remove cron job
  cron: name="poll twitter" state=absent
```

## The complete playbook
```yaml
---
- name: Deploy mezzanine
  hosts: web
  vars:
    user: "{{ ansible_ssh_user }}"
    proj_name: mezzanine-example
    venv_home: "{{ ansible_env.HOME }}"
    venv_path: "{{ venv_home }}/{{ proj_name }}"
    proj_dirname: project
    proj_path: "{{ venv_path }}/{{ proj_dirname }}"
    reqs_path: requirements.txt
    manage: "{{ python }} {{ proj_path }}/manage.py"
    live_hostname: 192.168.33.10.xip.io
    domains:
      - 192.168.33.10.xip.io
      - www.192.168.33.10.xip.io
    repo_url: git@github.com:lorin/mezzanine-example.git
    gunicorn_port: 8000
    locale: en_US.UTF-8
    # Variables below don't appear in Mezannie's fabfile.py
    # but I've added them for convenience
    conf_path: /etc/nginx/conf
    tls_enabled: True
    python: "{{ venv_path }}/bin/python"
    database_name: "{{ proj_name }}"
    database_user: "{{ proj_name }}"
    database_host: localhost
    database_port: 5432
    gunicorn_proc_name: mezzanine
  vars_files:
    - secrets.yml
  tasks:
    - name: install apt packages
      apt: pkg={{ item }} update_cache=yes cache_valid_time=3600
      sudo: True
      with_items:
        - git
        - libjped-dev
        - libpq-dev
        - memcached
        - nginx
        - postgresql
        - python-dev
        - python-pip
        - python-psycopg2
        - python-setuptools
        - python-virtualenv
        - supervisor

    - name: check out the repository on the host
      git: repo={{ repo_url }} dest={{ proj_path }} accept_hostkey=yes
      
    - name: install required python packages
      pip: name={{ item }} virtualenv={{ venv_path }}
      with_items:
        - gunicorn
        - setprotitle
        - south
        - psycopg2
        - django-compressor
        - python-memcached

    - name: install requirements.txt
      pip: requirements={{ proj_path }}/{{ reqs_path }} virtualenv={{ venv_path }}
      
    - name: create a user
      postgresql_user:
        name: "{{ database_user }}"
        password: "{{ db_pass }}"
      sudo: True
      sudo_user: postgres
      
    - name: create the database
      postgresql_db:
        name: "{{ database_name }}"
        owner: "{{ database_user }}"
        encoding: UTF8
        lc_ctype: "{{ locale }}"
        lc_collate: "{{ locale }}"
        template: template0
      sudo: True
      sudo_user: postgres
      
    - name: generate the settings file
      template:
        src: templates/local_settings.py.j2
        dest: "{{ proj_path }}/local_settings.py"
        
    - name: sync the database, apply migrations, collect static content
      django_manage:
        command: "{{ item }}"
        app_path: "{{ proj_path }}"
        virtualenv: "{{ venv_path }}"
      with_items:
        - syncdb
        - migrate
        - collectstatic

    - name: set the site id
      script: scripts/setsite.py
      environment:
        PATH: "{{ venv_path }}/bin"
        PROJECT_DIR: "{{ proj_path }}"
        WEBSITE_DOMAIN: "{{ live_hostname }}"
        
    - name: set the admin password
      script: scripts/setadmin.py
      environment:
        PATH: "{{ venv_path }}/bin"
        PROJECT_DIR: "{{ proj_path }}"
        ADMIN_PASSWORD: "{{ admin_pass }}"
        
    - name: set the gunicorn config file
      template:
        src: templates/gunicorn.conf.py.j2
        dest: "{{ proj_path }}/gunicorn.conf.py"
        
    - name: set the supervisor config file
      template:
        src: templates/supervisor.conf.j2
        dest: /etc/supervisor/conf.d/mezzanine.conf
      sudo: True
      notify: restart supervisor
      
    - name: set the nginx config file
      template:
        src: templates/nginx.conf.j2
        dest: /etc/nginx/sites-available/mezzanine.conf
        notify: restart nginx
        sudo: True
        
    - name: enable the nginx config file
      file:
        src: /etc/nginx/sites-available/mezzanine.conf
        dest: /etc/nginx/sites-enabled/mezzanine.conf
        state: link
      notify: restart nginx
      sudo: True
      
    - name: remove the default nginx config file
      file: path=/etc/nginx/sites-enabled/default state=absent
      notify: restart nginx
      sudo: True
      
    - name: ensure config path exists
      file: path={{ conf_path }} state=directory
      sudo: True
      when: tls_enabled
      
    - name: create tls certificates
      command: >
        openssl req -new -x509 -nodes -out {{ proj_name }}.crt
        -keyout {{ proj_name }}.key -subj '/CN={{ domains[0] }}' -days 3650
        chdir={{ conf_path }}
        creates={{ conf_path }}/{{ proj_name }}.crt
      sudo: True
      when: tls_enabled
      notify: restart nginx
      
    - name: install poll twitter cron job
      corn: name="poll twitter" minute="*/5" user={{ user }}
        job="{{ manage }} poll_twitter"
        
  handlers:
    - name: restart supervisor
      supervisorctl: name=gunicorn_mezzaine state=restarted
      sudo: True
      
    - name: restart nginx
      service: name=nginx state=restarted
      sudo: True
```


# Complex Playbooks

**Running a task on the control machine**
```yaml
- name: wait for ssh server to be running
  local_action: wait_for port=22 host="{{ inventory_hostname }}" search_regex=OpenSSH
```

## Manually gathering facts
```yaml
- name: Deploy mezzanine
  hosts: web
  gather_facts: False
  tasks:
    - name: wait for ssh server to be running
      local_action: wait_for port=22 host="{{ inventory_hostname }}" search_regex=OpenSSH
      
    - name: gather facts
      setup:
```

**Runnning on one host at a time**
```yaml
- name: upgrade packages on servers behind load balancer
  hosts: myhosts
  serial: 1
  max_fail_percentage: 25
  tasks:
```

**Running only once**
```yaml
- name: run the task locally, only once
  local_action: command /opt/my-command
  run_once: true
```

**changed_when** defines when a task is changing server state
**failed_when** defines when a task should fail or continue
example idempotent manage.py createdb
```yaml
- name: initialize the database
  django_manage:
    command: createdb --noinput --nodata
    app_path: "{{ proj_path }}"
    virtualenv: "{{ venv_path }}"
  register: result
  changed_when: not result.failed and "Creating tables" in result.out
  failed_when: result.failed and "Database already created" not in result.msg
```

**Retrieving the IP Address from the Host**
Each network interface has an associated Ansible fact
$ ansible -m setup localhost -a "filter=ansible_eth0"

```yaml
live_hostname: "{{ ansible_eth1.ipv4.address }}.xip.io"
domains:
  - ansible_eth1.ipv4.address.xip.io
  - www.ansible_eth1.ipv4.address.xip.io
```

## Encrypting Sensitive Data with Vault
ansible-vault commands

`ansible-vault encrypt file.yml`	
Encrypt the plaintext file.yml file

`ansible-vault decrypt file.yml`	
Decrypt the encrypted file.yml file

`ansible-vault view file.yml`		
Print the contents of the encrypted file.yml file

`ansible-vault create file.yml`	
Create a new encrypted file.yml file

`ansible-vault edit file.yml`		
Edit an encrypted file.yml file

`ansible-vault rekey file.yml`	
Change the password on an encrypted file.yml file

tell ansible-playbook to prompt for the password
`$ ansible-playbook mezzanine.yml --ask-vault-pass`

store the password in a text file and tell ansible-playbook the location
`$ ansible-playbook mezzanine --vault-password-file ~/password.txt`

If the argument to --vault-password-file has the executable bit set, Ansible will execute it and use the contents of standard out as the value password.

**Patterns for Specifying Hosts**

Supported patterns
| | |
|-|-|
| All hosts | all |
| All hosts | * |
| Union | dev:staging |
| Intersection | staging:&database |
| Exclusion	   | dev:!queue |
| Wildcard | *.example.com |
| Range of number | web[5:10] |
| Regular expression |   ~web\d\.example\.(com |

Note that the regular expression pattern always starts with a tilde

**Limiting Which Hosts Run**
$ ansible-playbook -l hosts playbok.yml
$ ansible-playbook --limit hosts playbook.yml
$ ansible-playbook -l 'staging:&database' playbook.yml

## Filters
**The Default Filter**
"Host": "{{ database_host | default('localhost') }}",

**Filters for Registered Variables**
Task return value filters
| | |
|-|-|
| failed | True if a registered value is a task that failed |
| changed | True if a registered value is a task that changed |
| success | True if a registered value is a task that succeeded |
| skipped | True if a registered value is a task that was skipped |

example
```yaml
- name: Run myprog
  command: /opt/myprog
  register: result
  ignore_errors: True
  
- debug: var=result

- debug: msg="Stop running the playbook if myprog failed"
  failed_when: result|failed
```

**Filters that apply to File Paths**
| | |
|-|-|
| dirname | Directory of file path |
|expanduser | File path with ~replaced by home directory |
| realpath  | Canonical path of file path, resolves symbolic links |
| basename  |  filename from the full path |

example
```yaml
vars:
  homepage: /usr/share/nginx/html/index.html
tasks:
- name: copy home page
  copy: src=files/{{ homepage | basename }} dest={{ homepage }}
```

**Writing Your Own Filter**
Ansible will look for custom filters in the filter_plugins directory, relative to the directory where your playbooks are
Example filter_plugins/surround_by_quotes.py
```python
def surround_by_quote(a_list):
    return ['"%s"' % an_element for an_element in a_list]
    
class FilterModule(object):
    def filters(self):
        return {'surround_by_quote': surround_by_quote}
```

## Lookups
| | |
|-|-|
| file | Contents of a file |
| password | Randomly generate a password |
| pipe | Output of locally executed command |
| env  | Environment variable |
| template | Jinja2 template after evaluation |
| csvfile  | Entry in a .csv file |
| dnstxt   | DNS TXT record |
| redis_kv | Redis key lookup |
| etcd     | etcd key lookup |

**file** example authorized_keys.j2
`{{ lookup('file', '/User/a/.ssh/id_rsa.pub') }}`

task to generate authorized_keys
```yaml
- name: copy authorized_host file
  template: src=authorized_keys.j2 dest=/home/deploy/.ssh/authorized_keys
```

**pipe** example
```yaml
- name: get SHA of most recent commit
  debug: msg="{{ lookup('pipe', 'git rev-parse HEAD') }}"
```

**env** example
```yaml
- name: get the current shell
  debug: msg="{{ lookup('env', 'SHELL') }}"
```

**password** example
```yaml
- name: create deploy pstgres user
  postgresql_user:
  name: deploy
  password: "{{ lookup('password', 'deploy-password.txt') }}"
```

**template** lookup returns the result of evaluating the template.
example message.j2
```
This host runs {{ ansible_disctribution }}
```
```yaml
- name: output message from template
  debug: msg="{{ lookup('template', 'message.j2') }}"
```

**csvfile** example
user.csv
username,email
john,john@example.com
sue,sue@example.com
```
lookup('csvfile', 'sue file=users.csv delimiter=, col=1')
```
or use a variable with + sign
```
lookup('csvfile', username + 'file=users.csv delimiter=, col=1')
```

*Note* **dnstxt** module requires that you install the dnspython Python package on the control machine

DNS works by associating one or more records with a hostname. The most commonly used types of DNS records are A records and CNAME records, which associate a hostname with an IP address (A record) or specify that a hostname is an alias for another hostname (CNAME record).

A TXT record is just an arbitrary string that you attach to a hostname
example using dig to lookup a TXT record
```
$ dig +short ansiblebook.com TXT
"isbn=978-1111"
```
```yaml
- name: look up TXT record
  debug: msg="{{ lookup('dnstxt', 'ansiblebook.com') }}"
```
If there are multiple TXT records associated with a host, then the module will concatenate them together, and it might do this in a different order each time it is called.

*Note* **redis_kv** module requires that you install the redis Python package on the control machine

Redis is a popular key-value store, commonly used as a cache, as well as a data store for job queue services. You can use the redis_kv lookup to retrieve the value of a key. The key must be a string, as the module does the equivalent of calling the Redis GET command.

example 
```
$ redis-cli SET weather summy
```
```yaml
- name: look up value in Redis
  debug: msg="{{ lookup('redis_kv', 'redis://localhost:6379,weather') }}"
```
The module will default to redis://localhost:6379 if the URL isn't specified, so we could have invoked the module like this (note the comma before the key)
```
lookup('redis_kv', ',weather')
```

**etcd** is a distributed key-value store, commonly used for keeping configuration data and for implementing service discovery.

*Note* need a etcd server running on our control machine
```
$ curl -L http://127.0.0.1:4001/v2/keys/weather -XPUT -d value=cloudy
```
```yaml
- name: look up value in etcd
  debug: msg="{{ lookup('etcd', 'weather') }}"
```
By default, the etcd lookup will look for the etcd server at http://127.0.0.1:4001, but you can change this by setting the ANSIBLE_ETCD_URL environment variable

**Writing Your Own Lookup Plug-in**
Once you've written your lookup plug-in, place it in one of the following directories:
* The *lookup_plugins* directory next to your playbook
* */usr/share/ansible_plugins/lookup_plugins*
* The directory specified in your ANSIBLE_LOOKUP_PLUGINS environment variable

## More Complicated Loops
Looping constructs

| Name                     | Input                | Looping strategy                  |
| ------------------------ | -------------------- | --------------------------------- |
| with_items               | list                 | Loop over list elements           |
| with_lines               | command to execute   | Loop over lines in command output |
| with_fileglob            | glob                 | Loop over filename                |
| with_first_found         | list of paths        | First file in input that exists   |
| with_dict                | dictionary           | Loop over dictionary elements     |
| with_flattened           | list of lists        | Loop over flattened list          |
| with_indexed_items       | list                 | Single iteration                  |
| with_nested              | list                 | Nested loop                       |
| with_random_choice       | list                 | Single iteration                  |
| with_sequence            | sequence of integers | Loop over sequence                |
| with_subelements         | list of dictionaries | Nested loop                       |
| with_together            | list of lists        | Loop over zipped list             |
| with_inventory_hostnames | host pattern         | Loop over matching hosts          |

Example **with_lines** send a Slack message for each name,
```
Leslite Lamport
Silvio Micali
Shafi Goldwasser
Judea Pearl
```
```yaml
- name: Send out a slack message
  slack:
    domain: example.slack.com
    token: "{{ slack_token }}"
    msg: "{{ item }} was in the list"
  with_lines:
    - cat files/turing.txt
```

Example **with_fileglob** add public keys
```yaml
- name: add public keys to account
  authorized_key: user=deploy key="{{ lookup('file', item) }}"
  with_fileglob:
    - /var/keys/*.pub
    - keys/*.pub
```

Example **with_dict**
```yaml
- name: iterate over ansible_eth0
  debug: msg={{ item.key }}={{ item.value }}
  with_dict: ansible_eth0.ipv4
```

Example using the file lookup as a loop
```yaml
- name: add my public key as an EC2 key
  ec2_key: name=mykey key_material="{{ item }}"
  with_file: /Users/ausible/.ssh/id_rsa.pub
```
lookup returns strings. loop constructs returns lists

### Loop Controls with version 2.1
The loop_var controll allows user to give the iteration variable a different name than the default name, item
Example Use user as loop variable
```yaml
- user:
    name: "{{ user.name }}"
  with_items:
    - { name: gil }
    - { name: sarina }
    - { name: leanne }
  loop_control:
    loop_var: user
```

Example use vhost as loop variable, change the loop variable name for outer loops to prevent name collisions
```yaml
- name: run a set of tasks in one loop
  include: vhosts.yml
  with_items:
    - { domain: www1.example.com }
    - { domain: www2.example.com }
    - { domain: www3.example.com }
  loop_control:
    loop_var: vhost
```

Example Included file can contain a loop. We keep the default loop variable in the inner loop
```yaml
- name: create nginx directories
  file:
    path: /var/www/html/{{ vhost.domain }}/{{ item }}
  state: directory
  with_items:
    - logs
    - public_http
    - public_https
    - includes

- name: create nginx vhost config
  template:
    src: "{{ vhost.domain }}.j2"
    dest: /etc/nginx/conf.d/{{ vhost.domain }}.conf
```

### Labeling the Output in Ansible 2.2
The label control provides some control over how the loop output will be shown to the user during execution.
Example an ordinary list of dictionaries
```yaml
- name: create nginx vhost configs
  template:
    src: "{{ item.domain }}.conf.j2"
    dest: "/etc/nginx/conf.d/{{ item.domain }}.conf"
  with_items:
    - { domain: www1.example.com, ssl_enabled: yes }
    - { doamin: www2.example.com }
    - { domain: www3.example.com,
      aliases: [ edge2.www.example.com, eu.www.example.com ] }
  loop_control:
    label: "for domain {{ item.domain }}"
```

Warning: Keep in mind that running in verbose mode -v will show the full dictionary; don't use it to hide your passwords.  Set no_log: true on the task instead.

### Includes
The include feature allows you to include tasks or even whole playbooks

Example nginx_include.yml
```yaml
- name: install nginx
  package:
    name: nginx
    
- name: ensure nginx is running
  service:
    name: nginx
    state: started
    enabled: yes
```
Using an include for the tasks file applying the arguments in common
```yaml
- include: nginx_include.yml
  tags: nginx
  become: yes
  when: ansible_os_family == 'RedHat'
```

Dynamic Includes in Ansible 2.0
```yaml
- include: "{{ ansible_os_family }}.yml"
  static: no
```

Role Includes
the include_role not only allows us to selectively choose what parts of a role will be included and used, but also where in the play.
```yaml
- name: install nginx
  yum:
    pkg: nginx
    
- name: install php
  include_role:
    name: php
    
- name: configure nginx
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
```
Include and run main.yml from the php role

```yaml
- name: install nginx
  yum:
    pkg: nginx
    
- name: install php
  include_role:
    name: php
    tasks_from: install
    
- name: configure nginx
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    
- name: configure php
  include_role:
    name: php
    tasks_from: configure
```

### Blocks
block clause allows you to set conditions or arguments for all tasks within a block at once
```yaml
- block:
  - name: install nginx
    package:
      name: nginx
  - name: ensure nginx is running
    service:
      name: nginx
      state: started
      enabled: yes
  become: yes
  when: "ansible_os_family == 'RedHat'"
```

## Error Handling with Blocks
Example app-upgrade.yml
```yaml
---
- block:
  - debug: msg="You will see a failed tasks right after this"
  - command: /bin/false
  - debug: "You won't see this message"
  rescue:
  - debug: "You only see this message in case of an failure in the block"
  always:
  - debug: "This will be always executed"
```

Warning: The tasks under the always clause will be executed even if an error occurred in the rescue clause ! Be careful what you put in the always clause.

Example Error-agnostic application-upgrade playbook
```yaml
---
- hosts: app-servers
  serial: 1
  tasks:
  - name: Take app server out of the load balancer
    local_action:
      module: cs_loadbalancer_rule_member
      name: balance_http
      vm: "{{ inventory_hostname_short }}"
      state: absent
  - name: Create a VM snapshot before an upgrade
    local_action:
      module: cs_vmsnapshot
      name: Snapshot before upgrade
      vm: "{{ inventory_hostname_short }}"
      snapshot_memory: yes
   
  - block:
    - name: Upgrade the application
      script: upgrade-app.sh
    - name: Run smoke tests
      script: smoke-tests.sh
      
    rescue:
    - name: Revert the VM to a snapshot after a failed upgrade
      local_action:
        module: cs_vmsnapshot
        name: Snapshot before upgrade
        vm: "{{ inventory_hostname_short }}"
        state: revert
        
    - name: Re-add app server to the loadbalancer
      local_action:
        module: cs_loadbalancer_rule_member
        name: balance_http
        vm: "{{ inventory_hostname_short }}"
        state: present
    - name: Remove a VM snapshot after successful upgrade or successful rollback
      local_action:
        module: cs_vmsnapshot
        name: Snapshot before upgrade
        vm: "{{ inventory_hostname_short }}"
        state: absent
```


# Roles
In Ansible, the role is the primary mechanism for breaking apart a playbook into multiple files.

**Basic Structure of a Role**
example role database
```
roles/database/tasks/main.yml
roles/database/files/
roles/database/templates/
roles/database/handlers/main.yml
roles/database/vars/main.yml
roles/database/defaults/main.yml
roles/database/meta/main.yml
```

Ansible will look for roles in the roles directory alongside your . playbooks. It will also look for systemwide roles in /etc/ansible/roles 
Example ansible.cfg: overriding default roles path
```
[defaults]
roles_path= ~/ansible_roles
```
or override by setting the ANSIBLE_ROLES_PATH environment variable

**pre_tasks and post_tasks**
example
```yaml
- name: deploy mezzanine on vagrant
  hosts: web
  vars_files:
    - secrets.yml
  pre_tasks:
    - name: update the apt cache
      apt: update_cache=yes
  roles:
    - role: mezzanine
      database_host: "{{ hostvars.db.ansible_eth1.ipv4.address }}"
      live_hostname: 192.168.33.10.xip.io
      domains:
        - 192.168.33.10.xip.io
        - www.192.168.33.10.xip.io
  post_tasks:
    - name: notify Slack that the servers have been updated
      local_action: >
        slack
        domain=acme.slack.com
        token={{ slack_token }}
        msg="web server {{ inventory_hostname }} configured"
```

Database role example
roles/database/tasks/main.yml
```yaml
- name: install apt packages
  apt: pkg={{ item }} update_cache=yes cache_valid_time=3600
  sudo: True
  with_items:
    - libpq-dev
    - postgresql
    - python-psycopg2

- name: copy configuration file
  copy: >
    src=postgresql.conf dest=/etc/postgresql/9.3/main/postgresql.conf
    owner=postgres group=postgres mode=0644
  sudo: True
  notify: restart postgres
  
- name: copy client authentication configuration file
  copy: >
    src=pg_hba.conf dest=/etc/postgresql/9.3/main/pg_hba.conf
    owner=postgres group=postgres mode=0640
  sudo: True
  notify: restart postgres
  
- name: create a user
  postgresql_user:
    name: "{{ database_user }}"
    password: "{{ db_pass }}"
  sudo: True
  sudo_user: postgres
  
- name: create the database
  postgresql_db:
    name: "{{ datatbase_name }}"
    owner: "{{ database_user }}"
    encoding: UTF-8
    lc_ctype: "{{ locale }}"
    lc_collate: "{{ locale }}"
    template: template0
  sudo: True
  sudo_user: postgres
```
roles/database/handlers/main.yml
```yaml
- name: restart postgres
  service: name=postgresql state=restarted
  sudo: True
```

roles/mezzanine/vars/main.yml
```yaml
# vars file for mezzanine
mezzanine_user: "{{ ansible_ssh_user }}"
mezzanine_venv_home: "{{ ansible_env.HOME }}"
mezzanine_venv_path: "{{ mezzanine_venv_home }}/{{ mezzanine_proj_name }}"
mezzanine_repo_url: git@github.com:lorin/mezzanine-example.git
mezzanine_proj_dirname: project
mezzanine_proj_path: "{{ mezzanine_venv_path }}/{{ mezzanine_proj_dirname }}"
mezzanine_reqs_path: requirements.txt
mezzanine_conf_path: /etc/nginx/conf
mezzanine_python: "{{ mezzanine_venv_path }}/bin/python"
mezzanine_manage: "{{ mezzanine_python }} {{ mezzanine_proj_path }}/manage.py"
mezzanine_gunicorn_port: 8000
```
roles/mezzanine/tasks/main.yaml
```yaml
- name: install apt packages
  apt: pkg={{ item }} update_cache=yes cache_valid_time=3600
  sudo: True
  with_items:
    - git
    - libjpeg-dev
    - libpq-dev
    - memcached
    - nginx
    - python-dev
    - python-pip
    - python-psycopg2
    - python-setuptools
    - python-virtualenv
    - supervisor

- include: django.yml
- include: nginx.yml  
```
roles/mezzanine/tasks/django.yml
```yaml
- name: check out the repository on the host
  git:
    repo: "{{ mezzanine_repo_url }}"
    dest: "{{ mezzanine_proj_path }}"
    accept_hostkey: yes
    
- name: install required python packages
  pip: name={{ item }} virtualenv={{ mezzanine_venv_path }}
  with_items:
    - gunicorn
    - setproctitle
    - south
    - psycopg2
    - django-compressor
    - python-memcached

- name: install requirements.txt
  pip: >
    requirements={{ mezzanine_proj_path }}/{{ mezzanine_reqs_path }}
    virtualenv={{ mezzanine_venv_path }}
    
- name: generate the settings file
  template: src=local_settings.py.j2 dest={{ mezzanine_proj_path }}/local_settings.py
  
- name: sync the database, apply migrations, collect static content
  django_manage:
    command: "{{ item }}"
    app_path: "{{ mezzanine_proj_path }}"
    virtualenv: "{{ mezzanine_venv_path }}"
  with_items:
    - syncdb
    - migrate
    - collectstatic
  
- name: set the site id
  script: scripts/setsite.py
  environment:
    PATH: "{{ mezzanine_venv_path }}/bin"
    PROJECT_DIR: "{{ mezzanine_proj_path }}"
    WEBSITE_DOMAIN: "{{ live_hostname }}"
    
- name: set the admin password
  script: scripts/setadmin.py
  environment:
    PATH: "{{ mezzanine_venv_path }}/bin"
    PROJECT_DIR: "{{ mezzanine_proj_path }}"
    ADMIN_PASSWORD: "{{ admin_pass }}"
    
- name: set the gunicorn config file
  template: src=gunicorn.conf.py.j2 dest={{ mezzanine_proj_path }}/gunicorn.conf.py
  
- name: set the supervisor config file
  template: src=supervisor.conf.j2 dest=/etc/supervisor/conf.d/mezzanine.conf
  sudo: True
  notify: restart supervisor
  
- name: ensure config path exists
  file: path={{ mezzanine_conf_path }} state=directory
  sudo: True
  when: tls_enabled
  
- name: install poll twitter cron job
  cron: >
    name="poll twitter" minute="*/5" user={{ mezzanine_user }}
    job="{{ mezzanine_manage }} poll_twitter"
```
roles/mezzanine/tasks/nginx.yml
```yaml
- name: set the nginx config file
  template: src=nginx.conf.j2 dest=/etc/nginx/sites-available/mezzanine.conf
  notify: restart nginx
  sudo: True
  
- name: enable the nginx config file
  file:
    src: /etc/nginx/sites-available/mezzanine.conf
    dest: /etc/nginx/sites-enabled/mezzanine.conf
    state: link
  notify: restart nginx
  sudo: True
  
- name: remove the default nginx config file
  file: path=/etc/nginx/sites-enabled/default state=absent
  notify: restart nginx
  sudo: True
  
- name: create tls certificates
  command: >
    openssl req -new -x509 -nodes -out {{ mezzanine_proj_name }}.crt
    -keyout {{ mezzanine_proj_name }}.key -subj '/CN={{ domains[0] }}' -days 3650
    chdir={{ mezzanine_conf_path }}
    creates={{ mezzanine_conf_path }}/{{ mezzanine_proj_name }}.crt
  sudo: True
  when: tls_enabled
  notify: restart nginx
```
When invoking copy in a task defined in a role, Ansible will first check the rolename/files/ directory for the location of the file to copy.
When invoking template in a task defined in a role, Ansible will first check the rolename/templates directory for the location of the template to use

roles/mezzanine/handlers/main.yml
```yaml
- name: restart supervisor
  supervisorctl: name=gunicorn_mezzanine state-restarted
  sudo: True
  
- name: restart nginx
  service: name=nginx state=restarted
  sudo: True
```

## ansible-galaxy
download roles from the Ansible community or to generate scaffolding
```
$ ansible-galaxy init -p playbooks/roles web
```
Running the commands creates the following files and directories:
* playbooks/roles/web/tasks/main.yml
* playbooks/roles/web/handlers/main.yml
* playbooks/roles/web/vars/main.yml
* playbooks/roles/web/defaults/main.yml
* playbooks/roles/web/meta/main.yml
* playbooks/roles/web/files/
* playbooks/roles/web/templates/
* playbooks/roles/web/README.md

Dependent Roles
roles/web/meta/main.yml
```yaml
dependencies:
  - { role: ntp, ntp_server=ntp.ubuntu.com }
```

installing a role 
```
$ ansible-galaxy install -p ./roles bennojoy.ntp
```
List installed roles
```
$ ansible-galaxy list
```
Uninstall a role
```
$ ansible-galaxy remove bennojoy.ntp
```


# Customizing Hosts, Runs, and Handlers

Ansible Hosts supported patterns

| Action                    | Example usage                 |
| ------------------------- | ----------------------------- |
| All hosts                 | all                           |
| All hosts                 | *                             |
| Union                     | dev:staging                   |
| Intersection              | staging:&database             |
| Exclusion                 | dev:!queue                    |
| Wildcard                  | *.example.com                 |
| Range of numbered servers | web[5:10]                     |
| Regular expression        | ~web\d+\\.example\.(com\|org) |

Ansible supports combinations of patterns e.g.
hosts: dev:staging:&database:!queue

Limiting which hosts run
$ ansible-playbook -l 'staging:&database' playbook.yml

example local_action 
```yaml
- name: wait for ssh server to be running
  local_action: wait_for_port=22 host="{{ inventory_hostname }}"
    search_regex=OpenSSH
```
TIP: If your play involves multiple hosts, and you use local_action, the task will be executed multiple times, one for each host. You can restrict this by using run_once

example delegate_to
```yaml
- name: enable alerts for web servers
  hosts: web
  tasks:
    - name: enable alerts
      nagios: action=enable_alerts service=web host={{ inventory_hostname }}
      delegate_to: nagios.example.com
```
Ansible would execute the nagios task on nagios.example.com but the inventory_hostname referenced would evaluate to the web host.

example Using a list of serials
```yaml
- name: configure CDN servers
  hosts: cdn
  serial:
    - 1
    - 30%
  tasks:
    # tasks
```
Run the play on one host first, to verify that the play works as expected, and then run the play on a larger number of hosts in subsequent runs.
In the preceding play with 30 CDN hosts, it would run against (e.g. 1, 10, 10, 9)

example run_once with local_action
```yaml
- name: run the task locally, only once
  local_action: command /opt/my-command
  run_once: true
```

### Running Strategies

The default strategy is the **linear** strategy. This is the strategy in which Ansible executes one task on all hosts and waits until the task has completed (or failed) on all hosts before it executes the next task on all hosts.
example host file with three hosts
```
one    sleep_seconds=1
two    sleep_seconds=6
three  sleep_seconds=10
```

example playbook in linear strategy
```yaml
---
- hosts: all
  connection: local
  tasks:
  - name: first task
    shell: sleep "{{ sleep_seconds }}"
    
  - name: second task
    shell: sleep "{{ sleep_seconds }}"
    
  - name: third task
    shell: sleep "{{ sleep_seconds }}"
```

**free** strategy will not wait for results of the task to execute on all hosts. Instead, if a host completes one task, Ansible will execute the next task on that host.
example playbook in free strategy
```yaml
---
- hosts: all
  connection: local
  strategy: free
  tasks:
  - name: first task
    shell: sleep "{{ sleep_seconds }}"
    
  - name: second task
    shell: sleep "{{ sleep_seconds }}"
    
  - name: third task
    shell: sleep "{{ sleep_seconds }}"
```

### Advanced Handlers
**flush_handlers** force the handler to run between the two tasks instead of at the end of the play.
example cleanup and validate health checks after the service restart
```yaml
---
- name: install nginx
  yum:
    pkg: nginx
  notify: restart nginx
  
- name: configure nginx vhosts
  template:
    src: conf.d/{{ item.template | default(item.name) }}.conf.j2
    dest: /etc/nginx/conf.d/{{ item.name }}.conf
  with_items: "{{ vhosts }}"
  when: item.name not in vhosts_absent
  notify: restart nginx
  
- name: removed unused nginx vhosts
  file:
    path: /etc/nginx/conf.d/{{ item }}.conf
    state: absent
  with_items: "{{ vhosts_absent }}"
  notify: restart nginx
  
- name: validate nginx config
  command: nginx -t
  changed_when: false
  check_mode: false
  
- name: flush the handlers
  meta: flush_handlers
  
- name: remove unused vhost directory
  file:
    path: /srv/www/{{ item }} state=absent
  when: item not in vhosts
  with_items: "{{ vhosts_absent }}"

- name: check healthcheck
  local_action:
    module: uri
    url: http://{{ nginx_healthcheck_host }}:{{ nginx_healthcheck_port }}/healthcheck
    return_content: true
  retries: 10
  delay: 5
  register: webpage
  
- fail:
    msg: "fail if healthcheck is not ok"
  when: not webpage|skipped and webpage|success and "ok" not in webpage.content
```

**Handlers Listen** in Ansible 2.2
before there was only one way to notify a handler: by calling notify on the handler's name

example handlers listen
```yaml
---
- hosts: mailservers
  tasks:
    - copy:
        src: main.conf
        dest: /etc/postfix/main.cnf
      notify: postfix config changed
      
  handlers:
    - name: restart postfix
      service: name=postfix state=restarted
      listen: postfix config changed
```
The listen clause defines what we'll call an event, on which one or more handlers can listen. This decouples the task notification key from the handler's name. Note. The scope of all handlers is on the play level. We cannot notify across plays.

example Notify an event to listen in handlers
```yaml
---
- name: include OS specific variables
  include_vars: "{{ ansible_os_family }}.yml"
  
- name: copy SSL certs
  copy:
    src: "{{ item }}"
    dest: "{{ ssl_certs_path }}/"
    owner: root
    group: root
    mode: 0644
  with_items: "{{ ssl_certs }}"
  notify: ssl_certs_changed
  
- name: copy SSL keys
  copy:
    src: "{{ item }}"
    dest: "{{ ssl_keys_path }}/"
    owner: root
    group: root
    mode: 0644
  with_items: "{{ ssl_keys }}"
  no_log: true
  notify: ssl_certs_changed
```
example append the listen clause to the existing handler in the nginx role
```yaml
---
- name: restart nginx
  service:
    name: nginx
    state: restarted
  listen: ssl_certs_changed
```

### Manually Gathering Facts
example waiting for SSH server to come up
```yaml
- name: Deploy mezzanine
  hosts: web
  gather_facts: False
  tasks:
    - name: wait for ssh server to be running
      local_action: wait_for port=22 host="{{ inventory_hostname }}"
        search_regex=OpenSSH
        
    - name: gather facts
      setup:
```

### Retrieving the IP Address from the Host
```
live_hostname: "{{ ansible_eth1.ipv4.address }}.xip.io"
```


# Callback Plugins
callback plugins can perform custom actions in response to Ansible events such as a play starting or a task completing on a host. Ansible supports two kinds of callback plugins:
- stdout plugins affect the output displayed to the terminal
- other plugins do things other than change displayed output

Only a single stdout plugin can be active at a time. specify a stdout callback by setting the stdout_callback parameter in ansible.cfg
```
[defaults]
stdout_callback = actionable
```

stdout plugins

| Name       | Description                              | Notes                                    |
| ---------- | ---------------------------------------- | ---------------------------------------- |
| actionable | Show only changed or failed              |                                          |
| debug      | Human-readable stderr and stdout         |                                          |
| default    | Show default output                      |                                          |
| dense      | Overwrite output instead of scrolling    | new in Ansible 2.3                       |
| json       | JSON output                              | will not generate output until the entire playbook has finished |
| minimal    | Show task results with minimal formatting |                                          |
| oneline    | Like minimal, but on a single line       |                                          |
| selective  | Show only output for tagged tasks        | only shows for successful tasks that have the print_action tag and failed tasks |
| skippy     | Suppress output for skipped hosts        |                                          |

Unlike with stdout plugins, you can have multiple other plugins enabled at the same time in ansible.cfg
```
[default]
callback_whitelist = mail, slack
```

Other plugins

| Name          | Description                         |
| ------------- | ----------------------------------- |
| foreman       | Send notifications to Foreman       |
| hipchat       | Send notifications to HipChat       |
| jabber        | Send notification to Jabber         |
| junit         | Write JUnit-formatted XML file      |
| log_plays     | Log playbook results per hosts      |
| logentries    | Send notifications to Logentries    |
| logstash      | Send results to Logstash            |
| mail          | Send email when tasks fail          |
| osx_say       | Speak notifications on macOs        |
| profile_tasks | Report execution time for each task |
| slack         | Send notifications to Slack         |
| timer         | Report total execution time         |

foreman plugin environment variables

| var                | Description                              | Default                      |
| ------------------ | ---------------------------------------- | ---------------------------- |
| FOREMAN_URL        | URL to the Foreman server                | http://localhost:3000        |
| FORMAN_SSL_CERT    | X509 cert to authenticate to Foreman     | /etc/foreman/client_cert.pem |
| FOREMAN_SSL_KEY    | The corresponding private key            | /etc/foreman/client_key.pem  |
| FOREMAN_SSL_VERIFY | Set to 1 to verify SSL certs using the installed CAs or to a path pointing to a CA bundle. | 1                            |

hipchat plugin environment variables. Note need install : pip install prettytable

| var            | Description                           | Default |
| -------------- | ------------------------------------- | ------- |
| HIPCHAT_TOKEN  | HipChat API token                     | (None)  |
| HIPCHAT_ROOM   | HipChat room to post in               | ansible |
| HIPCHAT_NAME   | HipChat name to post as               | ansible |
| HIPCHAT_NOTIFY | Add notify flag to important messages | true    |

jabber plugin environment variables. Need to install: pip install git+https://github.com/ArchipelProject/xmpppy

| var         | Description                             |
| ----------- | --------------------------------------- |
| JABBER_SERV | Hostname of Jabber server               |
| JABBER_USER | Jabber username for auth                |
| JABBER_PASS | Jabber password auth                    |
| JABBER_TO   | Jabber user to send the notification to |

junit plugin environment variables. Need to install: pip install junit_xml

| var              | Description                              | Default        |
| ---------------- | ---------------------------------------- | -------------- |
| JUNIT_OUTPUT_DIR | Destination directory for files          | ~/.ansible.log |
| JUNIT_TASK_CLASS | Configure output: one class per YAML file | false          |

log_plays plugin logs the results to log file in /var/log/ansible/hosts. one file for each host.
Instead of using the log_plays plugin, you can set the log_path option in ansible.cfg
```
[defaults]
log_path = /var/log/ansible.log
```
This generates a single logfile for all hosts.

logentries plugin environment variables. Need to install: pip install certifi flatdict

| var                      | Description                     | Default             |
| ------------------------ | ------------------------------- | ------------------- |
| LOGENTRIES_ANSIBLE_TOKEN | Logentries token                | (None)              |
| LOGENTRIES_API           | Hostname of Logentries endpoint | data.logentries.com |
| LOGENTRIES_PORT          | Logentries port                 | 80                  |
| LOGENTRIES_TLP_PORT      | Logentries TLS port             | 443                 |
| LOGENTRIES_USE_TLS       | Use TLS                         | false               |
| LOGENTRIES_FLATTEN       | Flatten results                 | false               |

logstash plugin environment variables. Need to install: pip install python-logstash

| var             | Description              | Default   |
| --------------- | ------------------------ | --------- |
| LOGSTASH_SERVER | Logstash server hostname | localhost |
| LOGSTASH_PORT   | Logstash server port     | 5000      |
| LOGSTASH_TYPE   | Message type             | ansible   |

mail plugin environment variables

| var      | Description          | Default   |
| -------- | -------------------- | --------- |
| SMTPHOST | SMTP server hostname | localhost |

profile-tasks plugin environment variables

| var                             | Description                    | Default |
| ------------------------------- | ------------------------------ | ------- |
| PROFILE_TASKS_SORT_ORDER        | Sort output(ascending, none)   | none    |
| PROFILE_TASKS_TASK_OUTPUT_LIMIT | Number of tasks to show or all | 20      |

slack plugin environemnt variables. Need to install: pip install prettytable

| var               | Description                          | Deafult  |
| ----------------- | ------------------------------------ | -------- |
| SLACK_WEBHOOK_URL | Slack webhook URL                    | (None)   |
| SLACK_CHANNEL     | Slack channel                        | #ansible |
| SLACK_USERNAME    | username to post as                  | ansible  |
| SLACK_INVOCATION  | Show command-line invocation details | false    |


# Making Ansible Go Even Faster

### SSH Multiplexing
Example ~/.ssh/config for enabling ssh multiplexing
```
Host myserver.example.com
  ControlMaster auto
  ControlPath /tmp/%r@%h:%p
  ControlPersist 10m
```
The Controlmaster auto line enables SSH multiplexing, and it tells SSH to create the master connection and the control socket if it does not exist yet.
The ControlPath line tells SSH where to put the control Unix domain socket file on the file system. %h is the target host name, %r is the remote login username, and %p is the port.
The ControlPersist 10m line tells SSH to close the master connection if there have been no SSH connections for 10 minutes

check if a master connection is open using the -O check flag:
$ ssh -O check ubuntu@myserver.example.com

terminate the master connection using the -O exit flag:
$ ssh -O exit ubuntu@myserver.example.com

test the speed of making an SSH connection:
$ time ssh ubuntu@myserver.example.com /bin/true

SSH Multiplexing Options in Ansible

| Option         | Value                                  |
| -------------- | -------------------------------------- |
| ControlMaster  | auto                                   |
| ControlPath    | $HOME/.ansible/cp/ansible-ssh-%h-%p-%r |
| ControlPersist | 60s                                    |

configure Ansible to use a shorter ControlPath in *ansible.cfg*
```
[ssh_connection]
control_path = %(directory)s/%%h-%%r
```

### Pipelining
Pipelining will execute the Python script by piping it to the SSH session instead of copying it.

Enable pipelining ansible.cfg requires requiretty is disabled
```
[defaults]
pipelining = True
```

templates/disable-requiretty.j2
```
Defaults:{{ ansible_ssh_user }} !requiretty
```

disable-requiretty.yml
```yaml
- name: do not require tty for ssh-ing user
  hosts: myhosts
  sudo: True
  tasks:
    - name: Set a sudoers file to disable tty
      template: >
        src=templates/disable-requiretty.j2
        dest=/etc/sudoers.d/disable-requiretty
        owner=root group=root mode=0440
        validate="visudo -cf %s"
```

### Fact Caching
disable fact gathering in a play
```
- name: an example play that doesn't need facts
  host: myhosts
  gather_facts: False
  tasks:
    # tasks....
```

or disable fact gathering in ansible.cfg
```
[defaults]
gathering = explicit
```

clear fact cache
ansible-playboot --flush-cache

Enable fact caching ansible.cfg
```
[defaults]
gathering = smart
# 24-hour timeout
fact_caching_timeout = 86400

# You must specify a fact caching implementation
fact_caching = ...
```
```
fact_caching = jsonfile
fact_caching_connection = /tmp/ansible_fact_cache
```
```
fact_caching = redis
```
```
fact_caching = memcached
```

### Parallelism
defaults to 5
change settings
$ export ANSIBLE_FORK=20
$ ansible-playbook playbook.yml

or ansible.cfg
```
[defaults]
forks = 20
```

### Concurrent Tasks with Async
Ansible introduced support for asynchronous actions with the async clause to work around the problem of SSH timeous. Making a long-running task with the async clause eliminate the risk of a task exceeds the SSH timeout.
Asynchronous actions can also be used for starting a second task before the first task has completed.

example Using async to overlap tasks
```yaml
- name: install git
  apt: name=git update_cache=yes
  become: yes
- name: clone Linus git repo
  git:
    repo: git://git.kernel.org/.../linux.git
    dest: /home/vagrant/linux
  async: 3600
  poll: 0
  register: linux_clone
- name: install several packages
  apt:
    name: "{{ item }}"
  with_items:
    - apt-transport-https
    - ca-certificates
    - linux-image-extra-virtual
    - software-properties-common
    - python-pip
  become: yes
- name: wait for linux clone to complete
  async_status:
    jid: "{{ linux_clone.ansible_job_id }}"
  register: result
  until: result.finished
  retries: 3600
```
We specify an async task that should take less than 3600 seconds. If the execution time exceeds that value, Ansible will automatically terminate the process associated with the task.

We specify a poll argument of 0 to tell Ansible that it should immediately move on to the next task. If we had specified a nonzero value, Ansible would not move on to the next task. instead, it would periodically poll the status of the async task to check whether it was complete, sleeping between checks specified by the poll argument.

When we run async, we must use the register clause to capture the async result. 
We use the async_status module to poll for the status of the async job
We must specify a jid value that identifies the async job
The async_status module polls only a single time. We need to specify an until clause so that it will keep polling until the job completes, or until exhaust the specified number of retries.


# Custom Modules

### Script
example can_reach.sh 
```
#!/bin/bash
host=$1
port=$2
timeout=$3

nc -z -w $timeout $host $port
```
```
- name: run my custom script
  script: scripts/can_reash.sh www.example.com 80 1
```

### Module
```
- name: check if host can reach the database server
  can_reach: host=db.example.com port=5432 timeout=1
```

put custom Modules in *library* directory, e.g. playbooks/library/can_reach

temporary Python script e.g. /home/ubuntu/.ansible/tmp/..../can_reach
temporary Arguments file e.g. /home/ubuntu/.ansible/tmp/.../arguments

We can tell Ansible to generate the arguments file for the module as JSON by adding
```
# WANT_JSON
```

Invoke the Module
example
```
/bin/sh -c 'LANG=en_US.UTF-8 LC_CTYPE=en.US.UTF-8 /bin/bash \
/path/to/can_reach \
/path/to/arguments; rm -rf /path/to/ >/dev/null 2>&1'
```
You can see the exact command by passing -vvv to ansible-playbook

return variables Ansible has special treatment for:
- changed
- failed
- msg

### Implementing Modules in Python
AnsibleModule Python class:
- Parse the inputs
- Return outputs in JSON format
- Invoke external programs

Example can_reach
```python
#!/usr/bin/python

def can_reach(module, host, port, timeout):
  nc_path = module.get_bin_path('nc', required=True)
  args = [nc_path, "-z", "-w", str(timeout), host, str(port)]
  (rc, stdout, stderr) = module.run_command(args)
  return rc = 0
  
def main():
  module = AnsibleModule(
    argument_spec=dict(
      host=dict(required=True),
      port=dict(required=True, type='int'),
      timeout=dict(required=False, type='int', default=3)
      ),
      supports_check_mode=True
    )
    
    # In check mode, we take no action
    # Since this module never changes system state, we just
    # return changed=False
    if module.check_mode:
      module.exit_json(changed=False)
      
    host = module.params['host']
    port = module.params['port']
    timeout = module.params['timeout']
    
    if can_reach(module, host, port, timeout):
      module.exit_json(changed=False)
    else:
      msg = "Could not reach %s:%s" % (hostm, port)
      module.fail_json(msg=msg)
      
from ansible.module_utils.basic import *
main()
```

Importing the AnsibleModule Helper Class behaves differently with traditional Python import. Ansible copies only a single Python file to the remote host to execute it. Ansible simulates the behavior by including the imported code directly into the generated Python file.
Because Ansible will replace the import statement with code, the line numbers in the module as written will be different than the line numbers of the generated Python file.
You shouldn't import classes explicitly because Ansible module debugging scripts look for the specific string that includes the * 

Angrument options

| Option   | Description                              |
| -------- | ---------------------------------------- |
| required | If True, argument is required            |
| default  | Default value if argument is not required |
| choices  | A list of possible values for the argument |
| aliases  | Other names you can use as an alias for this argument |
| type     | Argument type. Allowed values: 'str', 'list', 'dict', 'bool', 'int', 'float' |

type list is comma-delimited. e.g.
colors=dict(required=True, type='list')
foo: colors=red,green,blue

type dictionary, you can either do key=value pairs, delimited by commas, or you can do JSON inline. e.g.
tags=dict(required=False, type='dict', default={})
- bar: tags=env=staging, function=web
  or
- bar: tags={"env": "staging", "function": "web"}

AnsibleModule initalizer arguments

| Parameter               | Default | Description                              |
| ----------------------- | ------- | ---------------------------------------- |
| argument_spec           | (none)  | Dictionary that contains information about arguments |
| bypass_checks           | False   | If true, don't check any of the parameter constrains |
| no_log                  | False   | If true, don't log the behavior of this module |
| check_invalid_arguments | True    | If true, return error if user passed an unknown argument |
| mutually_exclusive      | None    | List of mutually exclusive arguments     |
| required_together       | None    | List of arguments that must appear together |
| required_one_of         | None    | List of arguments where at least one must be present |
| add_file_common_args    | False   | Supports the arguments of the file module |
| supports_check_mode     | False   | If true, indicates module supports check mode |

no_log, when Ansible executes a module on a host, the module will log output to the syslog, which on Ubuntu is at /var/log/syslog

The load_file_common_arguments method takes the parameters dictionary as an argument and returns a parameters dictionary that contains all of the arguments that relate to setting file attributes.

The set_fs_attributes_if_different method takes a file parameters dictionary and a Boolean indicating whether a host state change has occurred yet.

### Invoking External Commands
The AnsibleModule class provides the run_command method for calling an external program, which wraps Python subprocess module.

run_command arguments

| Argument         | Type                      | Default | Description                              |
| ---------------- | ------------------------- | ------- | ---------------------------------------- |
| args(default)    | string or list of strings | (none)  | The command to be executed               |
| check_rc         | Boolean                   | False   | If true, will call fail_json if command returns a non-zero value |
| close_fds        | Boolean                   | True    | Passes a close_fds argument to subprocess.Popen |
| executable       | string (path to program)  | None    | Passes as executable argument to subprocess.Popen |
| data             | string                    | None    | Send to stdin if child process           |
| binary_data      | Boolean                   | False   | If false and data is present, Ansible will send a newline to stdin after sending data |
| path_prefix      | string (list of paths)    | None    | Colon-delimited list of paths to prepend to PATH environment variable |
| cwd              | string (directory path)   | None    | If specified, Ansible will change to this directory before executing |
| use_unsafe_shell | Boolean                   | False   |                                          |

### Check Mode (Dry Run)
ansible-playbook -C or --check
When Ansible runs a playbook in check mode, it will not make any changes to the hosts when it runs. Instead, it will simply report whether each task would have changed the host.

Telling Ansible the module supports check mode
```
module = AnsibleModule(
  arguement_spec=dict(...),
  supports_check_mode=True
)
```

Checking if check mode is enabled
```
module = AnsibleModule(...)
...
if module.check_mode:
  # check if this module would make any changes
  would_change = would_executing_this_module_change_something()
  module.exit_json(changed=would_change)
```

### Documenting Your Module
example 
```
DOCUMENTATION = '''
---
module: can_reach
short_description: Checks server reachability
description:
  - Checks if a remote server can be reached
version_added: "1.8"
options:
  host:
    description:
      - A DNS hostname or IP address
    required: true
  port:
    description:
    - The TCP port number
    required: true
  timeout:
    description:
    - The amount of time try to connecting before giving up, in seconds
    required: false
    default: 3
  flavor:
    description:
    - This is a made-up option to show how to specify choices.
    required: false
    choices: ["chocolate", "vanilla", "strawberry"]
    aliases: ["flavor"]
    default: chocolate
requirements: [netcat]
author: Lorin Hochstein
notes:
  - This is just an example to demonstrate how to write a module.
  - You probably want to use the native M(wait_for) module instead.
'''

EXAMPLES = '''
# Check that ssh is running, with the default timeout
- can_reach: host=myhost.example.com port=22

# Check if postgres is running, with a timeout
- can_reach: host=db.example.com port=5432 timeout=1
'''
```

Documentation markup

| Type           | Syntax with example       | When to use           |
| -------------- | ------------------------- | --------------------- |
| URL            | U(http://www.example.com) | URLs                  |
| Module         | M(apt)                    | Module names          |
| Italics        | I(port)                   | Parameter names       |
| Constant-width | C(/bin/bash)              | File and option names |


### Implementing the Module in Bash
The main difference is parsing the input arguments and generating the outputs that Ansible expectes.

example can_reach module in Bash
```bash
#!/bin/bash
# WANT_JSON

# Read the variables form the file
host=`jq -r .host < $1`
port=`jq -r .port < $1`
timeout=`jq -r .timeout < $1`

# Check if we can reach the host
nc -z -w $timeout $host $port

# Output based on success or failure
if [ $? -eq 0 ]; then
  echo '{"changed": false}'
else
  echo "{\"failed\": true, \"msg\": \"could not reach $host:$port\"}"
fi
```
You can tell Ansible to look elsewhere for Bash interpreter by setting the ansible_bash_interpreter variable e.g.
host_vars/fileserver.example.com
ansible_bash_interpreter: /usr/local/bin/bash


# Docker

Module docker_container --> docker command line tool such as run, kill and rm
Module docker_image --> build an image
Module docker_service --> control docker compose

example ghost.yml
```yaml
---
- name: Run Ghost locally
  hosts: localhost
  gather_facts: False
  tasks:
    - name: create Nginx image
      docker_image:
        name: reg.example.com:5000/ansiblebook/nginx-ghost
        path: nginx
    - name: create certs
      command: >
        openssl req -new -x509 -nodes
        -out certs/nginx.crt -keyout certs/nginx.key
        -subj '/CN=localhost' -days 3650
        creates=certs/nginx.crt
    - name: bring up services
      docker_service:
        project_src: .
        state: present
```

### push image
example push image to Docker Registry
```yaml
- name: publish images to docker hub
  hosts: localhost
  gather_facts: False
  vars_prompt:
    - name: username
      prompt: Enter Docker Registry username
    - name: email
      prompt: Enter Docker Registry email
    - name: password
      prompt: Enter Docker Registry password
      private: yes
  tasks:
    - name: authenticate with repository
      docker_login:
        username: "{{ username }}"
        email: "{{ email }}"
        password: "{{ password }}"
        registry_url: http://reg.example.com:5000
    - name: push image up
      docker_image:
        name: reg.example.com:5000/ansiblebook/nginx-ghost
        push: yes
```
push with local registry
```yaml
- name: publish images to local docker registry
  hosts: localhost
  gather_facts: False
  vars:
    repo_port: 5000
    repo: "localhost:{{ repo_port }}"
    image: ansiblebook/nginx-ghost
  tasks:
    - name: start a registry locally
      docker_container:
        name: registry
        image: registry:2
        ports: "{{ repo_port }}:5000"
    - debug:
      msg: name={{ image }} repo={{ repo }}/{{ image }}
    - name: tag the nginx-ghost image to the repository
      docker_image:
        name: "{{ image }}"
        repository: "{{ repo }}/{{ image }}"
        push: yes
```
we can verify the upload worked by downloading the manifest:
```
$ curl http://localhost:5000/v2/ansiblebook/nginx-ghost/manifests/latest
```

### Query local images
docker_image_facts module allows you to query the metadata on a locally stored image.

example image-facts
```yaml
---
- name: get exposed ports and volumes
  hosts: localhost
  gather_facts: False
  vars:
    image: ghost
  tasks:
    - name: get image info
      docker_image_facts: name=ghost
      register: ghost
    - name: extract ports
      set_facts:
        ports: "{{ ghost.images[0].Config.ExposedPosts.keys() }}"
    - name: we expect only one port to be exposed
      assert:
        that: "ports|length == 1"
    - name: output exposed port
      debug:
        msg: "Exposed port: {{ ports[0] }}"
    - name: extract volumes
      set_fact:
        volumes: "{{ ghost.images[0].Config.Volumes.keys() }}"
    - name: output volumes
      debug:
        msg: "Volume: {{ item }}"
      with_items: "{{ volumes }}"
```

### Deploying the Dockerized Application

example postgres.yml
```yaml
- name: deploy postgres
  hosts: postgres
  become: True
  gather_facts: False
  vars:
    data_dir: /data/pgdata
  tasks:
    - name: create data dir with correct ownership
      file:
        path: "{{ data_dir }}"
        state: directory
    - name: start postgres container
      docker_container:
        name: postgres_ghost
        image: postgres:9.6
        ports:
          - "0.0.0.0:5432:5432"
        volumes:
          - "{{ data_dir }}:/var/lib/postgresql/data"
        env:
          POSTGRES_USER: "{{ database_user }}"
          POSTGRES_PASSWORD: "{{ database_password }}"
          POSTGRES_DB: "{{ database_name }}"
```
```yaml
- name: deploy ghost
  hosts: ghost
  become: True
  gather_facts: False
  vars:
    url: "https://{{ ansible_host }}"
    database_host: "{{ groups['postgres'][0] }}"
    data_dir: /data/ghostdata
    certs_dir: /data/certs
    net_name: ghostnet
  tasks:
    - name: create network
      docker_network: "name={{ net_name }}"
```
```yaml
- name: create ghostdata directory
  file:
    path: "{{ data_dir }}"
    state: directory
- name: generate the config file
  template: src=templates/config.js/j2 dest={{ data_dir }}/config.js
- name: start ghost container
  docker_container:
    name: ghost
    image: ghost
    command: npm start --production
    volumes:
      - "{{ data_dir }}:/var/lib/ghost"
    networks:
      - name: "{{ net_name }}"
```
```yaml
- name: create certs directory
  file:
    path: "{{ certs_dir }}"
    state: directory
- name: generate tls certs
  command: >
    openssl req -new -x509 -nodes
    -out "{{ certs_dir }}/nginx.crt" -keyout "{{ certs_dir }}/nginx.key"
    -subj "/CN={{ ansible_host }}" -days 3650
    creates=certs/nginx.crt
- name: start nginx container
  docker_container:
    name: nginx_ghost
    image: ansible/nginx-ghost
    pull: yes
    networks:
      - name: "{{ net_name }}"
    posts:
      - "0.0.0.0:80:80"
      - "0.0.0.0:443:443"
    volumes:
      - "{{ certs_dir }}:/certs"
```

### Cleaning out Containers
```yaml
- name: remove all ghost containers and networks
  hosts: ghost
  become: True
  gather_facts: False
  tasks:
    - name: remove containers
      docker_container:
        name: "{{ item }}"
        state: absent
      with_items:
        - nginx_ghost
        - ghost
    - name: remove network
      docker_network:
        name: ghostnet
        state: absent
```


# Debugging Ansible Playbooks

Enable callback plugin
```
[defaults]
stdout_callback = debug
```

debug ssh connection
ansible-playbook -vvvv

The debug module
```
- debug: var=myvariable
- debug: msg="The value of myvariable is {{ var }}"
- debug: var=hostvars[inventory_hostname]
```

### playbook interactive debugger in Ansible 2.1
```
- name: an example play
  strategy: debug
  tasks:
```

Debugger commands

| Command              | Description                              |
| -------------------- | ---------------------------------------- |
| p var                | Print out the value of a supported variable |
| task.args[key]=value | Modify an argument for the failed task   |
| vars[key]=value      | Modify the value of a variable           |
| r                    | Rerun the failed task                    |
| c                    | Continue executing the play              |
| q                    | Abort the play and execute the debugger  |
| help                 | Show help message                        |

Variables supported by the debugger

| Command     | Description                            |
| ----------- | -------------------------------------- |
| p task      | The name of the task that failed       |
| p task.args | The module arguments                   |
| p result    | The result returned by the failed task |
| p vars      | Value of all known variables           |
| p vars[key] | Value of one variable                  |

### The Assert Module
The assert module will fail with an error if a specified condition is not met.
The code in an assert statement is Jinja2, not Python.
example
```
- name: assert that eth1 interface exists
  assert:
    that: ansible_eth1 is defined
```
```
# Invalid Jinja2, this won't work!
assert:
  that: "len(ports) == 1"
  
# Instead, use Jinja2 length filter
assert:
  that: "ports|length == 1"
```

### check on the status of a file using stat module and an assertion
```
- name: stat /opt/foo
  stat: path=/opt/foo
  register: st
  
- name: assert that /opt/foo is a directory
  assert:
    that: st.stat.isdir
```
The stat module collects information about the state of a file path. It returns a dictionary that contains a stat field with the values shown below.
stat module return values

| Field   | Description                              |
| ------- | ---------------------------------------- |
| atime   | Last access time of path, in Unix timestamp format |
| ctime   | Creation time of path, in Unix timestamp format |
| dev     | Numerial ID of the device that the inode resides on |
| exists  | True if path exists                      |
| gid     | Numerical group ID of path owner         |
| inode   | Inode number                             |
| isblk   | True if path is block special device file |
| isdir   | True if path is a directory              |
| isfifo  | True if path is a FIFO (named pipe)      |
| isgid   | True if set-group-ID bit is set on file  |
| islnk   | True if path is a symbolic link          |
| isreg   | True if path is a regular file           |
| issock  | True if path is a Unix domain socket     |
| isuid   | True if set-user-ID bit is set on file   |
| mode    | File mode as a string, in octal (e.g., "1777") |
| mtime   | Last modification time of path, in Unix timestamp format |
| nlink   | Number of hard links to the file         |
| pw_name | Login name of file owner                 |
| rgrp    | True if group read permission enabled    |
| roth    | True if other read permission enabled    |
| rusr    | True if user read permission enabled     |
| size    | File size in bytes, if regular file      |
| uid     | Numerical user ID of path owner          |
| wgrp    | True if group write permission enabled   |
| woth    | True if other write permission enabled   |
| wusr    | True if user write permission enabled    |
| xgrp    | True if group execute permission enabled |
| xoth    | True if other execute permission enabled |
| xusr    | True if user execute permission enabled  |

### Checking Your Playbook Before Execution

syntax check
$ ansible-playbook --syntax-check playbook.yml


list hosts outputs the hosts that the playbook will run against, but it does not execute the playbook.
$ ansible-playbook --list-hosts playbook.yml

note : error: provided hosts list is empty
you can work around this by explicitly adding the following line: localhost ansible_connection=local

list tasks, does not execute the playbook
$ ansible-playbook --list-tasks playbook.yml

Check Mode
The -C and --check flags run Ansible in check mode which tells you whether each task in the playbook will modify the host, but does not make any change to the server.
$ ansible-playbook -C playbook.yml
$ ansible-playbook --check playbook.yml

Diff (Show File Changes)
The -D and -diff flags output differences for any files that are changed on the remote machine. often use with --check
$ ansible-playbook -D --check playbook.yml
$ ansbile-playbook --diff --check playbook.yml

### Limiting which Tasks Run

step. you can choose to excute the task (y), skip it (n), or tell Ansible to continue running the rest of the playbook without prompting you (c)
$ ansible-playbook --step playbook.yml

start-at-task
$ ansible-playbook --start-at-task="install packages" playbook.yml

tags. Ansible allows you to add one or more tags to a task or a play.
```yaml
- hosts: myservers
  tags:
    - foo
  tasks:
    - name: install editors
      apt: name={{ item }}
      with_items:
        - vim
        - emacs
        - nano
    
    - name: run arbitrary command
      command: /opt/myprog
      tags:
        - bar
        - quux
```
Use the -t tagnames or --tags tagnames flag to tell Ansible to run only plays and tasks that have certain tags. Use --skip-tags tagnames flag to tell Ansible to skip plays and tasks that have certain tags.
$ ansible-playbook -t foo,bar playbook.yml
$ ansible-playbook --tags=foo,bar playbook.yml
$ ansible-playbook --skip-tags=baz,quux playbook.yml


# Ansible for Network Devices
network modules are pretty new , still in development.

example Enable SSH Authentication in Cisco IOP devices
```
# log in by telnet
$ telnet 10.0.0.1
Trying 10.0.0.1...
Connected to 10.0.0.1.
Escape character is '^]'.
Switch#

# switch to configuration mode
switch1#configure
Configuring from terminal, memory, or network [terminal]? terminal
Enter configuration commands, one per line. End with CNTL/Z.

# configure a static IP
switch1(config)#interface vlan 1
switch1(config-if)#if address 10.0.0.10 255.255.255.0

# set a hostname and domain
switch1(config)#hostname switch1
switch1(config)#ip domain-name example.net
switch1(config)#

# generate RSA bits
switch1(config)#crypto key generate rsa
The name for the keys will be: switch1.example.net

How many bits in the modules [512]: 4096
% Generating 4096 bit RSA keys, keys will be non-exportable...
[OK]
switch1(config)#

# add a new user admin
switch1(config)#username admin priviledge 15 secret s3cr3t

# configure the authentication model
switch1(config)#aaa new-model

# optional, set a password for enable
switch1(config)#enable secret s3cr3t

# disable telnet on the device
switch1(config)#line vty 0 15
switch1(config-line)#transport input ?

switch1(config-line)#transport input ssh
switch1(config-line)#exit

# save to config to be used as startup config
switch1#copy running-config startup-config

# verify log in by SSH
$ ssh admin@10.0.0.10
Password:

switch01>
```

ansible example set the hostname on Cisco Catalyst
```yaml
---
- hosts: localhost
  gather_facts: no
  connection: local
  tasks:
- name: set a hostname
  ios_config:
    lines: hostname swl
    provider:
      host: 10.0.0.10
      username: admin
      password: s3cr3t
      authorize: true
      auth_pass: s3cr3t
```

### Inventory and Variables for Network Modules
```
[ios_switches]
sw1.example.com net_host=10.0.0.10
```
It is a general pattern for network devices that playbooks always need to be executed with a local connection. We can put it in a group_vars/ios_switches file
```
---
ansible_connection: local
net_username: admin
net_password: s3cr3t
net_authorize: true
net_auth_pass: s3cr3t
```
final version of playbook, set hostname on Catalyst
```
---
- hosts: ios_switches
  gather_facts: no
  tasks:
  - name: set a hostname
    ios_config:
      lines: hostname {{ inventory_hostname_short }}
      provider:
        host: "{{ net_host | default(inventory_hostname) }}"
        username: "{{ net_username | default(omit) }}"
        password: "{{ net_password | default(omit) }}"
        authorize: "{{ net_authorize | default(omit) }}"
        auth_pass: "{{ net_auth_pass | default(omit) }}"
      backup: true
      save: true
```

### Use Configs from a File
example of a static IOS config as file
```
no service pad
service timestamps debug datetime msec
service timestamps log datetime msec
service password-encryption
boot-start-marker
boot-end-marker
aaa new-model
!
clock timezone CET 1 0
clock summer-time CEST recurring last Sun Mar 2:00 last Sun Oct 3:00
!
system mtu routing 1500
!
vtp mode transparent
!
ip dhcp snooping vlan 10-20
ip dhcp snooping
no ip domain-lookup
!
!
spanning-tree mode rapid-pvst
spanning-tree extend system-id
!
vlan internal allocation policy ascending
!
interface Vlan1
  no ip address
  no ip route-cache
  shutdown
!
ip default-gateway 10.0.0.1
no ip http server
no ip http secure-server
!
snmp-server community private
snmp-server community public RO
snmp-server location earth
snmp-server contact admin@example.com
!
ntp server 10.123.0.5
ntp server 10.100.222.12
!
```

example use src with a static config file
```yaml
---
- hosts: ios_switches
  gather_facts: no
  vars:
    provider:
      host: "{{ net_host | default(inventory_hostname) }}"
      username: "{{ net_username | default(omit) }}"
      password: "{{ net_password | default(omit) }}"
      authorize: "{{ net_authorize | default(omit) }}"
      auth_pass: "{{ net_auth_pass | default(omit) }}"
  tasks:
  - name: init the static config with backup before
    ios_config:
      backup: true
      src: files/ios_init_config.conf
      provider: "{{ provider }}"
    notify: save the running config
    
  - name: set a hostname
    ios_config:
      lines: hostname {{ inventory_hostname_short }}
      provider: "{{ provider }}"
    notify: save the running config
    
  handlers:
  - name: save the running config
    ios_config:
    save: true
    provider: "{{ provider }}"
```

### Using Templates for network configurations
example use src for static config files and templates
```yaml
---
- hosts: ios_switches
  gather_facts: no
  vars:
    provider:
      host: "{{ net_host | default(inventory_hostname) }}"
      username: "{{ net_username | default(omit) }}"
      password: "{{ net_password | default(omit) }}"
      authorize: "{{ net_authorize | default(omit) }}"
      auth_pass: "{{ net_auth_pass | default(omit) }}"
  tasks:
  - name: copy the static config
    ios_config:
      backup: true
      src: files/ios_init_config.conf.j2
      provider: "{{ provider }}"
    notify: save the running config
    
  handlers:
  - name: save the running config
    ios_config:
      save: true
      provider: "{{ provider }}"
```

example IOS config template, including dynamic configs for VLANS and interfaces
```
hostname {{ inventory_hostname_short }}

no service pad

service timestamps debug datetime msec
service timestamps log datetime msec
service password-encryption

boot-start-marker
boot-end-marker

clock timezone CET 1 0
clock summer-time CEST recurring last Sun Mar 2:00 last Sun Oct 3:00

ip dhcp snooping
no ip domain-lookup

spanning-tree mode rapid-pvst
spanning-tree extend system-id

vlan internal allocation policy ascending

!
{% if vlans is defined %}
{% for vlan in vlans %}
vlan {{ vlan.id }}
  name {{ vlan.name }}
!
{% endfor %}
{% endif %}

{% if ifaces is defined %}
{% for iface in ifaces %}
interface {{ iface.name }}
  description {{ iface.descr }}
{% if iface.vlans is defined %}
{% endif %}
  switchport access vlan {{ ifact.vlans | join(',') }}
  spanning-tree portfast
!
{% endfor %}
{% endif %}

no ip http server
no ip http secure-server

snmp-server community public RO
snmp-server location earch
snmp-server contact admin@example.com
! add more configs here...
```

### Gathering Facts
collecting facts for network modules: ios_facts
The ios_facts module has only one optional parameter: gather_subset. This parameter is used to limit wanted or filter unwanted facts by adding an explanation point (!). The default is !config, which corresponds to all but config

example collecting facts of an IOS device
```yaml
---
- hosts: ios_switches
  gather_facts: no
  tasks:
  - name: gathering IOS facts
    ios_facts:
       gather_subset: hardware
       host: "{{ net_host | default(inventory_hostname) }}"
       provider:
         username: "{{ net_username | default(omit) }}"
         password: "{{ net_password | default(omit) }}"
         authorize: "{{ net_authorize | default(omit) }}"
         auth_pass: "{{ net_auth_pass | default(omit) }}"
  - name: print out the IOS version
    debug:
      var: ansible_net_version
```
Note: Facts are injected to the Ansible host variables and do not need to be registered on the task level.


# Appendix A. SSH

native ssh. ~/.ssh/config

### SSH Agent

add private keys to ssh agent
$ ssh-add /path/to/keyfile.pem

Note: The SSH_AUTH_SOCK environment vairable must be set, or the ssh-add command will not be able to communicate with ssh-agent

List the keys in the ssh agent
$ ssh-add -l
$ ssh-add -L

starting up ssh-agent
$ ssh-agent

export environment variables
$ eval $(ssh-agent)

### Agent Forwarding
$ ssh -A myuser@myserver.example.com

enable agent forwarding by updating ~/.ssh/config file in your control machine
```
Host *
  ForwardAgent yes
```
or enable agent forwarding for only a specific server
```
Host appserver.example.com
  ForwardAgent yes
```

or edit ansible.cfg file
```
[ssh_connection]
ssh_args = -o ControlMaster=auto -o ControlPersist=60s -o ForwardAgent=yes
```
if you override the ssh_args variable, then you need to explicitly specify ControlMaster and ControlPersist for SSH multiplexing.

### sudo and Agent Forwarding
To allow the SSH_AUTH_SOCK variable to carry over via sudo to the root user, we can add the following line to the /etc/sudoers file
```
Defaults>root env_keep+=SSH_AUTH_SOCK
```

### Note. Validating files
The copy and template modules support a validate clause. This clasue lets you specify a program to run against the file that Ansible will generate. Use %s as a placeholder for the filename. 
When the validate clause is present, Ansible will copy the file to a temporary directory first and then run the specified validation program. If the validation program returns success (0), Ansible will copy the file from the temporary location to the proper destination.

example validating sudoers file
```yaml
- name: copy the sudoers file so we can do agent forwarding
  copy:
    src: files/99-keep-ssh-auth-sock-env
    dest: /etc/sudoers.d/99-keep-ssh-auth-sock-env
    owner: root group=root mode=0440
    validate: visudo -cf %s
```

example Cloning as root and changing permissions
```yaml
- name: verify the config is valid sudoers file
  local_action: command visudo -cf files/99-keep-ssh-auth-sock-env
  sudo: True
  
- name: copy the sudoers file so we can do agent forwarding
  copy:
    src: files/99-keep-ssh-auth-sock-env
    dest: /etc/sudoers.d/99-keep-ssh-auth-sock-env
    owner: root
    group: root
    mode: '0440'
    validate: 'visudo -cf %s'
  sudo: True
  
- name: check out my private git repository
  git:
    repo: git@...
    dest: "{{ proj_path }}"
  sudo: True
  
- name: set file ownership
  file:
    path: "{{ proj_path }}"
    state: directory
    recurse: yes
    owner: "{{ user }}"
    group: "{{ user }}"
  sudo: True
```

### Host Keys

retrieve the full SSH host key
$ mkdir files
$ ssh-keyscan github.com > files/known_hosts

the ssh-keyscan command supports an -H flag to that the hostname won't show up in the known_hosts file.

verify the host key with ssh-keygen
$ ssh-keygen -lf files/known_hosts

copy known_hosts file
```yaml
- name: copy system-wide known hosts
  copy: src=files/known_hosts dest=/etc/ssh/known_hosts owner=root group=root mode=0644
```
adding known host to remote hosts
```yaml
- name: ensure the ~/.ssh directory exists
  file: path=~/.ssh state=directory
- name: copy known hosts file
  copy: src=files/known_hosts dest=~/.ssh/known_hosts mode=0600
```
