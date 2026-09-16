# Cheat Sheet

```bash
# compile / run
gcc q1.1.c -o q1.1
./q1.1

# process tree / zombie check
ps -ef
ps -ef | grep -E 'q2|defunct' | grep -v grep

# limit process count before fork test
ulimit -u 500
./q3
```

```c
// fork
pid_t rc = fork();

if (rc < 0) {
    perror("fork");
    exit(1);
}
else if (rc == 0) {
    // child
}
else {
    // parent, rc = child PID
}
```

```c
// wait for child
#include <sys/wait.h>
wait(NULL);
```

```c
// pipe
int fd[2];
pipe(fd);

fd[0]; // read end
fd[1]; // write end
```

```c
// write
write(fd[1], msg, len);

// read
ssize_t n = read(fd[0], buf, sizeof(buf) - 1);
buf[n] = '\0';
```

```c
// sender
close(fd[0]);
write(fd[1], msg, len);
close(fd[1]);

// receiver
close(fd[1]);
read(fd[0], buf, size);
close(fd[0]);
```

---

# Process / Fork / Pipe

## 1. `fork()`

`fork()` duplicates the current process.

```c
pid_t rc = fork();
```

Return value:

- `rc < 0` = fork failed
- `rc == 0` = child process
- `rc > 0` = parent process, `rc` = child PID

Without `wait()`, parent and child have **no guaranteed execution order**.

```text
fork()
├── parent
└── child
```

## 2. `wait()`

```c
int wc = wait(NULL);
```

- Parent blocks until one child finishes
- Returns PID of the child that was collected
- Used to control ordering + reap finished children

```text
child finishes
      ↓
parent wait() returns
      ↓
parent continues
```

## 3. Zombie Process

**Zombie** = child already exited, but parent has not called `wait()` yet.

```text
parent alive
   └── child exited → <defunct>
```

Example pattern:

```c
if (rc == 0) {
    exit(0);       // child dies immediately
}
else {
    sleep(30);     // parent does not wait yet
    wait(NULL);    // reap zombie
}
```

Before `wait()`:

```bash
ps -ef | grep defunct
```

After `wait()` → zombie disappears.

## 4. Orphan Process

**Orphan** = parent exits while child is still running.

```text
parent exits
   └── child still alive → re-parented
```

```c
if (rc == 0) {
    printf("before: PPID=%d\n", getppid());
    sleep(5);
    printf("after:  PPID=%d\n", getppid());
}
else {
    exit(0);
}
```

Child keeps running after parent exits; its parent changes to another system process.

## 5. Process Limit / Fork Chain

To test how many processes can be created, make only the **newest child fork again**.

```text
P0
 └── P1
      └── P2
           └── P3
                ...
```

Do **not** use:

```c
while (1) fork();
```

Every child continues the loop → exponential growth / fork bomb.

Safer pattern:

```c
void fork_chain(int depth) {
    int rc = fork();

    if (rc < 0) {
        printf("successful forks: %d\n", depth);
        return;
    }
    else if (rc == 0) {
        fork_chain(depth + 1);
        exit(0);
    }
    else {
        wait(NULL);
    }
}
```

Before testing:

```bash
ulimit -u 500
./q3
```

The experiment reached about `459` successful forks; available count decreases when other processes are already running.

## 6. `pipe()`

`pipe()` creates a kernel byte stream for communication between processes.

```c
int fd[2];
pipe(fd);
```

- `fd[0]` = read end
- `fd[1]` = write end

Create the pipe **before `fork()`** so parent and child inherit descriptors for the same pipe.

```text
child                    kernel pipe                    parent
write(fd[1])  ───────►  [ byte stream ]  ───────►  read(fd[0])
```

## 7. Close Unused Pipe Ends

Typical child sender / parent receiver:

```text
Child                    Parent
fd[0] CLOSED             fd[1] CLOSED
fd[1] WRITE   ───────►   fd[0] READ
```

Why close unused ends?

- prevents accidental read/write
- lets kernel know when no writers remain
- allows `read()` to eventually return EOF

## 8. `read()` Behavior

```c
ssize_t n = read(fd[0], buf, sizeof(buf) - 1);
```

- `n > 0` → received `n` bytes
- `n == 0` → EOF, all write ends are closed
- `n < 0` → error

If pipe is empty but some writer is still open:

```text
read() → BLOCK
```

If data later arrives:

```text
BLOCK → data arrives → read() returns
```

If every writer closes without sending:

```text
read() → 0 (EOF)
```

## 9. Pipe Has No Message Boundary

Pipe stores a **byte stream**, not separate messages.

