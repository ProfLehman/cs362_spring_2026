"""
tictactoe_states_by_move.py

prof. lehman
spring 2026

Chat GPT 5.2 prompts with minor output edits


Counts game states at each move depth (1..9), and how many terminal outcomes
(X wins, O wins, ties) occur at each depth, assuming X starts.

"State" here means a reached board position after exactly N moves along legal play,
where play stops after a win.
"""

from dataclasses import dataclass
from typing import List, Optional

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6)              # diagonals
]

@dataclass
class LevelStats:
    states: int = 0     # number of positions reached at this move depth
    x_wins: int = 0     # terminal positions at this depth where X has won
    o_wins: int = 0     # terminal positions at this depth where O has won
    ties: int = 0       # terminal positions at this depth that are ties

def winner(board: List[str]) -> Optional[str]:
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None

def board_full(board: List[str]) -> bool:
    return all(cell != " " for cell in board)

def legal_moves(board: List[str]) -> List[int]:
    return [i for i, cell in enumerate(board) if cell == " "]

def backtrack(
    board: List[str],
    turn: str,
    move_depth: int,
    levels: List[LevelStats]
) -> None:
    """
    move_depth = number of moves already made on the board (0..9).
    When we make a move, depth becomes move_depth+1 and we record a state at that level.
    """

    # If already terminal, stop (should only happen at root in weird calls; safe guard)
    w = winner(board)
    if w is not None or board_full(board):
        return

    for mv in legal_moves(board):
        board[mv] = turn
        new_depth = move_depth + 1  # 1..9

        # Record that we reached a state at this depth
        levels[new_depth].states += 1

        w = winner(board)
        if w == "X":
            levels[new_depth].x_wins += 1
            # stop expanding (game ends)
        elif w == "O":
            levels[new_depth].o_wins += 1
            # stop expanding (game ends)
        elif board_full(board):
            levels[new_depth].ties += 1
            # stop expanding (tie ends)
        else:
            next_turn = "O" if turn == "X" else "X"
            backtrack(board, next_turn, new_depth, levels)

        # undo move
        board[mv] = " "

def main() -> None:
    # index 0 unused for convenience; we use 1..9
    levels = [LevelStats() for _ in range(10)]

    board = [" "] * 9
    backtrack(board, "X", 0, levels)

    # Output
    print()
    print("=== Tic Tac Toe: game states and outcomes by move depth (X starts) ===")
    print()
    header = f"{'Move':>4}  {'States':>12}  {'X wins':>12}  {'O wins':>12}  {'Ties':>12}"
    print(header)
    print("-" * len(header))

    for depth in range(1, 10):
        s = levels[depth]
        print(f"{depth:>4}  {s.states:>12,}  {s.x_wins:>12,}  {s.o_wins:>12,}  {s.ties:>12,}")

    # Optional totals across all depths (terminal outcomes should sum to total games)
    total_terminal = sum(levels[d].x_wins + levels[d].o_wins + levels[d].ties for d in range(1, 10))
    print()
    print(f"{'Total terminal games:':<24}{total_terminal:>12,}")

if __name__ == "__main__":
    main()
