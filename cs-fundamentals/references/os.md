# Operating Systems — facts and worked examples

## Process vs thread
| | Process | Thread |
| --- | --- | --- |
| Address space | Own | Shared with the process |
| Creation / context switch | Heavier | Lighter |
| Communication | IPC needed | Shared memory directly |
| Failure | Isolated | One thread can crash the process |

Each thread has its own stack, registers and program counter.

## Process states
New → Ready → Running → Waiting (blocked) → Ready … → Terminated. Running → Ready happens on pre-emption.

## Scheduling
FCFS (non-pre-emptive; convoy effect), SJF (minimum average waiting time among non-pre-emptive; can starve long jobs), SRTF (pre-emptive SJF), Round Robin (time quantum; too large → FCFS, too small → overhead), Priority (starvation, fixed by aging).

Formulas: Turnaround = Completion − Arrival. Waiting = Turnaround − Burst.

**Worked example (verified):** P1=6, P2=8, P3=3, all arrive at 0.
- FCFS (P1,P2,P3): waits 0, 6, 14 → average 20/3 ≈ 6.67
- SJF (P3,P1,P2): waits 0, 3, 9 → average 4
- Round Robin q=4: completions P1=13, P2=17, P3=11 → waits 7, 9, 8 → average 8

## Deadlock
Four necessary conditions (all must hold): mutual exclusion, hold and wait, no pre-emption, circular wait.
Handling: prevention (break a condition), avoidance (Banker's algorithm), detection and recovery, ignore (ostrich).
Trap: a cycle in a resource-allocation graph means deadlock only with single instance per resource.

## Memory and paging
- Logical address = page number + offset. Physical address = frame number + offset.
- Page size 2^k → offset has k bits.
- **Worked example:** 32-bit logical address, 4 KB page (2^12) → offset 12 bits, page number 20 bits, page table has 2^20 entries.
- Internal fragmentation: inside allocated pages/partitions (paging). External fragmentation: scattered free holes (contiguous/segmentation).
- TLB caches page-table entries; a TLB miss goes to the page table.
- Page replacement: FIFO (Belady's anomaly possible), LRU, Optimal (best, not implementable). Thrashing = too much paging, little useful work.

## Synchronisation
- Race condition: result depends on interleaving. Critical-section needs mutual exclusion, progress, bounded waiting.
- Semaphore: counting or binary; `wait` (P) decrements, `signal` (V) increments. Mutex has ownership; a binary semaphore does not.
- Classic problems: producer-consumer, readers-writers, dining philosophers.

## Common MCQ traps
- Thread vs process sharing (stack is NOT shared).
- Belady's anomaly applies to FIFO, not LRU.
- SJF is optimal for average waiting time only when all jobs are available together.
