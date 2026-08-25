// 2.2 -- parent is dead while child is still running  => ORPHAN
//
// The parent exits immediately. The child survives, and the kernel hands it
// to the init process (PID 1). The child prints getppid() before and after,
// so the re-parenting is visible in the program's own output.

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[]) {

    setvbuf(stdout, NULL, _IONBF, 0);

    printf("parent (pid:%d) starting\n", (int) getpid());
    int rc = fork();

    if (rc < 0) {
        fprintf(stderr, "fork failed\n"); exit(1);
    }
    else if (rc == 0) {
        // Child outlives its parent.
        printf("child  (pid:%d) ppid:%d  <-- BEFORE parent exits\n",
               (int) getpid(), (int) getppid());
        sleep(5);
        printf("child  (pid:%d) ppid:%d  <-- AFTER parent exited (re-parented)\n",
               (int) getpid(), (int) getppid());
        printf(">>> in another terminal run:  ps -ef | grep q2 | grep -v grep\n");
        sleep(25);
        printf("child  (pid:%d) done\n", (int) getpid());
        exit(0);
    }
    else {
        // Parent dies first. The shell prompt comes back immediately, but the
        // child keeps running and keeps printing into the same terminal.
        printf("parent (pid:%d) exiting immediately, child %d left running\n",
               (int) getpid(), rc);
        exit(0);
    }

    return 0;
}
