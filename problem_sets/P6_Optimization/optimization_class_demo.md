## Class Demo – Optimization Game



![optimization_approaches](./optimization_approaches.png)

### Setup

1. Instructor selects a **random number (1–100)**  
2. Instructor selects a **random starting student**  
3. Each student picks a **random number (1–100)**  
   - Write it on a piece of paper  
   - Do **not share your number**  
4. Instructor **reveals the target number**

---

### Goal

Minimize your **distance to the target**:

> distance = |your number – target|

You may compare and **swap numbers with neighbors**  
(N, S, E, W, NE, NW, SE, SW)

---

# Approach 1 – Local Search (Greedy / Hill Climbing)

## Goal
Find a better solution by moving to a **better neighbor**

---

## Process

1. Start with the **selected student**
2. Look at **neighboring students**
3. If a neighbor has a **better value (closer to target)**:
   - Move to the **best neighbor**
4. **Repeat** steps 2–3
5. **Stop** when **no neighbor is better**

---

## Key Takeaways

> You may get stuck in a **local minimum**

- No better neighbor nearby  
- But not the best overall solution  
- You do not know if this is the best solution  
- Always choosing the best local move does not guarantee finding the **global optimum**

---

# Approach 2 – Simulated Annealing (Improved Local Search)

## Goal
Find a better solution by exploring neighbors while **occasionally accepting worse moves**

>Note on term **annealing**: When metals are heated, their atoms can move more freely; as they cool slowly, they settle into a stable, low-energy arrangement. If cooled too quickly, defects can form. Simulated annealing follows this pattern ie. start with flexibility (randomness), then slowly reduce it to reach a better overall solution.
---

## Process

1. Start with the **selected student**
2. Look at **neighboring students**
3. If a neighbor has a **better value (closer to target)**:
   - Move to that neighbor
4. If a neighbor is **worse**:
   - **Sometimes accept** the move (based on randomness)
5. Gradually **reduce randomness over time**  
   *(cooling / lowering temperature)*
6. **Repeat** until the system “stabilizes”

---

## Key Takeaways

> Early: explore more (accept worse moves)  
> Later: refine solution (accept only better moves)

- Can **escape local minima**
- Accepting worse moves becomes **less likely over time**
- More likely to find a **better overall (global) solution**
- May take longer
- Does **not guarantee** the absolute best solution

-- end --