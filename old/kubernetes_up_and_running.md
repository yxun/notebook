Reading notes from [Kubernetes: Up and Running](https://books.google.com/books/about/Kubernetes_Up_and_Running.html?id=fF4KswEACAAJ)

# Introduction

### Velocity
The core concepts that enable velocity are
- **Immutability**
- **Declarative Configuration**
- **Online Self-Healing System**

#### Immutability
Immutable container images are at the core of everything that you will build in Kubernetes.
Two different ways to upgrade your software:
1. You can log into a container, run a command to download your new software, kill the old server, and start the new one.
2. You can build a new container image, push it to a container registry, kill the existing container, and start a new one.

#### Declarative Configuration
Everything in Kubernetes is a declarative configuration object that represents the desired state of the system.

#### Self-Healing Systems
continuously takes actions to ensure that the current state matches the desired state.

TIP: the ideal team size is the "two-pizza team", or roughly six to eight people.

# Creating and Running Containers

Applications are typically comprised of a language runtime, libraries, and your source code.

A container image is a binary package that encapsulates all of the files necessary to run an application inside of an OS container.

Containers fall into two main categories: System containers, Application containers

System containers seek to mimic Virtual machines and often run a full boot process. They often include a set of system services typically found in a VM, such as ssh, cron, and syslog.
Application containers differ from system containers in that they commonly run a single application.

Files that are removed by subsequent layers in the system are actually still present in the images.

Limiting memory and CPU resources
```bash
$ docker run -d --name kuard \
--publish 8080:8080 \
--memory 200m \
--memory-swap 1G \
--cpu-shares 1024 \
image:1
```


# Common kubectl Commands

#### Namespaces
You can think of each namespaces as a folder that holds a set of objects. By default, the kubectl command-line tool interacts with the **default** namespace. If you want to use a different namespace, for example, `kubectl --namespace=mystuff`

#### Contexts
If you want ot change the default namespace more permanently, you can use a context. This gets recorded in a kubectl configuration file, usually located at $HOME/.kube/config . This configuration file also stores how to both find and authenticate to your cluster. For example, create a context
`$ kubectl config set-context my-context --namespace=mystuff`

To use this newly created context
`$ kubectl config use-context my-context`
Contexts can also be used to manage different clusters or different users for authenticating to those clusters using the `--users` or `--clusters` flags with the `set-context` command.

#### Viewing Kubernetes API Objects
If you run `kubectl get <resource-name>` you will get a listing of all resources in the current namespaces. If you want to get a specific resource, you can use `kubectl get <resource-name> <object-name>`

To get slightly more information `-o wide` flag.
view the objects as raw JSON or YAML `-o json` or `-o yaml` flags
skip the header `--no-headers` flag

extract specific fields from the object, for example, extract and print the IP address of the pod
`$ kubectl get pods my-pod -o jsonpath --template={.status.podIP}`

show more detailed information about a particular object
`$ kubectl describe <resource-name> <obj-name>`

#### Creating, Updating, and Destorying Kubernetes Objects
for example, create an object with yaml file
`$ kubectl apply -f obj.yaml`
Similarly, you can use the apply command again to update the object

interactive edits
`$ kubectl edit <resource-name> <obj-name>`
which will download the latest object state, and then launch an editor that contains the definition.
After you save the file, it will be automatically uploaded back to the Kubernetes cluster.

delete an object
`$ kubectl delete -f obj.yaml`
delete an object using the resource type and name
`$ kubectl delete <resource-name> <obj-name>`

#### Labeling and Annotating Objects
for example, add color=red label to a pod named bar
`$ kubectl label pods bar color=red`

overwrite an existing label, you need to add the `--overwrite` flag

remove a label
`$ kubectl label pods bar -color`

#### Debugging Commands
see the logs for a running container
`$ kubectl logs <pod-name>`
choose the container to view using the `-c` flag

continuously stream the logs back to the terminal, add `-f`(follow) command-line flag

execute a command in a running container
`$ kubectl exec -it <pod-name> -- bash`
This will provide an interactive shell

copy files from a running container to your local machine. You can also specify directories
`$ kubectl cp <pod-name>:/path/to/remote/file /path/to/local/file`
reverse the syntax to copy a file from your local machine to the container.

view help
`$ kubectl help` or `$ kubectl help command-name`


# Pods
A Pod represents a collection of application containers and volumes running in the same execution environment. Pods, not containers, are the smallest deployable artifact in a Kubernetes clusters. This means all of the containers in a Pod always land on the same machine.

Each container within a Pod runs in its own cgroup, but they share a number of Linux namespaces.
Applications running in the same Pod share the same IP address and port space (network namespace), have the same hostname (UTS namespace) , and can communicate using native interprocess communication channels over System V IPS or POSIX message queues (IPS namespace).

In general, containers work correctly if they land on different machines, then multiple Pods is probably the correct solution. If no, a Pod is the correct grouping for the containers.

#### The Pod Manifest
The Kubernetes API server accepts and processes Pod manifests before storing them in persistent storage (etcd).
Scheduling multiple replicas of the same application onto the same machine is worse ofr reliability, since the machine is a single failure domain.
Once scheduled to a node, Pods don't move and must be explicitly destroyed and rescheduled.

#### Creating a Pod
`$ kubectl run kuard --image=gcr.io/kuar-demo/kuard-amd64:1`

see the status of a Pod
`$ kubectl get pods`

delete a Pod
`$ kubectl delete deployment/kuard`

#### Creating a Pod Manifest
Pod manifests can be written using YAML or JSON. Pod manifests include a couple of key fields and attributes: mainly a **metadata** section for describing the Pod and its labels, a **spec** section for describing volumes, and a list of containers that will run in the Pod.

example kuard-pod.yaml
```
apiVersion: v1
kind: Pod
metadata:
  name: kuard
spec:
  containers:
    - image: gcr.io/kuar-demo/kuard-amd64:1
      name: kuard
      ports:
        - containerPort: 8080
          name: http
          protocol: TCP
```

#### Running Pods
launch a single instance of Pod
`$ kubectl apply -f kuard-pod.yaml`

#### Listing Pods
`$ kubectl get pods`
or
`$ kubectl describe pods kuard`

#### Deleting a Pod
`$ kubectl delete pods/kuard`
or
`$ kubectl delete -f kuard-pod.yaml`
When a Pod is deleted, it is not immediately killed. Instead, if you run kubectl get pods you will see that the Pod is in the Terminating state. All Pods have a termination grace period. By default, this is 30 seconds. When a Pod is transitioned to Terminating it no longer receives new requests.

#### Accessing your Pod
Using Port Forwarding
`$ kubectl port-forward kuard 8080:8080`
a secure tunnel is created from your local machine, through the Kubernetes master, to the instance of the Pod running on one of the worker nodes.
As long as the port-forward command is still running, you can access the Pod on , for example, http://localhost:8080

Getting logs
`$ kubectl logs kuard`  Adding the -f flag will cause you to continuously stream logs.
The kubectl logs command always tries to get logs from the currently running container. Adding the --previous flag will get logs from a previous instance of the container.

Running commands in Container with exec
`$ kubectl exec kuard date`
get an interactive session
`$ kubectl exec -it kuard ash`

Copying files to and from Containers
for example
`$ kubectl cp <pod-name>:/captures/capture3.txt ./capture3.txt`
`$ kubectl cp $HOME/config.txt <pod-name>:/config.txt`

#### Health Checks
kubernetes ensures that the main process of your application is always running. If it isn't, Kubernetes restarts it.
Application liveness health checks are defined in Pod manifest.

Liveness Probe
Liveness probes are defined per container. For example, kuard-pod-health.yaml
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kuard
spec:
  containers:
    - image: gcr.io/kuar-demo/kuard-amd64:1
      name: kuard
      livenessProbe:
        httpGet:
          path: /healthy
          port: 8080
        initialDelaySeconds: 5
        timeoutSeconds: 1
        periodSeconds: 10
        failureThreshold: 3
      ports:
        - containerPort: 8080
          name: http
          protocol: TCP
```
`$ kubectl apply -f kuard-pod-health.yaml`
`$ kubectl port-forward kuard 8080:8080`

Readiness Probe
Liveness determines if an application is running properly. Containers that fail liveness checks are restarted. Readiness describes when a container is ready to serve user requests. Containers that fail readiness checks are removed from service load balances.

Types of Health Checks
HTTP checks, tcpSocket, exec

#### Resource Management
we measure efficiency with the utilization metric. Utilization is defined as the amount of a resource actively being used divided by the amount of a resource that has been purchased.
Resource *requests* specify the minimum amount of a resource required to run the application. Resource *limits* specify the maximum amount of a resource that an application can consume.

for example, kuard-pod-reslim.yaml
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kuard
spec:
  containers:
    - image: gcr.io/kuar-demo/kuard-amd64:1
      name: kuard
      resources:
        requests:
          cpu: "500m"
          memory: "128Mi"
        limits:
          cpu: "1000m"
          memory: "256Mi"
      ports:
        - containerPort: 8080
          name: http
          protocol: TCP
```
Resources are  requested per container, not per Pod.
When the system runs out of memory, the kubelet terminates containers whose memory usage is greater than their requested memory. These containers are automatically restarted. but with less available memory on the machine for the container ot consume.

#### Persisting Data with Volumes
*spec.volumes* section defines all of the volumes that may be accessed by containers in the Pod manifest. *volumeMounts* array defines the volumes that are mounted into a particular container, and the path where each volume should be mounted.
example kuard-pod-vol.yaml
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kuard
spec:
  volumes:
    - name: "kuard-data"
      hostPath:
        Path:"/var/lib/kuard"
  containers:
    - image: gcr.io/kuar-demo/kuard-amd64:1
      name: kuard
      volumeMounts:
        - mountPath: "/data"
          name: "kuard-data"
      ports:
        - containerPort: 8080
          name: http
          protocol: TCP
```

Different ways of Using Volumes with Pods: communication/synchronization, cache, persistent data, mounting the host file system, persisting data using remote disks

example kuard-pod-full.yaml
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kuard
spec:
  volumes:
    - name: "kuard-data"
      nfs:
        server: my.nfs.server.local
        path: "/exports"
  containers:
    - image: gcr.io/kuar-demo/kuard-amd64:1
      name: kuard
      ports:
        - containerPort: 8080
          name: http
          protocol: TCP
      resources:
        requests:
          cpu: "500m"
          memory: "128Mi"
        limits:
          cpu: "1000m"
          memory: "256Mi"
      volumeMounts:
        - mountPath: "/data"
          name: "kuard-data"
      livenessProbe:
        httpGet:
          path: /healthy
          port: 8080
        initialDelaySeconds: 5
        timeoutSeconds: 1
        periodSeconds: 10
        failureThreshold: 3
      readinessProbe:
        httpGet:
          path: /ready
          port: 8080
        initialDelaySeconds:30
        timeoutSeconds: 1
        periodSeconds: 10
        failureThreshold: 3
```


# Labels and Annotations

Labels are key/value pairs that can be attached to Kubernetes objects such as Pods and ReplicaSets. Labels provides the foundation for grouping objects

Annotations are key/value pairs designed to hold nonidentifying information that can be leveraged by tools and libraries.

## Labels
Label keys can be broken down into two parts: an optional prefix and a name, separated by a slash. The prefix, if specified, must be a DNS subdomain with a 253-character limit. The key name is required and must be shorter than 63 characters. Names must also start and end with an alphanumeric character and permis the use of -, _ , and . between characters.
Label values are strings with a maximum length of 63 characters. The contents of the label values follow the same rules as for label keys.

Applying Labels
for example creating a few deployments with two apps and two environments for each. and also have two different versions
```
$ kubectl run alpaca-prod \
  --image=gcr.io/kuar-demo/kuard-amd64:1 \
  --replicas=2 \
  --labels="ver=1,app=alpaca,env=prod"

$ kubectl run alpaca-test \
  --image=gcr.io/kuar-demo/kuard-amd64:2 \
  --replicas=1 \
  --labels="ver=2,app=alpaca,env=test"

$ kubectl run bandicoot-prod \
  --image=gcr.io/kuar-demo/kuard-amd64:2 \
  --replicas=2 \
  --labels="ver=2,app=bandicoot,env=prod"

$ kubectl run bandicoot-staging \
  --image=gcr.io/kuar-demo/kuard-amd64:2 \
  --replicas=1 \
  --labels="ver=2,app=bandicoot,env=staging"
```
show labels
`$ kubectl get deployments --show-labels`

Modifying Labels
`$ kubectl label deployments alpaca-test "canary=true"`
Note: kubectl label command will only change the label on the deployment itself; it won't affect the objects (ReplicaSets and Pods) the deployment creates. To change those, you'll need to change the template embedded in the deployment.

Use the -L option to kubectl get to show a label value as a column
`$ kubectl get deployments -L canary`

Remove a label by applying a dash suffix
`$ kubectl label deployments alpaca-test "canary-"`

### Label Selectors
Label selectors are used to filter Kubernetes objects based on a set of labels.
for example, list pods that had the ver label set to 2
`$ kubectl get pods --selector="ver=2"`
if we specify two selectors separated by a comma, only the objects that satisfy both will be returned. This is a logical AND operation
`$ kubectl get pods --selector="app=bandicoot,ver=2"`
we can also ask if a label is one of a set of values
`$ kubectl get pods --selector="app in (alpaca,bandicoot)"`
list all of the deployment with a label set to anything
`$ kubectl get deployments --selector="canary"`

Selector operators

| Operator                   | Description                        |
| -------------------------- | ---------------------------------- |
| key=value                  | key is set to value                |
| key!=value                 | key is not set to value            |
| key in (value1, value2)    | key is one of value1 or value2     |
| key notin (value1, value2) | key is not one of value1 or value2 |
| key                        | key is set                         |
| !key                       | key is not set                     |

#### Label Selectors in API Objects
example
```yaml
selector:
  matchLabels:
    app: alpaca
  matchExpressions:
    - {key: ver, operator: In, values: [1, 2]}
```
All of the terms are evaluated as a logical AND

## Annotations
Annotations provide a place to store additional metadata for Kubernetes objects.
Users should avoid using the Kubernetes API server as a general-purpose database. Annotations are good for small bits of data that are highly associated with a specific resource.

### Defining Annotations
example
```yaml
...
metadata:
  annotations:
    example.com/icon-url: "https://example.com/icon.png"
...
```

## Cleanup
`$ kubectl delete deployments --all`


# Service Discovery

A Service object is way to create a named label selector.
We can use kubectl expose to create a service.
`$kubectl get services -o wide`

example port-forwarding
```
$ ALPACA_POD=$(kubectl get pods -l app=alpaca \
    -o jsonpath=`{.items[0].metadata.name}`)
$ kubectl port-forward $ALPACA_POD 48858:8080
```

Service DNS in DNS Resolver on the kuard server

Readiness Check example
```
spec:
  ...
  template:
    ...
    spec:
      containers:

        name: alpaca-prod
        readinessProbe:
          httpGet:
            path: /ready
            port: 8000
          periodSeconds: 2
          initialDelaySeconds: 0
          failureThreshold: 3
          successThreshold: 1
```

Type NodePorts and type LoadBalancer

### Endpoints
`$ kubectl describe endpoints alpaca-prod`
`$ kubectl get endpoints alpaca-prod --watch`

### Manual Service Discovery
`$ kubectl get pods -o wide --show-labels`
`$ kubectl get pods -o wide --selector=app=alpaca,env=prod`

### kube-proxy and Cluster IPs
The cluster IP is usually assigned by the API server as the service is created. The user can also specify a specific cluster IP. Once set, the cluster IP cannot be modified without deleting and recreating the Service object.

### Cleanup
`$ kubectl delete services,deployments -l app`


# ReplicaSets
Pods managed by ReplicaSets are automatically rescheduled under certain failure conditions such as node failures and network partitions.
The key characteristic of ReplicaSets is that every Pod that is created by the ReplicaSet controller is entirely homogeneous.

**A replication controller** on a regular basis to launch one or more instances of your applications. You can have multiple controllers configures in your cluster.

Each replication controller has a **desired state** that is managed by the application deployer. When a change is made to the desired state, a **reconciliation loop** detects this and attempts to mutate the existing state in order to match the desired state.
For example, if you increase the desired instance count from 3 to 4, the replication controller would see that one new instance needs to be created and launch it somewhere on the cluster.
This reconciliation process applies to any modified property of the pod template.

example of ReplicaSet definition, kuard-rs.yaml
```yaml
apiVersion: extensions/v1betal
kind: ReplicaSet
metadata:
  name: kuard
spec:
  replicas: 1
  template:
    metadata:
      labels:
        app: kuard
        version: "2"
    spec:
      containers:
        - name: kuard
          image: "gcr.io/kuar-demo/kuard-amd64:2"
```
`$ kubectl apply -f kuard-rs.yaml`
`$ kubectl describe rs kuard`
`$ kubectl get pods -l app=kuard,version=2`


### Scaling ReplicaSets
imperative scaling with kubectl scale
`$ kubectl scale kuard --replicas=4`
also need to update the configuration file to match the number of replicas

Declaratively Scaling with kubectl apply

### Autoscaling a ReplicaSet
horizontal pod autoscaling (HPA)
Note: HPA requires the presence of the heapster Pod on your cluster. heapster keeps track of metrics and provides an API for consuming metrics HPA uses when making scaling decisions.
You can validate its presence by
`$ kubectl get pods --namespace=kube-system`

autoscaling based on CPU
`$ kubectl autoscale rs kuard --min=2 --max=5 --cpu-percent=80`
`$ kubectl get hpa` and horizontalpodautoscalers resource

Warning: It's a bad idea to combine both autoscaling and imperative or declarative management of the number of replicas.

### Deleting ReplicaSets
`$ kubectl delete rs kuard`  
This also deletes the Pods that are managed by the ReplicaSet.

If you don't want to delete the Pods
`$ kubectl delete rs kuard --cascade=false`


# DaemonSets

A DaemonSet ensures a copy of a Pod is running across a set of nodes in a Kubernetes cluster. DaemonSet are used to deploy system daemons such as log collectors and monitoring agents, which typically must run on every node.

ReplicaSets should be used when your application is completely decoupled from the node and you can run multiple copies on a given node without special consideration. DaemonSets should be used when a single copy of your application must run on all or a subset of the nodes in the cluster.

### DaemonSet Scheduler
By default a DaemonSet will create a copy of a Pod on every node unless a node selector is used.
Like ReplicaSets, DaemonSets are managed by a reconciliation control loop that measures the desired state (e.g. a Pod is present on all nodes). If a new node is added to the cluster, then the DaemonSet controller notices that it is missing a Pod and adds the Pod to the new node.

### Creating DaemonSets
example fluentd.yaml
```yaml
apiVersion: extensions/v1betal
kind: DaemonSet
metadata:
  name: fluentd
  namespace: kube-system
  labels:
    app: fluentd
spec:
  template:
    metadata:
      labels:
        app: fluentd
    spec:
      containers:
      - name: fluentd
        image: fluent/fluentd:v0.14.10
        resources:
          limits:
            memory: 200Mi
          requests:
            cpu: 100m
            memory: 200Mi
        volumeMounts:
        - name: varlog
          mountPath: /var/log
        - name: varlibdockercontainers
          mountPath: /var/lib/docker/containers
          readOnly: true
        terminationGracePeriodSeconds: 30
        volumes:
        - name: varlog
          hostPath:
            path: /var/log
        - name: varlibdockercontainers
          hostPath:
            path: /var/lib/docker/containers
```
`$ kubectl apply -f fluentd.yaml`
`$ kubectl describe daemonset fluentd`
`$ kubectl get pods -o wide`

### Limiting DaemonSets to Specific Nodes
The first step is to add the desired set of labels to a subset of nodes.
example adds the ssd=true label to a single node
`$ kubectl label nodes k0-default-z7 ssd=true`
`$ kubectl get nodes --selector ssd=true`

Node selectors can be used to limit what nodes a Pod can run on in a given Kubernetes cluster. Node selectors are defined as part of the Pod spec when creating a DaemonSet.
example nginx-fast-storage.yaml
```yaml
apiVersion: extensions/v1betal
kind: "DaemonSet"
metadata:
  labels:
    app: nginx
    ssd: "true"
  name: nginx-fast-storage
spec:
  template:
    metadata:
      labels:
        app: nginx
        ssd: "true"
    spec:
      nodeSelector
        ssd: "true"
      containers:
        - name: nginx
          image: nginx:1.10.0
```
Adding the ssd=true label to additional nodes will case the nginx-fast-storage Pod to be deployed on those nodes. If a required label is removed from a node, the Pod will be removed by the DaemonSet controller.

### Updating a DaemonSet
If you are running a pre-1.6 version of Kubernetes, you can perform a rolling delete of the Pods a DaemonSet manages using a for loop
```
PODS=$(kubectl get pods -o jsonpath -template='{.items[*].metadata.name}')
for x in $PODS; do
  kubectl delete pods ${x}
  sleep 60
done
```

With Kubernetes 1.6 and above, as with rolling updates of deployments, the rolling update strategy gradually updates members of a DaemonSet until all of the Pods are running the new configuration. There are two parameters that control the rolling update of a DaemonSet:

- *spec.minReadySeconds*   determines how long a Pod must be "ready" before the rolling update proceeds to upgrade subsequent Pods.
- *spec.updateStrategy.rollingUpdate.maxUnavailable*  indicates how may Pods may be simultaneously updated by the rolling update

Once a rolling update has started, you can use the `kubectl rollout` commands to see the current status.
example `kubectl rollout status daemonSets my-daemon-set`

### Deleting a DaemonSet
`$ kubectl delete -f fluentd.yaml`
Deleting a DaemonSet will also delete all the Pods being managed by that DaemonSet. Set the --cascade flag to false to ensure only the DaemonSet is deleted and not the Pods.


# Jobs

Jobs are to run short-lived, one-off tasks. A Job creates Pods that run until successful termination (i.e. exist with 0)
In contrast, a regular Pod will continually restart regardless of its exit code.

### The Job Object
The Job object is responsible for creating and managing pods defined in a template in the Job specification. These pods generally run until successful completion.
If the Pod fails before a successful termination, the Job controller will create a new Pod based on the Pod template in the Job specification.

### Job Patterns
By default each Job runs a single Pod once until successful termination. This Job pattern is defined by two primary attributes of a Job, namely the number of Job completions (completions) and the number of Pods to run in parallel (parallelism).

Job patterns

| Type                       | Use case                                 | Behavior                                 | completions | parallelism |
| -------------------------- | ---------------------------------------- | ---------------------------------------- | ----------- | ----------- |
| One shot                   | Database migrations                      | A single pod running once until successful termination | 1           | 1           |
| Parallel fixed completions | Multiple pods processing a set of work in parallel | One or more Pods running one or more times until reaching a fixed completion count | 1+          | 1+          |
| Work queue: parallel Jobs  | Multiple pods processing from a centralized work queue | One or more Pods running once until successful termination | 1           | 2+          |

One shot Job. The easiest way is to use the kubectl commandline tool
```
$ kubectl run -i oneshot \
--image=gcr.io/kuar-demo/kuard-amd64:1 \
--restart=OnFailure \
-- --keygen-enable \
   --keygen-exit-on-complete \
   --keygen-num-to-gen 10
```
After the Job has completed, the Job object and related Pod are still around. This is so that you can inspect the log output.
`$ kubectl get jobs -a`   without -a flag kubectl hides completed Jobs.
Delete teh Job by
`$ kubectl delete jobs oneshot`

The other option for creating a one-shot Job is using a configuration file
example job-oneshot.yaml
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: oneshot
  labels:
    chapter: jobs
spec:
  template:
    metadata:
      labels:
        chapter: jobs
    spec:
      containers:
      - name: kuard
        image: gcr.io/kuar-demo/kuard-amd64:1
        imagePullPolicy: Always
        args:
        - "--keygen-enable"
        - "--keygen-exit-on-complete"
        - "--keygen-num-to-gen=10"
      restartPolicy: OnFailure
```
`$ kubectl apply -f job-oneshot.yaml`
`$ kubectl describe jobs oneshot`
`$ kubectl logs oneshot-4kfdt`

Note: The Job object will automatically pick a unique label and use it to identify the pods it creates.

#### Pod failure
restartPolicy OnFailure: CrashLoopBackOff status
restartPolicy Never: telling the kubelet not to restart the Pod on failure

#### Parallelism
for example, goal is to generate 100 keys by having 10 runs of kuard with each run generating 10 keys. limit only five pods at a time.
example job-parallel.yaml
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: parallel
  labels:
    chapter: jobs
spec:
  parallelism: 5
  completions: 10
  template:
    metadata:
      labels:
        chapter: jobs
    spec:
      containers:
      - name: kuard
        image: gcr.io/kuar-demo/kuard-amd64:1
        imagePullPolicy: Always
        args:
        - "--keygen-enable"
        - "--keygen-exit-on-complete"
        - "--keygen-num-to-gen=10"
      restartPolicy: OnFailure
```
`$ kubectl apply -f job-parallel.yaml`
`$ kubectl get pods -w`
`$ kubectl delete job parallel`

#### Work Queues
some task creates a number of work items and publishes them to a work queue. A worker Job can be run to process each work item until the work queue is empty.


# ConfigMaps and Secrets

ConfigMaps are used to provide configuration information for workloads. This can either be fine-grained information (a short string) or a composite value in the form of a file. Secrets focused on making sensitive information available to the workload.

## ConfigMaps

### Creating ConfigMaps
```
$ kubectl create configmap my-config \
	--from-file=my-config.txt \
	--from-literal=extra-param=extra-value \
	--from-literal=another-param=another-value
```
my-config.txt
```
parameter1 = value1
parameter2 = value2
```
```
$ kubectl get configmaps my-config -o yaml
```

### Using a ConfigMap
#### Filesystem
You can mount a ConfigMap into a Pod. A file is created for each entry based on the key name. The contents of that file are set to the value.

#### Environment variable
A ConfigMap can be used to dynamically set the value of an environment variable.

#### Command-line argument
Kubernetes supports dynamically creating the command line for a container based on ConfigMap values

example kuard-config.yaml
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kuard-config
spec:
  containers:
    - name: test-container
      image: gcr.io/kuar-demo/kuard-amd64:1
      imagePullPolicy: Always
      command:
        - "/kuard"
        - "$(EXTRA_PARAM)"
      env:
        - name: ANOTHER_PARAM
          valueFrom:
            configMapKeyRef:
              name: my-config
              key: another-param
        - name: EXTRA_PARAM
          valueFrom:
            configMapKeyRef:
              name: my-config
              key: extra-param
      volumeMounts:
        - name: config-volume
          mountPath: /config
  volumes:
    - name: config-volume
      configMap:
        name: my-config
  restartPolicy: Never
```
`$ kubectl apply -f kuard-config.yaml`
`$ kubectl port-forward kuard-config 8080`

## Secrets

### Creating Secrets
example create a secret to store a TLS key and certificate for the kuard application

```
$ kubectl create secret generic kuard-tls \
  --from-file=kuard.crt \
  --from-file=kuard.key
```
`$ kubectl describe secrets kuard-tls`

### Consuming Secrets
secrets can be accessed through the API server . we can also use a *secrets volume* to consume secrets.

Secret data can be exposed to pods using the secrets volume type. Secrets volumes are managed by the **kubelet** and are created at pod creation time. Secrets are stored on tmpfs volumes (aka RAM disks) and, as such, are not written to disk on nodes.

Each data element of a secret is stored in a separate file under the target mount point specified in the volume mount.

example kuard-secret.yaml
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kuard-tls
spec:
  containers:
    - name: kuard-tls
      image: gcr.io/kuar-demo/kuard-amd64:1
      imagePullPolicy: Always
      volumeMounts:
      - name: tls-certs
        mountPath: "/tls"
        readOnly: true
  volumes:
    - name: tls-certs
      secret:
        secretName: kuard-tls
```
`$ kubectl apply -f kuard-secret.yaml`
`$ kubectl port-forward kuard-tls 8443:8443`

### Private Docker Registries
*Image pull secrets* leverage the secrets API to automate the distribution of private registry credentials. Image pull secrets are consumed through the *spec.imagePullSecrets* Pod specification field.

Use the `create secret docker-registry` to create this special kind of secret:
```
$ kubectl create secret docker-registry my-image-pull-secret \
  --docker-username=<username> \
  --docker-password=<password> \
  --docker-email=<email-address>
```

example kuard-secret-ips.yaml
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kuard-tls
spec:
  containers:
    - name: kuard-tls
      image: gcr.io/kuar-demo/kuard-amd64:1
      imagePullPolicy: Always
      volumeMounts:
      - name: tls-certs
        mountPath: "/tls"
        readOnly: true
  imagePullSecrets:
  - name: my-image-pull-secret
  volumes:
    - name: tls-certs
      secret:
        secretName: kuard-tls
```

Key Naming Constraints
`[.]?[a-zA-Z0-9]([.]?[-_a-zA-Z0-9]*[a-zA-Z0-9])*`

ConfigMap data values are simple UTF-8 text specified directly in the manifest. As of Kubernetes 1.6, ConfigMaps are unable to store binary data.

Secret data values hold arbitrary data encoded using base64. The use of base64 encoding makes it possible to store binary data. This does, however, make it more difficult to manage secrets that are stored in YAML files as the base64-encoded value must be put in the YAML.

### Managing ConfigMaps and Secrets
Secrets and ConfigMaps are managed through the Kubernetes API. The usual *create*, *delete*, *get*, and *describe* commands work for manipulating these objects.

#### Listing
`$ kubectl get secrets`
`$ kubectl get configmaps`
`$ kubectl describe configmap my-config`

see the raw data:
`$ kubectl get configmap my-config -o yaml`
`$ kubectl get secret kuard-tls -o yaml`

#### Creating
*kubectl create secret generic* or *kubectl create configmap*
`--from-file=<filename>` Load from the file with the secret data key the same as the filename
`--from-file=<key>=<filename>` Load from the file with the secret data key explicitly specified
`--from-file=<directory>` Load all the files in the specified directory where the filename is an acceptable key name
`--from-literal=<key>=<value>` Use the specified key/value pair directly

#### Updating
You can update a ConfigMap or secret and have it reflected in running programs. There is no need to restart if the application is configured to reread configuration values.

Update from File
If you have a manifest for your ConfigMap or secret, you can just edit it directly and push a new version with `kubectl replace -f <filename>`. You can also use `kubectl apply -f <filename>` if you previously created the resource with kubectl apply.
there is no provision in kubectl to load data from an external file. The data must be stored directly in the YAML manifest.

ConfigMap manifest will be checked into source control. secret YAML files not.

Recreate and Update
If you store the inputs into your ConfigMaps or secrets as separate files on disk, you can use kubectl to recreate the manifest and then use it to update the object.
```
$ kubectl create secret generic kuard-tls \
  --from-file=kuard.crt --from-file=kuard.key \
  --dry-run -o yaml | kubectl replace -f -
```

Edit Current Version
update a ConfigMap use `kubectl edit` to bring up a version of the ConfigMap in your editor
`$ kubectl edit configmap my-config`
when save and close your editor, the new version of the object will be pushed to the Kubernetes API server.

Live Updates
Once a Configmap or secret is updated using the API, it'll automatically pushed to all volumes that use that ConfigMap or secret. Currently there is no built-in way to signal an application when a new version of a ConfigMap is deployed. It is up to the application to look for the config files to change and reload them.
Using the file browser in kuard (accessed through kubectl port-forward) is a great way to interactively play with dynamically updating secrets and ConfigMaps.


# Deployments

Both Pods and ReplicaSets are expected to be tied to specific container images that don't change.
The Deployment object exists to manage the release of new versions. Deployments represent deployed applications in a way that transcends any particular software version of the application.

you can view the Deployment object by:
```
$ kubectl run nginx --image=nginx:1.7.12
$ kubectl get deployments nginx
```

**ReplicaSets manage Pods, Deployments manage ReplicaSets**

this relationship is defined by labels and a label selector.
```
$ kubectl get deployments nginx \
  -o jsonpath --template {.spec.selector.matchLabels}

$ kubectl get replicasets --selector=run=nginx
```

we can resize the Deployment using the imperative scale commands
```
$ kubectl scale deployments nginx --replicas=2

$ kubectl get replicasets --selector=run=nginx
```
Scaling the Deployment has also scaled the ReplicaSet it controls.

try the opposite, scaling the ReplicaSet
```
$ kubectl scale replicasets nginx-1128242161 --replicas=1

$ kubectl get replicasets --selector=run=nginx
```
Despite scaling the ReplicaSet to one replica, it still has two replicas as its desired state.
The top-level Deployment object is managing this ReplicaSet. The Deployment controller notices changes and takes action to ensure the observed state matches the desired state.

If you ever want to manage that ReplicaSet directly, you need to delete the Deployment (remember to set **--cascade to false**, or else it will delete the ReplicaSet and Pods as well!)

### Creating Deployments

download this Deployment example into a YAML file
```
$ kubectl get deployments nginx --export -o yaml > nginx-deployment.yaml
$ kubectl replace -f nginx-deployment.yaml --save-config
```

example
```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  annotations:
    deployment.kubernetes.io/revision: "1"
  labels:
    run: nginx
  name: nginx
  namespace: default
spec:
  replicas: 2
  selector:
    matchLabels:
      run: nginx
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate
  template:
    metadata:
      labels:
        run: nginx
    spec:
      containers:
      - image: nginx:1.7.12
        imagePullPolicy: Always
      dnsPolicy: ClusterFirst
      restartPolicy: Always
```
Note: a lot of read-only and default fields were removed for brevity.
We also need to run kubectl replace --save-config. This adds an annotation so that, when applying changes in the future, kubectl will know what the last applied configuration was for smarter merging of configs. If you always use kubectl apply, this step is only required after the first time you create a Deployment using kubectl create -f.

There are two different strategies supported by Deployments: **Recreate** and **RollingUpdate**

### Managing Deployments

`$ kubectl describe deployments nginx`

`$ kubectl rollout history` obtain the history of rollouts

`$ kubectl rollout status` obtain the current status of a rollout

### Updating Deployments

#### Scaling a Deployment
The best practice is to manage your Deployments declaratively via the YAML files and then use those files to update your Deployment.
example
```yaml
...
spec:
  replicas: 3
...
```
`$ kubectl apply -f nginx-deployment.yaml`
`$ kubectl get deployments nginx`

#### Updating a Container Image
example
```yaml
...
containers:
  - image: nginx:1.9.10
    imagePullpPolicy: Always
...
```
```yaml
...
spec:
  ...
  template:
    metadata:
      annotations:
        kubernetes.io/change-cause: "Update nginx to 1.9.10"
...
```
`$ kubectl apply -f nginx-deployment.yaml`

Note: make sure you add this annotation to the template and not the Deployment itself. do not update the change-cause annotation when doing simple scaling operations. A modification of change-cause is a significant change to the template and will trigger a new rollout

`$ kubectl rollout status deployments nginx`

`$ kubectl get replicasets -o wide`

If you are in the middle of a rollout and you want to temporarily pause it, you can use the pause command

`$ kubectl rollout pause deployments nginx`

`$ kubectl rollout resume deployments nginx`

#### Rollout History

`$ kubectl rollout history deployment nginx`

The revision history is given in oldest to newest order.
add the --revision flag to view details about a specific revision

`$ kubectl rollout history deployment nginx --revision=2`

you can undo the last rollout

`$ kubectl rollout undo deployments nginx`

The undo command works regardless of the stage of the rollout. You can undo both partially completed and fully completed rollouts. An undo of a rollout is actually simply a rollout in reverse (e.g. from v2 to v1), and all of the same policies that control the rollout strategy apply to the undo strategy as well.

Note: When using declarative files to control your production systems, you want to, as much as possible, ensure that the check-in manifests match what is actually running in your cluster. An alternate way to undo a rollout is to revert your YAML file and kubectl apply the previous version.

It turns out that when you roll back to a previous revision, the Deployment simply reuses the template and renumbers it so taht it is the latest revision. for example, what was revision 2 before is now reordered into revision 4.

you can roll back to a specific revision
```
$ kubectl rollout undo deployments nginx --to-revision=3
$ kubectl rollout history deployment nginx
```
specifying a revision of 0 is a shorthand way of specifying the previous revision. kubectl rollout undo is equivalent to kubectl rollout undo --to-revision=0

set a maximum history size
```yaml
...
spec:
  # we daily rollouts, limit the revision history to two weeks of
  # releases as we don't expect to roll back beyond that.
  revisionHistoryLimit: 14
```

#### Deployment Strategies

two rollout strategies:
- Recreate
- RollingUpdate

Configuring a RollingUpdate

The **maxUnavailable** parameter sets the maximum number of Pods that can be unavailable during a rolling update. It can either be set to an absolute number or to a percentage.

there are situations where you don't want to fall below 100% capacity, but you are willing to temporarily use additional resources in order to perform a rollout. You can set the maxUnavailable parameter to 0%, and instead control the rollout using the maxSurge parameter.

The **maxSurge** parameter controls how many extra resources can be created to achieve a rollout.

Note: the recreate strategy is identical to the rolling update strategy with maxUnavailable set to 100%.
Setting maxSurge to 100% is equivalent to a blue/green deployment. The Deployment controller first scales the new version up to 100% of the old version. Once the new version is healthy, it immediately scales the old version down to 0%.

The Deployment controller always waits until a Pod reports that it is ready before moving on to updating the next Pod.
The Deployment controller examines the Pod's status as determined by its readiness checks.

```yaml
...
spec:
  minReadySeconds: 60
...
```
Setting **minReadySeconds** to 60 indicates that the Deployment must wait for 60 seconds after seeing a Pod become healthy before moving on to updating the next Pod.

In addition to waiting a period of time for a Pod to become healthy, you also want to set a timeout that limits how long the system will wait.
```yaml
...
spec:
  progressDeadlineSeconds: 600
...
```
If any particular stage in the rollout fails to progress in 10 minutes, then the Deployment is marked as failed, and all attempts to move the Deployment forward are halted.

*progress* is defined as any time the deployment creates or deletes a Pod.

### Deleting a Deployment

`$ kubectl delete deployments nginx`

or using YAML file

`$ kubectl delete -f nginx-deployment.yaml`

Deleting a Deployment will also delete ReplicaSets and Pods. you can use the --cascade=false flag to exclusively delete the Deployment object.


# Integrating Storage Solutions and Kubernetes

### Importing External Services

All Kubernetes objects are deployed into *namespaces*
for example
```yaml
kind: Service
metadata:
  name: my-database
  namespace: test
```
```yaml
kind: Service
metadata:
  name: my-database
  namespace: prod
```

To import an external database service into Kubeternetes, we start by creating a service without a Pod selector that references the DNS name of the database server
example dns-service.yaml
```yaml
kind: Service
apiVersion: v1
metadata:
  name: external-database
spec:
  type: ExternalName
  externalName: database.company.com
```
When a typical Kubernetes service is created, an IP address is also created and the Kubernetes DNS service is populated with an A record that points to that IP address. When you create a service of type *ExternalName* , the Kubernetes DNS service is instead populated with a CNAME record that points to the external name you specified.

If you don't have a DNS address for an external database service, just an IP address. create a Service without label selector, but also without the ExternalName type
exmaple external-ip-service.yaml
```yaml
kind: Service
apiVersion: v1
metadata:
  name: external-ip-database
```
At this point, Kubernetes will allocate a virtual IP address for this service and populate an A record for it. However, because there is no selector for the service, there will be no endpoints populated for the load balancer to redirect traffic to. The user is responsible for populating the endpoints manually with an Endpoints resource.
example external-ip-endpoints-yaml
```yaml
kind: Endpoints
apiVersion: v1
metadata:
  name: external-ip-database
subsets:
  - addresses:
    - ip: 192.168.0.1
    ports:
    - port: 3306
```

External services in Kubernetes have one significant restriction: they do not perform any health checking.

### Running Reliable Singletons

for small scale, run a single Pod that runs the database or other storage solution. limited downtime trade off for the reduced complexity.

#### Running a MySQL Singleton

create three basic objects:
* A persistent volume to manage the lifespan of the on-disk storage independently from the lifespan of the running MySQL application
* A MySQL Pod that will run the MySQL application
* A service that will expose this Pod to other containers in the cluster

This example uses NFS for maximum portability. To use other solutions, simply replace nfs with the appropriate cloud provider volume type (e.g., azure, awsElasticBlockStore, or gcePersistentDisk)
example nfs-volume.yaml
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: database
  labels:
    volume: my-volume
spec:
  accessModes:
  - ReadWriteMany
  capacity:
    storage: 1Gi
  nfs:
    server: 192.168.0.1
    path: "/exports"
```
`$ kubectl apply -f nfs-volume.yaml`

claim that persistent volume for our Pod.
example nfs-volume-claim.yaml
```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: database
spec:
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 1Gi
  selector:
    matchLabels:
      volume: my-volume
```

we can use a ReplicaSet to construct our singleton Pod.
example mysql-replicaset.yaml
```yaml
apiVersion: extensions/v1beta1
kind: ReplicaSet
metadata:
  name: mysql
  # labels so that we can bind a Service to this Pod
  labels:
    app: mysql
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - name: database
        image: mysql
        resources:
          requests:
            cpu: 1
            memory: 2Gi
        env:
        # Environment variables are not a best practice for security,
        # but we're using them here for brevity in the example.
        - name: MYSQL_ROOT_PASSWORD
          value: some-password-here
        livenessProbe:
          tcpSocket:
            port: 3306
        ports:
        - containerPort: 3306
        volumeMounts:
          - name: database
            # /var/lib/mysql is where MySQL stores its database
            mountPath: "/var/lib/mysql"
      volumes:
      - name: database
        persistentVolumeClaim:
          claimName: database
```

expose this as a Kubernetes service
example mysql-service.yaml
```yaml
apiVersion: v1
kind: Service
metadata:
  name: mysql
spec:
  ports:
  - port: 3306
    protocol: TCP
  selector:
    app: mysql
```

#### Dynamic Volume Provisioning

example a default storage class that automatically provisions disk objects on Microsoft Azure platform
example storageclass.yaml
```yaml
apiVersion: storage.k8s.io/v1beta1
kind: StorageClass
metadata:
  name: default
  annotations:
    storageclass.beta.kubernetes.io/is-default-class: "true"
  labels:
    kubernetes.io/cluster-service: "true"
provisioner: kubernetes.io/azure-disk
```

example dynamic-volume-claim.yaml
```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: my-claim
  annotations:
    volume.beta.kubernetes.io/storage-class: default
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

### Kubernetes-Native Storage with StatefulSets

Note: StatefulSets are a beta feature, it's possible that the API will change before it becomes an official Kubernetes API.

Properties of StatefulSets
* Each replica gets a persistent hostname with a unique index (e.g., database-0, database-1,)
* Each replica is created in order from lowest to highest index, and creation will block until the Pod at the previous index is healthy and available. This also applies to scaling up.
* When deleted, each replica will be deleted in order from highest to lowest. This also applies to scaling down the number of replicas.

#### Manually Replicated MongoDB with StatefulSets

example create a replicated set of three MongoDB Pods using a StatefulSet object, mongo-simple.yaml
```yaml
apiVersion: apps/v1beta1
kind: StatefulSet
metadata:
  name: mongo
spec:
  serviceName: "mongo"
  replicas: 3
  template:
    metadata:
      labels:
        app: mongo
    spec:
      containers:
      - name: mongodb
        image: mongo:3.4.1
        command:
        - mongod
        - --replSet
        - rs0
        ports:
        - containerPort: 27017
          name: peer
```
`$ kubectl apply -f mongo-simple.yaml`

 Once the StatefulSet is created, we also need to create a "headless" service to manage the DNS entries for the StatefulSet. In Kubernetes a service is called "headless" if it doesn't have a cluster virtual IP address. You can create a headless service using clusterIP: None in the service specification.
 example mongo-service.yaml
 ```yaml
apiVersion: v1
kind: Service
metadata:
  name: mongo
spec:
  ports:
  - port: 27017
    name: peer
  clusterIP: None
  selector:
    app: mongo
 ```

 Once you create that service, there are usually four DNS entries that are populated. mongo.default.svc.cluster.local is created, but unlike with a standard service, doing a DNS lookup on this hostname provides all the addresses in the StatefulSet. In addition, entries are created for mongo-0.mongo.default.svc.cluster.local as well as mongo-1.mongo and mongo-2.mongo. Each of these resolves to the specific IP address of the replica index in the StatefulSet.

 next we're going to manually set up Mongo replication using these per-Pod hostnames
```
$ kubectl exec -it mongo-0 mongo
> rs.initiate( {
  _id: "rs0",
  members:[ { _id: 0, host: "mongo-0.mongo:27017" } ]
});
```
This command tells mongodb to initiate the ReplicaSet rs0 with mongo-0.mongo as the primary replica
The rs0 name is arbitrary. You can use whatever you'd like, but you'll need to change it in the mongo.yaml StatefulSet definition as well.
You can add the remaining replicas
```
$ kubectl exec -it mongo-0 mongo
> rs.add("mongo-1.mongo:27017");
> rs.add("mongo-2.mongo:27017");
```

#### Automating MongoDB Cluster Creation
we are going to add an additional container to perform the initialization. We're going to use a ConfigMap to add a script into the existing MongoDB image.
```yaml
...
    - name: init-mongo
      image: mongo:3.4.1
      command:
      - bash
      - /config/init.sh
      volumeMounts:
      - name: config
        mountPath: /config
      volumes:
      - name: config
        configMap:
          name: "mongo-init"
```

example mongo-configmap.yaml
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: mongo-init
data:
  init.sh: |
    #!/bin/bash

    # Need to wait for the readiness health check to pass so that the
    # mongo names resolve. This is kind of wonky.
    until ping -c 1 ${HOSTNAME}.mongo; do
      echo "waiting for DNS (${HOSTNAME}.mongo)..."
      sleep 2
    done

    until /usr/bin/mongo --eval 'printjson(db.serverStatus())'; do
      echo "connecting to local mongo..."
      sleep 2
    done
    echo "connect to local."

    HOST=mongo-0.mongo:27017

    until /usr/bin/mongo --host=${HOST} --eval 'printjson(db.serverStatus())'; do
      echo "connecting to remote mongo..."
      sleep 2
    done
    echo "connected to remote."

    if [[ "${HOSTNAME}" != 'mongo-0' ]]; then
      until /usr/bin/mongo --host=${HOST} --eval="printjson(rs.status())" \
            | grep -v "no replset config has been received"; do
        echo "waiting for replication set initialization"
        sleep 2
      done
      echo "adding self to mongo-0"
      /usr/bin/mongo --host=${HOST} \
        --eval="printjson(rs.add('${HOSTNAME}.mongo'))"
    fi

    if [[ "${HOSTNAME}" == 'mongo-0' ]]; then
      echo "initializing replica set"
      /usr/bin/mongo --eval="printjson(rs.initiate(\
          {'_id': 'rs0', 'memebers': [{'_id': 0, \
           'host': 'mongo-0.mongo:27017'}]}))"
    fi
    echo "initialized"

    while true; do
      sleep 3600
    done
```

Note
This script currently sleeps forever after initializing the cluster. Every container in a Pod has to have the same RestartPolicy. Since we do not want our main Mongo container to be restarted, we need to have our initialization container run forever.

example the complete StatefulSet, mongo.yaml
```yaml
apiVersion: apps/v1beta1
kind: StatefulSet
metadata:
  name: mongo
spec:
  serviceName: "mongo"
  replicas: 3
  template:
    metadata:
      labels:
        app: mongo
    spec:
      containers:
      - name: mongodb
        image: mongo:3.4.1
        command:
        - mongod
        - --replSet
        - rs0
        ports:
        - containerPort: 27017
          name: web
      # This container initializes the mongodb server, then sleeps.
      - name: inti-mongo
        image: mongo:3.4.1
        command:
        - bash
        - /config/init.sh
        volumeMounts:
        - name: config
          mountPath: /config
      volumes:
      - name: config
        configMap:
          name: "mongo-init"
```
`$ kubectl apply -f mongo-config-map.yaml`
`$ kubectl apply -f mongo-service.yaml`
`$ kubectl apply -f mongo.yaml`


#### Persistent Volumes and StatefulSets
add the following onto the bottom of your StatefulSet definition:
```yaml
volumeClaimTemplates:
- metadata:
    name: database
    annotations:
      volume.alpha.kubernetes.io/storage-class: anything
  spec:
    accessModes: [ "ReadWriteOnce" ]
    resources:
      requests:
        storage: 100Gi
```
When you add a volume claim template to a StatefulSet definition, each time the StatefulSet controller creates a Pod that is part of the StatefulSet it will create a persistent volume claim based on this template as part of that Pod.

#### Readiness Probes
adding the following to the Pod template in the StatefulSet object:
```yaml
...
  livenessProbe:
    exec:
      command:
      - /usr/bin/mongo
      - --eval
      - db.serverStatus()
    initialDelaySeconds: 10
    timeoutSeconds: 10
...
```

# Deploying Real-World Applications

three examples
* Parse, an open source API server for mobile applications
* Ghost, a blogging and content management platform
* Redis, a lightweight, performant key/value store

### Parse

pre-req: a three-replica Mongo cluster, Docker hub login, Kubernetes cluster and kubectl tool

#### Building the parse-server
```
$ git clone https://github.com/ParsePlatform/parse-server
$ cd parse-server
$ docker build -t ${DOCKER_USER}/parse-server .
$ docker push ${DOCKER_USER}/parse-server
```

#### Deploying the parse-server

APPLICATION_ID: An identifier for authorizing your application
MASTER_KEY: An identifier that authorizes the master user
DATABASE_URI: The URI for your MongoDB cluster

example parse.yaml
```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: parse-server
  namespace: default
spec:
  replicas: 1
  template:
    metadata:
      labels:
        run: parse-server
    spec:
      containers:
      - name: parse-server
        image: ${DOCKER_USER}/parse-server
        env:
        - name: DATABASE_URI
          value: "mongodb://mongo-0.mongo:27017,\
            mongo-1.mongo:27017,mongo-2.mongo\
            :27017/dev?replicaSet=rs0"
        - name: APP_ID
          value: my-app-id
        - name: MASTER_KEY
          value: my-master-key
```

#### Testing Parse

example parse-service.yaml
```yaml
apiVersion: v1
kind: Service
metadata:
  name: parse-server
  namespace: default
spec:
  ports:
  - port: 1337
    protocol: TCP
    targetPort: 1337
  selector:
    run: parse-server
```

### Ghost

example ghost-config.js
```js
var path = require('path'),
    config;

config = {
    development: {
      url: 'http://localhost:2368',
      database: {
        client: 'sqlite3',
        connection: {
          filename: path.json(process.env.GHOST_CONTENT,
                              '/data/ghost-dev.db')
        },
        debug: false
      },
      server: {
        host: '0.0.0.0',
        port: '2368'
      },
      paths: {
        contentPath: path.join(process.env.GHOST_CONTENT, '/')
      }
    }
};

module.exports = config;
```
`$ kubectl create cm --from-file ghost-config.js ghost-config`

exmaple ghost.yaml
```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: ghost
spec:
  replicas: 1
  selector:
    matchLabels:
      run: ghost
  template:
    metadata:
      labels:
        run: ghost
    spec:
      containers:
      - image: ghost
        name: ghost
        command:
        - sh
        - -c
        - cp /ghost-config/ghost-config.js /var/lib/ghost/config.js
          && /usr/local/bin/docker-entrypoint.sh node current/index.js
        volumeMounts:
        - mountPath: /ghost-config
          name: config
      volumes:
      - name: config
        configMap:
          defaultMode: 420
          name: ghost-config
```

Note: ConfigMap can only mount directories, not individual files.
`$ kubectl apply -f ghost.yaml`
`$ kubectl expose deployments ghost --port=2368`
`$ kubectl proxy`

GHOST + MYSQL
modify config.js
```js
...
database: {
  client: 'mysql',
  connection: {
    host      : 'mysql',
    user      : 'root',
    password  : 'root',
    database  : 'ghost_db',
    charset   : 'utf-8'
  }
},
...
```
`$ kubectl create configmap ghost-config-mysql --from-file ghost-config.js`

update the Ghost deployment
```yaml
...
    - configMap:
        name: ghost-config-mysql
...    
```
```
$ kubectl exec -it mysql-zzmlw -- mysql -u root -p
...
mysql> create database ghost_db;
...
```
`$ kubectl apply -f ghost.yaml`

### Redis

Redis needs separate configurations for the master and slave replicas.
exmaple master.conf
```
bind 0.0.0.0
port 6379

dir /redis-data
```
This directs Redis to bind to all network interfaces on port 6379 and store its files in the /redis-data directory.

example slave.conf
```
bind 0.0.0.0
port 6379

dir .

slaveof redis-0.redis 6379
```

example sentinel.conf
```
bind 0.0.0.0
port 26379

sentinel monitor redis redis-0.redis 6379 2
sentinel parallel-syncs redis 1
sentinel down-after-milliseconds redis 10000
sentinel failover-timeout redis 20000
```

create a couple of simple wrapper scripts to use in StatefulSet deployment
The first script simply looks at the hostname for the Pod and determines whether this is the master or a slave.
example init.sh
```
#!/bin/bash
if [[ ${HOSTNAME} == 'redis-0' ]]; then
  redis-server /redis-config/master.conf
else
  redis-server /redis-config/slave.conf
fi
```

the other is to wait for the redis-0.redis DNS name to become avaiable
exmaple sentnel.sh
```
#!/bin/bash
while ! ping -c 1 redis-0.redis; do
  echo 'Waiting for server'
  sleep 1
done

redis-sentinel /redis-config/sentinel.conf
```

package all of these files into ConfigMap object
```
$ kubectl create configmap \
  --from-file=slave.conf=./slave.conf \
  --from-file=master.conf=./master.conf \
  --from-file=sentinel.conf=./sentinel.conf \
  --from-file=init.sh=./init.sh \
  --from-file=sentinel.sh=./sentinel.sh \
  redis-config
```

Creating a Redis Service
example redis-service.yaml
```yaml
apiVersion: v1
kind: Service
metadata:
  name: redis
spec:
  ports:
  - port: 6379
    name: peer
  clusterIP: None
  selector:
    app: redis
```
`$ kubectl apply -f redis-service.yaml`

Deploying Redis

example redis.yaml
```yaml
apiVersion: apps/v1beta1
kind: StatefulSet
metadata:
  name: redis
spec:
  replicas: 3
  serviceName: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - command: [sh, -c, source /redis-config/init.sh]
        image: redis:3.2.7-alpine
        name: redis
        ports:
        - containerPort: 6379
          name: redis
        volumeMounts:
        - mountPath: /redis-config
          name: config
        - mountPath: /redis-data
          name: data
      - command: [sh, -c, source /redis-config/sentinel.sh]
        image: redis:3.2.7-alpine
        name: sentinel
        volumeMounts:
        - mountPath: /redis-config
          name: config
      volumes:
      - configMap:
          defaultMode: 420
          name: redis-config
        name: config
      - emptyDir:
        name: data
```
`$ kubectl apply -f redis.yaml`

test Redis Cluster
determine which server the Redis sentinel believes is the master
```
$ kubectl exec redis-2 -c  redis \
  -- redis-cli p 26379 sentinel get-master-addr-by-name redis
```

confirm the replication is actually working. read the value foo from one of the replicas
`$ kubectl exec redis-2 -c redis -- redis-cli -p 6379 get foo`

write data to a replica
`$ kubectl exec redis-0 -c redis -- redis-cli -p 6379 set foo 10`


# Building a Raspberry Pi Kubernetes Cluster

### Assemble the pieces for your cluster. Shopping list:

1. Four Raspberry Pi 3 boards - $160
2. Four SDHC memory cards, at least 8 GB (high-quality ones) - $30-50
3. Four 12-inch Cat. 6 Ethernet cables - $10
4. Four 12-inch USB A-Micro USB cables - $10
5. One 5-port 10/100 Fast Ethernet switch - $10
6. One 5-port USB charger - $25
7. One Raspberry Pi stackable case capable of holding our Pis - $40
8. One USB-to-barrel plug for powering the Ethernet switch (optional) - $5

assume you have a device capable of flashing an SDHC card. If not, you need a USB --> memory card reader/writer

### Flashing Images
Hypriot

Boot your master node
change the default password

setting up networking
setup WiFi
edit `/boot/device-init.yaml` update the WiFi SSID and password and then sudo reboot
set up a static IP address for your cluster's internal network.
edit `/etc/network/interfaces.d/eth0`
```
allow-hotplug eth0
iface eth0 inet static
    address 10.0.0.1
    netmask 255.255.255.0
    broadcast 10.0.0.255
    gateway 10.0.01
```
Reboot the machine to claim the 10.0.0.1 address

install DHCP so it will allocate addresses to the worker nodes
`$ apt-get install isc-dhcp-server`

configure DHCP server (/etc/dhcp/dhcpd.conf)
```
# Set a domain name, can basically be anything
option domain-name "cluster.home";

# Use Google DNS by default, you can substitue ISP-supplied values here
option domain-name-servers 8.8.8.8, 8.8.4.4;

# We'll use 10.0.0.X for our subnet
subnet 10.0.0.0 netmask 255.255.255.0 {
  range 10.0.0.1 10.0.0.10;
  option subnet-mask 255.255.255.0;
  option broadcast-address 10.0.0.255;
  option routers 10.0.0.1;
}
default-lease-time 600;
max-lease-time 7200;
authoritative;
```
you may also need to edit /etc/defaults/isc-dhcp-server to set the INTERFACES environment variable to eth0
Restart the DHCP server sudo systemctl restart isc-dhcp-server
you can test DHCP by hooking up a second machine to the switch via the Ethernet. This second machine should get the address 10.0.0.2 from the DHCP server.

edit the /boot/device-init.yaml to rename this machine to node-1

Next setting up network address translation (NAT) so that your nodes can reach the public internet

edit /etc/sysctl.conf and set net.ipv4.ip_forward=1 to turn on IP forwarding

edit /etc/rc.local (or the equivalent) and add iptables rules for forwarding from eth0 to wlan0 (and back)
```
$ iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
$ iptables -A FORWARD -i wlan0 -o eth0 -m state \
  --state RELATED,ESTABLISHED -j ACCEPT
$ iptables -A FORWARD -i eth0 -o wlan0 -j ACCEPT
```

Validate this by first looking at /var/lib/dhcp/dhcpd.leases and then SSH to the nodes
(remember again to change the default password first thing).
Validate the nodes can connect to the external internet

Extra credit things of networking

edit /etc/hosts
```
...
10.0.0.1 kubernetes
10.0.0.2 node-1
10.0.0.3 node-2
10.0.0.4 node-3
...
```

set up passwordless SSH access, run ssh-keygen and copy the pub key to target authorized_keys


### Installing Kubernetes

Using SSH, run the following commands on all nodes to install the kubelet and kubeadm tools as root
First, add the encryption key for the packages:
```
# curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
```

Then add the repository to your list of repositories
```
# echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" \
  >> /etc/apt/sources.list.d/kubernetes.list
```

update and install the Kubernetes tools
```
# apt-get update
$ apt-get upgrade
$ apt-get install -y kubelet kubeadm kubectl kubernetes-cni
```

### Setting Up the Cluster

On the master node (the one running DHCP and connected to the internet)
```
$ sudo kubeadm init --pod-network-cidr 10.244.0.0/16 \
    --apiserver-advertise-address 10.0.0.1 \
    --apiserver-cert-extra-sans kubernetes.cluster.home
```
advertising internal-facing IP address

SSH onto each of the worker nodes and run
`$ kubeadm join --token=<token> 10.0.0.1`
when all of that is done, run
`$ kubectl get nodes`

Setting up cluster networking

you have your node-level networking setup, but you need to set up the pod-to-pod networking. The easiest way to manage this is to use the Flannel tool. Flannel supports a number of different routing modes. we will use the host-gw mode. you can download an example configuration from the Flannel project
```
$ curl https://rawgit.com/coreos/flannel/master/Documentation/kube-flannel.yml \
  > kube-flannel.yaml
```
the default config uses vxlan mode and uses AMD64 architecture. edit the configuration file and replace vxlan with host-gw and relace all instances of amd64 with arm
```
$ curl https://rawgit.com/coreos/flannel/master/Documentation/kube-flannel.yml \
| sed "s/amd64/arm/g" | sed "s/vxlan/host-gw/g" \
 > kube-flannel.yaml
```

create the Flannel networking
`$ kubectl apply -f kube-flannel.yaml`
This will create two objects, a ConfigMap used to configure Flannel and a DaemonSet that runs the actual Flannel daemon
```
$ kubectl describe --namespace=kube-system configmaps/kube-flannel-cfg
$ kubectl describe --namespace=kube-system daemonsets/kube-flannel-ds
```

Setting up the GUI
```
$ DASHSRC=https://raw.githubusercontent.com/kubernetes/dashboard/master
$ curl -sSL \
  $DASHSRC/src/deploy/recommended/kubernetes-dashboard-arm-head.yaml \
  | kubectl apply -f -
```
To access the UI, you can run kubectl proxy and then point your browser to http://localhost:8001/ui
you may need to set up an SSH tunnel to the root node using ssh - L8001:localhost:8001 <master-ip-address>
