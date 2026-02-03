# Alpha–beta

Alpha–beta pruning skips unnecessary branches by tracking bounds (α, β), while each node returns a single minimax value. It does not change the minimax value returned by the root node.

```
function ALPHABETA(node, depth, α, β, maximizingPlayer):

    if depth == 0 OR node is terminal:
        return EVALUATE(node)

    if maximizing Player:
        value ← -∞
        for each child in CHILDREN(node):
            value ← max(value, ALPHABETA(child, depth-1, α, β, false))
            α ← max(α, value)
            if α ≥ β:
                break        // PRUNE remaining children
        return value

    else:   // Minimizing Player
        value ← +∞
        for each child in CHILDREN(node):
            value ← min(value, ALPHABETA(child, depth-1, α, β, true))
            β ← min(β, value)
            if α ≥ β:
                break        // PRUNE remaining children
        return value
```

- α (alpha) = best value MAX has found so far (a lower bound for MAX).
- β (beta) = best value MIN has found so far (an upper bound for MAX).
- α and β are passed down the tree as bounds; they are not returned.
- Each call returns a single number: value (the node’s best minimax result found so far).
- Max nodes initialize value as -∞ and Min nodes initialize value as +∞
- Update rules for value and alpha/beta when child returns a value
  - At MAX: value = max(value, childValue) and then α = max(α, value)
  - At MIN: value = min(value, childValue) and then β = min(β, value)
- Prune rule: stop exploring remaining children when α ≥ β (equivalently β ≤ α).
- Note: value equals α at a MAX node or β at a MIN node at the moment a prune happens.
- Pruning rule: Stop evaluating children when: α (alpha) >= β (beta)

-- end --

    
