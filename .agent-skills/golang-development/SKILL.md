---
name: golang-development
description: Modern Go (Golang) development best practices (2024-2025). Use for project setup, modules, generics, concurrency, testing, HTTP/gRPC services, databases, CLI, linting, Docker, and production deployment.
metadata:
  tags: ["go", "golang", "backend", "concurrency", "microservices", "grpc", "cli", "testing", "docker"]
---

# Go Development

Modern Go development covering project structure, modules, generics, concurrency patterns, testing, web frameworks, gRPC, databases, CLI tools, linting, and production deployment. Targets Go 1.22+ with focus on 1.23+ and 1.24+ features.

> "Clear is better than clever." — The Go Proverbs

---

## 1. Project Setup & Modules

### Go Modules (`go.mod`)

Single source of truth for dependencies and module path.

```go
module github.com/example/myapp

go 1.23

require (
    github.com/gin-gonic/gin v1.10.0
    github.com/jackc/pgx/v5 v5.7.0
    google.golang.org/grpc v1.68.0
)

require (
    github.com/stretchr/testify v1.9.0 // indirect
)
```

**Key commands:**
```bash
go mod init github.com/example/myapp    # initialize module
go get github.com/gin-gonic/gin         # add dependency
go get -u ./...                         # update all dependencies
go mod tidy                             # remove unused, add missing
go mod download                         # download to module cache
go mod vendor                           # create vendor/ directory
go work init ./api ./worker             # Go workspace (multi-module)
```

### Standard Project Layout

```
myapp/
├── api/                    # API definitions (protobuf, OpenAPI)
│   └── proto/
├── cmd/                    # Application entry points
│   ├── api/
│   │   └── main.go
│   └── worker/
│       └── main.go
├── internal/               # Private application code
│   ├── domain/             # Business logic (entities, value objects)
│   ├── service/            # Use cases / application services
│   ├── repository/         # Data access layer
│   ├── handler/            # HTTP/gRPC handlers
│   └── config/             # Configuration
├── pkg/                    # Public library code (reusable)
│   └── utils/
├── migrations/             # Database migrations
├── scripts/                # Build and deployment scripts
├── configs/                # Configuration files
├── test/                   # Integration and e2e tests
├── go.mod
├── go.sum
├── Makefile
├── Dockerfile
└── README.md
```

**Rules:**
- `cmd/<app>/main.go` — one main per application
- `internal/` — cannot be imported by external modules
- `pkg/` — reusable packages, stable APIs

---

## 2. Go 1.22+ / 1.23+ / 1.24+ Features

### Go 1.22 — Enhanced For Loops

```go
// Loop variables are now per-iteration (no closure bugs)
funcs := []func(){}
for i := 0; i < 3; i++ {
    funcs = append(funcs, func() { fmt.Println(i) })
}
// Before 1.22: all print 3 (shared variable)
// Since 1.22: prints 0, 1, 2 (per-iteration)

// Range over integers
for i := range 10 {          // 0 to 9
    fmt.Println(i)
}

// Range with index and value (slices)
for i, v := range slices.All(mySlice) {
    // i = index, v = value (not pointer!)
}
```

### Go 1.23 — Iterators & New Packages

```go
// Iterators (range-over-func)
func CountUpTo(n int) func(yield func(int) bool) {
    return func(yield func(int) bool) {
        for i := range n {
            if !yield(i) {
                return
            }
        }
    }
}

// Usage
for v := range CountUpTo(5) {
    fmt.Println(v)  // 0, 1, 2, 3, 4
}

// slices package
import "slices"

nums := []int{3, 1, 4, 1, 5}
slices.Sort(nums)                    // [1, 1, 3, 4, 5]
slices.Contains(nums, 3)             // true
slices.Index(nums, 4)                // 3
slices.Compact(nums)                 // remove consecutive duplicates
slices.Delete(nums, 1, 3)            // remove range [1,3)

// maps package
import "maps"

m1 := map[string]int{"a": 1}
m2 := maps.Clone(m1)                 // deep copy
maps.Equal(m1, m2)                   // true

// unique package (interning)
import "unique"

s1 := unique.Make("hello")
s2 := unique.Make("hello")
fmt.Println(s1 == s2)                // true (same interned value)
```

### Go 1.24 — Generic Type Aliases & Testing

```go
// Generic type aliases (previously only non-generic allowed)
type StringSlice[T ~string] = []T

type MyStrings = StringSlice[string]  // []string

// testing/synctest — deterministic time for async tests
import "testing/synctest"

func TestTimeout(t *testing.T) {
    synctest.Run(func() {
        // Time advances only when goroutines block
        // Eliminates flaky timeouts in tests
    })
}

// FIPS 140-3 support (enterprise/security)
// GOEXPERIMENT=boringcrypto go build
```

