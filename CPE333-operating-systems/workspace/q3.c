// 3 -- how many times can we fork()?
//
// Following the hint: a recursive chain where every parent blocks in wait()
// and only the newest child forks again. That grows the process count
// LINEARLY. A naive "while (1) fork();" grows it as 2^n, because the children
// run the loop too -- that is a fork bomb and it will hang the machine.
//
// *** ALWAYS cap the process count before running this: ***
//        ulimit -u 500 && ./q3

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/wait.h>

static void fork_chain(int depth) {
    int rc = fork();

    if (rc < 0) {
        // fork() failed for us, so exactly `depth` calls succeeded before this
        // one. We are the deepest process in the chain.
        printf("\nfork() failed at depth %d -- errno %d (%s)\n",
               depth, errno, strerror(errno));
        printf(">>> successful fork() calls: %d\n", depth);
        return;
    }
    else if (rc == 0) {
        // Child: go one level deeper, then exit so our parent's wait() returns.
        if (depth % 100 == 0) {
            printf("depth %d ... ", depth);
        }
        fork_chain(depth + 1);
        exit(0);
    }
    else {
        // Parent: block until the entire chain below us has unwound.
        wait(NULL);
        return;
    }
}

int main(int argc, char *argv[]) {

    setvbuf(stdout, NULL, _IONBF, 0);

    printf("pid:%d -- forking until fork() fails\n", (int) getpid());
    printf("(cap this first:  ulimit -u 500 && ./q3)\n\n");

    fork_chain(0);

    printf("pid:%d -- chain unwound, done\n", (int) getpid());
    return 0;
}
