"""
alphabeta_trace_16leaves_compact.py
Spring 2026 (sample)
Prof. Lehman - Alpha-Beta narrated trace demo (compact)

- User inputs 16 integer leaf values (left-to-right).
- Tree is an implicit full binary tree of depth 4 (MAX at root).
- Prints a compact trace showing v, alpha, beta as each child is checked,
  when child returns, updates, and pruning.
"""

from __future__ import annotations
from typing import List

INF = 10**9  # sentinel for +infinity/-infinity in trace


# ----------------------------
# Formatting helpers
# ----------------------------
def fmt(x: int) -> str:
    """Format sentinel infinities as +I/-I, otherwise as integer."""
    if x >= INF:
        return "+I"
    if x <= -INF:
        return "-I"
    return str(x)


def fmt_update(old: int, new: int) -> str:
    """Format update with arrow only if changed."""
    if old == new:
        return fmt(old)
    return f"{fmt(old)}→{fmt(new)}"


# ----------------------------
# Input
# ----------------------------
def input_16_integers() -> List[int]:
    """
    Prompt user for exactly 16 integers.
    Accepts either space-separated values or one-per-line.
    """
    print("Enter 16 integer leaf values (left-to-right).")
    print("You can type them space-separated, or one per line.\n")

    values: List[int] = []
    while len(values) < 16:
        remaining = 16 - len(values)
        raw = input(f"Enter up to {remaining} more integer(s): ").strip()
        if not raw:
            continue
        parts = raw.split()
        try:
            nums = [int(p) for p in parts]
        except ValueError:
            print("  Please enter only integers.")
            continue
        values.extend(nums[:remaining])

    return values[:16]


# ----------------------------
# Alpha-Beta on implicit binary tree
# ----------------------------
def alphabeta(
    leaves: List[int],
    node_index: int,
    depth: int,
    alpha: int,
    beta: int,
    maximizing: bool,
    indent: str = "",
) -> int:
    """
    Alpha-beta minimax on an implicit full binary tree.

    - leaves length must be 2**root_depth (here 16 and root_depth=4).
    - node_index is the index at this depth in the implicit tree.
      At depth=0, node_index is the leaf index (0..15).
    """
    node_type = "MAX" if maximizing else "MIN"
    v = -INF if maximizing else INF

    print(f"{indent}Enter {node_type} d={depth} n={node_index}   "
          f"v:{fmt(v)}  a:{fmt(alpha)}  b:{fmt(beta)}")

    # Terminal
    if depth == 0:
        v = leaves[node_index]
        print(f"{indent}Exit  {node_type} d={depth} n={node_index}   return v={v}\n")
        return v

    for child in (0, 1):
        child_index = node_index * 2 + child

        # 1) Before calling child
        print(f"{indent}  Check child {child}:     "
              f"v:{fmt(v)}  a:{fmt(alpha)}  b:{fmt(beta)}")

        # 2) Call child
        r = alphabeta(
            leaves=leaves,
            node_index=child_index,
            depth=depth - 1,
            alpha=alpha,
            beta=beta,
            maximizing=not maximizing,
            indent=indent + "    ",
        )

        # 3) After child returns
        print(f"{indent}  Child {child} returns:   r={r}")

        old_v, old_a, old_b = v, alpha, beta

        # Update v and bounds
        if maximizing:
            v = max(v, r)
            alpha = max(alpha, v)
        else:
            v = min(v, r)
            beta = min(beta, v)

        # 4) Show updates
        print(
            f"{indent}  Update after c{child}:   "
            f"v:{fmt_update(old_v, v)}  "
            f"a:{fmt_update(old_a, alpha)}  "
            f"b:{fmt_update(old_b, beta)}"
        )

        # 5) Prune
        if alpha >= beta:
            print(f"{indent}  PRUNE after c{child}:    "
                  f"a={fmt(alpha)} ≥ b={fmt(beta)}   "
                  f"(skip remaining children)")
            break

    print(f"{indent}Exit  {node_type} d={depth} n={node_index}   "
          f"return v={fmt(v)}\n")
    return v


# ----------------------------
# Main
# ----------------------------
def main() -> None:
    leaves = input_16_integers()

    print("\nLeaf list (index:value):")
    for i, v in enumerate(leaves):
        print(f"  {i}: {v}")

    print("\n=== Alpha-Beta Trace (root is MAX, depth=4) ===\n")
    result = alphabeta(
        leaves=leaves,
        node_index=0,
        depth=4,          # because 2**4 = 16 leaves
        alpha=-INF,
        beta=INF,
        maximizing=True,  # root is MAX
        indent="",
    )

    print(f"FINAL RESULT at root = {result}")


if __name__ == "__main__":
    main()
