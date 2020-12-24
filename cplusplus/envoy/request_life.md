
# Life of a Request

## Terminology

- Cluster: a logical service with a set of endpoints that Envoy forwards requests to.
- Downstream: an entity connecting to Envoy. e.g. a remote client.
- Endpoints: network nodes that implement a logical service. Endpoints in a cluster are upstream of an Envoy proxy.
- Filter: a module in the connection or request processing pipeline providing some aspect of request handling.
- Filter chain: a series of filters.
- Listeners: Envoy module responsible for binding to an IP/port, accepting new TCP connections (or UDP datagrams) and orchestrating the downstream facing aspects of request processing.
- Upstream: an endpoint (network node) that Envoy connects to when forwarding requests for a service. e.g. a remote backend.

## Network topology

In the service mesh model, requests flow through Envoys as a gateway to the network. Requests arrive at an Envoy via either ingress or egress listeners.
It can also act as an internal load balancer or as an ingress/egress proxy on the network edge. In practice, a hybrid of these is often used.

## Configuration

Possible request paths are depending on:
- L3/4 protocol, e.g. TCP, UDP, Unix domain sockets
- L7 protocol, e.g. HTTP/1, HTTP/2, HTTP/3, gRPC, Thrift, Dubbo, Kafka, Redis and various databases
- Transport socket, e.g. plain text, TLS, ALTS
- Connection routing, e.g. PROXY protocol, original destination, dynamic forwarding
- Authentication and authorization
- Circuit breakers and outlier detection configuration and activation state
- Accessing logging, health checking, tracing and stats extensions

## High level architecture

- Listener subsystem: which handles downstream request processing and the response path to the client.
- Cluster subsystem: which is responsible for selecting and configuring the upstream connection to an endpoint.

## Request flow

The ListenerManager is responsible for taking configuration representing listeners and instantiating a number of Listener instances bound to their respective IP/ports. Listeners may be in one of three states:
- Warming: the listener is waiting for configuration dependencies (e.g. route configuration, dynamic secrets). The listener is not yet ready to accept TCP connections.
- Active: the listener is bound to its IP/port and accepts TCP connections.
- Draining: the listener no longer accepts new TCP connections while it existing TCP connections are allowed to continue for a drain period.

1. Listener TCP accept
2. Listener filter chains and network filter chain matching
3. TLS transport socket decryption
4. Network filter chain processing
5. HTTP/2 codec decoding, stream multiplexing
6. HTTP filter chain processing
7. Load balancing
8. HTTP/2 codec encoding
9. TLS transport socket encryption
10. Response path and HTTP lifecycle
11. Post-request processing






