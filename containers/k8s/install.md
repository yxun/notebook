```shell
# disable swap 
(kubelet)$ sudo swapoff -a
# Remove any matching reference found in /etc/fstab

# Verify the MAC address and product_uuid are unique
$ ipconfig -a
$ sudo cat /sys/class/dmi/id/product_uuid

# Check network adapters
# iptables see bridged traffic
$ sudo lsmod | grep br_netfilter
$ sudo modprobe br_netfilter
$ cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
$ sudo sysctl --system

# Check required ports
Control-plane node(s)
Protocol	Direction	Port Range	Purpose	Used By
TCP	Inbound	6443*	Kubernetes API server	All
TCP	Inbound	2379-2380	etcd server client API	kube-apiserver, etcd
TCP	Inbound	10250	Kubelet API	Self, Control plane
TCP	Inbound	10251	kube-scheduler	Self
TCP	Inbound	10252	kube-controller-manager	Self

Worker node(s)
Protocol	Direction	Port Range	Purpose	Used By
TCP	Inbound	10250	Kubelet API	Self, Control plane
TCP	Inbound	30000-32767	NodePort Services†	All

# Install runtime

# Install kubeadmin, kubelet, kubectl

$ cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-\$basearch
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
exclude=kubelet kubeadm kubectl
EOF
# Set SELinux in permissive mode (effectively disabling it)
$ sudo setenforce 0
$ sudo sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config

$ dnf install -y kubelet kubeadm kubectl –disableexcludes=kubernetes

$ sudo systemctl enable –now kubelet

# Configure cgroup driver used by kubelet on control-plane node

# verify connectivity to the gcr.io container image registry
(cp)$ kubeadm config images pull

# Initialize the control-plane node, args e.g. --pod-network-cidr
(cp)$ sudo kubeadm init <args>

# save a record of the kubeadm join command

# install network add-on, e.g. Calico
(cp)$ kubectl apply -f https://docs.projectcalico.org/v3.14/manifests/calico.yaml

$ kubectl get pods --all-namespaces | greo CoreDNS

# For a single-machine Kubernetes cluster
(cp)$ kubectl taint nodes --all node-role.kubernetes.io/master-

# find the token
(cp)$ kubeadm token list

# create a new token
(cp)$ kubeadm token create

# get ca-cert-hash
(cp)$ openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | \ 
    openssl rsa -pubin -outform der 2>/dev/null | \ 
    openssl dgst -sha256 -hex | sed 's/^.* //'

# Joining worker nodes
(worker)$ sudo kubeadm join --token <token> <control-plane-host>:<control-plane-port> --discovery-token-ca-cert-hash sha256:<hash>
$ kubectl get nodes

# generate an unique kubeconfig for regular user
(cp)$ kubeadm alpha kubeconfig user --client-name <CN> > ./config

# whitelist privileges
$ kubectl create (cluster)rolebinding

# proxying API server to localhost, http://localhost:8001/api/v1
(local)$ kubectl --kubeconfig ./config proxy

# Clean up

## Remove the node
(cp)$ kubectl drain <node name> --delete-local-data --force --ingore-daemonsets
(cp)$ kubectl delete node <node name>
(worker)$ kubeadm reset

## clean up iptables rules
$ iptables -F && iptables -t nat -F && iptables -t mangle -F && iptables -X
## or cleanup IPVS tables
$ ipvsadm -C

## clean up the control plane
(cp)$ kubeadm reset

## delete local references to a cluster
(local)$ kubectl config delete-cluster <name>

## delete local references to all cluster
(local)$ kubectl config unset clusters
(local)$ kubectl config unset contexts
(local)$ kubectl config unset users
```
