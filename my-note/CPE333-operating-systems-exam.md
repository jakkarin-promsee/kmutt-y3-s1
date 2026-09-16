
# Process algorithm

Sanity check:
- FCFS = FIFO
- RR = Loop 1 time slice for each process then go next. (1, 2, 3, 1, 2, 3, 1, 2, 3, ...)
- SJF = idle -> argmin(waiting time) -> do(process) until done -> loop
- STCF/SRTF = idle -> argmin(remaining time) -> do(process) for one time slice -> loop
( STCF/SRTF = Preemptive version of SJF)

- Arrival Time = when it come
- Burst Time = how long it take to execute
- Remaining Time = how long its exaction left

- average waiting time = the average time process has wait until it get select
- turnaround time = the average time process wait in queue
- time slice = how long 1 block can execute the program
