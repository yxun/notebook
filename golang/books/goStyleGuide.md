
## Introduction

### general guidelines

1. [Effective Go](https://golang.org/doc/effective_go.html)
2. [The Go common mistakes guide](https://github.com/golang/go/wiki/CodeReviewComments)

setting up editor to:
- Run `goimorts` on save
- Run `golint` and `go vet` to check for errors

## Guidelines

### Verify interface compliance

An interface is two fields:
1. A pointer to some type-specific information.
2. Data pointer.

You should be passing interfaces as values.

e.g. add a compile check for checking a type matches an interface

```
type Handler struct {
    // ...
}

var _ http.Hander = (*Handler)(nil)

func (h *Handler) ServeHTTP(w http.ResponseWriter, r *http.Request,) {
    // ...
}

```

```
type LogHandler struct {
    h    http.Handler
    log  *zap.Logger
}

var _ http.Handler = LogHandler{}

func (h LogHandler) ServeHTTP(
    w http.ResponseWriter,
    r *http.Request,
) {
    // ...
}

```

### Receivers and interfaces

Methods with value receivers can be called on pointers as well as values. Methods with pointer receivers can only be called on pointers or addressable values.

### Copy slices and maps at boundaries

e.g. make a copy of slices and maps instead of assigning them from arguments

```
func (d *Driver) SetTrips(trips []Trip) {
    d.trips = make([]Trip, len(trips))
    copy(d.trips, trips)
}

trips := ...
d1.SetTrips(trips)

// We can now modify trips[0] without affecting d1.trips
trips[0] = ...

```

Returning slices and maps
Similarly, be wary of user modifications to maps or slices exposing internal state.

```
type Stats struct {
    mu sync.Mutex
    counters map[string]int
}

func (s *Stats) Snapshot() map[string]int {
    s.mu.Lock()
    defer s.mu.Unlock()

    result := make(map[string]int, len(s.counters))
    for k, v := range s.counters {
        result[k] = v
    }
    return result
}

// Snapshot is now a copy
snapshot := stats.Snapshot()

```

### Defer to clean up
Use defer to clean up resources such as files and locks.

```
p.Lock()
defer p.Unlock()

if p.count < 10 {
    return p.count
}

p.count++
return p.count

```

### Channel size should be one or none

### Start Enums at one

```
type Operation int

const (
    Add Operation = iota + 1
    Subtract
    Multiply
)

// Add = 1, Subtract = 2, Multiply = 3
```

There are also cases where using the zero value make senses.

### Use "time" to handle time

e.g. Use time.Time for instants of time

```
func isActive(now, start, stop time.Time) bool {
    return (start.Before(now) || start.Equal(now)) && now.Before(stop)
}
```

e.g. Use time.Duration for periods of time

```
func poll(delay time.Duration) {
    for {
        // ...
        time.Sleep(delay)
    }
}

poll(10*time.Second)

```

Use time.Time and time.Duration with external systems
- Command-line flags: `flag` supports time.Duration via `time.ParseDuration`
- JSON: `encoding/json` supports encoding time.Time via its `UnmarshalJSON` method
- SQL: `database/sql` supports converting `DATETIME` or `TIMESTAMP` columns into `time.Time`
- YAML: `gopkg.in/yaml.v2` supports `time.Time` and `time.Duration` via `time.ParseDuration`

When it is not possible to use `time.Duration`, use int or float64 and include the unit in the name of the field.

```
// {"intervalMillis": 2000}
type Config struct {
    IntervalMillis int `json:"intervalMillis"`
}

```

### Error Types

There are various options for declaring errors:
- `errors.New` for errors with simple static strings
- `fmt.Errorf` for formatted error strings
- Custom types that implement an Error() method
- Wrapped errors using `"pkg/errors".Wrap`

If the client needs to detect the error, and you have created a simple error using `errors.New`, use a var for the error.
If you have an error that clients may need to detect, then you should use a custom type.

```
type errNotFound struct {
    file string
}

func (e errNotFound) Error() string {
    return fmt.Sprintf("file %q not found", e.file)
}

func open(file string) error {
    return errNotFound{file: file}
}

func use() {
    if err := open("testfile.txt"); err != nil {
        if _, ok := err.(errNotFound); ok {
            // handle
        } else {
            panic("unknown error")
        }
    }
}

```

Be careful with exporting custom error types directly since they become part of the public API. It is preferable to expose matcher functions to check the error instead.

```
// package foo

type errNotFound struct {
    file string
}

func (e errNotFound) Error() string {
    return fmt.Sprintf("file %q not found", e.file)
}

func IsNotFoundError(err error) bool {
    _, ok := err.(errNotFound)
    return ok
}

func Open(file string) error {
    return errNotFound{file: file}
}

// package bar

if err := foo.Open("foo"); err != nil {
    if foo.IsNotFoundError(err) {
        // handle
    } else {
        panic("unknown error")
    }
}

```

### Error Wrapping

There are three main options for propagating errors if a call fails:
- Return the original error if there is no additional context to add and you want to maintain the original error type.
- Add context using "pkg/errors".Wrap so that the error message provides more context and "pkg/errors".Cause can be used to extract the original error.
- Use fmt.Errorf if the callers do not need to detect or handle that specific error case.

### Handle Type Assertion Failures

```
t, ok := i.(string)
if !ok {
    // handle the error gracefully
}

```

### Don't panic
Code running in production must avoid panics.

```
func run(args []string) error {
    if len(args) == 0 {
        return errors.New("an argument is required")
    }
    // ...
    return nil
}

func main() {
    if err := run(os.Args[1:]); err != nil {
        fmt.Fprintln(os.Stderr, err)
        os.Exit(1)
    }
}

```

Panic/recover is not an error handling strategy. A program must panic only when something irrecoverable happens such as a nil dereference.
Even in tests, prefer `t.Fatal` or `t.FailNow` over panics to ensure that the test is marked as failed

### Avoid Mutable Globals

Avoid mutating global variables, instead opting for dependency injection. This applies to function pointers as well as other kinds of values.

```
// sign.go

type signer struct {
    now func() time.Time
}

func newSigner() *signer {
    return &signer{
        now: time.Now,
    }
}

func (s *signer) Sign(msg string) string {
    now := s.now()
    return signWithTime(msg, now)
}

// sign_test.go

func TestSigner(t *testing.T) {
    s := newSigner()
    s.now = func() time.Time {
        return someFixedTime
    }

    assert.Equal(t, want, s.Sign(give))
}

```

### Avoid embedding types in public structs

Instead, hand-write only the methods to your concrete list that will delegate to the abstract list.

```
// ConcreteList is a list of entities.
type ConcreteList struct {
    list *AbstractList
}

// Add adds an entity to the list.
func (l *ConcreteList) Add(e Entity) {
    return l.list.Add(e)
}

// Remove removes an entity from the list.
func (l *ConcreteList) Remove(e Entity) {
    return l.list.Remove(e)
}

```

An embedded type is rarely necessary. It is a convenience that helps you avoid writing tedious delegate methods. But it will leak the detail.

### Avoid using built-in names

Note that the compiler will not generate errors when using predeclared identifiers, but tools such as `go vet` should correctly point out.

### Avoid init()

Avoid init() where possible. When init() is unavoidable or desirable, code should attempt to:
1. Be completely deterministic, regardless of program environment or invocation.
2. Avoid depending on the ordering or side-effects of other init() functions.
3. Avoid accessing or manipulating global or environment state, such as machine information, environment variables, working directory, program arguments/inputs, etc.
4. Avoid I/O, including both filesystem, network, and system calls.

Considering the above, some situations in which init() may be preferable or necessary might include:
- Complex expressions that cannot be represented as single assignments.
- Pluggable hooks, such as database/sql dialects, encoding type registries, etc.
- Optimizations to Google Cloud Functions and other forms or deterministic precomputations.

## Performance

### Prefer strconv over fmt

When converting primitives to/from strings, strconv is faster than fmt .

```
for i := 0; i < b.N; i++ {
    s := strconv.Itoa(rand.Int())
}
```

### Avoid string-to-byte conversion

Do not create byte slices from a fixed string repeatedly. Instead, perform the conversion once and capture the result.

```
data := []byte("Hello world)
for i := 0; i < b.N; i++ {
    w.Write(data)
}
```

### Prefer specifying container capacity

where possible, provide capacity hints when initializing maps with make()

make(map[T1]T2, hint)

```
files, _ := ioutil.ReadDir("./files")

m := make(map[string]os.FileInfo, len(files))
for _, f := range files {
    m[f.Name()] = f
}

```

When possible, provide capacity hints when initializing slices with make(), particularly when appending.

make([]T, length, capacity)

Unlike maps, slice capacity is not a hint.

```
for n := 0; n < b.N; n++ {
    data := make([]int, 0, size)
    for k := 0; k < size; k++ {
        data = append(data, k)
    }
}
```

## Style

### Be consistent

Only group related declarations. Do not group declarations that are unrelated.
Groups are not limited in where they can be used. For example, you can use them inside of functions.

### Import group ordering

standard library and then everyting else

### Package Names

- All lower-case. No capitals or underscores.
- Does not need to be renamed using named imports at most call sites.
- Short and succinct. Remember that the name is identified in full at every call site.
- Not plural. For example, net/url, not net/urls
- Not "common", "util", "shared", or "lib". These are bad, uninformative names.

### Function Names

MixedCaps for function names. An exception is made for test functions, which may contain underscores for the purpose of grouping related test cases.

### Import aliasing

Import aliasing must be used if the package name does not match the last element of the import path.
In all other scenarios, import aliases should be avoided unless there is a direct conflict between imports.

### Function Grouping and Ordering

- Functions should be sorted in rough call order.
- Functions in a file should be grouped by receiver.

Exported functions should appear first in a file, after struct, const, var definitions.
Plain utility functions should appear towards the end of the file.

### Reduce Nesting

Code should reduce nesting where possible by handling error cases/special conditions first and returning early or continuing the loop.

```
for _, v := range data {
    if v.F1 != 1 {
        log.Printf("Invalid v: %v", v)
        continue
    }

    v = process(v)
    if err := v.Call(); err != nil {
        return err
    }
    v.Send()
}

```

### Top-level variable declarations

At the top level, use the standard var keyword. Do not specify the type, unless it is not the same type as the expression.

```
var _s = F()

func F() string { return "A" }

```

### Prefix Unexported Globals with _

Prefix unexported top-level var and const with _ to make it clear when they are used that they are global symbols. Exception: Unexported error values, which should be prefixed with err.
Rationale: Top-level variables and constants have a package scope. Using a generic name makes it easy to accidentally use the wrong value in a different file.

### Embedding in structs

Embedded types (such as mutexes) should be at the top of the field list of a struct, and there must be an empty line separating embedded fields from regular fields.

```
type Client struct {
    http.Client

    version int
}

```

Embedding should not:
- Be purely cosmetic or convenience-oriented.
- Make outer types more difficult to construct or use.
- Affect outer types' zero values.
- Expose unrelated functions or fields from the outer type as a side-effect of embedding the inner type.
- Expose unexported types.
- Affect outer types' copy semantics.
- Change the outer type's API or type semantics.
- Embed a non-canonical form of the inner type.
- Expose implementation details of the outer type.
- Allow users to observe or control type internals.
- Change the general behavior of inner functions through wrapping in a way that would reasonably surprise users.

```
type countingWriteCloser struct {
    // Good: Write() is provided at this
    // outer layer or a specific
    // purpose, and delegates work
    // to the inner type's Write()
    io.WriteCloser

    count int
}

func (w *countingWriteCloser) Write(bs []byte) (int, error) {
    w.count += len(bs)
    return w.WriteCloser.Write(bs)
}

type Book struct {
    // Good: has useful zero value
    bytes.Buffer
}

var b Book
b.Read(...)
b.String()
b.Write()       // ok and avoid nil pointer panic

type Client struct {
    mtx sync.Mutex
    wg sync.WaitGroup
    buf bytes.Buffer
    url url.URL
}
```

### Use field names to initialize structs

```
k := User{
    FirstName: "John",
    LastName: "Doe",
    Admin: true,
}
```

Exception: Field names may be omitted in test tables when there are 3 or fewer fields.

### Local variable declarations

Short variable declarations := should be used if a variable is being set to some value explicitly.

nil is a valid slice of length 0. You should not return a slice of length zero explicitly. Return nil instead.
To check if a slice is empty, always use len(s) == 0 Do not check for nil
The zero value (a slice declared with var) is usable immediately without make()

### Avoid naked parameters
Add C-style comments (/*...*/) for parameters names when their meaning is not obvious.

```
// func printInfo(name string, isLocal, done bool)

printInfo("foo", true /* isLocal */, true /* done */)
```

### Use raw string literals to avoid escaping

raw string literals, which can span multiple lines and include quotes.

```
wantError := `unknown error: "test"`
```

### Initializing struct references
Use &T{} instead of new(T) when initializing struct references so that it is consistent with the struct initialization.

### Initializing maps
Prefer make(...) for empty maps, and maps populated programmatically.
On the other hand, if the map holds a fixed list of elements, use map literals to initialize the map.

### Format Strings outside Printf

```
const msg = "unexpected values %v, %v\n"
fmt.Printf(msg, 1, 2)
```

## Patterns

### Test Tables

Use table-driven tests with subtests to avoid duplicating code when the core test logic is repetitve.

```
// func TestSplitHostPort(t *testing.T)

tests := []struct{
    give        string
    wantHost    string
    wantPort    string
}{
  {
    give:       "192.0.2.0:8000",
    wantHost:   "192.0.2.0",
    wantPort:   "8000",
  },
  {
    give:       ":8000",
    wantHost:   "",
    wantPort:   "8000",
  },
}

for _, tt := range tests {
    t.Run(tt.give, func(t *testing.T) {
        host, port, err := net.SplitHostPort(tt.give)
        require.NoError(t, err)
        assert.Equal(t, tt.wantHost, host)
        assert.Equal(t, tt.wantPort, port)
    })
}

```

### Functional options

Use this pattern for optional arguments in constructors and other public APIs that you foresee needing to expand, especially if you already have three or more arguments on those functions.
Our suggested way of implementing this pattern is with an Option interface that holds an unexported method, recording options on an unexported options struct.

```
type options struct {
    cache   bool
    logger  *zap.Logger
}

type Option interface {
    apply(*options)
}

type cacheOption bool

func (c cacheOption) apply(opts *options) {
    opts.cache = bool(c)
}

func WithCache(c bool) Option {
    return cacheOption(c)
}

type loggerOption struct {
    Log *zap.Logger
}

func (l loggerOption) apply(opts *options) {
    opts.logger = l.log
}

func WithLogger(log *zap.Logger) Option {
    return loggerOption{Log: log}
}

// Open creates a connection.
func Open(
    addr string,
    opts ...Option,
) (*Connection, error) {
    options := options{
        cache:  defaultCache,
        logger: zap.NewNop(),
    }

    for _, o := range opts {
        o.apply(&options)
    }
    // ...
}

```

## Linting

- errcheck
- goimports
- golint
- govet
- staticcheck

