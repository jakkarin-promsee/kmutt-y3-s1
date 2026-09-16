# Cheat Sheet

```bash
# compile / run
gcc PS4.c -o PS4
./PS4

# run 3 times
./PS4
./PS4
./PS4

# compile without PIE
gcc -no-pie -o PS4_nopie PS4.c
./PS4_nopie

# inspect executable type
file PS4
file PS4_nopie
readelf -h PS4 | grep Type
readelf -h PS4_nopie | grep Type
```

```c
// storage class
auto int x = 3;
static int y = 5;
extern int global_x;
register int i;
```

```c
// dynamic memory
int *a = (int *)malloc(10 * sizeof(int));
a = (int *)realloc(a, 1000 * sizeof(int));
free(a);
```

```c
// address meaning
&a;       // address of pointer variable a
a;        // address stored in a
&a[0];    // first allocated element
&a[9];    // element 9

c;        // array base address in most expressions
&c[0];    // first array element
&c[9];    // element 9
```

---

# C Storage Class

## 1. Storage Class

**Storage Class** defines a variable's:

- **Scope** = where the variable name is visible
- **Lifetime** = how long the variable exists
- **Storage location** = where the variable is stored

Storage classes in the material:

- `auto`
- `static`
- `extern`
- `register`

## 2. `auto`

`auto` = default storage class for local variables.

```c
int x = 3;
auto int y = 5;
```

For local variables:

```text
int x = 3;
      ≈
auto int x = 3;
```

Automatic local variable:

- local scope
- created when its block is entered
- lifetime ends when its block is left
- initialization runs again on each block entry

```c
while (x > 0) {
    int y = 5;
    y++;
    printf("%d\n", y);
    x--;
}
```

```text
6
6
6
```

## 3. `static`

`static` local variable = local scope + lifetime for the whole program execution.

```c
static int y = 5;
```

- initialized once
- value persists between repeated block/function entries
- same object remains alive for the process lifetime

```c
while (x > 0) {
    static int y = 5;
    y++;
    printf("%d\n", y);
    x--;
}
```

```text
6
7
8
```

Address inside one run:

```text
iteration 1: &y = A
iteration 2: &y = A
iteration 3: &y = A
```

### `auto` vs `static`

| Property | `auto` local | `static` local |
| --- | --- | --- |
| Scope | local | local |
| Lifetime | current block execution | whole program execution |
| Initialization | every block entry | once |
| Lab values | `6, 6, 6` | `6, 7, 8` |

An automatic variable may reuse the same memory location on later iterations; equal numerical addresses do not imply one continuous lifetime.

## 4. `extern`

`extern` = declaration that refers to an existing variable defined elsewhere.

```c
int x = 20;          // definition

void display(void) {
    extern int x;    // declaration / reference
}
```

```c
int x = 20;
```

- defines the global object
- allocates storage
- initializes `x` to `20`

```c
extern int x;
```

- refers to the existing `x`
- does not create a new local object

If `main()` and `display()` both use `extern int x;`:

```text
main x      = 20
main &x     = A

display x  = 20
display &x = A
```

## 5. Removing `extern` in `main()`

Change:

```c
extern int x;
```

to:

```c
int x;
```

Result:

```text
global x = 20
local  x = uninitialized
```

The local `x`:

- is a new automatic local variable
- shadows the global `x` inside `main()`
- has an uninitialized / indeterminate value

`display()` still uses:

```c
extern int x;
```

so it still refers to the global `x = 20`.

```text
main x      = indeterminate
main &x     = A

display x  = 20
display &x = B

A != B
```

## 6. `register`

`register` = storage class for a local variable intended to be stored in a CPU register instead of RAM.

```c
register int i;
```

---

# Position Independent Executable (PIE)

## 1. PIE

**PIE (Position Independent Executable)** = executable that can be loaded at a different virtual address each time it runs.

PIE uses position-independent / relative addressing instead of fixed absolute addresses.

```text
Run 1: executable base = A
Run 2: executable base = B
Run 3: executable base = C
```

Executable-associated addresses may therefore change between runs.

## 2. Default vs `-no-pie`

Default compile:

```bash
gcc -o program program.c
```

No PIE:

```bash
gcc -no-pie -o program_nopie program.c
```

Check executable type:

```bash
readelf -h program | grep Type
readelf -h program_nopie | grep Type
```

```text
PIE executable      → DYN
non-PIE executable  → EXEC
```

