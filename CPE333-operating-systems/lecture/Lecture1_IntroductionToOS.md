# Lecture 1 — Introduction to Operating Systems

> Text cache of `Lecture1_IntroductionToOS.pptx`. Auto-generated transcription — layout and some figure detail are lost. Read the source deck directly if visuals matter.

## Slide 1 — Lecture 1: Introduction to Operating System

Lecture 1
Introduction to Operating System

## Slide 2 — From previous semester …

Every second:

- Millions instructions are fetched by a processor (from a memory),
- then decoded (processor figure out what instruction it is),
- then executed (and maybe write)

In this class, we will learn that while a program is run, a lot of other things are going on…and

There is a body of software that is responsible for

- making programs run
- Allowing programs to share memory
- Enabling programs to interact with devices
- Etc.

Operating System is in charge of making sure that the system operates correctly and efficiently in an easy-to-use manner

## Slide 3 — Things covered in this course

Lectures

- Introduction to OS (1 wk)
- Part I – Virtualization (5 wks)
  - Processor
  - Memory
- Part II – Concurrency (4 wks)
  - Thread API
  - Locks and Semaphores
  - Deadlock
- Part III – Persistence (2 wks)
  - I/O System
  - File System
  - Storage and Mass-Storage Management

Mini Projects

- Project 1 – Compile and build an OS
- Project 2 – Study and present in details, a few key components of an OS
- Project 3 – Modify some modules in the kernel

## Slide 4 — Virtualization

- OS takes a physical resources (processor, memory, disk, etc) and transform it into a more general, powerful virtual form of itself.
  - Ex OS can turn a single CPU into a seemingly infinite number of CPUs – virtualizing the CPU
- Sometime, we refer to OS as a virtual machine
- OS allows CPUs, memory, I/O to be shared, thus it can also be called a resource manager.
- OS provides APIs (system calls) to applications in order to access resources.

## Slide 5 — Processor

- Q: If two programs want to run at the same time, then what ?
- Q: Who (which program) gets what (which resources), and when ?
  - Policies, many and many of them
  - APIs for user programs to communicate desired activities to the OS.

## Slide 6 — Memory (1)

- Is accessed all the time when a program is running.
  - Programs keep all data in memory, and accesses them through various instructions (lw, sw)
  - Programs' instructions are also stored in the memory

P1

```c
main ()
{
      int *p= malloc (sizeof(int))l
      *p = 0;
}
```

P2

```c
main ()
{
      int *p= malloc (sizeof(int))l
      *p = 0;
}
```

> **Notes:** Memory is just an array of bytes: to read, one must specify an address to be able to access the data stored there; to write, one must also specify the data to be written to the given address.

## Slide 7 — Memory (2)

- Q: when P1 and P2 are running their program, it always appear that the value can be updated independently, why ?
  - Each running program has its own private memory (private address space), which can be mapped onto the physical memory
  - A memory reference within one program does not affect address space of others.
  - OS is virtualizing memory

*Figure: a screenshot reproducing the same P1/P2 malloc code shown on the previous slide, reused here to illustrate that each process has its own independent address space.*

## Slide 8 — It's all about 'Concurrency'

- OS has to juggle many things at once, which leads to some interesting problems.
- Ultimate Goal: how to make all programs execute with correct conditions
  - What techniques are needed from the OS
  - What mechanisms should be provided by the hardware
  - How can we use them to solve the problems
- Multi-threaded programs also exhibit the same problems
  - Solutions are different from OS-level concurrency as threads share same address space.

## Slide 9 — Persistence

- In memory, data can be easily lost, as DRAM is volatile.
  - Power out -> data lost
  - System crash -> data lost
- We need a disk drive for long-lived information.
- Thus, OS must manage the disk(s) in addition to other things.  This is called a file system.
- The file system stores files in a reliable and efficient manner on the disk(s)
- No abstraction here, OS does not create a private, virtualized disk for each application, why ?

## Slide 10 — Persistence (cont.)

- Files are shared across different processes.
  - Process A: Editor (vi, emacs) creates a source code file
  - Process B: Compiler use it to create a new executable file.
- All system calls related to file manipulation are routed to the 'file system', who handles the requests.
- OS deals with all device drivers in order to get device to do something.
- Issues:
  - Delay 'writes' and try to batch them for better performance
  - Handle system crashes during writes
  - Handle different data structures and access methods
  - RAID for data redundancy and performance improvement

> **Notes:** RAIN: Redundant Arrays of Inexpensive Disks (RAID)

## Slide 11 — Building an OS, we must consider ..

- Abstractions: make it convenient and easy to use through virtualization
- High performances: minimizing overheads (extra time, extra space)
- Isolation: protection schemes between applications (malicious or accidental bad behavior of one does not harm others)
- Reliability: OS runs non-stop.  However, when it fails, all applications fail as well.  Millions lines of code are dedicated to reliability.
- Energy-efficiency:  green world, longer battery usage time
- Security: against malicious applications
- Mobility: for smaller devices

## Slide 12 — Summary and Transition to OS History

*(This slide has no title placeholder text in the source.)*

Operating system takes physical resources and virtualizes them.  It also handles concurrency and persistence issues as well as others

Now… let's look at the history of OS

## Slide 13 — Early days of Mainframe

- Early OS:  just libraries of commonly used functions such as I/O manipulations
  - One program at a time, controlled by a human (human-scheduler).
- Libraries with Protection: code run on behalf of OS is special; it should be treated differently from others
  - Cannot allow any program to access anywhere on the disk (privacy).
  - Modes of execution is added: user and kernel
  - In contrast to a procedure call, a system call transfers control into the OS, raising the hardware privilege level.  This allow full access to hardware of the system.
    - Initiate I/O requests
    - Make more memory available to a program

## Slide 14 — Multiprogramming on Minicomputer

- To make better use of machine resources, people pay lots of attention to multiprogramming.
- Instead of running one job at a time, OS load a number of jobs into memory and swatch between them, improving CPU utilization.
- I/O is slow, doing this CPU does not have to wait.
- Issues arise:
  - Memory protection
  - Interrupts (must make sure OS is working correctly)
- Leads to the introduction of UNIX and with it the C language !

## Slide 15 — The Modern Era of PCs

People forgot to look at what're good in the minicomputer OS. So…..

- DOS: memory protection is absent
- Mac OS (1st gen): poor job scheduling

After some years of trying

- Windows NT incorporated features from minicomputer OS
- Mac OS X had UNIX at its core

The concept: "one machine per desktop instead of a shared minicomputer per workgroup".

> **Notes:** DOS: Without a good memory protection scheme, a poorly-programmed application or malicious applications can scribble all over memory.
> Mac OS: a thread that accidently got stuck in an infinite loop could take over the entre system forcing a reboot.