---

## 3. Modern Go Types & Generics

### Type Parameters (Go 1.18+)

```go
// Generic function
func Max[T comparable](a, b T) T {
    if a > b {  // ERROR: comparable doesn't support >
        return a
    }
    return b
}

// Correct: use constraints.Ordered
import "golang.org/x/exp/constraints"

func Max[T constraints.Ordered](a, b T) T {
    if a > b {
        return a
    }
    return b
}

// Generic struct
type Stack[T any] struct {
    items []T
}

func (s *Stack[T]) Push(v T) {
    s.items = append(s.items, v)
}

func (s *Stack[T]) Pop() (T, bool) {
    var zero T
    if len(s.items) == 0 {
        return zero, false
    }
    v := s.items[len(s.items)-1]
    s.items = s.items[:len(s.items)-1]
    return v, true
}

// Type sets
 type Number interface {
     ~int | ~int64 | ~float64  // ~ allows underlying types
 }

func Sum[T Number](vals []T) T {
    var sum T
    for _, v := range vals {
        sum += v
    }
    return sum
}
```

### Interfaces & Embedding

```go
// Interface composition
 type Reader interface {
     Read(p []byte) (n int, err error)
 }

 type Writer interface {
     Write(p []byte) (n int, err error)
 }

 type ReadWriter interface {
     Reader
     Writer
 }

// Any (alias for interface{})
 func PrintAny(v any) {
     fmt.Printf("%T: %v\n", v, v)
 }

// Type assertions and switches
 func Describe(v any) string {
     switch val := v.(type) {
     case string:
         return "string: " + val
     case int:
         return fmt.Sprintf("int: %d", val)
     case fmt.Stringer:
         return val.String()
     default:
         return "unknown"
     }
 }
```

---

## 4. Error Handling

### Idiomatic Error Handling

```go
// Sentinel errors
 var ErrNotFound = errors.New("resource not found")
 var ErrInvalidInput = errors.New("invalid input")

// Error wrapping
 func LoadUser(id string) (*User, error) {
     user, err := db.QueryUser(id)
     if err != nil {
         return nil, fmt.Errorf("loading user %s: %w", id, err)
     }
     if user == nil {
         return nil, fmt.Errorf("user %s: %w", id, ErrNotFound)
     }
     return user, nil
 }

// Error checking
 user, err := LoadUser("123")
 if err != nil {
     if errors.Is(err, ErrNotFound) {
         http.Error(w, "Not found", http.StatusNotFound)
         return
     }
     log.Printf("unexpected error: %v", err)
     http.Error(w, "Internal error", http.StatusInternalServerError)
     return
 }

// Error type assertion
 var notFound *NotFoundError
 if errors.As(err, &notFound) {
     fmt.Printf("Resource type: %s, ID: %s\n", notFound.Resource, notFound.ID)
 }
```

### Custom Error Types

```go
 type NotFoundError struct {
     Resource string
     ID       string
 }

 func (e *NotFoundError) Error() string {
     return fmt.Sprintf("%s %s not found", e.Resource, e.ID)
 }

// Validation errors with multiple fields
 type ValidationError struct {
     Field   string
     Message string
 }

 type ValidationErrors []ValidationError

 func (v ValidationErrors) Error() string {
     var msgs []string
     for _, e := range v {
         msgs = append(msgs, fmt.Sprintf("%s: %s", e.Field, e.Message))
     }
     return "validation failed: " + strings.Join(msgs, "; ")
 }
```

---

## 5. Concurrency

### Goroutines & Channels

```go
// Basic goroutine
 go func() {
     fmt.Println("running concurrently")
 }()

// Buffered channel
 ch := make(chan int, 10)
 go func() {
     for i := range 5 {
         ch <- i
     }
     close(ch)
 }()

 for v := range ch {
     fmt.Println(v)
 }

// Select for multiplexing
 select {
 case v := <-ch1:
     fmt.Println("from ch1:", v)
 case v := <-ch2:
     fmt.Println("from ch2:", v)
 case <-time.After(5 * time.Second):
     fmt.Println("timeout")
 default:
     fmt.Println("no channel ready")
 }
```

### Context — Request Scoping & Cancellation

