import scraper
import solver
import argparse
import time

def display_board(board):
    print(*board, sep="\n", end="\n\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sudoku Puzzle Solver')
    parser.add_argument('-n', '--number', type=int, help="puzzle number")
    args = parser.parse_args()

    puzzle = scraper.get_puzzle(args.number)
    print("Puzzle")
    display_board(puzzle)

    start = time.perf_counter() 
    solved = solver.solve(puzzle)
    end = time.perf_counter()

    print("Solution")
    display_board(solved)

    print(f"Solved in {end - start:3f} seconds")
