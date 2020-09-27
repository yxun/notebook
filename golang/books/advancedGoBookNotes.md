
1.1 Go history

CSP --> Squeak --> Newsqueak --> Alef -->
C -->
Pascal --> Modula-2 --> Oberon --> Oberon-2 -->

1.3 Array, String and Slice

Array copy on value. String read-only array.
Slice copy on head value (reference).

GO assignment and parameter copy on value except clousure.

1.3.1 Array

Array a fixed length sequence of certain type elements.
length is part of an array.

Array definition:

```
var a [3]int                    // length 3 int array, elements all 0
var b = [...]int(1,2,3)         // length 3 int array, elements 1,2,3
var c = [...]int{2: 3, 1: 2}    // length 3 int array, elements 0,2,3
var d = [...]int{1,2,4: 5, 6}   // length 6 int array, elements 1,2,0,0,5,6
```

define a empty array

```
var d [0]int        
var e = [0]int{}
var f = [...]int{}
```

usage

```
c1 := make(chan [0]int)
go func() {
    fmt.Println("c1")
    c1 <- [0]int{}
}()
<-c1
```

alternative using annonymous struct

```
c2 := make(chan struct{})
go func() {
    fmt.Println("c2")
    c2 <- struct{}{}  // struct{} is type, {} is value
}()
<-c2
```

1.3.2 String

```
type StringHeader struct {
    Data uintptr
    Len  int
}
```

len function can return the length of a string. We can also use reflect.StringHeader

```
fmt.Println("len(s):", (*reflect.StringHeader)(unsafe.Pointer(&s)).Len)
```
'for range' cannot iterate non-UTF8 encoded string.

[]rune is an alas of []int32.

1.3.3 slice

```
type SliceHeader struct {
    Data uintptr
    Len  int
    Cap  int
}
```

define a slice

```
var (
    a []int             // nil slice, equal to nil, represent a not existing slice
    b = []int{}         // empty slice, not equal to nil
    c = []int{1,2,3}
    d = c[:2]
    e = c[0:2:cap(c)]
    f = c[:0]
    g = make([]int, 3)
    h = make([]int, 2, 3)
    i = make([]int, 0, 3)
)
```

add element into slice

```
var a []int
a = append(a, 1)
a = append(a, 1, 2, 3)
a = append(a, []int{1,2,3}...)

a = append([]int{0}, a...)
a = append([]int{-3,-2,-1}, a...)

a = append(a[:i], append([]int{x}, a[i:]...)...)
a = append(a[:i], append([]int{1,2,3}, a[i:]...)...)

a = append(a, 0)
copy(a[i+1:], a[i:])
a[i] = x

a = append(a, x...)
copy(a[i+len(x):], a[i:])
copy(a[i:], x)
```

delete an element

```
a = []int{1, 2, 3}
a = a[:len(a)-1]
a = a[:len(a)-N]

a = a[1:]
a = a[N:]

a = append(a[:0], a[1:]...)
a = append(a[:0], a[N:]...)

a = a[:copy(a, a[1:])]
a = a[:copy(a, a[N:])]

a = append(a[:i], a[i+1:]...)
a = append(a[:i], a[i+N:]...)

a = a[:i+copy(a[i:], a[i+1:])]
a = a[:i+copy(a[i:], a[i+N:])]
```

examples

```
func TrimSpace(s []byte) []byte {
    b := s[:0]      // 0 length slice
    for _, x := range s {
        if x != ' ' {
            b = append(b,x)
        }
    }
    return b
}
```

```
func FindPhoneNumber(filename string) []byte {
    b, _ := ioutil.ReadFile(filename)
    b = regexp.MustCompile("[0-9]+").Find(b)
    return append([]byte{}, b...)
}
```

If a slice element is a pointer, delete an element but the underline array is still referenced. 
To avoid above memory leak, set the element to nil

```
var a []*int{...}
a[len(a)-1] = nil   // GC will collect last element
a = a[:len(a)-1]
```

enforce type convert examples

