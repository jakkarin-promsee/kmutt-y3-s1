"""Compile every PS2 program through WSL.

Compile only by default -- several of these must NOT be launched blindly:
  q2.1 / q2.2  sleep for 30s and need `ps` run from a second terminal
  q3           forks until failure; run it as  `ulimit -u 500 && ./q3`
Pass --run to also execute the ones that finish quickly on their own.
"""

import os
import sys

# Always compile from this file's folder, not wherever you launched Python.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

files = [
    "q1.1.c", "q1.2.c",
    "q2.1.c", "q2.2.c",
    "q3.c",
    "q4.c",
    "q5.1.c", "q5.2.c", "q5.3.c",
]

# The rest either sleep for half a minute or need a process cap first.
SAFE_TO_AUTORUN = {"q1.1", "q1.2", "q4", "q5.1", "q5.2", "q5.3"}

run = "--run" in sys.argv

for src in files:
    # split('.')[0] would turn q1.1.c into "q1" -- both files would clobber
    # the same binary. splitext keeps the "q1.1" / "q1.2" stem.
    name = os.path.splitext(src)[0]

    print(f"\n=== {src} ===")
    # -Wall matters here: it is what catches a missing #include <sys/wait.h>,
    # which otherwise compiles fine on gcc 13 and hard-fails on gcc 14+.
    if os.system(f"wsl gcc -Wall -o {name} {src}") != 0:
        print(f"!!! {src} failed to compile")
        continue

    if run and name in SAFE_TO_AUTORUN:
        print(f"--- ./{name} ---")
        os.system(f"wsl ./{name}")

print("\ndone. run the rest by hand:")
print("  ./q2.1     then  ps -ef | grep -E 'q2|defunct' | grep -v grep")
print("  ./q2.2     then  ps -ef | grep q2 | grep -v grep")
print("  ulimit -u 500 && ./q3")