## 3. Static Address Pattern

PIE, separate runs:

```text
Run 1: &y = A
Run 2: &y = B
Run 3: &y = C
```

Same run:

```text
iteration 1: &y = A
iteration 2: &y = A
iteration 3: &y = A
```

With `-no-pie`, executable-associated addresses are normally stable across repeated runs on the same machine.

---

# Pointer / Memory Allocation

## 1. Typical Linux Memory Areas

```text
automatic local variables / local arrays → stack
malloc / realloc allocation             → heap
static / global objects                 → program data area
```

Printed addresses are process **virtual addresses**.

## 2. Pointer Variable vs Stored Address

```c
int *a;
float *b;
```

```text
&a = address of pointer variable a itself
 a = address value stored inside a
```

```text
STACK
+--------------------+
| a = 0x5000         |-----> allocated memory
+--------------------+
  ^
  |
&a = 0x7fff...
```

## 3. Uninitialized Pointer

```c
int *a;
float *b;

printf("%p\n", a);
printf("%p\n", b);
```

Before assignment / `malloc()`:

- `a` and `b` are uninitialized
- stored pointer values are indeterminate
- printed values are not valid allocated target addresses

`&a` and `&b` are still valid addresses of the pointer variables themselves.

## 4. `malloc()`

```c
a = (int *)malloc(10 * sizeof(int));
```

`malloc(size)` = allocate a dynamic memory block of `size` bytes and return its starting address.

Allocation size:

```text
10 * sizeof(int)
```

After successful allocation:

```text
a == &a[0]
```

```c
printf("%p\n", a);
printf("%p\n", &a[0]);
printf("%p\n", &a[9]);
```

For `int *a`:

```text
&a[i] = a + i elements
```

Therefore:

```text
&a[0] = a
&a[9] = a + 9 elements
```

Byte distance:

```text
&a[9] - &a[0] = 9 * sizeof(int) bytes
```

Do not assume `sizeof(int) == 4`; use `sizeof(int)` in the formula.

## 5. Local Array `c`

```c
int c[10];
```

In most expressions, array name `c` decays to a pointer to its first element.

```text
c == &c[0]
```

```c
printf("%p\n", c);
printf("%p\n", &c[0]);
printf("%p\n", &c[9]);
```

```text
c     = &c[0]
&c[9] = c + 9 elements
```

Byte distance:

```text
&c[9] - &c[0] = 9 * sizeof(int) bytes
```

### Dynamic allocation vs local array

| Property | `a = malloc(...)` | `int c[10]` |
| --- | --- | --- |
| Storage | dynamic allocation | automatic local array |
| Base address | `a` | `c` |
| First element | `&a[0]` | `&c[0]` |
| Resize | `realloc()` | no |
| Release | `free(a)` | automatic at block exit |

## 6. `realloc()`

```c
a = (int *)realloc(a, 1000 * sizeof(int));
```

`realloc()` = resize an existing dynamic allocation.

Possible results:

```text
Case 1: grow in place
old a = A
new a = A
```

```text
Case 2: move to a new block
old a = A
new a = B
```

The returned address is not guaranteed to stay the same.

After allocation for `1000` integers:

```text
a       = &a[0]
&a[9]   = a + 9 elements
&a[999] = a + 999 elements
```

```text
&a[999] - &a[0] = 999 * sizeof(int) bytes
allocation size = 1000 * sizeof(int) bytes
```

## 7. Allocating `b` Before `realloc(a)`

Original:

```c
a = (int *)malloc(10 * sizeof(int));
a = (int *)realloc(a, 1000 * sizeof(int));
```

After uncommenting `b`:

```c
a = (int *)malloc(10 * sizeof(int));
b = (float *)malloc(10 * sizeof(float));
a = (int *)realloc(a, 1000 * sizeof(int));
```

Possible heap layout:

```text
[a block][b block][free space ...]
```

`b` changes the heap layout and may prevent `a` from expanding in place.

```text
a may stay at the same address
OR
a may move to a new address
```

Exact behavior depends on the allocator / current memory layout.

## 8. `free()`

```c
free(a);
free(b);
```

`free(ptr)` = release dynamic memory previously allocated by `malloc()` / `realloc()`.

After `free(a)`:

```text
pointer variable a still exists
old allocated block must no longer be accessed through a
```

Common pattern:

```c
free(a);
a = NULL;
```

---
