# CS 362 Artificial Intelligence and Machine Learning
**Spring 2026**  
**Due: Thursday, January 29th at 5:00 pm.**  
**60 points**  

# P2 - AI Search - Min Max 

## Overview 

The **Minimax algorithm** is a recursive backtracking search used in adversarial games such as Tic-Tac-Toe. It constructs a decision tree of possible future moves and evaluates positions to determine the best move assuming optimal play by both players.

In standard Tic-Tac-Toe minimax showing **all possible outcomes**, terminal positions are scored as:

- **+1** if **X wins**
- **−1** if ****O wins**
- **0** for a **draw**


**Player X (MAX)** chooses moves to **maximize the score**,   

while **Player O (MIN)** chooses moves to **minimize the score**.

In this assignment, you will compare:
1. A complete minimax tree (4 moves remaining), and
2. A depth-limited minimax tree (only 2 moves remaining), evaluated using a heuristic function describe by Tanimoto in *The Elements of Artificial Intelligence*.

---
## Part 1. Complete Tree with four remining moves (20 points)

Choose a Tic-Tac-Toe board state with exactly four empty squares remaining. **Your state must be different from the two class examples**.

```
 X | X | O                 X | O |
---+---+---               ---+---+---
   | O |                     | X | X
---+---+---               ---+---+---
 X |   |                     |   | O
```

Have **X** move first, thus your starting board will have three X's and two O's, thus it will be **O's** turn.


Draw the **entire minimax decision tree** from this position to the end of the game. There are most **four moves** as you can stop any branch that reaches a "win" for either X or O.

All leaf nodes must be terminal positions labeled:

- **+1** if **X wins**
- **−1** if ****O wins**
- **0** for a **draw**

Each internal node must show:
- whose turn it is (MAX or MIN)
- the value selected at that node  

Propagate values back to the root using minimax.
  
Clearly indicate the best move at the root.

Trees should match format demonstrated in class examples.

Neatly hand draw your decision tree representing all possible moves from the current state of the game and showing the Min/Max values that would be propagated back to the root node. Use colored ink/pencils to make your diagrams clear. You may want to use 11” x 14” paper.

---
## Part 2. Partial Tree with two remaing moves (20 points)

Using the **same starting board** state from Part 1.  Create a tree that shows the **next two moves** using the evaluation function describe by Tanimoto in *The Elements of Artificial Intelligence*.

Score = (A x 100) + (B x 10) + C - [ (D x 100) + (E x 10) + F ]

A is the number of 3 in a row X's  
B is the number of 2 in a row X's with open blank  
C is the number of 1 in a row X's with open blanks  

D is the number of 3 in a row O's  
E is the number of 2 in a row O's with open blank  
F is the number of 1 in a row O's with open blanks  

---
## Part 3. Analysis (10 points)

1. What move does the full minimax tree (Part 1) recommend?
2. What move does the depth-limited tree (Part 2) recommend?
3. Are the two recommended moves the same? If they differ, explain why the evaluation function may favor a different move.
4. Does the depth-limited tree appear to favor short-term advantage or long-term outcomes? Give one example from your tree.
5. Do the moves recommended for Part 1 and 2 match with what you think is the best move?
6. Will a different move for Part 1 lead to a quicker win?



---
## Collaboration

Work with another student and agree on the same **starting board**.  

You must each submit your own hand-drawn tree, but you are encouraged to discuss and compare results. Note the person (or persons) on your work submitted.

--- 

## Note on AI  use

You may use AI to help understand the minimax algorithm. 

List any AI system (or systems) you used to assist with the homework and briefly (1-sentence) describe how you used the system.

---

## Submitting your Assignment

Upload a copy of your answers for Part 3. and submit paper copies of your trees for Parts 1 and 2.

11 x 14 paper is availalbe from Prof. Lehman

-- end --