```go
// Create context with timeout
 ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
 defer cancel()

// Pass through call chain
 func ProcessRequest(ctx context.Context, req Request) (*Response, error) {
     // Check cancellation
     select {
     case <-ctx.Done():
         return nil, ctx.Err()  // context.DeadlineExceeded or context.Canceled
     default:
     }

     // Pass to downstream
     user, err := userService.Get(ctx, req.UserID)
     if err != nil {
         return nil, err
     }
     // ...
 }

// Context with values (request-scoped metadata)
 type contextKey string
 const requestIDKey contextKey = "request-id"

 func WithRequestID(ctx context.Context, id string) context.Context {
     return context.WithValue(ctx, requestIDKey, id)
 }

 func RequestIDFrom(ctx context.Context) string {
     if id, ok := ctx.Value(requestIDKey).(string); ok {
         return id
     }
     return ""
 }
```

### sync Package Patterns

```go
// WaitGroup for goroutine synchronization
 var wg sync.WaitGroup
 for i := range 3 {
     wg.Add(1)
     go func(id int) {
         defer wg.Done()
         fmt.Printf("worker %d done\n", id)
     }(i)
 }
 wg.Wait()

// Mutex for shared state
 type Counter struct {
     mu    sync.Mutex
     count int
 }

 func (c *Counter) Inc() {
     c.mu.Lock()
     defer c.mu.Unlock()
     c.count++
 }

// RWMutex for read-heavy workloads
 type Cache struct {
     mu    sync.RWMutex
     data  map[string]string
 }

 func (c *Cache) Get(key string) (string, bool) {
     c.mu.RLock()
     defer c.mu.RUnlock()
     v, ok := c.data[key]
     return v, ok
 }

 func (c *Cache) Set(key, value string) {
     c.mu.Lock()
     defer c.mu.Unlock()
     c.data[key] = value
 }

// sync.Once for one-time initialization
 var (
     db     *sql.DB
     dbOnce sync.Once
 )

 func GetDB() *sql.DB {
     dbOnce.Do(func() {
         var err error
         db, err = sql.Open("postgres", dsn)
         if err != nil {
             log.Fatal(err)
         }
     })
     return db
 }

// sync.Map for concurrent map (rarely needed, prefer RWMutex)
 var m sync.Map
 m.Store("key", "value")
 if v, ok := m.Load("key"); ok {
     fmt.Println(v)
 }
```

### errgroup — Concurrent Error Handling

```go
 import "golang.org/x/sync/errgroup"

 func ProcessBatch(ctx context.Context, items []Item) error {
     g, ctx := errgroup.WithContext(ctx)
     g.SetLimit(10)  // max concurrent

     for _, item := range items {
         item := item  // capture loop variable (pre-1.22)
         g.Go(func() error {
             return processItem(ctx, item)
         })
     }

     if err := g.Wait(); err != nil {
         return fmt.Errorf("batch processing: %w", err)
     }
     return nil
 }
```

### Worker Pools

```go
 func WorkerPool(ctx context.Context, jobs <-chan Job, numWorkers int) <-chan Result {
     results := make(chan Result, numWorkers)

     var wg sync.WaitGroup
     for range numWorkers {
         wg.Add(1)
         go func() {
             defer wg.Done()
             for job := range jobs {
                 select {
                 case <-ctx.Done():
                     return
                 default:
                     results <- process(job)
                 }
             }
         }()
     }

     go func() {
         wg.Wait()
         close(results)
     }()

     return results
 }
```

---

## 6. Testing

### Table-Driven Tests

```go
 func TestCalculate(t *testing.T) {
     tests := []struct {
         name     string
         a, b     int
         op       string
         expected int
         wantErr  bool
     }{
         {"add", 2, 3, "+", 5, false},
         {"subtract", 5, 3, "-", 2, false},
         {"divide by zero", 5, 0, "/", 0, true},
     }

     for _, tt := range tests {
         t.Run(tt.name, func(t *testing.T) {
             got, err := Calculate(tt.a, tt.b, tt.op)
             if tt.wantErr {
                 if err == nil {
                     t.Errorf("expected error, got nil")
                 }
                 return
             }
             if err != nil {
                 t.Errorf("unexpected error: %v", err)
                 return
             }
             if got != tt.expected {
                 t.Errorf("Calculate(%d, %d, %q) = %d, want %d",
                     tt.a, tt.b, tt.op, got, tt.expected)
             }
         })
     }
 }
```

### testify — Assertions & Mocks