```
// +build amd64 arm64

import "sort"

var a = []float64{4,2,5,7,2,1,88,1}

func SortFloat64FastV1(a []float64) {
    var b []int = ((*[1 << 20]int)(unsafe.Pointer(&a[0])))[:len(a):cap(a)]

    sortInts(b)
}

func SortFloat64FastV2(a []float64) {
    var c []int
    aHdr := (*reflect.SliceHeader)(unsafe.Pointer(&a))
    cHdr := (*reflect.SliceHeader)(unsafe.Pointer(&c))
    *cHdr = *aHdr

    sort.Ints(c)
}
```

1.4 function, method and interface

Go program execution starts from main.main 
main --> import pkg1 --> const --> var --> init() --> main()

1.4.1 function

function supports variable length parameter. It must be the last parameter. It is a actually a slice.

```
func Sum(a int, more ...int) int {
    for _, v := range more {
        a += v
    }
    return a
}
```

If return value has a name, we can use it to modify return value

```
func Inc() (v int) {
    defer func(){ v++ }()
    return 42
}
```
above defer func is a clousure.

```
func main() {
    for i := 0; i < 3; i++ {
        defer func(){ println(i) }()
    }
}
// Output
// 3
// 3
// 3
```

Fix apporach

```
func main() {
    for i := 0; i < 3; i++ {
        i := i  // define a local variable i
        defer func(){ println(i) }()
    }
}

func main() {
    for i := 0; i < 3; i++ {
        // parse i to function 
        defer func(i int){ println(i) }(i)
    }
}
```

1.4.2 method

method to function

```
// func CloseFile(f *File) error
var CloseFile = (*File).Close

// func ReadFile(f *File, offset int64, data []byte) int
var ReadFile = (*File).Read

f, _ := OpenFile("foo.dat")
ReadFile(f, 0, data)
CloseFile(f)
```

Use closure to overload a method

```
f, _ := OpenFile("foo.dat")

// func Close() error
var Close = func() error {
    return (*File).Close(f)
}

// func Read(offset int64, data []byte) int
var Read = func(offset int64, data []byte) int {
    return (*File).Read(f, offset, data)
}

Read(0, data)
Close()

```

simple version

```
f, _ := OpenFile("foo.dat")

var Close = f.Close

var Read = f.Read

Read(0, data)
Close()

```

Inheritance
Go use an annonymous member in a struct.

```
import "image/color"

type Point struct{ X, Y float64 }

type ColoredPoint struct {
    Point
    Color color.RGBA
}

var cp ColoredPoint
cp.X = 1
fmt.Println(cp.Point.X)  // 1
cp.Point.Y = 2
fmt.Println(cp.Y)  // 2

```
compiler will replace cp.X and cp.Y with cp.Point.X and cp.Point.Y

Use interface to achieve polymophism 

1.4.3 Interface

Interface and duck typing
Interface is an abstruction of other type.
If an object looks like an implementation of an interface, it can be used as the interface.

```
// fmt.Fprintf
func Fprintf(w io.Writer, format string, args ...interface{}) (int, error)

type io.Writer interface {
    Write(p []byte) (n int, err error)
}

type error interface {
    Error() string
}
...

...
// example of printing a upper case string 

type UpperWriter struct {
    io.Writer
}

func (p *UpperWriter) Write(data []byte) (n int, err error) {
    return p.Writer.Write(bytes.ToUpper(data))
}

func main() {
    fmt.Fprintln(&UpperWriter{os.Stdout}, "hello, world")
}
```

...
// example define format to print upper case string

type UpperString string

func (s UpperString) String() string {
    return strings.ToUpper(string(s))
}

type fmt.Stringer interface {
    String() string
}

func main() {
    fmt.Fprintln(os.Stdout, UpperString("hello, world"))
}
...

interfacd convertion

```
var (
    a io.ReadCloser = (*os.File)(f)  // *os.File implements io.ReadCloser interface
    b io.Reader = a 
    c io.Closer = a
    d io.Reader = c.(io.Reader)     // normal convertion 
)
```

