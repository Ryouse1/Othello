const API_BASE = (window.location.hostname === 'localhost') ? 'http://localhost:8000/api' : '/api';

export async function apiNewGame(){ const r = await fetch(`${API_BASE}/new_game`); return r.json(); }
export async function apiAiMove(board, turn, engine='chatgpt'){ const r = await fetch(`${API_BASE}/ai/move?engine=${engine}`, { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({ board, turn }) }); return r.json(); }
