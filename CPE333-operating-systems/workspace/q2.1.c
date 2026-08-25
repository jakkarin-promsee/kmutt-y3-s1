// 2.1 -- child is dead while parent is still running  => ZOMBIE
//
// The parent forks, then deliberately never calls wait(). The child exits
// straight away. Because nobody has collected the child's exit status, the
// kernel must keep its process-table entry alive -> ps shows it as <defunct>.

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[]) {

    setvbuf(stdout, NULL, _IONBF, 0);   // see note about fork() + buffering

    printf("parent (pid:%d) starting\n", (int) getpid());
    int rc = fork();

    if (rc < 0) {
        fprintf(stderr, "fork failed\n"); exit(1);
    }
    else if (rc == 0) {
        // Child: report my parent, then die immediately.
        printf("child  (pid:%d) ppid:%d  -- exiting right now\n",
               (int) getpid(), (int) getppid());
        exit(0);
    }
    else {
        // Parent: NO wait() on purpose. Stay alive so the corpse is visible.
        printf("parent (pid:%d) forked child %d, sleeping 30s WITHOUT wait()\n",
               (int) getpid(), rc);
        printf(">>> in another terminal run:  ps -ef | grep -E 'q2|defunct' | grep -v grep\n");
        sleep(30);

        // Only now do we reap it -- the zombie disappears at this moment.
        int wc = wait(NULL);
        printf("parent (pid:%d) finally reaped %d -- zombie is gone\n",
               (int) getpid(), wc);
    }

    return 0;
}