```go
 import "github.com/stretchr/testify/assert"
 import "github.com/stretchr/testify/require"
 import "github.com/stretchr/testify/mock"

 func TestSomething(t *testing.T) {
     // Assert continues on failure
     assert.Equal(t, 42, result)
     assert.NoError(t, err)

     // Require stops test on failure
     require.NotNil(t, obj)
     require.NoError(t, err)

     // Now safe to use obj
     assert.Equal(t, "expected", obj.Name)
 }

// Mock with testify/mock
 type MockRepository struct {
     mock.Mock
 }

 func (m *MockRepository) GetUser(id string) (*User, error) {
     args := m.Called(id)
     if args.Get(0) == nil {
         return nil, args.Error(1)
     }
     return args.Get(0).(*User), args.Error(1)
 }

 func TestService(t *testing.T) {
     repo := new(MockRepository)
     repo.On("GetUser", "123").Return(&User{ID: "123", Name: "Alice"}, nil)

     svc := NewService(repo)
     user, err := svc.GetUser("123")

     require.NoError(t, err)
     assert.Equal(t, "Alice", user.Name)
     repo.AssertExpectations(t)
 }
```

### Fuzzing (Go 1.18+)

```go
 func FuzzParse(f *testing.F) {
     // Seed corpus
     f.Add("hello")
     f.Add("12345")

     f.Fuzz(func(t *testing.T, input string) {
         result, err := Parse(input)
         if err != nil {
             t.Skip()  // invalid input is ok
         }
         // Invariant: result must be valid
         if result.Len() < 0 {
             t.Errorf("negative length: %d", result.Len())
         }
     })
 }
```

```bash
go test -fuzz=FuzzParse -fuzztime=30s ./...
```

### Benchmarks

```go
 func BenchmarkProcess(b *testing.B) {
     data := generateLargeDataset()
     b.ResetTimer()
     for range b.N {
         Process(data)
     }
 }

// Memory allocation benchmark
 func BenchmarkAlloc(b *testing.B) {
     b.ReportAllocs()
     for range b.N {
         _ = make([]byte, 1024)
     }
 }
```

```bash
go test -bench=. -benchmem ./...
```

### Integration Tests

```go
//go:build integration

 func TestDatabase(t *testing.T) {
     if testing.Short() {
         t.Skip("skipping integration test")
     }

     db := setupTestDB(t)
     defer teardownTestDB(t, db)

     // Run tests against real database
 }
```

```bash
go test -tags=integration ./...
go test -short ./...          # skip integration
```

---

## 7. HTTP Servers

### Standard Library (`net/http`)

```go
 package main

 import (
     "encoding/json"
     "log"
     "net/http"
     "time"
 )

 type Handler struct {
     service Service
 }

 func (h *Handler) GetUser(w http.ResponseWriter, r *http.Request) {
     id := r.PathValue("id")  // Go 1.22+ path values

     user, err := h.service.GetUser(r.Context(), id)
     if err != nil {
         if errors.Is(err, ErrNotFound) {
             http.Error(w, "Not found", http.StatusNotFound)
             return
         }
         log.Printf("error: %v", err)
         http.Error(w, "Internal error", http.StatusInternalServerError)
         return
     }

     w.Header().Set("Content-Type", "application/json")
     json.NewEncoder(w).Encode(user)
 }

 func main() {
     mux := http.NewServeMux()
     h := &Handler{service: NewService()}

     // Go 1.22+ routing
     mux.HandleFunc("GET /users/{id}", h.GetUser)
     mux.HandleFunc("POST /users", h.CreateUser)
     mux.HandleFunc("GET /users", h.ListUsers)

     server := &http.Server{
         Addr:         ":8080",
         Handler:      mux,
         ReadTimeout:  5 * time.Second,
         WriteTimeout: 10 * time.Second,
         IdleTimeout:  120 * time.Second,
     }

     log.Println("Server starting on :8080")
     if err := server.ListenAndServe(); err != nil {
         log.Fatal(err)
     }
 }
```

### Chi Router

```go
 import "github.com/go-chi/chi/v5"
 import "github.com/go-chi/chi/v5/middleware"

 r := chi.NewRouter()
 r.Use(middleware.Logger)
 r.Use(middleware.Recoverer)
 r.Use(middleware.RequestID)
 r.Use(middleware.Timeout(30 * time.Second))

 r.Route("/api/v1", func(r chi.Router) {
     r.Use(authMiddleware)

     r.Get("/users", listUsers)
     r.Post("/users", createUser)
     r.Get("/users/{id}", getUser)
     r.Put("/users/{id}", updateUser)
     r.Delete("/users/{id}", deleteUser)
 })

 http.ListenAndServe(":8080", r)
```

### Gin

```go
 import "github.com/gin-gonic/gin"

 r := gin.Default()

 r.GET("/users/:id", func(c *gin.Context) {
     id := c.Param("id")
     user, err := service.GetUser(c.Request.Context(), id)
     if err != nil {
         if errors.Is(err, ErrNotFound) {
             c.JSON(404, gin.H{"error": "not found"})
             return
         }
         c.JSON(500, gin.H{"error": "internal error"})
         return
     }
     c.JSON(200, user)
 })

 r.POST("/users", func(c *gin.Context) {
     var req CreateUserRequest
     if err := c.ShouldBindJSON(&req); err != nil {
         c.JSON(400, gin.H{"error": err.Error()})
         return
     }
     user, err := service.CreateUser(c.Request.Context(), req)
     if err != nil {
         c.JSON(500, gin.H{"error": err.Error()})
         return
     }
     c.JSON(201, user)
 })

 r.Run(":8080")
```

