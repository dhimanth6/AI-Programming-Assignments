
# AI Programming Assignment

**Name:** Dhimanth Reddy
**Roll Number:** SE24UCSE055  
**Course:** Artificial Intelligence  

---

This repository contains implementations of:
1. Turing Test Simulation
2. CAPTCHA System
3. Eight Queens Problem using BFS, DFS, IDDFS



1️⃣ Assignment 1: Turing Test (turingtest.py)

Simulates the Turing Test — a judge tries to tell apart a human and a bot based on their responses.

Objective

To demonstrate how machines can imitate human conversation and how a judge attempts to detect machine-like behavior.

Components

BotPlayer – produces robotic/scripted responses

HumanPlayer – produces natural responses

Judge – analyzes responses and assigns suspicion score

Suspicion ≥ 40% → classified as BOT

How to Run
python turingtest.py
Sample Output
Q: Do you have feelings?
Bot   : I process sentiment data.
Judge : BOT (suspicion: 40%)
Human : Yes, I feel happy and excited.
Judge : HUMAN (suspicion: 0%)
2️⃣ Assignment 2: CAPTCHA System (captcha.py)

Implements a CAPTCHA system that blocks bots and allows humans to pass.

Objective

To design a system that distinguishes humans from automated programs.

CAPTCHA Types
Type	Example	Purpose
Math	Solve: 14 + 7 = ?	Arithmetic ability
Logic	What comes after Tuesday?	Common knowledge
Text	Type: R X X R W	Character recognition
Architecture

User → Challenge Generated → User Response → Verification → Access Granted/Blocked

How to Run
python captcha.py
Sample Output
Type      : Math CAPTCHA
Challenge : Solve: 2 - 14 = ?
Bot   answered ??? → FAIL
Human answered -12 → PASS
3️⃣ Assignment 3: Eight Queens Problem (8queens.py)

Place 8 queens on a chessboard so that no two queens attack each other.

Objective

To implement uninformed search strategies (BFS, DFS, IDDFS) to solve a constraint satisfaction problem.

Problem Rules

No two queens share the same row

No two queens share the same column

No two queens share the same diagonal

State Representation

A list where:

Index = row

Value = column

Example:

[0, 4, 7, 5, 2, 6, 1, 3]
Algorithms Implemented
Algorithm	Strategy	Optimal?	Memory Usage
BFS	Level-order search	Yes	High
DFS	Depth-first search	Not guaranteed	Low
IDDFS	Iterative deepening	Yes	Medium
How to Run
python eight_queens.py
Sample Output
8 Queens – Uninformed Search

BFS
Nodes explored: 2057
Time: 5.18 ms

DFS
Nodes explored: 113
Time: 0.43 ms

IDDFS
Nodes explored: 346
Time: 1.21 ms

Solution Board:

Q . . . . . . .
. . . . Q . . .
. . . . . . . Q
. . . . . Q . .
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .


3️⃣ Assignment 3: Eight Queens Problem (8queens.py)
Algorithms Used
1️⃣ Breadth-First Search (BFS)

Explores nodes level by level.

Uses a queue.

Guarantees shortest solution in terms of depth.

Higher memory usage because it stores many states.

2️⃣ Depth-First Search (DFS)

Explores deepest nodes first.

Uses a stack.

Uses less memory.

May find solution faster, but not guaranteed optimal.

3️⃣ Iterative Deepening DFS (IDDFS)

Combines BFS completeness and DFS memory efficiency.

Repeatedly runs DFS with increasing depth limit.

Optimal and complete.

Performance Comparison
Algorithm	Nodes Explored	Time (ms)	Memory Usage
BFS	Higher	Slower	High
DFS	Lower	Faster	Low
IDDFS	Medium	Medium	Medium
Observations

BFS explores more nodes but guarantees optimal solution.

DFS explores fewer nodes but depends on search order.

IDDFS balances memory efficiency and completeness.

Time Complexity

Let:

b = branching factor

d = depth of solution

Algorithm	Time Complexity	Space Complexity
BFS	O(b^d)	O(b^d)
DFS	O(b^d)	O(d)
IDDFS	O(b^d)	O(d)