1.5 Currency

1.5.1 Goroutine and system threads

goroutine is a light weighted thread. it is different from os thread.
Every os thread has a fixed size stack (around 2MB). It is used for storing parameters and local variables in recursion function calls.

A goroutine uses a small size stack (2KB or 4KB). If it is not big enough, it will dynamically resize the stack up to 1GB.

runtime.GOMAXPROCS variable can control runtime number of goroutines

1.5.2 Atomic operations

In concurrent programming, atomic operation is the minimum non-concurrent operation.
If multiple threads access a shared resource, atomic operation means there is only one thread operation at a moment.

Use mutual exclusive to achieve atomic operations. Example of a simulation sync.Mutex

```
import (
    "sync"
)

var total struct {
    sync.Mutex
    value int
}

func worker(wg *sync.WaitGroup) {
    defer wg.Done()

    for i := 0; i <= 100; i++ {
        total.Lock()
        total.value += i
        total.Unlock()
    }
}

func main() {
    var wg sync.WaitGroup
    wg.Add(2)
    go worker(&wg)
    go worker(&wg)
    wg.Wait()

    fmt.Println(total.value)
}
```

Use lock is not efficient. sync/atomic package can support that

```
import (
    "sync"
    "sync/atomic"
)

var total uint64

func worker(wg *sync.WaitGroup) {
    defer wg.Done()

    var i uint64
    for i := 0; i <= 100; i++ {
        atomic.AddUint64(&total, i)
    }
}

func main() {
    var wg sync.WaitGroup
    wg.Add(2)

    go worker(&wg)
    go worker(&wg)
    wg.Wait()
}

```

another example of using a flag

```
type singleton struct {}

var (
    instance    *singleton
    initialized uint32
    mu          sync.Mutex
)

func Instance() *singleton {
    if atomic.LoadUint32(&initialized) == 1 {
        return instance
    }

    mu.Lock()
    defer mu.Unlock()

    if instance == nil {
        defer atomic.StoreUint32(&initialized, 1)
        instance = &singleton{}
    }
    return instance
}

```

Use sync.Once

```
type Once struct {
    m    Mutex
    done uint32
}

func (o *Once) Do(f func()) {
    if atomic.LoadUint32(&o.done) == 1 {
        return
    }

    o.m.Lock()
    defer o.m.Unlock()

    if o.done == 0 {
        defer atomic.StoreUint32(&o.done, 1)
        f()
    }
}

```

Use sync.Once rewrite the instance 

```
var (
    instance   *singleton
    once       sync.Once
)

func Instance() *singleton {
    once.Do(func() {
        instance = &singleton{}
    })
    return instance
}

```

atomic.Value supports Load and Store methods for loading and storing data. Return value interface{}

```
var config atomic.Value  // save current configure information, shared variable

// init config
config.Store(loadConfig())

// server, start a goroutine and generate and load updated config
go func() {
    for {
        time.Sleep(time.Second)
        config.Store(loadConfig())
    }
}()


// client load latest config
for i := 0; i < 10; i++ {
    go func() {
        for r := range requests() {
            c := config.Load()
            // ...
        }
    }()
}

```

1.5.3 memory consistent order model

Golang, execution order is consistent in a same Goroutine. 
But there is not a memory consistent order garantee between multiple Goroutines.

```
func main() {
    go println("hello, world")
}
```

this may not print any message. main routine completed and exit without waiting any other goroutine

Fix example,
```
func main() {
    done := make(chan int)

    go func() {
        println("hello, world")
        done <- 1
    }()
    <-done
}
```

```
func main() {
    var mu sync.Mutex
    mu.Lock()
    go func() {
        println("hello, world")
        mu.Unlock()
    }()
    mu.Lock()
}
```

1.5.4 init order
if there is a goroutine in init(), the new goroutine will be executed with main.main not with the init().

1.5.5 create goroutine

1.5.6 communication with channel
non-cached send to channel always executed before cooresponding received from the channel.
After close a channel, the receiver will receive channel type zero value.