### Middleware Patterns

```go
// Logging middleware
 func LoggingMiddleware(next http.Handler) http.Handler {
     return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
         start := time.Now()
         next.ServeHTTP(w, r)
         log.Printf("%s %s %v", r.Method, r.URL.Path, time.Since(start))
     })
 }

// Authentication middleware
 func AuthMiddleware(next http.Handler) http.Handler {
     return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
         token := r.Header.Get("Authorization")
         if token == "" {
             http.Error(w, "Unauthorized", http.StatusUnauthorized)
             return
         }
         user, err := validateToken(token)
         if err != nil {
             http.Error(w, "Unauthorized", http.StatusUnauthorized)
             return
         }
         ctx := context.WithValue(r.Context(), userKey, user)
         next.ServeHTTP(w, r.WithContext(ctx))
     })
 }

// Recovery middleware
 func RecoveryMiddleware(next http.Handler) http.Handler {
     return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
         defer func() {
             if rec := recover(); rec != nil {
                 log.Printf("panic: %v\n%s", rec, debug.Stack())
                 http.Error(w, "Internal error", http.StatusInternalServerError)
             }
         }()
         next.ServeHTTP(w, r)
     })
 }
```

---

## 8. gRPC & Protocol Buffers

### Protobuf Definition

```protobuf
// api/proto/user.proto
syntax = "proto3";
package user;
option go_package = "github.com/example/myapp/api/proto/user";

service UserService {
  rpc GetUser(GetUserRequest) returns (User);
  rpc ListUsers(ListUsersRequest) returns (ListUsersResponse);
  rpc CreateUser(CreateUserRequest) returns (User);
  rpc StreamUsers(StreamUsersRequest) returns (stream User);
}

message User {
  string id = 1;
  string name = 2;
  string email = 3;
  int64 created_at = 4;
}

message GetUserRequest {
  string id = 1;
}

message ListUsersRequest {
  int32 page = 1;
  int32 page_size = 2;
}

message ListUsersResponse {
  repeated User users = 1;
  int32 total = 2;
}
```

### Server Implementation

```go
 package main

 import (
     "context"
     "log"
     "net"

     "google.golang.org/grpc"
     "google.golang.org/grpc/codes"
     "google.golang.org/grpc/status"
     pb "github.com/example/myapp/api/proto/user"
 )

 type userServer struct {
     pb.UnimplementedUserServiceServer
     service UserService
 }

 func (s *userServer) GetUser(ctx context.Context, req *pb.GetUserRequest) (*pb.User, error) {
     user, err := s.service.GetUser(ctx, req.Id)
     if err != nil {
         if errors.Is(err, ErrNotFound) {
             return nil, status.Errorf(codes.NotFound, "user not found: %s", req.Id)
         }
         return nil, status.Errorf(codes.Internal, "internal error: %v", err)
     }
     return &pb.User{
         Id:        user.ID,
         Name:      user.Name,
         Email:     user.Email,
         CreatedAt: user.CreatedAt.Unix(),
     }, nil
 }

 func main() {
     lis, err := net.Listen("tcp", ":50051")
     if err != nil {
         log.Fatalf("failed to listen: %v", err)
     }

     s := grpc.NewServer(
         grpc.UnaryInterceptor(loggingInterceptor),
     )
     pb.RegisterUserServiceServer(s, &userServer{service: NewService()})

     log.Println("gRPC server starting on :50051")
     if err := s.Serve(lis); err != nil {
         log.Fatalf("failed to serve: %v", err)
     }
 }
```

### Interceptors (Middleware)

```go
 func loggingInterceptor(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {
     start := time.Now()
     resp, err := handler(ctx, req)
     log.Printf("gRPC %s duration=%v error=%v", info.FullMethod, time.Since(start), err)
     return resp, err
 }

 func authInterceptor(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {
     md, ok := metadata.FromIncomingContext(ctx)
     if !ok {
         return nil, status.Errorf(codes.Unauthenticated, "missing metadata")
     }
     token := md.Get("authorization")
     if len(token) == 0 {
         return nil, status.Errorf(codes.Unauthenticated, "missing token")
     }
     // validate token...
     return handler(ctx, req)
 }
```

---

## 9. Database Access

### database/sql with pgx

