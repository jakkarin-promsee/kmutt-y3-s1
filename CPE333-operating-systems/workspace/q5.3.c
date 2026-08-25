// 5.3 -- sender writes several messages before the receiver reads once.
//
// The child does three separate write() calls. The parent sleeps, then does a
// SINGLE read(). If a pipe kept message boundaries, the first read() would
// return only message 1. It does not.

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

#define BUFSIZE 256
#define NMSG    3

int main(int argc, char *argv[]) {

    setvbuf(stdout, NULL, _IONBF, 0);

    int fd[2];
    if (pipe(fd) < 0) { perror("pipe"); exit(1); }

    int rc = fork();
    if (rc < 0) { perror("fork"); exit(1); }

    if (rc == 0) {
        // ---------- child = sender: three separate write() calls ----------
        close(fd[0]);

        for (int i = 1; i <= NMSG; i++) {
            char msg[BUFSIZE];
            // No '\0' is written -- we send raw text so the concatenation is
            // plainly visible on the other side.
            int len = snprintf(msg, sizeof(msg), "[msg %d from PID %d]",
                               i, (int) getpid());
            write(fd[1], msg, len);
            printf("  child : write() #%d -> %d bytes\n", i, len);
        }

        close(fd[1]);
        exit(0);
    }
    else {
        // ---------- parent = receiver: one read(), much later ----------
        close(fd[1]);
        sleep(2);                     // let all three writes pile up first

        char buf[BUFSIZE];
        ssize_t n = read(fd[0], buf, sizeof(buf) - 1);
        buf[n > 0 ? n : 0] = '\0';
        printf("  parent: read() #1 -> %zd bytes: \"%s\"\n", n, buf);
        printf("          ^^ all %d messages arrived in ONE read()\n", NMSG);

        // A second read finds nothing left, and every write end is closed.
        ssize_t n2 = read(fd[0], buf, sizeof(buf) - 1);
        printf("  parent: read() #2 -> %zd  (0 = EOF, pipe drained)\n", n2);

        close(fd[0]);
        wait(NULL);
    }

    return 0;
}