if a non-cached receive from a channel is executed before a send to the channel operation, the send operation can only complete exeuction after the receive is done.

cached channel, kth receive executed before k+c th send, c is the channel cache size.
we can use channel cache size to control the maximum number of goroutines,

```
var limit = make(chan int, 3)

func main() {
    for _, w := range work {
        go func() {
            limit <- 1
            w()
            <-limit
        }()
    }
    select{}
}
```
select{} is an empty pipe. It can conjuct the main thread. similar approaches: for{}, <-make(chan int)
the program can exit with os.Exit(0)

1.6 concurrent programming patterns
Do not communicate by sharing memory; instead, share memory by communicating.

1.6.1 concurrent hello world

```
func main() {
    done := make(chan int, 1) // cached channel

    go func() {
        fmt.Println("hello, world")
        done <- 1
    }()
    <-done
}
```

more than 1 cache

```
func main() {
    done := make(chan int, 10)  // cache size 10

    for i := 0; i < cap(done); i++ {
        go func() {
            fmt.Println("hello, world")
            done <- 1
        }()
    }

    // wait until all done
    for i := 0; i < cap(done); i++ {
        <-done
    }
}
```

there is a simple way when using sync.WaitGroup

```
import (
    "fmt"
    "os"
    "os/signal"
    "syscall"
)

func main() {
    var wg sync.WaitGroup

    for i := 0; i < 10; i++ {
        wg.Add(1)

        go func() {
            fmt.Println("hello, world")
            wg.Done()
        }()
    }

    // wait all done
    wg.Wait()
}
```

1.6.2 producer and consumer pattern

```
// producer, generate times of factor
func Producer(factor int, out chan<- int) {
    for i := 0; ; i++ {
        out <- i*factor
    }
}

// consumer
func Consumer(in <-chan int) {
    for v := range in {
        fmt.Println(v)
    }
}

func main() {
    ch := make(chan int, 64)

    go Producer(3, ch)
    go Producer(5, ch)
    go Consumer(ch)

    // Ctrl+C exit
    sig := make(chan os.Signal, 1)
    signal.Notify(sig, syscall.SIGINT, syscall.SIGTERM)
    fmt.Printf("quit (%v)\n", <-sig)
}

```

1.6.3 publish-and-subscribe pattern
pub/sub send and receive a message from a topic.
producer:consumer  M:N

```
// package pubsub implements a simple multi-topic pub-sub library.
package pubsub

import (
    "fmt"
    "sync"
    "strings"
    "time"
)

type (
    subscriber chan interface{}          // sub is a channel
    topicFunc  func(v interface{}) bool  // topic is a filter
)

// Publisher
type Publisher struct {
    m           sync.RWMutex                // read, write lock
    buffer      int                         // sub cache size
    timeout     time.Duration               // publish timeout
    subscribers map[subscriber]topicFunc    // subscribers info
}

// pub constructer
func NewPublisher(publishTimeout time.Duration, buffer int) *Publisher {
    return &Publisher{
        buffer:         buffer,
        timeout:        publishTimeout,
        subscribers:    make(map[subscriber]topicFunc),
    }
}

// add a new sub, subscribe all topics
func (p *Publisher) Subscribe() chan interface{} {
    return p.SubscribeTopic(nil)
}

// add a new sub, subscribe filtered topic
func (p *Publisher) SubscribeTopic(topic topicFunc) chan interface{} {
    ch := make(chan interface{}, p.buffer)
    p.m.Lock()
    p.subscribers[ch] = topic
    p.m.Unlock()
    return ch
}

// exit subscribe
func (p *Publisher) Evict(sub chan interface{}) {
    p.m.Lock()
    defer p.m.Unlock()

    delete(p.subscribers, sub)
    close(sub)
}

// publish a topic
func (p *Publisher) Publish(v interface{}) {
    p.m.RLock()
    defer p.m.RUnlock()

    var wg sync.WaitGroup
    for sub, topic := range p.subscribers {
        wg.Add(1)
        go p.sendTopic(sub, topic, v, &wg)
    }
    wg.Wait()
}

// close publisher and close all subscribe channels
func (p *Publisher) Close() {
    p.m.Lock()
    defer p.m.Unlock()

    for sub := range p.subscribers {
        delete(p.subscribers, sub)
        close(sub)
    }
}

// publish a topic and timeout
func (p *Publisher) sendTopic(sub subscriber, topic topicFunc, v interface{}, wg *sync.WaitGroup) {
    defer wg.Done()
    if topic != nil && !topic(v) {
        return
    }

    select {
    case sub <- v:
    case <-time.After(p.timeout):
    }
}

func main() {
    p := pubsub.NewPublisher(100*time.Millisecond, 10)
    defer p.Close()

    all := p.Subscribe()
    golang := p.SubscribeTopic(func(v interface{}) bool {
        if s, ok := v.(string); ok {
            return strings.Contains(s, "golang")
        }
        return false
    })

    p.Publish("hello, world")
    p.Publish("hello, golang")

    go func() {
        for msg := range all {
            fmt.Println("all:", msg)
        }
    }()

    go func() {
        for msg := range golang {
            fmt.Println("golang:", msg)
        }
    }()

    // run 3 seconds and exit
    time.Sleep(3 * time.Second)
}

```

