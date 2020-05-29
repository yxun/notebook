
# Docker
> Reference: https://www.aquasec.com/wiki/display/containers/Docker+Architecture

## Containers vs Virtual Machines

![](../img/Container_VM_Implementation.png)

Docker moves up the abstraction of resources from the hardware level to the Operating System level which results in much faster and more lightweight instances.

Containers benefits:
- application protability
- infrastructure separation
- self-contained microservices

Advantages:
- Resource Efficiency: Process level isolation and usage of the container host's kernel is more efficient when compared to virtualizing an entire hardware server.
- Portability: All the dependencies for an application are bundled in the container. They can be easily moved between development, test and production environments.
- Continuous Deployment and Testing

## The Docker Engine

Develop, assemble, ship and run applications using the following components:
- Docker Daemon: A persistent background process that manages Docker images, containers, networks and storage volumes. The Docker daemon constantly listens for Docker API requests and processes them.
- Docker Engine REST API: An API used by applications to interact with the Docker daemon; it can be accessed by an HTTP client.
- Docker CLI: A command line interface client for interacting with the Docker daemon. It greatly simplifies how you manage container instances.

![](../img/Docker_Engine.png)


## Docker Architecture

![](../img/Docker_Architecture.png)

### Docker Objects

#### Images: A read-only binary template used to build containers.

#### Containers: An encapsulated environment in which you run applications.

#### Networking: 
Two types of networks available: the default Docker network and user-defined networks.

Default Docker network: none, bridge and host.

The none and host networks are part of the network stack in Docker. 
The bridge network automatically creates a gateway and IP subnet and all containers that belong to this network can talk to each other via IP addressing. This network is not commonly used.

Three types of user-defined networks: 
- Bridge network: Similar to the default bridge network, a user-defined Bridge network differs in that there is no need for port forwarding for containers within the network to communicate with each other. And it has full support for automatic network discovery.
- Overlay network: An Overlay network is used when you need containers on separate hosts to be able to communicate with each other, as in the case of a distributed network. However, a caveat is that swam mode must be enabled for a cluster of Docker engines.
- Macvlan network: When using Bridge and Overlay networks a bridge resides between the containers and the host. A Macvlan network removes this bridge, providing the benefit of exposing container resources to external networks without dealing with port forwarding. This is realized by using MAC addresses instead of IP addresses.

#### Storage:
You can store data within the writable layer of a container but it requires a storage driver.

In terms of persistent storage, Docker offers four options:
- Data Volumes: with the ability to rename volumes, list volumes and also list the container that is associated with the volume. Data Volumes sit on the host file system within the Docker volumes folder, outside the containers.
  > Copy on write mechanism: (Implicit sharing or shadowing), if a resource is duplicated but not modified, instead of creating a new resource, the resource is shared between the copy and the original. Modifications are still create a copy. The copy operation is deferred to the first write.
- Data Volume Container: A dedicated container hosts a volume and to mount that volume to other containers. The volume container is independent of the application container and therefore can be shared across more than one container.
- Directory Mounts: Mount a host's local directory into a container. It can be outside the Docker volumes folder.
- Storage Plugins: connect to external storage platforms. These plugins map storage from the host to an external storage.

#### Docker Registries
Store and download images

> Service Discovery allows containers to find out about the environment they are in and find other services offered by other containers.


