# BFS and DFS (graphs, grids, trees)

**Invariant:** every node is marked visited when it is first discovered (BFS: when enqueued), so it is processed at most once.

## Signals
- Grid/graph connectivity, "number of islands", flood fill
- Shortest path with equal edge weights → BFS
- Explore all possibilities / components / cycle detection / tree traversals → DFS
- Level-order → BFS

## Template (count islands, BFS on a grid) — verified
```python
from collections import deque

def islands(g):
    R, C = len(g), len(g[0])
    seen, count = set(), 0
    for i in range(R):
        for j in range(C):
            if g[i][j] == 1 and (i, j) not in seen:
                count += 1
                q = deque([(i, j)]); seen.add((i, j))
                while q:
                    x, y = q.popleft()
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < R and 0 <= ny < C and g[nx][ny] == 1 and (nx, ny) not in seen:
                            seen.add((nx, ny)); q.append((nx, ny))
    return count
```
Time O(R·C): each cell is enqueued once and checks 4 neighbours. Space O(R·C) for `seen` and the queue.

## Dry run: g = [[1,1,0],[0,0,1],[0,0,1]]
| start | action | cells visited | count |
| --- | --- | --- | --- |
| (0,0) | new island, BFS | (0,0),(0,1) | 1 |
| (1,2) | new island, BFS | (1,2),(2,2) | 2 |
Answer: 2.

## BFS vs DFS
BFS uses a queue and gives shortest paths in unweighted graphs. DFS uses recursion or a stack; its depth can hit recursion limits on large inputs (use an explicit stack).

## Misconceptions
- Marking visited on dequeue instead of enqueue (duplicates blow up the queue).
- Using BFS shortest path on weighted edges (needs Dijkstra).
- Skipping the bounds check before indexing.
- Recursive DFS on 10^5+ nodes (stack overflow).

## Ladder
Easy: Flood Fill → Medium: Number of Islands / Rotting Oranges → Harder: Word Ladder (all LeetCode).

## Interviewer twists
Diagonal moves; multi-source BFS; detect cycles in directed vs undirected graphs; return the path.
