// 4 -- pipe() + fork(): child is the sender, parent is the receiver.
//
// pipe() MUST come before fork(), because fork() copies the file descriptor
// table. After the fork there are FOUR open ends (read+write in each process),
// so each side has to close the end it does not use.

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

#define BUFSIZE 128

int main(int argc, char *argv[]) {

    setvbuf(stdout, NULL, _IONBF, 0);

    int fd[2];                        // fd[0] = read end, fd[1] = write end
    if (pipe(fd) < 0) {
        perror("pipe"); exit(1);
    }

    int rc = fork();
    if (rc < 0) {
        perror("fork"); exit(1);
    }
    else if (rc == 0) {
        // ---------- child = SENDER ----------
        close(fd[0]);                 // a sender never reads

        printf("Child: Child PID: %d -> sender\n", (int) getpid());

        char msg[BUFSIZE];
        int len = snprintf(msg, sizeof(msg),
                           "Hello from child PID: %d", (int) getpid());
        write(fd[1], msg, len);

        close(fd[1]);                 // closing the LAST write end sends EOF
        exit(0);
    }
    else {
        // ---------- parent = RECEIVER ----------
        close(fd[1]);                 // a receiver never writes.
                                      // Skip this line and read() below hangs
                                      // forever: the kernel still sees an open
                                      // write end (ours) so it never signals EOF.

        printf("Parent: Parent PID: %d -> receiver\n", (int) getpid());

        char buf[BUFSIZE];
        ssize_t n = read(fd[0], buf, sizeof(buf) - 1);
        if (n < 0) {
            perror("read"); exit(1);
        }
        buf[n] = '\0';                // read() does NOT NUL-terminate for you

        printf("Parent received: %s\n", buf);

        close(fd[0]);
        wait(NULL);
    }

    return 0;
}
