"""
tictactoe_enumerate_games.py

prof. lehman
spring 2026

Chat GPT 5.2 prompts with minor output edits

Displays all Tic Tac Toe games without any reduction in search space for symmetry.

Set DISPLAY_LIMIT to show more/less boards

Enumerate ALL possible Tic Tac Toe games (all move sequences) assuming X starts.
For each terminal game, count:
- total completed games (move sequences that end at win or tie)
- X wins
- O wins
- ties

Also (optionally) display each terminal game's move list + final board.
Warning: printing every game is a LOT of output. Set DISPLAY_GAMES = False by default.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, Tuple

DISPLAY_GAMES = True          # Set True to print every terminal game
DISPLAY_LIMIT = 3              # If DISPLAY_GAMES is True, print at most this many games

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6)              # diagonals
]

@dataclass
class Counts:
    total_games: int = 0
    x_wins: int = 0
    o_wins: int = 0
    ties: int = 0

def winner(board: List[str]) -> Optional[str]:
    """Return 'X' or 'O' if there is a winner; otherwise None."""
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None

def board_full(board: List[str]) -> bool:
    return all(cell != " " for cell in board)

def format_board(board: List[str]) -> str:
    """Pretty 3x3 board."""
    rows = []
    for r in range(0, 9, 3):
        rows.append(" | ".join(board[r:r+3]))
    return "\n---------\n".join(rows)

def legal_moves(board: List[str]) -> List[int]:
    """Return list of empty-square indices (0..8)."""
    return [i for i, cell in enumerate(board) if cell == " "]

def backtrack_all_games(
    board: List[str],
    turn: str,
    move_seq: List[int],
    counts: Counts,
    printed: List[int]
) -> None:
    """
    Explore every possible move sequence until terminal (win or tie).
    Count terminal outcomes; optionally print them.
    """
    w = winner(board)
    if w is not None:
        counts.total_games += 1
        if w == "X":
            counts.x_wins += 1
        else:
            counts.o_wins += 1

        if DISPLAY_GAMES and printed[0] < DISPLAY_LIMIT:
            printed[0] += 1
            print(f"\nGame #{counts.total_games}  Result: {w} wins")
            print("Moves (0-8):", move_seq)
            print(format_board(board))
        return

    if board_full(board):
        counts.total_games += 1
        counts.ties += 1

        if DISPLAY_GAMES and printed[0] < DISPLAY_LIMIT:
            printed[0] += 1
            print(f"\nGame #{counts.total_games}  Result: Tie")
            print("Moves (0-8):", move_seq)
            print(format_board(board))
        return

    # Recurse for each legal move
    for mv in legal_moves(board):
        board[mv] = turn
        move_seq.append(mv)

        next_turn = "O" if turn == "X" else "X"
        backtrack_all_games(board, next_turn, move_seq, counts, printed)

        # undo
        move_seq.pop()
        board[mv] = " "

def main() -> None:
    board = [" "] * 9
    counts = Counts()
    printed = [0]  # mutable counter for printing limit

    backtrack_all_games(board, "X", [], counts, printed)

    print()
    print("=== Tic Tac Toe (all move sequences), X starts ===")
    print()

    print(f"{'Total terminal games (move sequences):':<38}{counts.total_games:>12,}")

    print()
    print(
        f"{'X wins:':<38}"
        f"{counts.x_wins:>12,} "
        f"-{counts.x_wins / counts.total_games * 100:6.2f}%"
    )

    print()
    print(
        f"{'O wins:':<38}"
        f"{counts.o_wins:>12,} "
        f"-{counts.o_wins / counts.total_games * 100:6.2f}%"
    )

    print(
        f"{'Ties:':<38}"
        f"{counts.ties:>12,} "
        f"-{counts.ties / counts.total_games * 100:6.2f}%"
    )



    if DISPLAY_GAMES:
        if counts.total_games > DISPLAY_LIMIT:
            print(f"\n(Displayed only first {DISPLAY_LIMIT} terminal games.)")

if __name__ == "__main__":
    main()
