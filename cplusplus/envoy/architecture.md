
## Threading model
Envoy uses a single process with multiple threads architecture.
A single primary thread controls various sporadic coordination tasks while some number of worker threads perform listening, filtering, and forwarding. Once a connection is accepted by a listener, the connection spends the rest of its lifetime bound to a single worker thread.

# Listeners
