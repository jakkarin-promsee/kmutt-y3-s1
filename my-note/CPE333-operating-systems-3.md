# Cheat Sheet

```bash
# process monitoring
ps
ps aux
ps -ef
top

# priority
nice -n 10 command
renice 10 -p PID

# kill
kill PID
kill -9 PID

# jobs
jobs
jobs -l

# foreground / background
command &
fg %1
bg %1

# permissions
chmod +x file.sh

# run script
./file.sh

# compile C
gcc PS3.c -o PS3

# run PS3
./PS3 case1.csv
```

---

# Setup for Class

> Using Windows OS

### 1. Install WSL

```bash
wsl --install
```

### 2. Update packages

```bash
sudo apt update
sudo apt install build-essential
```

---

# Process Manipulation and Monitoring

## 1. Program / Process

- **Program** = instruction/code file stored on disk, e.g. `/bin/bash`
- **Process** = running instance of a program
  - PID
  - state
  - CPU usage
  - memory usage
  - priority
  - parent process

## 2. PID / PPID

- **PID** = Process ID
- **PPID** = Parent Process ID

```text
bash (parent)
 └── sleep 1000
```

```text
bash PID   = 500
sleep PID  = 620
sleep PPID = 500
```

## 3. Bash Commands

### Process type

- Foreground: `sleep 10` → shell waits for 10s
- Background: `sleep 10 &` → shell prompt stays usable

### Basic job control

```bash
$ sleep 1000 &
[1] 4326
```

- `[1]` = Job ID
- `4326` = PID
- `%1` = job 1
- `fg %1` = move job 1 to foreground
- `kill 4326` or `kill %1` = terminate process/job

### Process status: `ps`

```text
$ ps
    PID TTY          TIME CMD
    392 pts/0    00:00:00 bash
   4326 pts/0    00:00:00 sleep
   4360 pts/0    00:00:00 ps
```

```text
$ ps -ef
UID          PID    PPID  C STIME TTY          TIME CMD
root           1       0  0 19:33 ?        00:00:01 /usr/lib/systemd/systemd --system --deserialize=61
root           2       1  0 19:33 hvc0     00:00:00 /init
root           7       2  0 19:33 hvc0     00:00:00 plan9 --control-socket 7 --log-level 4 --server-fd 8 --pipe-fd 10 --
root          53       1  0 19:33 ?        00:00:00 /usr/lib/systemd/systemd-journald
```

```text
$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.1  21988 13316 ?        Ss   19:33   0:01 /usr/lib/systemd/systemd --system --deserialize=61
root           2  0.0  0.0   3184  2216 hvc0     Sl+   19:33   0:00 /init
root           7  0.0  0.0   3196  2120 hvc0     Sl+   19:33   0:00 plan9 --control-socket 7 --log-level 4 --server-fd 8
root          53  0.0  0.1  50440 16556 ?        S<s   19:33   0:00 /usr/lib/systemd/systemd-journald
root          98  0.0  0.0  25020  6404 ?        Ss   19:33   0:00 /usr/lib/systemd/systemd-udevd
```

- `USER` = process owner
- `PID` = Process ID
- `%CPU` = CPU usage
- `%MEM` = RAM usage
- `STAT` = process state
  - `R` = Running / runnable
  - `S` = Sleeping
  - `T` = Stopped
  - `Z` = Zombie
- `TIME` = accumulated CPU time
- `COMMAND` = command/process name

### Real-time status: `top`

```text
$ top

top - ...
Tasks: ...
%Cpu(s): ...
MiB Mem : ...

PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND
...
```

- `q` = quit
- `top` = real-time view
- `ps` = snapshot

## 4. `grep`

```bash
$ ps aux | grep sleep
night       4326  0.0  0.0   3136  1968 pts/0    S    21:26   0:00 sleep 1000
night       4365  0.0  0.0   4100  2164 pts/0    S+   21:35   0:00 grep --color=auto sleep
```

## 5. Process Scheduling and Priority

Nice value (**NI**) range: `-20` to `19`

- Higher NI → lower priority
- Lower NI → higher priority
- More "nice" → gives more CPU opportunity to others

Normal run:

```bash
$ ./myprogram
```

Run with NI:

```bash
$ nice -n 10 ./myprogram
```

Check:

```text
$ ps -o pid,ni,comm
PID    NI COMMAND
1000    0 bash
1050   10 myprogram
```

Change NI of running process:

```bash
$ renice 10 -p 1050
```

## 6. Kill Process

```bash
$ kill 1234
$ kill -SIGTERM 1234
$ kill -15 1234
```

