# AI Programming Assignment

**Name:** Dhimanth Reddy  
**Roll Number:** SE24UCSE055  
**Course:** Artificial Intelligence  

---

## Overview

This repository contains implementations of:

- Turing Test Simulation  
- CAPTCHA System  
- Eight Queens Problem using BFS, DFS, and IDDFS  

All programs are implemented in Python 3 without external libraries.

---

# 1️⃣ Assignment 1: Turing Test (turingtest.py)

Simulates the Turing Test — a judge attempts to distinguish between a human and a machine based on their responses.

## Objective

To demonstrate how machines imitate human conversation and how a judge evaluates responses to determine whether they are human or artificial.

## Components

- **Machine** – generates robotic responses  
- **Human** – generates natural responses  
- **Judge** – assigns a suspicion score based on keywords and response structure  

If suspicion score ≥ 40%, the response is classified as **BOT**, otherwise **HUMAN**.

## How to Run

```bash
python turingtest.py
```

## Sample Output

```
Machine Responses:
  I analyze input before producing output.

Human Responses:
  Haha that’s interesting!

Judge Verdict:
Machine → BOT (50%)
Human   → HUMAN (0%)
```

---

# 2️⃣ Assignment 2: CAPTCHA System (Captcha.py)

Implements a CAPTCHA system that distinguishes humans from bots using different challenge types.

## Objective

To design a security mechanism that allows human users to pass while blocking automated programs.

## CAPTCHA Types

| Type  | Example | Purpose |
|-------|----------|----------|
| Math  | What is 12 + 8? | Arithmetic reasoning |
| Logic | What comes after Tuesday? | Common knowledge |
| Text  | Enter code: A B X 9 P | Character recognition |

## Architecture

User → Challenge Generated → User Response → Verification → Access Granted / Blocked

## How to Run

```bash
python Captcha.py
```

## Sample Output

```
Session ID : 3F82AB91CD
Challenge  : What is 15 + 9?
Response   : 24
Result     : Access Granted.
```

---

# 3️⃣ Assignment 3: Eight Queens Problem (8queens.py)

Place 8 queens on a chessboard such that no two queens attack each other.

## Objective

To implement uninformed search strategies (BFS, DFS, IDDFS) to solve a constraint satisfaction problem.

## Problem Rules

- No two queens share the same row  
- No two queens share the same column  
- No two queens share the same diagonal  

## State Representation

The state is represented as a list:

- Index = row number  
- Value = column number  

Example:

```
[0, 4, 7, 5, 2, 6, 1, 3]
```

---

## Algorithms Implemented

### 1️⃣ Breadth-First Search (BFS)
- Explores nodes level by level
- Uses a queue
- Guarantees optimal depth solution
- Higher memory usage

### 2️⃣ Depth-First Search (DFS)
- Explores deepest nodes first
- Uses a stack
- Lower memory usage
- Not guaranteed optimal

### 3️⃣ Iterative Deepening DFS (IDDFS)
- Combines BFS completeness and DFS efficiency
- Repeatedly applies depth-limited DFS
- Optimal and complete

---

## How to Run

```bash
python 8queens.py
```

---

## Performance Comparison

| Algorithm | Time Complexity | Space Complexity |
|------------|----------------|------------------|
| BFS | O(b^d) | O(b^d) |
| DFS | O(b^d) | O(d) |
| IDDFS | O(b^d) | O(d) |

Where:
- **b** = branching factor  
- **d** = depth of solution  

---

## Observations

- BFS explores more nodes but guarantees optimal solution.
- DFS may find solution faster but depends on search order.
- IDDFS balances memory efficiency and completeness.

---

## Requirements

- Python 3
- No external libraries required

---

## Conclusion

This assignment demonstrates:
- Human vs machine differentiation (Turing Test)
- Security validation using CAPTCHA
- Problem solving using uninformed search algorithms

All implementations follow modular design and standard AI search principles.
