import scraper
import solver
import argparse
import time


def display_board(board):
    print(*board, sep="\n", end="\n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sudoku Puzzle Solver")
    parser.add_argument("-n", "--number", type=int, help="puzzle number")
    args = parser.parse_args()

    puzzle = scraper.get_puzzle(args.number)
    print("Puzzle")
    display_board(puzzle)

    solver_ = solver.Solver(puzzle)

    start = time.perf_counter()
    solver_.solve()
    end = time.perf_counter()

    print("Solution")
    display_board(solver_.puzzle)

    print(f"Solved in {end - start:3f} seconds")
