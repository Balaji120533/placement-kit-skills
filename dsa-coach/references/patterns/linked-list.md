# Linked list (pointer manipulation, fast/slow)

**Invariant:** at every step the nodes behind your pointers form a correct partial result and you still hold a reference to the rest of the list.

## Signals
- Reverse, merge, reorder, remove nth from end
- Detect a cycle, find the middle, find the cycle start
- "In place", "O(1) space"

## Template 1: reverse — verified
```python
def reverse(head):
    prev = None
    while head:
        nxt = head.next      # 1. save the rest
        head.next = prev     # 2. flip the link
        prev = head          # 3. advance prev
        head = nxt           # 4. advance head
    return prev
```
Time O(n), one visit per node. Space O(1).

## Template 2: cycle detection (Floyd) — verified
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```
Time O(n): if a cycle exists the gap closes by 1 per step. Space O(1).

## Dry run: reverse 1→2→3
| head | nxt | prev after | list state |
| --- | --- | --- | --- |
| 1 | 2 | 1 | 1→None |
| 2 | 3 | 2 | 2→1→None |
| 3 | None | 3 | 3→2→1→None |

## Misconceptions
- Losing the rest of the list by overwriting `head.next` before saving it.
- Null checks: `fast` and `fast.next` both needed before `fast.next.next`.
- Comparing node values instead of node identity (`is`) for cycles.
- Forgetting a dummy head when the head itself may be removed.

## Ladder
Easy: Reverse Linked List → Medium: Linked List Cycle II / Remove Nth Node From End → Harder: Reverse Nodes in k-Group (all LeetCode).

## Interviewer twists
Recursive version (O(n) stack space), reverse a sub-range, doubly linked list.
