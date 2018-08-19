import copy
import sys
# place n queens on an n-n board


class Board:
    def __init__(self, size: int, board = None, queens = None) -> 'None':
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

    def valid_diagonal(self, this, that) -> 'boolean':
        this_x = this[0]
        this_y = this[1]
        that_x = that[0]
        that_y = that[1]
        return not abs(that_y - this_y) == abs(that_x - this_x)


    def valid(self) -> 'boolean':
        for queen in self._queens:
            other_queens = list(filter(lambda q: q != queen, self._queens))
            for other_queen in other_queens: 
                if queen[0] == other_queen[0]:
                    return False
                if queen[1] == other_queen[1]:
                    return False
                if not self.valid_diagonal(queen, other_queen):
                    return False
        return True

    def __str__(self) -> 'str':
        """ convenience dunder method for debugging """
        ret = ""
        for x in range(self._size):
            for y in range(self._size):
                ret += " 0 " if not self._board[x][y] else " 1 "
            ret += "\n"
        return ret
                
def _solve(board: Board, col: int) -> 'boolean':
    if len(board._queens) == board._size:
        return True
    if col >= board._size: # we overstepped our columns
        return False
    else:
        for row in range(board._size):
            if board.add_queen(col, row).valid():
                # place queen
                next_board = board.add_queen(col, row)
                # solve nextcol
                if _solve(next_board, col + 1):
                    print(next_board)
                    exit(0)

        # no match found
        return False





def solve() -> 'Board':
    board = Board(20) # Demo for the original 8x8 
    for i in range(board._size):
        solution = _solve(board, i)

if __name__ == '__main__':
    solve()
