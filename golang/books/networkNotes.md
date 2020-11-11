

## Protocol Layers

### ISO OSI Protocol

OSI layers
- Application
- Presentation
- Session
- Transport
- Network
- Data Link
- Physical

Network layers provides switching and routing technologies.
Transport layer provides transparent transfer of data between end systems and is responsible for end-to-end error recovery and flow control.
Session layer establishes, manages and terminates connections between applications.
Presentation layer provides independence from differences in data representation (e.g. encryption)
Application layer supports application and end-user processes.

### TCP/IP Protocol

application     OSI 5-7
TCP, UDP        OSI 4
IP              OSI 3
h/w interface   OSI 1-2

#### Alternative Protocol

- Firewire
- USB
- Bluetooth
- WiFi

## Networking

## Gateways

## Packet encapsulation

Each layer adds header information to the packet it receives from the layer above, as the packet passes down. On the receiving side, these headers are removed as the packet moves up.

## Connection Models

### Connection oriented
A single connection is established for the session. Two-way communications flow along the connection. When the session is over, the connection is broken. The analogy is to a phone conversation. An example is TCP.

### Connectionless
Messages are sent independent of each other. Ordinary mail is the analogy. Connectionless messages may arrive out of order. An example is the IP protocol.

## Communication Models

### Remote procedure call

## Component Distribution
Application is to consider them as made up of three parts:
- Presentation component
- Application logic
- Data access

### Gartner Classification

Examples: 
1.Distributed Database
2. Network File Service
3. Web
4. Terminal Emulation
5. X Window System

## Middleware

The functions of middleware include
- Initiation of processes at different computers
- Session management
- Directory services to allow clients to locate servers
- remote data access
- Concurrency control to allow servers to handle multiple clients
- Security and integrity
- Monitoring
- Termination of processes both local and remote

## Points of Failure

- The client side of the application could crash
- The client system may have h/w problems
- The client's network card could fail
- Network contention could cause timeouts
- There may be network address conflicts
- Transmission errors may lose messages
- The client and server versions may be incompatible
- The server's network card could fail
- The server system may have h/w problems
- The server s/w may crash
- The server's database may become corrupted