```go
 import "github.com/jackc/pgx/v5/pgxpool"

 type UserRepository struct {
     pool *pgxpool.Pool
 }

 func NewUserRepository(ctx context.Context, dsn string) (*UserRepository, error) {
     pool, err := pgxpool.New(ctx, dsn)
     if err != nil {
         return nil, fmt.Errorf("creating connection pool: %w", err)
     }
     return &UserRepository{pool: pool}, nil
 }

 func (r *UserRepository) GetByID(ctx context.Context, id string) (*User, error) {
     var user User
     err := r.pool.QueryRow(ctx, `
         SELECT id, name, email, created_at
         FROM users
         WHERE id = $1
     `, id).Scan(&user.ID, &user.Name, &user.Email, &user.CreatedAt)

     if err != nil {
         if errors.Is(err, pgx.ErrNoRows) {
             return nil, ErrNotFound
         }
         return nil, fmt.Errorf("querying user: %w", err)
     }
     return &user, nil
 }

 func (r *UserRepository) Create(ctx context.Context, user *User) error {
     _, err := r.pool.Exec(ctx, `
         INSERT INTO users (id, name, email, created_at)
         VALUES ($1, $2, $3, $4)
     `, user.ID, user.Name, user.Email, user.CreatedAt)
     if err != nil {
         return fmt.Errorf("inserting user: %w", err)
     }
     return nil
 }

// Transaction
 func (r *UserRepository) Transfer(ctx context.Context, from, to string, amount int64) error {
     tx, err := r.pool.Begin(ctx)
     if err != nil {
         return err
     }
     defer tx.Rollback(ctx)

     _, err = tx.Exec(ctx, "UPDATE accounts SET balance = balance - $1 WHERE id = $2", amount, from)
     if err != nil {
         return err
     }

     _, err = tx.Exec(ctx, "UPDATE accounts SET balance = balance + $1 WHERE id = $2", amount, to)
     if err != nil {
         return err
     }

     return tx.Commit(ctx)
 }
```

### sqlx — Struct Scanning

```go
 import "github.com/jmoiron/sqlx"

 type User struct {
     ID        string    `db:"id"`
     Name      string    `db:"name"`
     Email     string    `db:"email"`
     CreatedAt time.Time `db:"created_at"`
 }

 func (r *UserRepository) ListUsers(ctx context.Context) ([]User, error) {
     var users []User
     err := r.db.SelectContext(ctx, &users, "SELECT * FROM users ORDER BY created_at DESC")
     if err != nil {
         return nil, err
     }
     return users, nil
 }
```

### GORM

```go
 import "gorm.io/gorm"
 import "gorm.io/driver/postgres"

 type User struct {
     gorm.Model
     Name  string `gorm:"size:255;not null"`
     Email string `gorm:"size:255;uniqueIndex;not null"`
 }

 db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
 if err != nil {
     log.Fatal(err)
 }

// Auto migrate
 db.AutoMigrate(&User{})

// CRUD
 db.Create(&User{Name: "Alice", Email: "alice@example.com"})

 var user User
 db.First(&user, "email = ?", "alice@example.com")

 db.Model(&user).Update("Name", "Alice Smith")

 db.Delete(&user)
```

### Migrations (golang-migrate)

```bash
# Install
 go install -tags 'postgres' github.com/golang-migrate/migrate/v4/cmd/migrate@latest

# Create migration
 migrate create -ext sql -dir migrations -seq create_users_table

# Run migrations
 migrate -database "postgres://user:pass@localhost/db?sslmode=disable" -path migrations up

# Rollback
 migrate -database "postgres://user:pass@localhost/db?sslmode=disable" -path migrations down
```

```sql
-- migrations/000001_create_users_table.up.sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- migrations/000001_create_users_table.down.sql
DROP TABLE users;
```

---

## 10. CLI Tools

### Cobra (Recommended)

```go
 package main

 import (
     "fmt"
     "github.com/spf13/cobra"
 )

 var rootCmd = &cobra.Command{
     Use:   "myapp",
     Short: "My application CLI",
 }

 var serveCmd = &cobra.Command{
     Use:   "serve",
     Short: "Start the HTTP server",
     RunE: func(cmd *cobra.Command, args []string) error {
         port, _ := cmd.Flags().GetString("port")
         fmt.Printf("Starting server on port %s\n", port)
         return runServer(port)
     },
 }

 var migrateCmd = &cobra.Command{
     Use:   "migrate [up|down]",
     Short: "Run database migrations",
     Args:  cobra.ExactArgs(1),
     RunE: func(cmd *cobra.Command, args []string) error {
         direction := args[0]
         return runMigrations(direction)
     },
 }

 func init() {
     serveCmd.Flags().StringP("port", "p", "8080", "Server port")
     rootCmd.AddCommand(serveCmd)
     rootCmd.AddCommand(migrateCmd)
 }

 func main() {
     if err := rootCmd.Execute(); err != nil {
         fmt.Println(err)
     }
 }
```

