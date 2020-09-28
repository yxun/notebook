
### Comment Sentences

```
// Request represents a request to run a command.
type Request struct { ... }

// Encode writes the JSON encoding of req to w.
func Encode(w io.Writer, req *Request) { ... }

```

### Contexts

Must functions that use a Context should accept it as their first parameter:
func F(ctx context.Context, /* other arguments */) {}

A function that is never request-specific may use `context.Background()`
Don't add a Context memeber to a struct type; instead add a ctx parameter to each method on that type that needs to pass it along.
Don't create custom Context types or use interfaces other than Context in function signatures.
Contexts are immutable, so it's fine to pass the same ctx to multiple calls.

### Copying

In general, do not copy a value of type T if its methods are associated with the pointer type, *T

### Crypto Rand

Do not use package `math/rand` to generate keys. It is seeded with `time.Nanoseconds()`. 
Instead, use `crypto/rand` 's Reader.

```
import (
    "crypto/rand"
    // "encoding/base64"
    // "encoding/hex"
    "fmt"
)

func Key() string {
    buf := make([]byte, 16)
    _, err := rand.Read(buf)
    if err != nil {
        panic(err)    // out of randomness, should never happen
    }
    return fmt.Sprintf("%x", buf)
    // or hex.EncodeToString(buf)
    // or base64.StdEncoding.EncodeToString(buf)

}

```

### Declaring Empty Slices

prefer

`var t []string`

over

`t := []string{}`

The former declares a nil slice value, while the latter is non-nil but zero-length. There are limited circumstances where a non-nil but zero-length slice is preferred, such as when encoding JSON objects
(a nil slice encodes to null, while []string{} encodes to the JSON array [])

### Error Strings

Error strings should not be capitalized (unless beginning with proper nouns or acronyms) or end with punctuation. use `fmt.Errorf("something bad")` not `fmt.Errorf("Something bad")`
This does not apply to logging.

### Goroutine lifetimes

When you spawn goroutines, make it clear when - or whether - they exit. The garbage collector will not terminate a goroutine even if the channels it is blocked on are unreachable.

### Handle Errors

Do not discard errors using _ variables.

### Imports

Avoid renaming imports except to avoid a name collision. Imports are organized in groups, with black lines between them. The standard library packages are always in the first group.

### Indent Error Flow

```
x, err := f()
if err != nil {
    // error handling
    return
}
// use x

```

### Interfaces

Do not define interfaces on the implementor side of an API "for mocking"; instead, design the API so that it can be tested using the public API of the real implementation.

Do not define interfaces before they are used; without a realistic example of usage, it is too difficult to see whether an interface is even necessary.

### Receiver Type

- If the receiver is a map, func or chan, don't use a pointer to them. If the receiver is a slice and the method doesn't reslice or reallocate the slice, don't use a pointer to it.
- If the method needs to mutate the receiver, the receiver must be a pointer.
- If the receiver is a struct that contains a sync.Mutex or similar synchronizing field, the receiver must be a pointer to avoid copying.
- If the receiver is a large struct or arrary, a pointer receiver is more efficient.
- Can function or methods, either concurrently or when called from this method, be mutating the receiver ? If changes must be visible in the original receiver, the receiver must be a pointer.
- If the receiver is a struct, array or slice and any of its elements is a pointer to something that might be mutating, prefer a pointer receiver.
- If the receiver is a small array or struct that is naturally a value type (for instance, something like the time.Time type), with no mutable fields and no pointers, or is just a simple basic type such as int or string, a value receiver make sense.
- Finally, when in doubt, use a pointer receiver.
