# stub ChatGPT engine: ranks candidates by a simple eval and optionally calls OpenAI if API key present
import os
try:
    import openai
except Exception:
    openai = None
from logic.board import Board

def simple_eval(board, turn):
    # basic heuristic: count discs
    s = sum(sum(row) for row in board)
    return s * turn

class ChatGPTEngine:
    def __init__(self):
        self.max_candidates = 6
        if os.getenv('OPENAI_API_KEY') and openai:
            openai.api_key = os.getenv('OPENAI_API_KEY')

    def choose_move(self, board_json, turn):
        b = Board.from_json(board_json)
        candidates = b.legal_moves(turn)
        if not candidates:
            return {"move": None, "board": board_json, "turn": -turn}
        scored = []
        for m in candidates:
            nb = Board.from_json(board_json)
            nb.apply_move(m[0], m[1], turn)
            scored.append((m, simple_eval(nb.to_json(), turn)))
        scored.sort(key=lambda x: x[1], reverse=True)
        move = scored[0][0]
        nb = Board.from_json(board_json)
        nb.apply_move(move[0], move[1], turn)
        return {"move": [move[0], move[1]], "board": nb.to_json(), "turn": -turn}
