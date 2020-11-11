roughly make the analogy: service => class, rpc => function and message => global variables

$ cd ..
$ protoc --go_out=plugins=grpc:. hellopb/hello.proto