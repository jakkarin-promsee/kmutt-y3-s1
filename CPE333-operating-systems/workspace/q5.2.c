// 5.2 -- what happens when the receiver reads before the sender sends?
//
//   A) sender is slow but WILL send   -> read() blocks until data arrives
//   B) sender closes without sending  -> read() returns 0 (EOF), no blocking
//
// Timestamps are printed so the blocking is measurable, not just claimed.

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <errno.h>
#include <string.h>
#include <sys/wait.h>

#define BUFSIZE 128
#define DELAY   5

static void experiment(const char *name, int sender_actually_sends) {

    printf("\n=== %s ===\n", name);

    int fd[2];
    if (pipe(fd) < 0) { perror("pipe"); exit(1); }

    int rc = fork();
    if (rc < 0) { perror("fork"); exit(1); }

    if (rc == 0) {
        // ---------- child = sender, but a lazy one ----------
        close(fd[0]);
        printf("  child : sleeping %d seconds before doing anything\n", DELAY);
        sleep(DELAY);

        if (sender_actually_sends) {
            char msg[BUFSIZE];
            int len = snprintf(msg, sizeof(msg), "Hello from child PID: %d",
                               (int) getpid());
            write(fd[1], msg, len);
            printf("  child : sent the message now\n");
        } else {
            printf("  child : exiting WITHOUT sending anything\n");
        }

        close(fd[1]);
        exit(0);
    }
    else {
        // ---------- parent = receiver, reads immediately ----------
        close(fd[1]);

        time_t t0 = time(NULL);
        printf("  parent: calling read() immediately -- t = 0s\n");

        char buf[BUFSIZE];
        ssize_t n = read(fd[0], buf, sizeof(buf) - 1);
        long elapsed = (long) (time(NULL) - t0);

        if (n < 0) {
            printf("  parent: read() -> -1, errno %d (%s) after %lds\n",
                   errno, strerror(errno), elapsed);
        } else if (n == 0) {
            printf("  parent: read() -> 0 (EOF) after %lds"
                   "  <-- all write ends closed, so no blocking\n", elapsed);
        } else {
            buf[n] = '\0';
            printf("  parent: read() -> \"%s\" after %lds"
                   "  <-- it was BLOCKED the whole time\n", buf, elapsed);
        }

        close(fd[0]);
        wait(NULL);
    }
}

int main(int argc, char *argv[]) {

    setvbuf(stdout, NULL, _IONBF, 0);

    experiment("A: receiver reads first, sender sends 5s later", 1);
    experiment("B: receiver reads first, sender never sends",    0);

    return 0;
}
