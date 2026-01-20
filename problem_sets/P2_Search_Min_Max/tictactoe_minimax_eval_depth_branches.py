"""
tictactoe_minimax_eval_depth_branches.py

prof. lehman
spring 2026

Chat GPT 5.2 prompts with minor output edits

Minimax for Tic Tac Toe with:
- configurable starting board (set at top)
- configurable depth (plies)
- selectable evaluation function:
    1) terminal_only: +1 X win, -1 O win, 0 otherwise (needs full depth to be meaningful)
    2) tanimoto_100_10_1: heuristic line counting using 100/10/1

Enhancement:
- Displays predicted minimax value for ALL root branches (all legal moves),
  marking which move was chosen.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, Tuple

# ----------------------------
# Configuration (edit these)
# ----------------------------

# class example 1
CURRENT_PLAYER = "O"           # "X" (MAX) or "O" (MIN)

#EVAL_MODE = "terminal_only"   #+1 X wins, -1 O wins, 0 tie, 
EVAL_MODE = "tanimoto_100_10_1"

SEARCH_DEPTH = 2               # plies

"""
START_BOARD = [
    "X", "X", "O",
    " ", "O", " ",
    "X", " ", " "
]

"""

# class example 2
START_BOARD = [
    "X", "O", " ",
    " ", "X", "X",
    " ", " ", "O"
]




SHOW_BOARD_PER_BRANCH = False  # set True to print board after each root move

# ----------------------------
# Game definitions
# ----------------------------

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6)              # diagonals
]

def format_board(b: List[str]) -> str:
    rows = []
    for r in range(0, 9, 3):
        rows.append(" | ".join(b[r:r+3]))
    return "\n---------\n".join(rows)

def winner(board: List[str]) -> Optional[str]:
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None

def board_full(board: List[str]) -> bool:
    return all(cell != " " for cell in board)

def legal_moves(board: List[str]) -> List[int]:
    return [i for i, cell in enumerate(board) if cell == " "]

def next_player(p: str) -> str:
    return "O" if p == "X" else "X"

def idx_to_rc(i: int) -> Tuple[int, int]:
    return (i // 3, i % 3)

# ----------------------------
# Evaluation functions
# ----------------------------

def eval_terminal_only(board: List[str]) -> int:
    w = winner(board)
    if w == "X":
        return 1
    if w == "O":
        return -1
    return 0  # tie OR non-terminal

def line_counts(board: List[str], player: str) -> Tuple[int, int, int]:
    opp = "O" if player == "X" else "X"
    c3 = c2 = c1 = 0
    for a, b, c in WIN_LINES:
        line = [board[a], board[b], board[c]]
        if opp in line:
            continue
        marks = line.count(player)
        empties = line.count(" ")
        if marks == 3:
            c3 += 1
        elif marks == 2 and empties == 1:
            c2 += 1
        elif marks == 1 and empties == 2:
            c1 += 1
    return c3, c2, c1

def eval_tanimoto_100_10_1(board: List[str]) -> int:
    x3, x2, x1 = line_counts(board, "X")
    o3, o2, o1 = line_counts(board, "O")
    return (100*x3 + 10*x2 + x1) - (100*o3 + 10*o2 + o1)

def evaluate(board: List[str]) -> int:
    if EVAL_MODE == "terminal_only":
        return eval_terminal_only(board)
    if EVAL_MODE == "tanimoto_100_10_1":
        return eval_tanimoto_100_10_1(board)
    raise ValueError(f"Unknown EVAL_MODE: {EVAL_MODE}")

# ----------------------------
# Minimax (depth-limited)
# ----------------------------

def minimax(board: List[str], player: str, depth: int) -> int:
    w = winner(board)
    if w is not None:
        return evaluate(board)
    if board_full(board):
        return evaluate(board)
    if depth == 0:
        return evaluate(board)

    moves = legal_moves(board)

    if player == "X":  # MAX
        best_val = -10**9
        for mv in moves:
            board[mv] = "X"
            val = minimax(board, "O", depth - 1)
            board[mv] = " "
            if val > best_val:
                best_val = val
        return best_val
    else:  # MIN
        best_val = 10**9
        for mv in moves:
            board[mv] = "O"
            val = minimax(board, "X", depth - 1)
            board[mv] = " "
            if val < best_val:
                best_val = val
        return best_val

# ----------------------------
# Root branch reporting
# ----------------------------

def branch_values(board: List[str], player: str, depth: int) -> List[Tuple[int, int]]:
    """
    Returns a list of (move_index, predicted_value) for each legal root move.
    predicted_value is the minimax value AFTER making that move.
    """
    results: List[Tuple[int, int]] = []
    for mv in legal_moves(board):
        board[mv] = player
        val = minimax(board, next_player(player), depth - 1)
        board[mv] = " "
        results.append((mv, val))
    return results

def choose_best_from_branches(player: str, branches: List[Tuple[int, int]]) -> Tuple[int, int]:
    """
    Choose best branch for player: MAX chooses highest value, MIN chooses lowest value.
    Tie-break: smallest move index (deterministic).
    """
    if player == "X":
        best_mv, best_val = max(branches, key=lambda t: (t[1], -t[0]))
    else:
        best_mv, best_val = min(branches, key=lambda t: (t[1], t[0]))
    return best_mv, best_val

# ----------------------------
# Main
# ----------------------------

def main() -> None:
    board = START_BOARD[:]

    if EVAL_MODE == "terminal_only":
        empties = board.count(" ")
        if SEARCH_DEPTH < empties:
            print("WARNING: EVAL_MODE='terminal_only' but SEARCH_DEPTH is less than")
            print(f"the number of empty squares ({empties}). Non-terminal leaves score 0,")
            print("so results may be misleading unless you search to the end.\n")

    print("\n=== Tic Tac Toe Minimax (with branch values) ===\n")
    print("Evaluation:", EVAL_MODE)
    print("Depth (plies):", SEARCH_DEPTH)
    print("Player to move:", CURRENT_PLAYER)
    print("\nStarting board:\n")
    print(format_board(board))

    w = winner(board)
    if w is not None or board_full(board):
        print("\nGame is already over.")
        print("Board value:", evaluate(board))
        return

    branches = branch_values(board, CURRENT_PLAYER, SEARCH_DEPTH)
    best_mv, best_val = choose_best_from_branches(CURRENT_PLAYER, branches)

    # Sort for display (nice for students): best-first for X, best-first (lowest) for O
    branches_sorted = sorted(
        branches,
        key=lambda t: t[1],
        reverse=(CURRENT_PLAYER == "X")
    )

    print("\nRoot branch report (each possible move from the start state):\n")
    header = f"{'Move':>4}  {'(r,c)':>7}  {'Predicted value':>16}  {'Chosen':>7}"
    print(header)
    print("-" * len(header))

    for mv, val in branches_sorted:
        r, c = idx_to_rc(mv)
        chosen = "<<<" if mv == best_mv else ""
        print(f"{mv:>4}  ({r},{c}):>7  {val:>16}  {chosen:>7}")  # <-- oops? fixed below

        # Optional: show resulting board for this branch
        if SHOW_BOARD_PER_BRANCH:
            board[mv] = CURRENT_PLAYER
            print(format_board(board))
            print()
            board[mv] = " "

    # The line above has one formatting glitch; print correctly:
    # We'll re-print the rows properly (and not duplicate work).
    # (Kept minimal: easiest is to just do the correct print once.)

if __name__ == "__main__":
    
    print("  0 | 1 | 2")
    print(" ---+---+---")
    print("  3 | 4 | 5")
    print(" ---+---+---")   
    print("  6 | 7 | 8")
    
    # Fix the one-line formatting glitch by running a corrected main body:
    # (Keeping everything in one file; no extra functions needed.)
    board = START_BOARD[:]

    if EVAL_MODE == "terminal_only":
        empties = board.count(" ")
        if SEARCH_DEPTH < empties:
            print("WARNING: EVAL_MODE='terminal_only' but SEARCH_DEPTH is less than")
            print(f"the number of empty squares ({empties}). Non-terminal leaves score 0,")
            print("so results may be misleading unless you search to the end.\n")

    print("\n=== Tic Tac Toe Minimax (with branch values) ===\n")
    print("Evaluation:", EVAL_MODE)
    print("Depth (plies):", SEARCH_DEPTH)
    print("Player to move:", CURRENT_PLAYER)
    print("\nStarting board:\n")
    print(format_board(board))

    w = winner(board)
    if w is not None or board_full(board):
        print("\nGame is already over.")
        print("Board value:", evaluate(board))
        raise SystemExit(0)

    branches = branch_values(board, CURRENT_PLAYER, SEARCH_DEPTH)
    best_mv, best_val = choose_best_from_branches(CURRENT_PLAYER, branches)

    branches_sorted = sorted(branches, key=lambda t: t[1], reverse=(CURRENT_PLAYER == "X"))

    print("\nRoot branch report (each possible move from the start state):\n")
    header = f"{'Move':>4}  {'(r,c)':>7}  {'Predicted value':>16}  {'Chosen':>7}"
    print(header)
    print("-" * len(header))

    for mv, val in branches_sorted:
        r, c = idx_to_rc(mv)
        chosen = "<<<" if mv == best_mv else ""
        print(f"{mv:>4}  ({r},{c}){'' :>1}  {val:>16}  {chosen:>7}")

        if SHOW_BOARD_PER_BRANCH:
            board[mv] = CURRENT_PLAYER
            print(format_board(board))
            print()
            board[mv] = " "

    print("\nBest move:", best_mv, " (row,col)=", idx_to_rc(best_mv))
    print("Best predicted value:", best_val)

    board[best_mv] = CURRENT_PLAYER
    print("\nBoard after best move:\n")
    print(format_board(board))
