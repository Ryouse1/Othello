from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from logic.board import Board
from engines.chatgpt_engine import ChatGPTEngine
from engines.claude_engine import ClaudeEngine
from engines.egaroucid_engine import EgaroucidEngine
from typing import Optional

router = APIRouter()

chatgpt = ChatGPTEngine()
claude = ClaudeEngine()
egar = EgaroucidEngine()

class MovePayload(BaseModel):
    board: list
    turn: int

@router.get('/new_game')
def new_game():
    b = Board()
    return {"board": b.to_json(), "turn": 1}

@router.post('/move')
def player_move(payload: MovePayload):
    b = Board.from_json(payload.board)
    # in this scaffold we expect client to have validated move
    return {"board": b.to_json(), "turn": payload.turn}

@router.post('/ai/move')
def ai_move(payload: MovePayload, engine: Optional[str] = 'chatgpt'):
    if engine == 'chatgpt':
        mv = chatgpt.choose_move(payload.board, payload.turn)
    elif engine == 'claude':
        mv = claude.choose_move(payload.board, payload.turn)
    elif engine == 'egaroucid':
        mv = egar.best_move(payload.board, payload.turn)
    else:
        raise HTTPException(status_code=400, detail='unknown engine')
    return mv

@router.get('/engines')
def list_engines():
    return {"engines": ["chatgpt","claude","egaroucid"]}
