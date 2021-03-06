

```shell

# Question: How to push image to registry
$ docker login <registry>
$ docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
$ docker push TARGET_IMAGE[:TAG]


# Question: How to copy docker images from one host to another without via repository?
# save docker image as a tar file
$ docker images
$ docker save -o <save image to new file path> <image name>

# copy image file to target VM
# local image in target docker
$ docker load -i <path to image tar file>


# Question: How to push image to local registry
# run local docker registry in container e.g.
$ docker run -d -p 5000:5000 --restart always --name <registry name> registry 

$ docker images
# tag image
# docker tag SOURCE_IMAGE[:TAG] RISTRY_HOST:PORT/TARGET_IMAGE[:TAG] e.g.
$ docker tag SOURCE_IMAGE[:TAG] localhost:5000/TARGET_IMAGE[:TAG]
# push image 
$ docker push localhost:5000/TARGET_IMAGE[:TAG]
# verification
$ curl http://localhost:5000/v2/_catalog


# Question: How to change the default docker container location on fedora
$ sudo systemctl stop docker
$ sudo systemctl daemon-reload
$ sudo mkdir -p [new docker directory]
$ sudo rsync -aqxP /var/lib/docker/ [new docker directory]
# update /etc/sysconfig/docker by adding  other_args="-g [new docker directory]"
$ sudo systemctl daemon-reload
$ sudo systemctl start docker

# clean docker volumes
$ docker volume rm $(docker volume ls -qf dangling=true)
$ docker volume ls -qf dangling=true | xargs -r docker volume rm

# or 
$ docker system prune

# Tell SELinux it is ok to allow systemd to manipulate its Cgroups configuration
# setsebool -P container_manage_cgroup true

# extract docker image SHA from inspect
$ docker inspect [repo]/[image_name]:[tag] | jq '.[0].RepoDigests[0]'

# macos stop docker desktop and disable vmnetd
$ ps aux | grep docker
$ netstat -an | grep vmnet
$ launchctl list | grep -i docker
$ sudo launchctl disable system/com.docker.vmnetd
$ sudo rm -f /Library/LaunchDaemons/com.docker.vmnetd.plist
$ sudo rm -f /Library/PrivilegedHelperTools/com.docker.vmnetd

```