example of concurrent search

```
func main() {
    ch := make(chan string, 32)

    go func() {
        ch <- searchByBing("golang")
    }()
    go func() {
        ch <- searchByGoogle("golang")
    }()
    go func() {
        ch <- searchByBaidu("golang")
    }()

    fmt.Println(<-ch)
}
```

1.6.6 prime number filter

concurrent CSP model performance is not good.

```
// generate natural numbers: 2,3,4, ...
func GenerateNatural() chan int {
    ch := make(chan int)
    go func() {
        for i := 2; ; i++ {
            ch <- i
        }
    }()
    return ch
}

// delete numbers can be divided by the prime
func PrimeFilter(in <-chan int, prime int) chan int {
    out := make(chan int)
    go func() {
        for {
            if i := <-in; i % prime != 0 {
                out <- i
            }
        }
    }()
    return out
}

func main() {
    ch := GenerateNatural()
    for i := 0; i < 100; i++ {
        prime := <-ch
        fmt.Printf("%v: %v\n", i+1, prime)
        ch = PrimeFilter(ch, prime)
    }
}

```

1.6.7  safe exit of goroutine

goroutines use channel to communicate. When we need to process multiple channels, we use keyword select
when there are multiple cases of select, select will randomly pick one. If there is no available branch, it will pick default.
Otherwise, select will hold the channel.

example of timeout detection

```
select {
case v := <-in:
    fmt.Println(v)
case <-time.After(time.Second):
    return   // timeout
}

```

example use select default hold until sending or receiving data

```
select {
case v := <-in:
    fmt.Println(v)
default:
    // no data
}

```

Use select to avoid main function exit

```
func main() {
    // do something
    select{}
}

```

Use select randomly pick a branch. We can generate a random sequence

```
func main() {
    ch := make(chan int)
    go func() {
        for {
            select {
            case ch <- 0:
            case ch <- 1:
            }
        }
    }()

    for v := range ch {
        fmt.Println(v)
    }
}

```

Use select and default implements a goroutine exit control

```
func worker(cannel chan bool) {
    for {
        select {
        default:
            fmt.Println("hello")
        case <-cannel:
            // exit
        }
    }
}

func main() {
    cannel := make(chan bool)
    go worker(cannel)

    time.Sleep(time.Second)
    cannel <- true
}

```

Use close . All data receive from a closed channel is a zero value and a fail flag

```
func worker(cannel chan bool) {
    for {
        select {
        default:
            fmt.Println("hello")
        case <-cannel:
            // exit
        }
    }
}

func main() {
    cancel := make(chan bool)

    for i := 0; i < 10; i++ {
        go worker(cancel)
    }

    time.Sleep(time.Second)
    close(cancel)
}

```

