
Reading notes from [The Docker Book](https://books.google.com/books/about/The_Docker_Book.html?id=4xQKBAAAQBAJ)

## Installing Docker
*Installing on Red Hat and family*
Docker is shipped by Red Hat as a native package on Red Hat Enterprise Linux 7 and later.
```shell
$ sudo subscription-manager repos --enable=rhel-7-server-extras-rpms
$ sudo yum install -y docker
```
*Starting the Docker daemon on the Red Hat family*
```shell
$ sudo systemctl start docker
$ sudo systemctl enable docker
$ sudo docker info
```
*Docker installation script*
```shell
$ curl https://get.docker.com/ | sudo sh
```

### The Docker daemon
*Configuring the Docker daemon*
```shell
$ sudo dockerd -H tcp://0.0.0.0:2375
```
or
```shell
$ export DOCKER_HOST="tcp://0.0.0.0:2375"
```
or
```shell
$ sudo dockerd -H tcp://0.0.0.0:2375 -H unix://home/docker/docker.sock
```
*Increase the verbosity of the Docker daemon*
```shell
$ sudo dockerd -D
```

## Getting Started with Docker
*Running container*
```shell
$ sudo docker run -i -t ubuntu /bin/bash
```
docker ps will only see the running containers, -a will show all containers, -l will show the last container that was run

*give a container name*
```shell
$ sudo docker run --name bob_the_container -i -t ubuntu /bin/bash
```
*Starting a stopped container*
```shell
$ sudo docker start bob_the_container
```
or start container by ID

*Attaching to a container*
```shell
$ sudo docker attach bob_the_container
```
you might need to hit Enter to bring up the prompt
If we exit this shell, our container will again be stopped.

*Creating daemonized containers*
```shell
$ sudo docker run --name daemon_dave -d ubuntu /bin/sh -c "while true; do echo hello world; sleep 1; done"
```
*Seeing log inside container*
```shell
$ sudo docker logs -f daemon_dave
```
-f append new entry, --tail 10 get the last tem lines of a log, -t prefix with timestamps

Docker log drivers, --log-driver, default json-file
```shell
$ sudo docker run --log-driver="syslog" --name daemon_dwayne -d ubuntu /bin/sh -c "while true; do echo hello world; sleep 1; done"
```
If you're running inside Docker for Mac or Windows you might need to start the Syslog daemon inside the VM. Use docker-machine ssh to connect to the Docker VM and run the syslogd command to start the Syslog daemon

*Inspecting the container's processes*
```shell
$ sudo docker top daemon_dave
```
*Docker statistics*
```shell
$ sudo docker stats daemon_dave daemon_dwayne
```
*Running a process inside an already running container*
```shell
$ sudo docker exec -d daemon_dave touch /etc/new_config_file
```
-u specify a new process owner for docker exec launch processes
```shell
$ sudo docker exec -t -i daemon_dave /bin/bash
```
*Stopping a daemonized container*
```shell
$ sudo docker stop daemon_dave
```
the docker stop command sends a SIGTERM signal to the Docker container's running process. the docker kill command sends a SIGKILL signal

*Automatic container restarts*
```shell
$ sudo docker run --restart=always --name daemon_alice -d ubuntu /bin/sh -c "while true; do echo hello world; sleep 1; done"
```
or --restart=on-failure:5

Finding out more about container
```shell
$ sudo docker inspect daemon_alice
```
we can also selectively query the inspect results using -f or --format
```shell
$ sudo docker inspect --format='{{ .State.Running }}' daemon_alice
$ sudo docker inspect --format '{{ .NetworkSettings.IPAddress }}' daemon_alice
$ sudo docker inspect --format '{{.Name}} {{.State.Running}}' \
daemon_dave daemon_alice
```

*Deleting a container*
```shell
$ sudo docker rm 80430f8d0921
```
**Deleting all containers**
```shell
$ sudo docker rm -f `sudo docker ps -a -q`
```
-a lists all containers, -q only returns the container IDs, -f force removes

*Listing Docker images*
```shell
$ sudo docker images
```
*Pull Docker image*
```shell
$ sudo docker pull ubuntu:16.04
```
*Search for images*
```shell
$ sudo docker search puppet
```
*Pull down an image*
```shell
$ sudo docker pull jamtur01/puppetmaster
```
Push images
```shell
$ sudo docker push youruser/yourimage
```
Delete image
```shell
$ sudo docker rmi youruser/yourimage
```
Delete all images
```shell
$ sudo docker rmi `docker images -a -q`
```

### Building our own images
*  via the docker commit command
*  via the docker build command with a Dockerfile

Login docker hub
```shell
$ sudo docker login
```
your credentials will be stored in the $HOME/.docker/config.json

Exit from the container, commit an image
```shell
$ sudo docker commit -m "A new custom image" -a "James Turnbull" \
4aab3ce3cb76 jamtur01/apache2:webserver
$ sudo docker inspect jamtur01/apache2:webserver
```

## Build images with a Dockerfile
1. Creating a directory(the build context) to hold Dockerfile
   Docker will upload the build context to Docker daemon

*first Dockerfile sample*
```dockerfile
# Version: 0.0.1
FROM ubuntu:16.04
MAINTAINER James Turnbull "james@example.com"
RUN apt-get update; apt-get install -y nginx
RUN echo 'Hi, I am in your container' \
        >/var/www/html/index.html
EXPOSE 80
```
By default, the RUN instruction executes inside a shell using /bin/sh -c
If you wish to execute without a shell, you can specify the instruction in exec format
RUN [ "apt-get", " install", "-y", "nginx" ]

You can specify multiple EXPOSE instructions to mark multiple ports
You can expose ports at run time with the docker run command with the --expose option

Build the image from Dockerfile
```shell
$ sudo docker build -t="jamtur01/static_web:v1" .
```
-t option to mark our resulting image with a repository and a name
If you don't specify any tag, Docker will automatically tag your image as latest
The trailing . tells Docker to look in the local directory to find the Dockerfile

You can also specify a Git repo as a source for the Dockerfile
```shell
$ sudo docker build -t="jamtur01/static_web:v1" \
github.com/turnbullpublishing/docker-static_web
```
You can specify a path to a file to use -f flag.
The file specified doesn't need to be called Dockerfile but must still be within the build context

If a file named .dockerignore exists in the root of the build context then
it is interpreted as a newline-separated list of exclusion patterns.
Globbing using Go's filepath.

Dockerfiles and the build cache
we can use the --no-cache flag with docker build command
```shell
$ sudo docker build --no-cache -t="jamtur01/static_web" .
```

*Dockerfile template 1*
```shell
FROM ubuntu:16.04
MAINTAINER James Turnbull "james@example.com"
ENV REFRESHED _AT 2016-07-01
RUN apt-get -qq update
```
or RUN yum -q makecache

Viewing new image
```shell
$ sudo docker images jamtur01/static_web
$ sudo docker history 22d47c8cb6e5
```

Launching a container from new image
```shell
$ sudo docker run -d -p 80 --name static_web jamtur01/static_web nginx -g "daemon off;"
```
-d to run detached in the background for Nginx daemon
nginx -g "daemon off;" launch Nginx in the foreground
-p manages ports
*Docker can randomly assign a port from 32768 to 61000 on the Docker host that maps to port 80 on the container*

*You can specify a port on the Docker host that maps to container*
```shell
$ sudo docker ps -l
```
-l shows the last container launched
```shell
$ sudo docker port 6751b94bb5c0 80
```
```shell
$ sudo docker run -d -p 8080:80 --name static_web_8000 jamtur01/static_web nginx -g "daemon off;"
```
bind port 80 on the container to port 8080 on the local host
```shell
$ sudo docker run -d -p 127.0.0.1:80:80 --name static_web_lb jamtur01/static_web nginx -g "daemon off;"
$ sudo docker run -d -p 127.0.0.1::80 --name static_web_random jamtur01/static_web nginx -g "daemon off;"
```
We can bind UDP ports by adding the suffix /udp to the port binding
```shell
$ sudo docker run -d -P --name static_web_all jamtur01/static_web nginx -g "daemon off;"
-P to publish all ports exposed via EXPOSE instructions in Dockerfile
```

## Dockerfile instructions

### CMD
*specifies the command to run when a container is launched.*
```shell
$ sudo docker run -i -t jamtur01/static_web /bin/true
```
This would be articulated in the Dockerfile as: CMD ["/bin/true"]
You can specify parameters to the command: CMD ["/bin/bash","-l"]
We can use the docker run command to override the CMD instruction.

**TIP**: You can only specify one CMD instruction in a Dockerfile. If more than one is specified, then the last CMD instruction will be used. If you need to run multiple processes or commands as part of starting a container you should use a service management tool like Supervisor.

### ENTRYPOINT
*provides a command that isn't as easily overridden. Instead, any arguments we specify on the docker run command line will be passed as arguments to the command specified in the ENTRYPOINT.*
```dockerfile
ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]
ENTRYPOINT ["/usr/sbin/nginx"]
```
```shell
$ sudo docker run -t -i jamtur01/static_web -g "daemon off;"
```
we can also combine ENTRYPOINT and CMD. This allows us to build in a default command to execute combined with overridable options and flags on the docker run command line.
```dockerfile
ENTRYPOINT ["/usr/sbin/nginx"]
CMD ["-h"]
```
**TIP**: If required at runtime, you can override the ENTRYPOINT instruction using the docker run command with --entrypoint flag

### WORKDIR
*provides a way to set the working directory for the container and the ENTRYPOINT and/or CMD to be executed.*
```dockerfile
WORKDIR /opt/webapp/db
RUN bundle install
WORKDIR /opt/webapp
ENTRYPOINT ["rackup"]
```
You can override the working directory at runtime with the -w flag
```shell
$ sudo docker run -it -w /var/log ubuntu pwd
```

### ENV
*used to set environment variables during the image build process*
```dockerfile
ENV RVM_PATH /home/rvm/
ENV RVM_PATH=/home/rvm RVM_ARCHFLAGS="-arch i386"
```
**NOTE**: You can also escape environment variables when needed by prefixing them with a backslash.
These environment variables will also be persisted into containers created from your image.
You can also pass environment variables on the docker run command line using the -e flag. These variables will only apply at runtime
```shell
$ sudo docker run -it -e "WEB_PORT=8080" ubuntu env
```

### USER
*specifies a user that the image should be run as*
```dockerfile
USER nginx
```
This will cause containers created from the image to be run by the nginx user.
```dockerfile
USER user
USER user:group
USER uid
USER uid:gid
USER user:gid
USER uid:group
```
You can also override this at runtime by specifying the -u flag with the docker run command
**TIP**: The default user if you don't specify the USER instruction is root

### VOLUME

A volume is a specially designated directory within one or more containers that bypasses the Union File System to provide several useful features for persistent or shared data:
* Volumes can be shared and reused between containers.
* A container doesn't have to be running to share its volumes.
* Changes to a volume are made directly.
* Changes to a volume will not be included when you update an image.
* Volumes persist until no containers use them.

This allows us to add data into an image without committing it to the image and allows us to share that data between containers.
```dockerfile
VOLUME ["/opt/project"]
```
This would attempt to create a mount point /opt/project to any container created from the image.
**TIP**: Also useful and related is the docker cp command. This allows you to copy files to and from your containers.
```dockerfile
VOLUME ["/opt/project", "/data"]
```

### ADD
Adds files and directories from our build environment into our image.
The ADD instruction specifies a source and a destination for the files
```dockerfile
ADD software.lic /opt/application/software.lic
```
The source of the file can be a URL, filename, or directory as long as it is inside the build context or environment.
If the destination ends in a /, then it considers the source a directory. If it doesn't end in a /, it considers the source a file.

If a tar archive (valid archive types include gzip, bzip2, xz) is specified as the source file, then Docker will automatically unpack it for you:
```dockerfile
ADD latest.tar.gz /var/www/wordpress/
```
The archive is unpacked with the same behavior as running tar with the -x option: the output is the union of whatever exists in the destination plus the contents of the archive.

If a file or directory with the same name already exists in the destination, it will not be overwritten.
If the destination doesn't exist, Docker will create the full path for us, including any directories. New files and directories will be created with a mode of 0755 and a UID and GID of 0.

**NOTE**: the build cache can be invalidated by ADD instructions. If the files or directories added by an ADD instruction change then this will invalidate the cache for all following instructions in the Dockerfile.

### COPY
Purely focused on copying local files from the build context and does not have any extraction or decompression capabilities.
```dockerfile
COPY conf.d/ /etc/apache2/
```
Anything outside of the build context is not available. The destination should be an absolute path inside the container.
If the source is a directory, the entire directory is copied, including filesystem metadata; if the source is any other kind of file, it is copied individually along with its metadata.

### LABEL
Adds metadata to a Docker image. The metadata is in the form of key/value pairs.
```dockerfile
LABEL location="New York" type="Data Center" role="Web Server"
```
We recommend combining all your metadata in a single LABEL. You can inspect the labels using the docker inspect command.

### STOPSIGNAL
Sets the system call signal that will be sent to the container when you tell it to stop. 
This signal can be a valid number from the kernel syscall table, for instance 9, or a signal name in the format SIGNAME, for instance SIGKILL.

### ARG
Defines variables that can be passed at build-time vid the docker build command. This is done using the --build-arg flag. You can only specify build-time arguments that have been defined in the Dockerfile.

**Note**
The ARG instruction defines a variable that users can pass at build-time to the builder with the docker build command using the --build-arg <varname>=<value> flag.

The ENV instruction sets the environment variable <key> to the value <value>. The environment variable set using ENV will persist when a container is run from the resulting image.

```dockerfile
ARG build
ARG webapp_user=user
```
The second ARG instruction sets a default, if no value is specified for the argument at build-time then the default is used.
```shell
$ docker build --build-arg build=1234 -t jamtur01/webapp .
```
Don't pass secrets like credentials or keys. Your credentials will be exposed during the build process and in the build history of the image.

Docker has a set of predefined ARG variables that you can use at build-time without a corresponding ARG instruction in the Dockerfile.
```
HTTP_PROXY
http_proxy
HTTPS_PROXY
https_proxy
FTP_PROXY
ftp_proxy
NO_PROXY
no_proxy
```
To use these predefined variables, pass them using the --build-arg <variable>=<value> flag to the docker build command.

### SHELL
Allows the default shell used for the shell form of commands to be overridden. The default shell on Linux is ["/bin/sh", "-c"] and on Windows is ["cmd", "/S", "/C"].

The SHELL instruction can be used multiple times.

### HEALTHCHECK
Tells Docker how to test a container to check that it is still working correctly.
```dockerfile
HEALTHCHECK --interval=10s --timeout=1m --retries=5 CMD curl http://localhost || exit 1
```
--interval - defaults to 30 seconds. This is the period between health checks.
--timeout - defaults to 30 seconds. If the health check takes longer the timeout then it is deemed to have failed.
--retries - defaults to 3. The number of failed checks before the container is marked as unhealthy.

The command should exit with 0 to indicate health or 1 to indicate an unhealthy state. We can see the state of the health check using the docker inspect command.
```shell
$ sudo docker inspect --format '{{.State.Health.Status}}' static_web
```
The health check state and related data is stored in the .State.Health namespace.
```shell
$ sudo docker inspect --format '{{range .State.Health.log}} {{.ExitCode}} {{.Output}} {{end}}' static
```
Here we're iterating through the array of .Log entries in the docker inspect output.
There can only be one HEALTHCHECK instruction in a Dockerfile. If you list more than one then only the last will take effect.
You can also disable any health checks
```dockerfile
HEALTHCHECK NONE
```

### ONBUILD
Adds triggers to images. A trigger is executed when the image is used as the basis of another image.
The trigger inserts a new instruction in the build process, as if it were specified right after the FROM instruction.
```dockerfile
ONBUILD ADD . /app/src
ONBUILD RUN cd /app/src; make
```
The ONBUILD triggers are executed in the order specified in the parent image and are only inherited once (i.e., by children and not grandchildren).

**NOTE**: There are several instructions you can't ONBUILD: FROM, MAINTAINER, and ONBUILD itself.

### Run a registry from a container
```shell
$ docker run -d -p 5000:5000 --name registry registry:2
```
This will launch a container running version 2.0 of the registry application and bind port 5000 to the localhost

Test the new registry
first identify the image's ID
```shell
$ sudo docker images jamtur01/static_web
```
Next tag the image for our new registry. prefix the image name with the hostname and port of our new registry
```shell
$ sudo docker tag 22d47c8c6e5 docker.example.com:5000/jamtur01/static_web
```
then we can push it to the new registry
```shell
$ sudo docker push docker.example.com:5000/jamtur01/static_web
```
The image is then posted in the local registry and available for us to build new containers
```shell
$ sudo docker run -t -i docker.example.com:5000/jamtur01/static_web /bin/bash
```

## Testing with Docker
Using Docker to test a static website
*Dockerfile*
```dockerfile
FROM ubuntu:16.04
MAINTAINER James Turnbull "james@example.com"
ENV REFRESHED_AT 2016-06-01
RUN apt-get -yqq update; apt-get -yqq install nginx
RUN mkdir -p /var/www/html/website
ADD global.conf /etc/nginx/conf.d/
ADD nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
```
*global.conf*
```nginx
server {
listen 0.0.0.0:80;
server_name     _;

root /var/www/html/website;
index index.html index.html;

access_log /var/log/nginx/default_access.log;
error_log  /var/log/nginx/default_error.log;
}
```
*nginx.conf*
```nginx
user www-data;
worker_process 4;
pid /run/nginx.pid;
daemon off;

events { }

http {
        sendfile on;
        tcp_nopush on;
        tcp_nodelay on;
        keepalive_timeout 65;
        types_hash_max_size 2048;
        include /etc/nginx/mime.types;
        default_type application/octet-stream;
        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;
        gzip on;
        gzip_disable "msie6";
        include /etc/nginx/conf.d/*.conf;
}
```
In the configuration file, the daemon off; option stops Nginx from going into the background and forces it to run in the foreground.
```shell
$ sudo docker build -t jamtur01/nginx .
$ sudo docker run -d -p 80 --name website \
-v $PWD/website:/var/www/html/website \
jamtur01/nginx nginx
```
-v Volumes are specially designated directories within one or more containers that bypass the layered Union File System to provide persistent or shared data for Docker.

We can also specify the read/write status of the container directory by adding either rw or ro
```shell
$ sudo docker run -d -p 80 --name website \
-v $PWD/website:/var/www/html/website:ro \
jamtur01/nginx nginx
```

## Using Docker to build and test a web application

Build Sinatra application
$ mkdir -p sinatra
$ cd sinatra

*Dockerfile*
```dockerfile
FROM ubuntu:16.04
MAINTAINER James Turnbull "james@example.com"
ENV REFRESHED_AT 2016_06_01

RUN apt-get update -yqq; apt-get -yqq install ruby ruby-dev build -essential redis-tools
RUN gem install --no-rdoc --no-ri sinatra json redis
RUN mkdir -p /opt/webapp
EXPOSE 4567
CMD [ "/opt/webapp/bin/webapp" ]
```
```shell
$ sudo docker build -t jamtur01/sinatra .
```

Creating Sinatra container

*webapp source code in the sinatra /webapp/lib/app.rb*
```ruby
require "rubygems"
require "sinatra"
require "json"

class App < Sinatra::Application

        set :bind, '0.0.0.0'

        get '/' do
                "<h1>DockerBook Test Sinatra app</h1>"
        end
    
        post '/json/?' do
                params.to_json
        end

end
```
```shell
$ chmod +x webapp/bin/webapp

$ sudo docker run -d -p 4567 --name webapp \
-v $PWD/webapp:/opt/webapp jamtur01/sinatra
$ sudo docker logs webapp
$ sudo docker top webapp
$ sudo docker port webapp 4567

$ curl -i -H 'Accept: application/json' \
-d 'name=Foostatus=Bar' http://localhost:49160/jsonHTTP/1.1 200 OKContent-Type: text/html;charset=utf-8Content-Length: 29X-Xss-Protection: 1; mode=blockX-Content-Type-Options: nosniffX-Frame-Options: SAMEORIGINServer: WEBrick/1.3.1 (Ruby/2.3.1/2016-04-26)Date: Wed, 03 Aug 2016 18:30:06 GMTConnection: Keep-Alive"name":"Foo","status":"Bar"
```

Extending Sinatra application to use Redis

*source code in lib/app.rb*
```ruby
require "rubygems"
require "sinatra"
require "json"
require "redis"

class App < Sinatra::Application

        redis = Redis.new(:host => 'db', :port => '6379')

        set :bind, '0.0.0.0'

        get '/' do
"<h1>DockerBook Test Redis-enabled Sinatra app</h1>"
        end

        get '/json' do
params = redis.get "params"
params.to_json
        end

        post '/json/?' do
redis.set "params", [params].to_json
params.to_json
        end

end
```
```shell
$ chmod +x webapp_redis/bin/webapp
```

Building a Redis database image
$ mkdir redis
$ cd redis
*Dockerfile*
```dockerfile
FROM ubuntu:16.04
MAINTAINER James Turnbull "james@example.com"
ENV REFRESHED_AT 2016-06-01
RUN apt-get -yqq update; apt-get -yqq install redis-server redis-tools
EXPOSE 6379
ENTRYPOINT [ "/usr/bin/redis-server" ]
CMD []
```
```shell
$ sudo docker build -t jamtur01/redis .

$ sudo docker run -d -p 6379 --name redis jamtur01/redis
$ sudo docker port redis 6379
```
Connect to that Redis instance
```shell
$ sudo apt-get -y install redis-tools
$ sudo yum install -y -q redis
$ redis-cli -h 127.0.0.1 -p 49160
redis 127.0.0.1:49160>quit
```

## Connecting Sinatra application to the Redis container

### Docker internal networking

Every Docker container is assigned an IP address, provided through an interface *docker0* created when we installed Docker.
The docker0 interface has an RFC1918 private IP address in the 172.16-172.30 range. 172.17.42.1 will be the gateway address for the Docker network and all our Docker containers.
```shell
$ ip a show docker0
```
Every time Docker creates a container, it creates a pair of peer interfaces that are like opposite ends of a pipe. It gives one of the peers to the container to become its eth0 interface and keeps the other peer, with a unique name like veth\*, out on the host machine.
```shell
$ sudo docker run -t -i ubuntu /bin/bash
$ ip a show eth0
```
```shell
$ sudo iptables -t nat -L -n
$ sudo docker inspect redis
$ sudo docker inspect -f '{{ .NetworkSettings.IPAddress }}' redis
```

There are two big rough edges in using docker internal networking:
1. we'd need to hard-code the IP address of our Redis container into our applications.
2. if we restart the container, Docker changes the IP address.

### Docker networking

To use Docker networks we first need to create a network and then launch a container inside the network.
```shell
$ sudo docker network create app
```
This uses the docker network command to create a bridge network called app.
```shell
$ sudo docker network inspect app
```
**TIP** In addition to bridge networks, which exist on a single host, we can also create overlay networks, which allow us to span multiple hosts.

list all current netowrks
```shell
$ sudo docker network ls
```
remove a network
```shell
$ sudo docker network rm
```
add a container to network
```shell
$ sudo docker run -d --net=app --name db jamtur01/redis
$ sudo docker network inspect app
```
```shell
$ cd sinatra
$ sudo docker run -p 4567 \
--net=app --name network_test -t -i \
jamtur01/sinatra /bin/bash
```
As the container has been started inside the app network, Docker will have taken note of all other containers running inside that network and populated their addresses in local DNS.
```shell
$ apt-get install -y dnsutils iputils-ping
$ nslookup db
```

A Docker network will also add the app network as a domain suffix for the network, any host in the app network can be resolved by hostname.app, here db.app.
```shell
$ ping db.app
```
In our case we just need the db entry to make our application function.
redis = Redis.new(:host => 'db', :port => '6379')
```shell
$ sudo docker run -d -p 4567 \
--net=app --name webapp_redis \
-v $PWD/webapp_redis:/opt/webapp jamtur01/sinatra
$ sudo docker port webapp_redis 4567
```
```shell
$ curl -i -H 'Accept: application/json' \
-d 'name=Foostatus=Bar' http://localhost:49162/jsonHTTP/1.1 200 OKContent-Type: text/html;charset=utf-8Content-Length: 29X-Xss-Protection: 1; mode=blockX-Content-Type-Options: nosniffX-Frame-Options: SAMEORIGINServer: WEBrick/1.3.1 (Ruby/2.3.1/2016-04-26)Date: Wed, 03 Aug 2016 18:30:06 GMTConnection: Keep-Alive"name":"Foo", "status":"Bar"

$ curl -i http://localhost:49162/json
```

Connecting existing containers to the network
```shell
$ sudo docker run -d --name db2 jamtur01/redis
$ sudo docker network connect app db2
$ sudo docker network inspect app
```
disconnect a container from a network
```shell
$ sudo docker network disconnect app db2
```
Containers can belong to multiple networks at once.

## Using Docker for continuous integration
### Build a Jenkins and Docker server
*Jenkins and Docker Dockerfile*
```dockerfile
FROM Jenkins
MAINTAINER james@example.com
ENV REFRESHED_AT 2016-06-01

USER root
RUN apt-get -qqy update; apt-get install -qqy sudo
RUN echo "Jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers
RUN wget http://get.docker.com/builds/Linux/x86_64/docker-latest.tgz
RUN tar -xzvf docker-latest.tgz
RUN mv docker/* /usr/bin/

USER Jenkins
RUN /usr/local/bin/install-plugins.sh junit git git-client ssh-slaves greenballs chucknorris
```

Next, create a directory to hold our Jenkin's configuration
```shell
$ sudo mkdir -p /var/jenkins_home
$ cd /var/jenkins_home
$ sudo chown -R 1000 /var/jenkins_home
```
we set the ownership of the jenkins_home directory to 1000, which is the UID of the Jenkins user inside the image.
```shell
$ sudo docker build -t jamtur01/jenkins .

$ sudo docker run -d -p 8080:8080 -p 50000:50000 \
-v /var/jenkins_home:/var/jenkins_home \
-v /var/run/docker.sock:/var/run/docker.sock \
--name Jenkins \
jamtur01/jenkins
```
**WARNING** This is a security risk. By binding the Docker socket inside the Jenkins container you give the container access to the underlying Docker host.

$ sudo docker logs Jenkins
Take note of the initial admin password. This is also stored in a file in the jenkins_home directory at:
*/var/jenkins_home/secrets/initialAdminPassword*

### Create a new Jenkins job
name job Docker_test_job, job type Freestyle project
Advanced... Use Custom workspace and specify */var/jenkins_home/jobs/${JOB_NAME}/workspace* as the Directory.

Under Source Code Management, select Git and specify https://github.com/turnbullpublishing/docker-jenkins-sample.git
This is a simple repository containing some Ruby-based RSpec tests.

Add Build Step, Execute shell
```shell
# Build the image to be used for this job.

IMAGE=$(sudo docker build . | tail -1 | awk '{ print $NF }')

# Build the directory to be mounted into Docker.

MNT="$WORKSPACE/.."

# Execute the build inside Docker.
CONTAINER=$(sudo docker run -d -v $MNT:/opt/project/ $IMAGE /bin/bash -c 'cd /opt/project/workspace; rake spec')

# Attach to the  container so that we can see the output.
sudo docker attach $CONTAINER

# Get its exit code as soon as the container stops.
RC=$(sudo docker wait $CONTAINER)

# Delete the container we've just used.
sudo docker rm $CONTAINER

# Exit with the same values as that with which the process exited.
exit $RC
```

*The Docker test job Dockerfile*
```dockerfile
FROM ubuntu:16.04
MAINTAINER James Turnbull "james@example.com"
ENV REFRESHED_AT 2016-06-01
RUN apt-get update
RUN apt-get -y install ruby rake
RUN gem install --no-rdoc --no-ri ripes ci_reporter_rspec
```
The ci_reporter_rspec gem allows RSpec output to be converted to JUnit-formatted XML that Jenkins can consume.
The docker wait command blocks until the command the container is executing finishes

Next we click the Add post-build action and add Publish JUnit test result report. In the Test report XMLs, we need to specify spec/reports/\*.xml
 We can also automate our Jenkins job further by enabling SCM polling or with a post-commit hook.
 **TIP** You should also use parameterized builds to make this job and the shell script step more generic to suit multiple frameworks and languages.

### Multi-configuration Jenkins
 New Item, Multi-configuration project, Add Axis, select User-defined Axis, named OS and specify three values: centos, debian, and ubuntu. In the Build Environment, tick Delete workspace before build starts.

### Jenkins multi-configuration shell step
```shell
# Build the image to be used for this run.
cd $OS; IMAGE=$(sudo docker build . | tail -1 | awk '{ print $NF }')

# Build the directory to be mounted into Docker.
MNT="$WORKSPACE/.."

# Execute the build inside Docker.
CONTAINER=$(sudo docker run -d -v "$MNT:/opt/project" $IMAGE /bin/bash -c "cd /opt/project/$OS; rake spec")

# Attach to the container's streams so that we can see the output.
sudo docker attach $CONTAINER

# As soon as the process exits, get its return value.
RC=$(sudo docker wait $CONTAINER)

# Delete the container we've just used.
sudo docker rm $CONTAINER

# Exit with the same value as that with which the process exited.
exit $RC
```

*CentOS-based Dockerfile*
```dockerfile
FROM centos:latest
MAINTAINER James Turnbull "james@example.com"
ENV REFRESHED_AT 2016-06-01
RUN yum -y install ruby rubygems rubygem-rake
RUN gem install --no-rdoc --no-ri rspec ci_reporter_rspec
```
Add a post-build action of Publish JUnit test result report and specify the location of XML output: spec/reports/*.xml.

## Building services with Docker
### Build Jekyll framework with two images
* An image that both installs Jekyll and the prerequisites
* An image that serves our Jekyll site via Apache

workflow is going to be:
* Create the Jekyll base image and the Apache image (once-off)
* Create a container from our Jekyll image that holds our website source mounted via a volume
* Create a Docker container from our Apache image that uses the volume containing the compiled site and serve that out
* Rinse and repeat as the site needs to be updated.

*The Jekyll base image Dockerfile*
```dockerfile
FROM ubuntu:16.04
MAINTAINER James Turnbull <james@example.com>
ENV REFRESHED_AT 2016-06-01

RUN apt-get -yqq update
RUN apt-get -yqq install ruby ruby-dev build-essential nodejs
RUN gem install --no-rdoc --no-ri jekyll -v 2.5.3

VOLUME /data
VOLUME /var/www/html
WORKDIR /data

ENTRYPOINT [ "jekyll", "build", "--destination=/var/www/html" ]
```

* /data/, which is going to hold our new website source code
* /var/www/html/, which is going to hold our compiled Jekyll site

Building the Jekyll base image
```shell
$ sudo docker build -t jamtur01/jekyll .
$ sudo docker images
```

*The Apache image Dockerfile*
```dockerfile
FROM ubuntu:16.04
MAINTAINER James Turnbull <james@example.com>
ENV REFRESHED_AT 2016-06-01

RUN apt-get -yqq update
RUN apt-get -yqq install apache2

VOLUME [ "/var/www/html" ]
WORKDIR /var/www/html

ENV APACHE_RUN_USER www-data
ENV	APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2

RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR

EXPOSE 80

ENTRYPOINT [ "/usr/sbin/apache2" ]
CMD [ "-D", "FOREGROUND" ]
```

Build the Jekyll Apache image
```shell
$ sudo docker build -t jamtur01/apache .
```
Launching our Jekyll site
get source code
$ HOME=/home/james
$ cd $HOME
$ git clone

Create a Jekyll container
```shell
$ sudo docker run -v /home/james/james_blog:/data/ \
--name james_blog jamtur01/jekyll
```
**TIP** Volumes live on Docker host, in the */var/lib/docker/volumes*
```shell
$ sudo docker inspect -f "{{ range .Mounts }}{{.}}{{end}}" james_blog
```
Create an Apache container
```shell
$ sudo docker run -d -P --volumes-from james_blog jamtur01/apache
```
Updating Jekyll site
editing the james_blog/_config.yml
```shell
$ sudo docker start james_blog
$ sudo docker logs james_blog

# Backing up Jekyll volume
$ sudo docker run --rm --volume-from james_blog \
-v $(pwd):/backup ubuntu \
tar cvf /backup/james_blog_backup.tar /var/www/html
```
### Build a Java application server with Docker
* An image that pulls down specified WAR files from a URL and stores them in a volume.
* An image with Tomcat server installed that runs those downloaded WAR files.

*war file fetcher*
```dockerfile
FROM ubuntu:16.04
MAINTAINER James Turnbull <james@example.com>
ENV REFRESHED_AT 2016-06-01

RUN apt-get -yqq update
RUN apt-get -yqq install wget

VOLUME [ "/var/lib/tomcat7/webapps/" ]
WORKDIR /var/lib/tomcat7/webapps/

ENTRYPOINT [ "wget" ]
CMD [ "-?" ]
```
```shell
$ sudo docker build -t jamtur01/fetcher .
$ sudo docker run -it --name sample jamtur01/fetcher \
https://tomcat.apache.org/tomcat-7.0-doc/appdev/sample/sample.war
$ sudo docker inspect -f "{{ range .Mounts }}{{.}}{{end}}" sample
```
*Tomcat7 Application server*
```dockerfile
FROM ubuntu:16.04
MAINTAINER James Turnbull <james@example.com>
ENV REFRESHED_AT 2016-06-01

RUN apt-get -yqq update
RUN apt-get -yqq install tomcat7 default-jdk

ENV CATALINA_HOME /usr/share/tomcat7
ENV CATALINA_BASE /var/lib/tomcat7
ENV CATALINA_PID /var/run/tomcat7.pid
ENV CATALINA_SH /usr/share/tomcat7/bin/catalina.sh
ENV CATALINA_TMPDIR /tmp/tomcat7-tomcat7-tmp

RUN mkdir -p $CATALINA_TMPDIR

VOLUME [ "/var/lib/tomcat7/webapps/" ]

EXPOSE 8080

ENTRYPOINT [ "/usr/share/tomcat7/bin/catalina.sh", "run" ]
```
```shell
$ sudo docker build -t jamtur01/tomcat7 .
$ sudo docker run --name sample_app --volumes-from sample \
-d -P jamtur01/tomcat7

# TProv application
$ sudo apt-get -qqy install ruby make ruby-dev
$ sudo gem install --no-rdoc --no-ri tprov
$ sudo tprov
```

## A multi-container application stack (Node.js)

* A Node container to serve our Node application, linked to:
* A Redis primary container to hold and cluster our state, linked to:
* Two Redis replica containers to cluster our state.
* A logging container to capture our application logs.

*Node.js image Dockerfile*
```dockerfile
FROM ubuntu: 16.04
MAINTAINER James Turnbull <james@example.com>
ENV REFRESHED_AT 2016-06-01

RUN apt-get -yqq update
RUN apt-get -yqq install nodejs npm
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN mkdir -p /var/log/nodeapp

ADD nodeapp /opt/nodeapp/

WORKDIR /opt/nodeapp
RUN npm install

VOLUME [ "/var/log/nodeapp" ]

EXPOSE 3000

ENTRYPOINT [ "nodejs", "server.js" ]
```
```shell
$ sudo docker build -t jamtur01/nodejs .
```
*Redis base image Dockerfile*
```dockerfile
FROM ubuntu:16.04
MAINTAINER James Turnbull <james@example.com>
ENV REFRESHED_AT 2016-06-01

RUN apt-get -yqq update
RUN apt-get install -yqq software-properties-common python-software-properties
RUN add-apt-repository ppa:chris-lea/redis-server
RUN apt-get -yqq update
RUN apt-get -yqq install redis-server redis-tools

VOLUME [ "/var/lib/redis", "/var/log/redis" ]

EXPOSE 6379
CMD []
```
```shell
$ sudo docker build -t jamtur01/redis .
```
*Redis primary image Dockerfile*
```dockerfile
FROM jamtur01/redis
MAINTAINER James Turnbull <james@example.com>
ENV REFRESHED_AT 2016-06-01

ENTRYPOINT [ "redis-server", "--logfile /var/log/redis/redis-server.log" ]
```
```shell
$ sudo docker build -t jamtur01/redis_primary .
```

*Redis replica image Dockerfile*
```dockerfile
FROM jamtur01/redis
MAINTAINER James Turnbull <james@example.com>
ENV REFRESHED_AT 2016-06-01

ENTRYPOINT [ "redis-server", "--logfile /var/log/redis/redis-replica.log", "--slaveof redis-primary 6379" ]
```
```shell
$ sudo docker build -t jamtur01/redis_replica .

$ sudo docker network create express
$ sudo docker run -d -h redis-primary \
--net express --name redis_primary jamtur01/redis_primary

# NOTE do not use underscores in hostnames.

$ sudo docker run -it --rm --volume-from redis_primary \
ubuntu cat /var/log/redis/redis-server.log

$ sudo docker run -d -h redis-replica1 \
--name redis_replica1 \
--net express \
jamtur01/redis_replica
$ sudo docker run -it --rm --volumes-from redis_replica1 \
ubuntu cat /var/log/redis/redis-replica.log

$ sudo docker run -d -h redis-replica2 \
--name redis_replica2 \
--net express \
jamtur01/redis_replica
$ sudo docker run -it --rm --volumes-from redis_replica2 ubuntu \
cat /var/log/redis/redis-replica.log

$ sudo docker run -d \
--name nodeapp -p 3000:3000 \
--net express \
jamtur01/nodejs
```
### Capturing application logs
*Logstash image Dockerfile*
```dockerfile
FROM ubuntu:16.04
MAINTAINER James Turnbull <james@example.com>
ENV REFRESHED_AT 2016-06-01

RUN apt-get -yqq update
RUN apt-get -yqq install wget
RUN wget -0 -http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key add -
RUN echo 'deb http://packages.elasticssearch.org/logstash/1.5/debian stable main' > /etc/apt/sources.list.d/logstash.list
RUN apt-get -yqq update
RUN apt-get -yqq install logstash default-jdk

ADD logstash.conf /etc/

WORKDIR /opt/logstash

ENTRYPOINT [ "bin/logstash" ]
CMD [ "--config=/etc/logstash.conf" ]
```

*Logstash configuration*
```
input {
	file {
		type => "syslog"
		path => ["/var/log/nodeapp/nodeapp.log", "/var/log/redis/redis-server.log"]
	}
}
output {
	stdout {
		codec => rubydebug
	}
}
```
```shell
$ sudo docker build -t jamtur01/logstash .
$ sudo docker run -d --name logstash \
--volumes-from redis_primary \
--volumes-from nodeapp \
jamtur01/logstash
```

## Docker Orchestration and Service Discovery

### Docker Compose
YAML format

### Installing Docker Compose on Linux
```shell
$ sudo curl -L https://github.com/docker/compose/releases/download/1.8.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose

# installing Docker Compose on OS X
$ sudo bash -c "curl -L https://github.com/docker/compose/releases/download/1.8.0/docker-compose-Darwin-x86_64 > /usr/ local/bin/docker-compose"
$ sudo chmod +x /usr/local/bin/docker-compose
```
**TIP** Replace the 1.8.0 with the release number of the current Docker Compose release
```shell
$ Installing Compose via Pip
$ sudo pip install -U docker-compose

$ docker-compose --version
```
### Sample Python Flask, Redis application
$ mkdir composeapp
$ cd composeapp

*The app.py file*
```python
from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host="redis", port=6379)

@app.route('/')
def hello():
	redis.incr('hits')
	return 'Hello Docker Book reader! I have been seen {0} times'.format(redis.get('hits'))


if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
```

*The requirements.txt*
```
flask
redis
```

*The composeapp Dockerfile*
```dockerfile
# Compose Sample application image
FROM python:2.7
MAINTAINER James Turnbull <james@example.com>
ENV REFRESHED_AT 2016-06-01

ADD . /composeapp

WORKDIR /composeapp

RUn pip install -r requirements.txt
```

### build the composeapp application
```shell
$ sudo docker build -t jamtur01/compseapp .
```
We will use the default Redis image on the Docker Hub

*The docker-compose.yml file*
$ touch docker-compose.yml
```yaml
web:
  image: jamtur01/compseappp
  command: python app.py
  ports:
    - "5000:5000"
  volumes:
    - .:/composeapp
  links:
    - redis
redis:
  image: redis
```

The docker run equivalent command
```shell
$ sudo docker run -d -p 5000:5000 -v .:/composeapp --link redis:redis \
--name jamtur01/composeapp python app.py
```
Running Compose
$ cd composeapp
$ sudo docker-compose up

**TIP** You must be inside the directory with the docker-compose.yml file

Compose has prefixed and suffixed the names specified in the docker-compose.yml file with the directory and a number respectively

We can also run Componse with -d flag to run services daemonized

$ sudo docker-compose up -d

**TIP** By default, Compose connect to local Docker daemon. We can use the DOCKER_HOST environment variable to connect to a remote Docker host.

### check compose 
```shell
$ sudo docker-compose ps
$ sudo docker-compose logs

# stop running services
$ sudo docker-compose stop

# If the services don't stop, you can use 
$ sudo docker-compose kill 

# restart services
$ sudo docker-compose start

# remove services
$ sudo docker-compose rm
```

### Service Discovery, Consul
Consul uses the Raft consensus algorithm to require a quorum for writes. It also exposes a key value store and service catalog.
* A service catalog with an API instead of the traditional key=value store of most service discovery tools
* Both a DNS-based query interface through an inbuild DNS server and a HTTP-based REST API to query the information
* Service monitoring AKA health checks.

### Building a Consul image
$ mkdir consul
$ cd consul
$ touch Dockerfile
```dockerfile
FROM ubuntu:16.04
MAINTAINER James Turnbull <james@example.com>
ENV REFRESHED_AT 2014-08-01

RUN apt-get -qqy update
RUN apt-get -qqy install curl unzip

ADD https://releases.hashicorp.com/consul/0.6.4/consul_0.6.4_linux_amd64.zip /tmp/consul.zip
RUN cd /usr/sbin; unzip /tmp/consul.zip; chmod +x /usr/sbin/consul; rm /tmp/consul.zip

RUN mkdir -p /webui/
ADD https://releases.hashicorp.com/consul/0.6.4/consul_0.6.4_web_ui.zip /webui/webui.zip
RUN cd /webui; unzip webui.zip; rm webui.zip

ADD consul.json /config/

EXPOSE 53/udp 8300 8301 8301/udp 8302 8302/udp 8400 8500

VOLUME ["/data"]

ENTRYPOINT [ "/usr/sbin/consul", "agent", "-config-dir=/config" ]
CMD []
```

*The consul.json configuation file*
```
{
	"data_dir": "/data",
	"ui_dir": "/webui",
	"client_addr": "0.0.0.0",
	"posts": {
		"dns": 53
	},
	"recursor": "8.8.8.8"
}
```
```shell
$ sudo docker build -t="jamtur01/consul" .
$ sudo docker run -p 8500:8500 -p 53:53/udp \
-h node1 jamtur01/consul -server -bootstrap
```
Getting public IP on larry
```shell
larry$ PUBLIC_IP="$(ifconfig etho0 | awk -F ' *|:' '/inet addr/{print $4')"
larry$ echo $PUBLIC_IP
```
getting public IP on curly and moe
adding the cluster IP address

Start the Consul bootstrap node
```shell
larry$ sudo docker run -d -h $HOSTNAME \
-p 8300:8300 -p 8301:8301 \
-p 8301:8301/udp -p 8302:8302 \
-p 8302:8302/udp -p 8400:8400 \
-p 8500:8500 -p 53:53/udp \
--name larry_agent jamtur01/consul \
-server -advertise $PUBLIC_IP -bootstrap-expect 3
```
Starting the agnet on curly
```shell
curly$ sudo docker run -d -h $HOSTNAME \
-p 8300:8300 -p 8301:8301 \
-p 8301:8301/udp -p 8302:8302 \
-p 8302:8302/udp -p 8400:8400 \
-p 8500:8500 -p 53:53/udp \
--name curly_agent jamtur01/consul \
-server -advertise $PUBLIC_IP -join $JOIN_IP
```
Getting the docker0 IP address
```shell
larry$ ip addr show docker0
```
Testing the Consul DNS
```shell
larry$ dig @172.17.0.1 consul.service.consul
```

Creating a distributed_app Dockerfile directory
$ mkdir distributed_app
$ cd distributed_app
$ touch Dockerfile

*The distributed_app Dockerfile*
```dockerfile
FROM ubuntu:16.04
MAINTAINER James Turnbull "james@example.com"
ENV REFRESHED_AT 2016-06-01

RUN apt-get -qqy update
RUN apt-get -qqy install ruby-dev git libcurl4-openssl-dev curl build-essential python
RUN gem install --no-ri --no-rdoc uwsgi sinatra

RUN mkdir -p /opt/distributed_app
WORKDIR /opt/distributed_app

RUN uwsgi --build-plugin https://github.com/unbit/uwsgi-consul

ADD uwsgi-consul.ini /opt/distributed_app/
ADD config.ru /opt/distributed_app/

ENTRYPOINT [ "uwsgi", "--ini", "uwsgi-consul.ini", "--ini", "uwsgi-consul.ini:server1", "--ini", "uwsgi-consul.ini:server2"]
CMD []
```

*The uWSGI configuration*
```
[uwsgi]
plugins = consul
socket = 127.0.0.1:9999
master = true
enable-threads = true

[server1]
consul-register = url=http://%h.node.consul:8500,name=distributed_app,id=server1,port=2001
mule = config.ru

[server2]
consul-register = url=http://%h.node.consul:8500,name=distributed_app,id=server2,port=2002
mule = config.ru
```

*The distributed_app config.ru file*
```ruby
require 'rubygems'
require 'sinatra'

get '/' do
"Hello World!"
end

run Sinatra::Application
```

$ sudo docker build -t="jamtur01/distributed_app" .

*The distributed_client Dockerfile*
```dockerfile
FROM ubuntu:16.04
MAINTAINER James Turnbull "james@example.com"
ENV REFRESHED_AT 2016-06-01

RUN apt-get -qqy update
RUN apt-get -qqy install ruby ruby-dev build-essential
RUN gen install --no-ri --no-rdoc json

RUN mkdir -p /opt/distributed_client
ADD client.rb /opt/distributed_client/

WORKDIR /opt/distributed_client

ENTRYPOINT [ "ruby", "/opt/distributed_client/client.rb" ]
CMD []
```

*The distributed_client application*
```ruby
require "rubygems"
require "json"
require "net/http"
require "uri"
require "resolv"

uri = URI.parse("http://consul.service.consul:8500/v1/catalog/service/distributed_app")

http = Net::HTTP.new(uri.host, uri.port)
request = Net::HTTP::Get.new(uri.request_uri)
response = http.request(request)

while true
	if response.body = "{}"
		puts "There are no distributed applications registered in Consul"
		sleep(1)
	elsif
		result = JSON.parse(response.body)
		result.each do |service|
			puts "Application #{service['ServiceName']} with element #{service["ServiceID"]} on port #{service["ServicePort"]} found on node #{service["Node"]} (#{service["Address"]})."
			dns = Resolv::DNS.new.getresources("distributed_app.service.consul", Resolv::DNS::Resource::IN::A)
			puts "We can also resolve DNS - #{service['ServiceName']} resolves to #{dns.collect { |d| d.address }.join(" and ")}."
			sleep(1)
		end
	end
end
```
```shell
$ sudo docker build -t="jamtur01/distributed_client" .

larry$ sudo docker run --dns=172.17.0.1 -h $HOSTNAME -d --name larry_distributed \
jamtur01/distributed_app
curly$ sudo docker run --dns=172.17.0.1 -h $HOSTNAME -d --name curly_distributed \
jamtur01/distributed_app
```

## Docker Swarm
A swarm is made up of manager and worker nodes. Each unit of work is called a task. Services defined which tasks are executed on your nodes. Each service consists of a container image and a series of commands to execute inside one or more containers on the nodes. Replicated services, Global services.

### Setting up a Swarm
Docker Swarm default ports
| Port       | Description        |
| ---------- | ------------------ |
| 2377       | Cluster Management |
| 7946 + udp | Node communication |
| 4789 + udp | Overlay network    |

Initializing a swarm on larry
$ sudo docker swarm init --advertise-addr $PUBLIC_IP

**TIP** If you ever need to get this token back, you can run
$ sudo docker swarm join-token worker

$ sudo docker into
$ sudo docker node ls

curly$ sudo docker swarm join \
--token S.. \
162.243.167.159:2377

### Running a service on your Swarm
Creating a swarm service
```shell
$ sudo docker service create --replicas 2 --name heyworld ubuntu /bin/sh -c "while true; do echo hey world; sleep 1; done"
$ sudo docker service ls
$ sudo docker service inspect --pretty heyworld
$ sudo docker service ps heyworld
```
Scaling the heyworld service
```shell
$ sudo docker service scale heyworld=3
```
Running a global service
```
$ sudo docker service create --name heyworld_global --mode global ubuntu /bin/sh -c "while true; do echo hey world; sleep 1;done"
$ sudo docker service ps heyworld_global

$ sudo docker service rm heyworld
```

## Orchestration alternatives
- Fleet and etcd 
- Kubernetes
- Apache Mesos
- Helios
- Centurion

# Docker APIs
- Regiestry API
- Docker Hub API
- Docker Remote API

**TIP** any user that belongs to the docker group can run docker without need ing root priviledges

/etc/default/docker
/etc/init/docker.conf
/lib/systemd/system/docker.service
/etc/sysconfig/docker
/usr/lib/systemd/system/docker.service

Default systemd daemon start options
```
ExecStart=/usr/bin/dockerd --selinux-enabled
```

Network binding systemd daemon start options
```
ExecStart=/usr/bin/dockerd --selinus-enabled -H tcp://0.0.0.0:2375

$ sudo systemctl --system daemon-reload
```

Connecting to a remote Docker daemon
```
$ sudo docker -H docker.example.com:2375 info
```

Revisiting the DOCKER_HOST environment variable
```
$ export DOCKER_HOST="tcp://docker.example.com:2375"
```

**Warning**: this connection is unauthenticated, later discuss add authentication

API samples
```shell
$ curl http://docker.example.com:2375/info | python3 -mjson.tool

$ curl http://docker.example.com:2375/images/json | python3 -mjson.tool

$ curl "http://docker.example.com:2375/images/search?term=jamtur01" | python3 -mjson.tool

$ curl -s "http://docker.example.com:2375/containers/json?all=1" | python3 -mjson.tool

$ curl -X POST -H "Content-Type: application/json" \
http://docker.example.com:2375/containers/create \
-d '{
     "Image":"jamtur01/jekyll"
     "Hostname":"jekyll"
}'

$ curl -X POST -H "Content-Type: application/json" \
http://docker.example.com:2375/containers/591..../start \
-d '{
       "PublishAllPorts":true
}'

$ curl http://docker.example.com:2375/containers/591.../json | python3 -mjson.tool
```

The Docker Ruby client example
```ruby
require 'docker'
...

module TProvAPI
  class Application < Sinatra::Base

...

    Docker.url = Env['DOCKER_URL'] || 'http://localhost:2375'
    Docker.options = {
      :ssl_verify_peer => false
    }
```

Installing the Docker Ruby client API prereq
$ sudo yum -y install ruby ruby-irb
...
$ sudo gen install docker-api json
...
$ irb

updated TProv
```ruby
def get_war(name, url)
  container = Docker::Container.create('Cmd' => url, 'Image' => 'jamtur01/fetcher', 'name' => name)
  container.start
  container.id
end

def create_instance(name)
  container = Docker::Container.create('Image' => 'jamtur01/tomcat7')
  container.start('PublishAllPorts' => true, 'VolumesFrom' => name)
  container.id
end

def delete_instance(cid)
  container = Docker::Container.get(cid)
  container.kill
end
```

## Authenticating the Docker Remote API

**TLS authentication** 

### Create certificate authority

**Warning**: This relies on a local CA running on your Docker host. This is not as secure as using a full-fledged CA

### checking for openssl
```shell
$ which openssl
```
```shell
# create a CA directory
$ sudo mkdir /etc/docker

# generating a private key
$ cd /etc/docker
$ echo 01 | sudo tee ca.srl
sudo openssl genrsa -des3 -out ca-key.pem
Enter pass phrase for ca-key.pem:
Verifying - Enter pass phrase for ca-key.pem:

# Creating a CA certificate
$ sudo openssl req -new -x509 -days 365 -key ca-key.pem -out ca.pem
Enter pass phrase for ca-key.pem:

Country Name (2 letter code) [US]:
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [IBM]:
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or Your name) []:docker.example.com
Email Address []:
```

This will create the ca.pem file that is the certificate for our CA

### Create a server certificate signing request and key
### Create a server key
```shell
$ sudo openssl genrsa -des3 -out server-key.pem
Enter pass phrase for server-key.pem:
Verifying - Enter pass phrase for server-key.pem:
```
```shell
# Creating our server CSR(certificate signing request)
$ sudo openssl req -new -key server-key.pem -out server.csr
Enter pass phrase for server-key.pem:

Country Name [US]:
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company):
Organizational Unit Name (eg, section) []:
Common Name (eg, server FQDN or Your name) []:*
Email Address []:

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
```

This will create a file called server.csr
The most important option here is Common Name or CN. This should either be the FQDN (fully qualified domain name) or *, which will allow us to use the server certificate on any server

### Signing our CSR and generate our server certificate
```shell
$ sudo openssl x509 -req -days 365 -in server.csr -CA ca.pem \
-CAkey ca-key.pem -out server-cert.pem
Enter pass phrase for ca-key.pem:
```
This will generate a file called server-cert.pem

Removing the passphrase from the server.key
```
$ sudo openssl rsa -in server-key.pem -out server-key.pem
Enter pass phrase for server-key.pem:
writing RSA key
```

Securing the key and certificate on the Docker server
```shell
$ sudo chmod 0600 /etc/docker/server-key.pem /etc/docker/server-cert.pem \
/etc/docker/ca-key.pem /etc/docker/ca.pem
```


Configuring the Docker daemon
Enabling Docker TLS on systemd
```
ExecStart=/usr/bin/docker -d -H tcp://0.0.0.0:2376 --tlsverify --tlscacert=/etc/docker/ca.pem --tlscert=/etc/docker/server-cert.pem --tlskey=/etc/docker/server-key.pem
```
```shell
$ sudo systemctl --system daemon-reload
```
**TIP** You can use the --tls flag to enable TLS, but not client-side authentication

### Creating client side certificate and key
```shell
$ sudo openssl genrsa -des3 -out client-key.pem
Enter pass phrase for client-key.pem:
Verifying - Enter pass phrase for client-key.pem:

$ sudo openssl req -new -key client-key.pem -out client.csr
Enter pass phrase for client-key.pem:

Country Name [US]:
State or Province Name:
Locality Name []:
Organization Name:
Organizational Unit Name:
Common Name:
Email Address:

A challenge password:
An optional company name:
```
```shell
# Adding Client Authentication attributes
$ echo extendedKeyUsage = clientAuth > extfile.cnf

# Signing our client CSR
```
```shell
$ sudo openssl x509 -req -days 365 -in client.csr -CA ca.pem \
-CAkey ca-key.pem -out client-cert.pem -extfile extfile.cnf

Enter pass phrase for ca-key.pem:
```
this generate client-cert.pem

### Stripping out the client key pass phrase
```shell
$ sudo openssl rsa -in client-key.pem -out client-key.pem
Enter pass phrase for client-key.pem:
writing RSA key
```

### Configuring Docker client for authentication
copy ca.pem, client-cert.pem and client-key.pem to the Docker client host

### Copying the key and certificate on the Docker client
```shell
$ mkdir -p ~/.docker/
$ cp ca.pem ~/.docker/ca.pem
$ cp client-key.pem ~/.docker/key.pem
$ cp client-cert.pem ~/.docker/cert.pem
$ chmod 0600 ~/.docker/key.pem ~/.docker/cert.pem
```

### Testing TLS-authenticated connection
```shell
$ sudo docker -H=docker.example.com:2376 --tlsverify info
```

