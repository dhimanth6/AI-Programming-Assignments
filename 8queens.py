"""
8 Queens Problem – Uninformed Search
State: List of column positions per row
Goal: Place 8 queens without attacking each other
"""

from collections import deque
import time


N = 8


def is_safe(state, row, col):
    for r in range(row):
        if state[r] == col or abs(state[r] - col) == abs(r - row):
            return False
    return True


def bfs():
    queue = deque([[]])
    nodes = 0

    while queue:
        state = queue.popleft()
        nodes += 1

        row = len(state)
        if row == N:
            return state, nodes

        for col in range(N):
            if is_safe(state, row, col):
                queue.append(state + [col])

    return None, nodes


def dfs():
    stack = [[]]
    nodes = 0

    while stack:
        state = stack.pop()
        nodes += 1

        row = len(state)
        if row == N:
            return state, nodes

        for col in reversed(range(N)):
            if is_safe(state, row, col):
                stack.append(state + [col])

    return None, nodes


def dls(state, depth):
    if len(state) == N:
        return state
    if depth == 0:
        return None

    row = len(state)
    for col in range(N):
        if is_safe(state, row, col):
            result = dls(state + [col], depth - 1)
            if result:
                return result
    return None


def iddfs():
    nodes = 0
    for depth in range(1, N + 1):
        result = dls([], depth)
        nodes += depth
        if result:
            return result, nodes
    return None, nodes


def print_board(solution):
    print("\nSolution Board:\n")
    for r in range(N):
        row = ["Q" if solution[r] == c else "." for c in range(N)]
        print(" ".join(row))


def compare():
    print("\n8 Queens – Uninformed Search Comparison")

    for name, func in [("BFS", bfs), ("DFS", dfs), ("IDDFS", iddfs)]:
        start = time.perf_counter()
        solution, nodes = func()
        elapsed = (time.perf_counter() - start) * 1000
        print(f"\n{name}")
        print(f"Nodes explored: {nodes}")
        print(f"Time: {elapsed:.4f} ms")
        print_board(solution)


if __name__ == "__main__":
    compare()