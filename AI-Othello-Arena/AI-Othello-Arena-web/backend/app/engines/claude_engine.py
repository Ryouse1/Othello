# stub Claude engine: simple heuristic or Anthropic client if available
import os
try:
    import anthropic
except Exception:
    anthropic = None
from logic.board import Board

class ClaudeEngine:
    def __init__(self):
        self.client = None
        if os.getenv('ANTHROPIC_API_KEY') and anthropic:
            self.client = anthropic.Client(api_key=os.getenv('ANTHROPIC_API_KEY'))

    def choose_move(self, board_json, turn):
        b = Board.from_json(board_json)
        candidates = b.legal_moves(turn)
        if not candidates:
            return {"move": None, "board": board_json, "turn": -turn}
        # prefer edges in stub
        candidates.sort(key=lambda m: (m[0] in (0,7) or m[1] in (0,7)), reverse=True)
        move = candidates[0]
        nb = Board.from_json(board_json)
        nb.apply_move(move[0], move[1], turn)
        return {"move": [move[0], move[1]], "board": nb.to_json(), "turn": -turn}
