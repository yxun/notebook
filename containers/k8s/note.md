
Components

- Control Plane
  - kube-controller manager
  - cloud-controller manager
  - kube-api-server
  - kube-scheduler
  - etcd

- Nodes
  - kubelet
  - kube-proxy

Addons

- DNS
- Dashboard
- Resource Monitoring
- Logging
- Networking

API

Kubernetes Objects
Required Fields: apiVersion, kind, metadata, spec


Node status

$ kubectl describe node <node-name>

Controllers
Each controller tries to move the current cluster state closer to the desired state.

Using a Private image Registry
Specifying ImagePullSecrets on a Pod

$ kubectl create secret docker-registry <name> --docker-server=<> --docker-username=<> --docker-password=<> --docker-email=<>

.spc.imagePullSecrets.name: <name>

can be automated by setting the imagePullSecrets in a serviceAccount resource

Container environment
- a filesystem, which is a combination of an image and one or more volumes
- Container information
- cluster objects

The hostname of a Container is the name of the Pod. User defined environment variables from the Pod definition are also available to the Container, as are any environment variables specified statically in the Docker image.


