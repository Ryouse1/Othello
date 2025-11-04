from copy import deepcopy
DIRS = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

class Board:
    def __init__(self, board=None):
        if board:
            self.board = deepcopy(board)
        else:
            self.board = [[0]*8 for _ in range(8)]
            self.board[3][3] = -1
            self.board[3][4] = 1
            self.board[4][3] = 1
            self.board[4][4] = -1

    def to_json(self):
        return self.board

    @classmethod
    def from_json(cls, j):
        return cls(j)

    def inside(self, r,c):
        return 0 <= r < 8 and 0 <= c < 8

    def legal_moves(self, turn):
        moves = []
        for r in range(8):
            for c in range(8):
                if self.board[r][c] != 0: continue
                if self._would_flip(r,c,turn):
                    moves.append((r,c))
        return moves

    def _would_flip(self, r,c,turn):
        for dr,dc in DIRS:
            rr,cc = r+dr, c+dc
            found = False
            while self.inside(rr,cc) and self.board[rr][cc] == -turn:
                found = True
                rr += dr; cc += dc
            if found and self.inside(rr,cc) and self.board[rr][cc] == turn:
                return True
        return False

    def apply_move(self, r,c,turn):
        if not self._would_flip(r,c,turn):
            raise ValueError('illegal move')
        self.board[r][c] = turn
        for dr,dc in DIRS:
            rr,cc = r+dr, c+dc
            path = []
            while self.inside(rr,cc) and self.board[rr][cc] == -turn:
                path.append((rr,cc))
                rr += dr; cc += dc
            if path and self.inside(rr,cc) and self.board[rr][cc] == turn:
                for pr,pc in path:
                    self.board[pr][pc] = turn

    def is_terminal(self):
        return len(self.legal_moves(1))==0 and len(self.legal_moves(-1))==0

    def score(self):
        s = 0
        for r in range(8):
            for c in range(8):
                s += self.board[r][c]
        return s
