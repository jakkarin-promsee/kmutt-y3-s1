#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>   // wait() lives here -- without it gcc only *guesses*

int main(int argc, char *argv[]) {
    
    printf("hello world (pid:%d)\n", (int) getpid());
    int rc = fork();

    if (rc < 0) { 
        fprintf(stderr, "fork failed\n"); exit(1); 
    }
    else if (rc == 0) {
        printf("hello, I am child (pid:%d)\n", (int) getpid());
    }
    else {
        // wait() blocks the parent until the child finishes, and returns the
        // PID it reaped -- so wc should always come back equal to rc.
        int wc = wait(NULL);
        printf("hello, I am parent of %d (wc:%d) (pid:%d)\n",
               rc, wc, (int) getpid());
    }

    return 0;
}