- `SIGTERM` / signal `15` = ask process to terminate cleanly

```bash
$ kill -SIGKILL 1234
$ kill -9 1234
```

- `SIGKILL` / signal `9` = OS force-kills the process

```text
Ctrl + C
```

- `SIGINT` / signal `2` = interrupt from terminal

```text
Ctrl + Z
```

- `SIGTSTP` / signal `18` = suspend / stop process

## 7. Jobs

```text
$ jobs
[1]+  Stopped                 sleep 1000
[2]   Running                 sleep 1001 &
[3]   Running                 sleep 1002 &
[4]-  Running                 sleep 1003 &
```

```text
$ jobs -l
[1]+  4369 Stopped                 sleep 1000
[2]   4370 Running                 sleep 1001 &
[3]   4371 Running                 sleep 1002 &
[4]-  4372 Running                 sleep 1003 &
```

- `fg %1` = resume job 1 in foreground
- `bg %1` = resume job 1 in background

## 8. `nano`

```bash
nano ss1_1.sh
```

```bash
#!/bin/bash

echo "Start"
sleep 10
echo "Finish"
```

- `#!/bin/bash` = shebang; use `/bin/bash` as interpreter
- `Ctrl + O` = save
- `Ctrl + X` = exit
- `Ctrl + K` = cut
- `Ctrl + U` = paste
- `Alt + U` = undo
- `Alt + E` = redo

Give execute permission, then run:

```bash
$ chmod +x ss1_1.sh
$ ./ss1_1.sh
```

- `x` = executable

## 9. CRLF Problem

Linux uses **LF**. CRLF can cause:

```text
/bin/bash^M: bad interpreter
```

Save file as **LF**. In VS Code, line ending is shown at the bottom-right.

## 10. GNOME System Monitor

Linux GUI task manager.

```bash
sudo apt update
sudo apt install gnome-system-monitor
```

```bash
gnome-system-monitor
```

- Process Name = process name
- PID = Process ID
- User = process owner
- CPU = CPU usage
- Memory = RAM usage
- Status = running / sleeping / stopped
- Priority = priority
- Resources = CPU / RAM / system usage
- File Systems = disk / file-system usage

Windows Task Manager also shows:

- CPU
- Memory
- Disk
- Network
- GPU

## 11. Set Priority / Set Affinity

Connects to Nice (NI). Windows priority levels:

- Realtime
- High
- Above normal
- Normal
- Below normal
- Low

Suppose CPU has multiple logical processors:

- CPU 0
- CPU 1
- CPU 2

**Affinity** = which logical processors a process is allowed to run on.

## 12. Shortest Time-to-Completion (STCF)

Also called **Shortest Remaining Time First (SRTF)**.

> Preemptive version of Shortest Job First (SJF)

### Shortest Job First (SJF)

> Select process with shortest burst time.

```text
P1 burst = 8
P2 burst = 3
P3 burst = 5
```

Order: `P2 → P3 → P1` because `3 < 5 < 8`.

### Shortest Time-to-Completion (STCF)

Always choose the ready process with the **smallest remaining time**.
A newly arrived shorter process can preempt the current process.

- `Arrival` = time process enters ready queue
- `Burst` = total CPU time needed
- `Remaining` = CPU time still needed
- `Tie-breaking` = if equal, choose lowest PID first

Example:

| Process | Arrival | Burst |
| --- | ---: | ---: |
| P1 | 0 | 5 |
| P2 | 1 | 2 |
| P3 | 2 | 1 |

`t = 0`
- Ready = `[P1(5)]`
- Run `P1` → remaining `4`

`t = 1`
- Ready = `[P1(4), P2(2)]`
- Run `P2` → remaining `1`

`t = 2`
- Ready = `[P1(4), P2(1), P3(1)]`
- Tie → `P2` first (`PID P2 < P3`)
- Run `P2` → remaining `0`

`t = 3`
- Ready = `[P1(4), P3(1)]`
- Run `P3` → remaining `0`

`t = 4`
- Ready = `[P1(4)]`
- Run `P1` → remaining `3`

`...`

`t = 7`
- Ready = `[P1(1)]`
- Run `P1` → remaining `0`

Complete.

Pseudo code:

```c
initialize remaining time of every process

current_time = 0
completed = 0

while completed < number_of_processes

    find process where:
        arrival_time <= current_time
        remaining_time > 0

    choose smallest remaining_time

    if remaining_time ties:
        choose smallest process_id

    if no process available:
        CPU is idle
    else:
        run selected process for 1 time unit
        remaining_time--

        if remaining_time == 0:
            completed++

    current_time++
```

