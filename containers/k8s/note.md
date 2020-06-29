
## Components

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

## Containers

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

Specify a RuntimeClass

```yaml
apiVersion: node.k8s.io/v1beta1  # RuntimeClass is defined in the node.k8s.io API group
kind: RuntimeClass
metadata:
  name: myclass  # The name the RuntimeClass will be referenced by
  # RuntimeClass is a non-namespaced resource
handler: myconfiguration  # The name of the corresponding CRI configuration
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  runtimeClassName: myclass
  # ...
```

Container hooks, PostStart, PreStop

## Pods

Pods provide two kinds of shared resources: networking and storage
Each pod is assigned a unique IP address for each address family. Every container in a Pod shares the IP address, IPC namespace and network ports space. containers inside a Pod can communicate with one another using localhost.
shared storage Volumes

Pods do not, by themselves, self-heal. Kubernetes uses controller that handles the work of managing Pod instances.

A controller for the resource handles replication and rollout and automatic healing in case of Pod failure.

workload resources that manage one or more Pods:
- Deployment
- StatefulSet
- DaemonSet
- Job

Controllers for workload resources create Pods from a pod template.
Modifying the pod template, a new Pod is created to match the revised pod template.

If a Node dies, the Pods scheduled to that node are scheduled for deletion, after a timeout period. A given Pod (as defined by a UID) is not "rescheduled" to a new node, instead, it can be replaced by an identical Pod with a new UID.
When something has the same lifetime as a Pod, such as a volume, it is destroyed and created anew if that Pod is deleted for any reason.

$ kubectl delete --grace-period=0 --force , force deletes the Pod from the cluster state and etcd immediately.

Privileged mode for pod containers, using the privileged flag on the security context of the container spec.

Pod lifecycle

Pod phase: Pending, Running, Succeeded, Failed, Unknown

Container probes, three types of handlers: ExecAction, TCPSocketAction, HTTPGetAction
Three kinds of probes on running Containers: livenessProbe, readinessProbe, startupProbe

Container States: Waiting, Running, Terminated
$ kubectl describe pod [POD_NAME]

restartPolicy: Always, OnFailure, Never

PodDisruptionBudget (PDB) ensures minimal number of running Pods

Ephemeral Containers, a special type of container that runs temporarily in an existing Pod to accomplish user-initiated actions such as troubleshooting distroless containers.

## Controllers

### ReplicaSet
