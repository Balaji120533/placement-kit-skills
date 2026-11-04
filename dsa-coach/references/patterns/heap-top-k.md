# Heap and top-k

**Invariant:** the heap holds the best k candidates seen so far; its root is the weakest of them, so it is the first to be evicted.

## Signals
- "k largest/smallest/most frequent", "kth largest"
- Streaming data, repeatedly need min or max
- Merge k sorted lists, scheduling by priority, running median (two heaps)

## Template (k largest elements, min-heap of size k) — verified
```python
import heapq

def topk(a, k):
    h = []                          # min-heap
    for x in a:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)        # drop the smallest of the k+1
    return sorted(h, reverse=True)
```
Time O(n log k): each of n elements costs one push and at most one pop on a heap of size ≤ k+1. Space O(k).
Compare: sorting is O(n log n); use the heap when k ≪ n or data streams.

## Dry run: a = [3,1,5,12,2,11], k = 3
| x | heap after push | pop | heap kept |
| --- | --- | --- | --- |
| 3 | [3] | – | {3} |
| 1 | {1,3} | – | {1,3} |
| 5 | {1,3,5} | – | {1,3,5} |
| 12 | {1,3,5,12} | 1 | {3,5,12} |
| 2 | {2,3,5,12} | 2 | {3,5,12} |
| 11 | {3,5,11,12} | 3 | {5,11,12} |
Result [12,11,5].

## Misconceptions
- Using a max-heap of size n for top-k (O(n log n), no benefit).
- Python's `heapq` is a min-heap only; negate values for a max-heap.
- Believing the heap is sorted: only the root is guaranteed.
- Quickselect is O(n) average but O(n²) worst case.

## Ladder
Easy: Kth Largest Element in a Stream → Medium: Top K Frequent Elements / Kth Largest Element in an Array → Harder: Merge k Sorted Lists / Find Median from Data Stream (all LeetCode).

## Interviewer twists
Online updates; kth smallest in a matrix; ties and ordering rules.
