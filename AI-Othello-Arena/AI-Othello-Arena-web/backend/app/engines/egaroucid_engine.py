# stub Egaroucid engine: prefer corners then max flips
import os
import json
from logic.board import Board

class EgaroucidEngine:
    def __init__(self):
        self.path = os.getenv('EGAROUCID_PATH', '/usr/local/bin/egaroucid')

    def best_move(self, board_json, turn):
        b = Board.from_json(board_json)
        candidates = b.legal_moves(turn)
        if not candidates:
            return {"move": None, "board": board_json, "turn": -turn}
        for corner in [(0,0),(0,7),(7,0),(7,7)]:
            if corner in candidates:
                move = corner
                nb = Board.from_json(board_json)
                nb.apply_move(move[0], move[1], turn)
                return {"move": [move[0], move[1]], "board": nb.to_json(), "turn": -turn}
        best = None; best_flips = -1
        for (r,c) in candidates:
            nb = Board.from_json(board_json)
            nb.apply_move(r,c,turn)
            flips = sum(1 for rr in range(8) for cc in range(8) if nb.board[rr][cc]==turn)
            if flips > best_flips:
                best_flips = flips; best = (r,c)
        nb = Board.from_json(board_json)
        nb.apply_move(best[0], best[1], turn)
        return {"move": [best[0], best[1]], "board": nb.to_json(), "turn": -turn}
