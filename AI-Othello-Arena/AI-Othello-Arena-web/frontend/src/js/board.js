import { apiNewGame, apiAiMove } from './api.js';

const canvas = document.getElementById('board');
const ctx = canvas.getContext('2d');
const size = 8; const cell = canvas.width / size;
let board = []; let turn = 1;

function draw(){
  ctx.fillStyle = '#2a7a2a'; ctx.fillRect(0,0,canvas.width,canvas.height);
  ctx.strokeStyle = '#000';
  for(let i=0;i<=size;i++){
    ctx.beginPath(); ctx.moveTo(i*cell,0); ctx.lineTo(i*cell,canvas.height); ctx.moveTo(0,i*cell); ctx.lineTo(canvas.width,i*cell); ctx.stroke();
  }
  for(let r=0;r<size;r++){
    for(let c=0;c<size;c++){
      if(board[r][c]===1){ drawStone(r,c,'#000'); }
      else if(board[r][c]===-1){ drawStone(r,c,'#fff'); }
    }
  }
}
function drawStone(r,c,color){ const padding = cell*0.08; ctx.beginPath(); ctx.fillStyle=color; ctx.ellipse(c*cell+cell/2, r*cell+cell/2, cell/2-padding, cell/2-padding, 0, 0, Math.PI*2); ctx.fill(); }
function log(s){ document.getElementById('log').textContent = s + '\n' + document.getElementById('log').textContent }

canvas.addEventListener('click', (ev)=>{
  const rect = canvas.getBoundingClientRect(); const x = ev.clientX-rect.left; const y = ev.clientY-rect.top; const c = Math.floor(x/cell); const r = Math.floor(y/cell);
  try{ if(board[r][c]!==0){log('そこには置けません');return;} board[r][c]=turn; draw(); log(`あなた: ${String.fromCharCode(65+c)}${r+1}`); turn=-turn; }catch(e){console.error(e)}
});

document.getElementById('new').addEventListener('click', async ()=>{ const res = await apiNewGame(); board = res.board; turn = res.turn; draw(); log('新しいゲーム'); });
document.getElementById('ai-move').addEventListener('click', async ()=>{ const engine = document.getElementById('engine').value; const res = await apiAiMove(board, turn, engine); if(res.move===null){ log('AI: pass'); turn=res.turn; return;} board = res.board; turn = res.turn; draw(); log(`AI(${engine}): ${String.fromCharCode(65+res.move[1])}${res.move[0]+1}`); });
window.onload = ()=>{ document.getElementById('new').click(); }
