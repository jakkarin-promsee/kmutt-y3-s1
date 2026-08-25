// 5.1 -- can the sender read back its own message?
//
// Two experiments, each with its own fresh pipe:
//   A) sender closes its read end first (the correct way), then tries to read
//   B) sender keeps its read end open, then reads
// The difference tells you what a pipe actually is.

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/wait.h>

#define BUFSIZE 128

static void experiment(const char *name, int sender_closes_read_end) {

    printf("\n=== %s ===\n", name);

    int fd[2];
    if (pipe(fd) < 0) { perror("pipe"); exit(1); }

    int rc = fork();
    if (rc < 0) { perror("fork"); exit(1); }

    if (rc == 0) {
        // ---------- child = sender ----------
        if (sender_closes_read_end) {
            close(fd[0]);
        }

        char msg[BUFSIZE];
        int len = snprintf(msg, sizeof(msg), "Hello from child PID: %d",
                           (int) getpid());
        write(fd[1], msg, len);
        printf("  child : wrote \"%s\"\n", msg);

        // Now try to read back what we just sent.
        char buf[BUFSIZE];
        ssize_t n = read(fd[0], buf, sizeof(buf) - 1);
        if (n < 0) {
            printf("  child : read() -> -1, errno %d (%s)\n",
                   errno, strerror(errno));
        } else {
            buf[n] = '\0';
            printf("  child : read() -> %zd bytes: \"%s\"   <-- read its OWN message\n",
                   n, buf);
        }

        close(fd[1]);
        exit(0);
    }
    else {
        // ---------- parent = receiver ----------
        close(fd[1]);
        sleep(1);                     // let the child write AND try to read first

        char buf[BUFSIZE];
        ssize_t n = read(fd[0], buf, sizeof(buf) - 1);
        if (n < 0) {
            printf("  parent: read() -> -1, errno %d (%s)\n",
                   errno, strerror(errno));
        } else if (n == 0) {
            printf("  parent: read() -> 0 (EOF)   <-- pipe was empty, child took it\n");
        } else {
            buf[n] = '\0';
            printf("  parent: read() -> %zd bytes: \"%s\"\n", n, buf);
        }

        close(fd[0]);
        wait(NULL);
    }
}

int main(int argc, char *argv[]) {

    setvbuf(stdout, NULL, _IONBF, 0);

    experiment("A: sender CLOSED its read end, then reads", 1);
    experiment("B: sender KEPT its read end open, then reads", 0);

    return 0;
}