```c
write(fd[1], "Cat", 3);
write(fd[1], "Dog", 3);
```

Receiver may see:

```text
CatDog
```

One `read()` does not mean one `write()`.

Use your own boundary/protocol, e.g.

```text
Cat\nDog\n
```

or send a known number of bytes.

## 10. Reading Removes Data

Reading consumes bytes from the pipe.

```text
pipe = "CatDog"

reader A reads "Cat"
pipe = "Dog"

reader B can only read "Dog"
```

If sender keeps `fd[0]` open, it can read from the same pipe and may consume its own data before the parent gets it.

---

# C Writing Patterns

## 1. Basic Child Process

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void) {
    pid_t rc = fork();

    if (rc < 0) {
        perror("fork");
        exit(1);
    }
    else if (rc == 0) {
        printf("child pid=%d ppid=%d\n", getpid(), getppid());
    }
    else {
        printf("parent pid=%d child=%d\n", getpid(), rc);
    }

    return 0;
}
```

Pattern to remember:

```text
fork
 ↓
check error
 ↓
rc == 0 ? child : parent
```

## 2. Parent Waits for Child

```c
#include <sys/wait.h>

pid_t rc = fork();

if (rc == 0) {
    // child work
    exit(0);
}
else if (rc > 0) {
    wait(NULL);
    // parent continues AFTER child
}
```

## 3. Child → Parent Pipe

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

#define BUFSIZE 128

int main(void) {
    int fd[2];
    if (pipe(fd) < 0) {
        perror("pipe");
        exit(1);
    }

    pid_t rc = fork();
    if (rc < 0) {
        perror("fork");
        exit(1);
    }

    if (rc == 0) {
        // child = sender
        close(fd[0]);

        char msg[] = "hello parent";
        write(fd[1], msg, sizeof(msg) - 1);

        close(fd[1]);
        exit(0);
    }
    else {
        // parent = receiver
        close(fd[1]);

        char buf[BUFSIZE];
        ssize_t n = read(fd[0], buf, sizeof(buf) - 1);

        if (n > 0) {
            buf[n] = '\0';
            printf("received: %s\n", buf);
        }

        close(fd[0]);
        wait(NULL);
    }

    return 0;
}
```

Memory shortcut:

```text
pipe → fork → close unused end → write/read → close → wait
```

## 4. Send PID / Formatted Data

Build message first:

```c
char msg[128];
int len = snprintf(msg, sizeof(msg),
                   "Hello from PID %d", getpid());

write(fd[1], msg, len);
```

Receiver:

```c
char buf[128];
ssize_t n = read(fd[0], buf, sizeof(buf) - 1);

if (n > 0) {
    buf[n] = '\0';
    printf("%s\n", buf);
}
```

`read()` does **not** append `\0` automatically.

## 5. Receiver Reads Before Sender

No special code needed.

```c
// child
sleep(5);
write(fd[1], msg, len);

// parent
read(fd[0], buf, size);   // blocks here until data arrives
```

As long as a write end is still open, empty pipe ≠ EOF.

## 6. Send Multiple Messages

```c
for (int i = 1; i <= 3; i++) {
    char msg[128];
    int len = snprintf(msg, sizeof(msg), "[msg %d]", i);
    write(fd[1], msg, len);
}
```

Do not assume:

```text
1 write = 1 read
```

Instead define a protocol:

```c
snprintf(msg, sizeof(msg), "message %d\n", i);
```

Then split by `\n`, or send fixed-size / length-prefixed data.

## 7. Pipe Coding Template

When blanking in exam/lab, write this first:

```c
int fd[2];
pipe(fd);

pid_t rc = fork();

if (rc == 0) {
    // CHILD
    close(fd[0]);

    // write(fd[1], ...);

    close(fd[1]);
    exit(0);
}
else {
    // PARENT
    close(fd[1]);

    // read(fd[0], ...);

    close(fd[0]);
    wait(NULL);
}
```

Then only fill in the actual message / processing logic.

## 8. Common Includes

```c
#include <stdio.h>      // printf, perror
#include <stdlib.h>     // exit
#include <unistd.h>     // fork, pipe, read, write, close, sleep, getpid
#include <sys/wait.h>   // wait
#include <string.h>     // strlen, strerror
#include <errno.h>      // errno
```

---

# Quick Mental Model

```text
fork()  = duplicate process
wait()  = parent waits + collects child
zombie  = child dead, parent has not collected it
orphan  = parent dead, child still running

pipe()  = shared kernel byte stream
fd[0]   = read
fd[1]   = write
close() = tell kernel this process no longer uses that end
read()  = consume bytes
EOF     = all write ends closed
```
