
## Kubernetes

### Overview
The master is responsible for exposing the API, scheduling the deployments and managing the overall cluster.
Each node runs a container runtime, such as Docker or rkt, along with an agent that communicates with the master.
The node also runs additional components for logging, monitoring, service discovery and optional add-ones.
> Reference: https://thenewstack.io/kubernetes-an-overview/

![](./img/Chart_02_Kubernetes-Architecture.png)

![](./img/Chart_03_Kubernetes-Master.png)

![](./img/Chart_04_Kubernetes-Node.png)

### Pods
A pod is a collection of one or more containers. Pods act as the logical boundary for containers sharing the same context and resources.

Replica sets deliver the required scale and availability by maintaining a predefined set of pods at all times.
A single pod or a replica set can be exposed to the internal or external consumers via services. Pods are associated to services through key-value pairs called labels and selectors. Any new pod with labels that match the selector will automatically be discovered by teh service.

### etcd
A distributed key-value database, which acts as the single source of truth (SSOT) for all components of the Kubernetes cluster.

> SSOT: https://en.wikipedia.org/wiki/Single_source_of_truth

### Key Design Principles

#### Workload Scalability
Applications deployed in Kubernetes are packaged as microservices. These microservices are composed of multiple containers grouped as pods. Each container is designed to perform only one task. Stateless pods can be scaled on-demand or through dynamic auto-scaling.
> horizontal pod auto-scaling, which automatically scales the number of pods in a replication controller based on CPU utilization.


#### High Availability
ReplicaSets, ReplicationControllers and StatefulSets.
High availability of stateful workloads needs to add an available storage layer.
Each component of a Kubernetes cluster, etcd, API server, nodes can be configured for high availability.

#### Security
The API endpoints are secured through TLS.
Kubernetes clusters have two categories of users:
- Service accounts: managed directly by Kubernetes.
- Normal users: assumed to be managed by an independent service.

A secret is a Kubernetes object that contains a small amount of sensitive data, such as a password, token or key.
Usernames and passwords are encoded in base64 before storing them within a Kubernetes cluster. The caveat is that the secret is available to all the users of the same cluster namespace.

To allow or restrict network traffic to pods, network policies can be applied to the deployment.
A network policy is a specification of how selections of pods are allowed to communicate with each other and with other network endpoints.

#### Portability
Possible to mix and match clusters running across multiple cloud providers and on-premises (hybrid cloud).

