---
# Draft
---

# CS 362 Artificial Intelligence and Machine Learning
**Spring 2026**  
**60 points**  

# P4 - AI Search - Algorithms - Draft

![BFS DFS A-Star logo]bfs_dfs_astar.png)

## Overview 

**Breadth-First Search (BFS)**, **Depth-First Search (DFS**), and **A-Star Search** are fundamental 
to the field of Artificial Intelligence (AI) as they serve as foundational concepts for 
implementing AI solutions to a wide range of applications.  

In this assignment you will compare these three algorithms by running them on a set of mazes and analyzing performance.

### Starter Files

Use the provided files:

1. [`p4_maze_creator.py`](p4_maze_creator.py) – Text-based maze generator that creates a maze file using `X` and `.`, note you must add A and B;
2. [`p4_maze_search.py`](p4_maze_search.py) – Runs BFS, DFS, and A-star algorithms
displaying steps explored and number of steps to solution, and storing history file to be used by viewer
3. [`p4_maze_viewer.py`](p4_maze_viewer.py) – view history files to show how path found


---

## Part 1 — Create Six Mazes

Create **six** mazes total and run each maze with **BFS, DFS, and A*** (18 total runs).

Note: use the same `A` and `B` values for each maze size.

### Maze Trials

| Trial | Table Size (approx.) | Maze Type                        |
| ----: | -------------------- | -------------------------------- |
|     1 | 10 rows × 15 columns  | Empty with `A` and `B`           |
|     2 | 10 rows × 15 columns  | Light walls 5% `X` |
|     3 | 10 rows × 15 columns  | heavy walls 35% X` |
|     4 | 20 rows × 40 columns | Empty with `A` and `B`           |
|     5 | 20 rows × 40 columns | Light walls 5% `X` |
|     6 | 20 rows × 40 columns | heavy walls 35% X` |

### Maze Rules

* `A` = start
* `B` = goal
* `X` = wall / blocked cell
* (space or `.`) = open cell (whatever your code expects)
* All mazes must be solvable (there must be at least one valid path from A to B).

**Sparse with minimal X**: include *some* walls, but keep the maze mostly open (e.g., 5–15% walls), and avoid long continuous barriers.

---
### Create three maze files.

**Sample Maze 1 — 5×10 Empty**

```
A.........
..........
..........
..........
.........B
```

**Sample Maze 2 — 5x10 Light Walls 5%**
```
A.X.......
......X...
..........
.........X
.........B
```

**Trial 3 — 5×10 Heavy Walls 35%**

```
A.....XXX.
...X..X.X.
...XX.....
...XX.....
.......XXB
```


---
## Part 2 — Experiment

Run **x6 trials (mazes)** with each of the **three search algorithms (bfs, dfs, a-start)** for a total of **x18 experiments** and Record results


For **each run** record:

1. **Number of Steps** = length of the final path from `A` to `B` (how many moves along the solution path).
2. **Steps of Steps Explored** = number of states/cells/nodes explored during the search (how many positions the algorithm examined/expanded).


---

## Part 3 — Create Your Submission Document

Submit **one document** (PDF or Word preferred) that includes:

### A) Your six original mazes (no solution path shown)

For each maze, paste the **original maze layout** exactly as used in the experiment.

Sample Maze to Demonstrate Format (create your own):


---

### B) Summary Tables for All 18 Runs

Create a set of tables (one per trial may  be easiest) showing results for **BFS, DFS, A***.

Use this format:

#### Trial 1 (5×10 Empty)

| Algorithm | Steps (path length) | Steps Explored |
| --------- | ------------------- | -------------- |
| BFS       |                     |                |
| DFS       |                     |                |
| A*        |                     |                |

*(If you prefer one big table, that’s fine too—as long as all 18 runs are clearly recorded.)*


**Save the history** for each of your **x18 runs** ie. maze_5_10_empty_bfs.csv, maze_5_10_empty_dfs.csv, etc ...

Repeat for Trials 2–6.



---

### C) Analysis (2–3 paragraphs minimum)

Write **at least 2–3 paragraphs** that interpret your results. Your analysis should address:

* How did BFS, DFS, and A* compare on **Steps** and **Steps Explored**?
* Did the algorithms behave as expected on:

  * Empty vs sparse mazes?
  * Small vs large mazes?
  * Any surprises? 

---

## Submission Checklist

Your document must include:

* [ ] Six original mazes (no solution overlay)
* [ ] Results recorded for x6 Trials (Algorithm + Steps + Steps Explored), clearly labeled
* [ ] 2–3+ paragraphs of analysis comparing BFS/DFS/A*


* [ ] x18 history files as .zip file

Upload document and x18 history files as a single.zip file

-- end --

