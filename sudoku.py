import scraper
import solver
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sudoku Puzzle Solver')
    parser.add_argument('-n', '--number', type=int, help="puzzle number")
    args = parser.parse_args()
    puzzle = scraper.get_puzzle(args.number)
    solver.solve(puzzle)
