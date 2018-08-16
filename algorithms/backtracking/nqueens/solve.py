import copy
import sys
# place n queens on an n-n board


class Board:
    def __init__(self, size: int, board = None, queens = None):
        self._size = size
        if queens == None:
            self._queens = []
        else:
            self._queens = queens
        if board == None:
            self._board = [[False for x in range(size)] for y in range(size)] 
        else:
            self._board = board

    def add_queen(self, x: int, y: int) -> 'Board':
        copy_board = copy.deepcopy(self._board)
        copy_board[x][y] = True
        copy_queens = copy.deepcopy(self._queens)
        copy_queens.append((x,y))
        return Board(self._size, copy_board, copy_queens)


    def valid(self) -> 'boolean':
        for queen in self._queens:
            for other_queen in list(filter(lambda q: q != queen, self._queens)):
                # todo: horizontal check
                if queen[0] == other_queen[0]:
                    return False
                if queen[1] == other_queen[1]:
                    return False
        return True

    def __str__(self) -> 'str':
        ret = ""
        for x in range(self._size):
            for y in range(self._size):
                ret += " 0 " if not self._board[x][y] else " 1 "
            ret += "\n"
        return ret
                
# go from an int to a (x,y) tuple for the next_queen
def _solve(board: Board, next_queen: int) -> 'Board':
    queen_x = next_queen // 8
    queen_y = next_queen % 8
    next_board = board.add_queen(queen_x, queen_y)
    print(next_board)
    print(board)
    if len(next_board._queens) == 8 and next_board.valid():
        print("found solution..")
        print(next_board)
        exit(0)
    if next_board.valid():
        return _solve(next_board, next_queen + 1)
    return _solve(board, next_queen + 1)



def solve() -> 'Board':
    board = Board(8) # Demo for the original 8x8 
    _solve(board, 0)


if __name__ == '__main__':
    solve()
