
# place n queens on an n-n board


class Board:
    def __init__(self, size: int, board = None):
        self._size = size
        if board == None:
            self._board = [[False for x in range(size)] for y in range(size)] 
        else:
            self._board = board

    def add_queen(self, x: int, y: int) -> 'Board':
        copy_board = self._board.copy()
        copy_board[x][y] = True
        return Board(self._size, copy_board)

    def __str__(self) -> 'str':
        ret = ""
        for x in range(self._size):
            for y in range(self._size):
                ret += " 0 " if not self._board[x][y] else " 1 "
            ret += "\n"
        return ret
                
def solve(board: Board) -> 'Board':
    Board(8)


def solve() -> 'Board':
    board = Board(8)
    print(board)
    cb = board.add_queen(0,0)
    print(cb)



if __name__ == '__main__':
    solve()