### Viper — Configuration

```go
 import "github.com/spf13/viper"

 func LoadConfig() (*Config, error) {
     viper.SetConfigName("config")
     viper.SetConfigType("yaml")
     viper.AddConfigPath(".")
     viper.AddConfigPath("$HOME/.myapp")

     // Environment variables
     viper.SetEnvPrefix("MYAPP")
     viper.AutomaticEnv()

     // Defaults
     viper.SetDefault("server.port", "8080")
     viper.SetDefault("server.timeout", 30)
     viper.SetDefault("database.max_connections", 10)

     if err := viper.ReadInConfig(); err != nil {
         return nil, err
     }

     var cfg Config
     if err := viper.Unmarshal(&cfg); err != nil {
         return nil, err
     }
     return &cfg, nil
 }
```

---

## 11. Linting & Static Analysis

### golangci-lint (Standard)

```yaml
# .golangci.yml
run:
  timeout: 5m
  go: "1.23"

linters:
  enable:
    - errcheck      # unchecked errors
    - gosimple      # simplify code
    - govet         # suspicious constructs
    - ineffassign   # ineffectual assignments
    - staticcheck   # static analysis
    - unused        # unused code
    - gocritic      # style and performance
    - gosec         # security issues
    - misspell      # spelling mistakes
    - revive        # fast linter framework
    - errname       # sentinel error naming

linters-settings:
  gocritic:
    enabled-tags:
      - performance
      - style
      - experimental
  gosec:
    excludes:
      - G104  # unchecked errors (covered by errcheck)

issues:
  exclude-use-default: false
```

```bash
# Install
go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest

# Run
golangci-lint run ./...
golangci-lint run --fix ./...    # auto-fix where possible
```

### go vet & staticcheck

```bash
go vet ./...                     # built-in analysis
staticcheck ./...                # advanced static analysis
```

### Pre-commit

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/golangci/golangci-lint
    rev: v1.62.0
    hooks:
      - id: golangci-lint
        args: [--fast]

  - repo: local
    hooks:
      - id: go-fmt
        name: go fmt
        entry: gofmt -w
        language: system
        types: [go]

      - id: go-mod-tidy
        name: go mod tidy
        entry: go mod tidy
        language: system
        pass_filenames: false
```

---

## 12. Structured Logging

### slog (Standard Library, Go 1.21+)

```go
 import "log/slog"
 import "os"

 func setupLogger() *slog.Logger {
     opts := &slog.HandlerOptions{
         Level:     slog.LevelInfo,
         AddSource: true,
     }

     var handler slog.Handler
     if os.Getenv("ENV") == "production" {
         handler = slog.NewJSONHandler(os.Stdout, opts)
     } else {
         handler = slog.NewTextHandler(os.Stdout, opts)
     }

     return slog.New(handler)
 }

 var logger = setupLogger()

// Usage
 logger.Info("user_created",
     slog.String("user_id", user.ID),
     slog.String("email", user.Email),
     slog.Duration("duration", time.Since(start)),
 )

 logger.Error("database_query_failed",
     slog.String("query", query),
     slog.Any("error", err),
 )

// With context (request-scoped)
 func WithRequestID(ctx context.Context, id string) context.Context {
     return slog.With("request_id", id).Context(ctx)
 }
```

### zap (High Performance)

```go
 import "go.uber.org/zap"

 func setupZap() *zap.Logger {
     var cfg zap.Config
     if os.Getenv("ENV") == "production" {
         cfg = zap.NewProductionConfig()
     } else {
         cfg = zap.NewDevelopmentConfig()
     }
     logger, _ := cfg.Build()
     return logger
 }

 logger.Info("request processed",
     zap.String("method", r.Method),
     zap.String("path", r.URL.Path),
     zap.Duration("latency", duration),
     zap.Int("status", status),
 )
```

---

## 13. Docker for Go

### Multi-Stage Dockerfile

```dockerfile
# Build stage
FROM golang:1.23-alpine AS builder

RUN apk add --no-cache git ca-certificates tzdata

WORKDIR /app

# Cache dependencies
COPY go.mod go.sum ./
RUN go mod download

# Build
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-w -s" -o /bin/api ./cmd/api

# Runtime stage — distroless for minimal attack surface
FROM gcr.io/distroless/static-debian12:nonroot

COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /usr/share/zoneinfo /usr/share/zoneinfo
COPY --from=builder /bin/api /api