Use sync.WaitGroup to add some cleanup steps when close a channel

```
func worker(wg *sync.WaitGroup, cannel chan bool) {
    defer wg.Done()

    for {
        select {
        default:
            fmt.Println("hello")
        case <-cannel:
            return
        }
    }
}

func main() {
    cancel := make(chan bool)

    var wg sync.WaitGroup
    for i := 0; i < 10; i++ {
        wg.Add(1)
        go worker(&wg, cancel)
    }

    time.Sleep(time.Second)
    close(cancel)
    wg.Wait()
}

```

1.6.8 context package

Go 1.7 context package simplify single request and multiple goroutines operations.

Use context control exit and timeout

```
func worker(ctx context.Context, wg *sync.WaitGroup) error {
    defer wg.Done()

    for {
        select {
        default:
            fmt.Println("hello")
        case <-ctx.Done():
            return ctx.Err()
        }
    }
}

func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)

    var wg sync.WaitGroup
    for i := 0; i < 10; i++ {
        wg.Add(1)
        go worker(ctx, &wg)
    }

    time.Sleep(time.Second)
    cancel()

    wg.Wait()
}

```

Use context to avoid memory leak in prime filter example

```
func GenerateNatural(ctx context.Context) chan int {
    ch := make(chan int)
    go func() {
        for i := 2; ; i++ {
            select {
            case <- ctx.Done():
                return
            case ch <- i:
            }
        }
    }()
    return ch
}

func PrimeFilter(ctx context.Context, in <-chan int, prime int) chan int {
    out := make(chan int)
    go func() {
        for {
            if i := <-in; i%prime != 0 {
                select {
                case <- ctx.Done():
                    return
                case out <- i:
                }
            }
        }
    }()
    return out
}

func main() {
    // use Context to control background goroutine status
    ctx, cancel := context.WithCancel(context.Background())

    ch := GenerateNatural(ctx)
    for i := 0; i < 100; i++ {
        prime := <-ch
        fmt.Printf("%v: %v\n", i+1, prime)
        ch = PrimeFilter(ctx, ch, prime)
    }
    cancel()
}

```

1.7.1 error handling
use defer to close a file after opening a file. Use recover() to convert a panic into an error.

```
func ParseJSON(input string) (s *Syntax, err error) {
    defer func() {
        if p := recover(); p != nil {
            err = fmt.Errorf("JSON: internal error : %v", p)
        }
    }()
    // ...parser...
}
```

1.7.2 capture error context
We can define a support function WrapError. It wraps error information and also keep the original error type.

e.g. github.com/chai2010/errors

```
for i, e := range err.(errors.Error).Wrapped() {
    fmt.Printf("wraped(%d): %v\n", i, e)
}

for i, x := range err.(errors.Error).Caller() {
    fmt.Printf("caller:%d: %s\n", i, x.FuncName)
}

// network transport error using JSON string
func sendError(ch chan<- string, err error) {
    ch <- errors.ToJson(err)
}

func recvError(ch <-chan string) error {
    p, err := errors.FromJson(<-ch)
    if err != nil {
        log.Fatal(err)
    }
    return p
}

// bind a http response code with an error
err := errors.NewWithCode(404, "http error code")

fmt.Println(err)
fmt.Println(err.(errors.Error).Code())

```

1.7.4 throw panic

recover function return value is same as the parameter of the panic function

```
func panic(interface{})
func recover() interface{}

```

recover function needs to be called in a defer func, not in a defer statment.

We cannot use MyRecover (which encapsulates recover()) function in a defer func.
We cannot use recover func in the ... , defer func() { defer func() {...} }

Avoid using panic(nil). Otherwise, recover() will always return nil

e.g. panic to error with different error types

```
func foo() (err error) {
    defer func() {
        if r := recover(); r != nil {
            switch x := r.(type) {
            case string:
                err = errors.New(x)
            case error:
                err = x
            default:
                err = fmt.Errorf("Unknown panic: %v", r)
            }
        }
    }()

    panic("TODO")
}

```