USER nonroot:nonroot
EXPOSE 8080

ENTRYPOINT ["/api"]
```

**Alternative runtime images:**
- `gcr.io/distroless/static` — smallest, no shell
- `alpine:latest` — small, has shell for debugging
- `chainguard/static` — hardened, minimal

### .dockerignore

```
*.md
*.git
*.gitignore
Dockerfile*
docker-compose*
.env
.env.*
bin/
dist/
tmp/
*.test
*.out
coverage/
```

---

## 14. Observability

### OpenTelemetry

```go
 import (
     "go.opentelemetry.io/otel"
     "go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc"
     "go.opentelemetry.io/otel/sdk/resource"
     sdktrace "go.opentelemetry.io/otel/sdk/trace"
     semconv "go.opentelemetry.io/otel/semconv/v1.26.0"
 )

 func initTracer() (*sdktrace.TracerProvider, error) {
     exporter, err := otlptracegrpc.New(context.Background(),
         otlptracegrpc.WithEndpoint("otel-collector:4317"),
         otlptracegrpc.WithInsecure(),
     )
     if err != nil {
         return nil, err
     }

     tp := sdktrace.NewTracerProvider(
         sdktrace.WithBatcher(exporter),
         sdktrace.WithResource(resource.NewWithAttributes(
             semconv.SchemaURL,
             semconv.ServiceName("myapp"),
             semconv.ServiceVersion("1.0.0"),
         )),
     )
     otel.SetTracerProvider(tp)
     return tp, nil
 }

// Usage
 tracer := otel.Tracer("myapp")
 ctx, span := tracer.Start(ctx, "process_order")
 defer span.End()

 span.SetAttributes(
     attribute.String("order.id", orderID),
     attribute.Float64("order.total", total),
 )

 if err != nil {
     span.RecordError(err)
     span.SetStatus(codes.Error, err.Error())
 }
```

### Metrics (Prometheus)

```go
 import "github.com/prometheus/client_golang/prometheus"
 import "github.com/prometheus/client_golang/prometheus/promhttp"

 var (
     requestDuration = prometheus.NewHistogramVec(
         prometheus.HistogramOpts{
             Name:    "http_request_duration_seconds",
             Help:    "HTTP request duration",
             Buckets: prometheus.DefBuckets,
         },
         []string{"method", "path", "status"},
     )

     requestCount = prometheus.NewCounterVec(
         prometheus.CounterOpts{
             Name: "http_requests_total",
             Help: "Total HTTP requests",
         },
         []string{"method", "path", "status"},
     )
 )

 func init() {
     prometheus.MustRegister(requestDuration, requestCount)
 }

// Middleware
 func MetricsMiddleware(next http.Handler) http.Handler {
     return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
         start := time.Now()
         rw := &responseWriter{ResponseWriter: w, statusCode: 200}
         next.ServeHTTP(rw, r)
         duration := time.Since(start).Seconds()

         labels := prometheus.Labels{
             "method": r.Method,
             "path":   r.URL.Path,
             "status": strconv.Itoa(rw.statusCode),
         }
         requestDuration.With(labels).Observe(duration)
         requestCount.With(labels).Inc()
     })
 }

// Expose metrics endpoint
 http.Handle("/metrics", promhttp.Handler())
```

---

## 15. Integration with Other Skills

| This skill provides | Related skill | For deeper dive |
|---|---|---|
| HTTP/gRPC patterns | `security-analysis` | OWASP, auth, rate limiting |
| Domain modeling | `ddd-tactical` | Aggregates, Entities, Value Objects |
| Project structure | `c4-level3-component` | Folder mapping, dependency boundaries |
| Docker patterns | `docker-containerization` | Multi-stage builds, compose |
| K8s deployment | `kubernetes-orchestration` | Manifests, HPA, probes |
| Database design | `c4-level4-code` | ER diagrams, schema design |
| Testing patterns | `evolutionary-architecture` | Fitness functions, architecture tests |
| CLI tools | `python-development` | Typer for Python equivalents |

---

## References

- [Go Documentation](https://go.dev/doc/)
- [Effective Go](https://go.dev/doc/effective_go)
- [Go Proverbs](https://go-proverbs.github.io/)
- [Go Modules Reference](https://go.dev/ref/mod)
- [Go Wiki: CodeReviewComments](https://github.com/golang/go/wiki/CodeReviewComments)
- [golangci-lint Documentation](https://golangci-lint.run/)
- [gRPC Go Documentation](https://grpc.io/docs/languages/go/)
- [Cobra Documentation](https://github.com/spf13/cobra)
- [pgx Documentation](https://github.com/jackc/pgx)
