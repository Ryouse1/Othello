# AI-Othello-Arena (Web edition) - Ready-to-run scaffold

This is a web-focused scaffold for AI-Othello-Arena:
- Backend: FastAPI (mock/hookable AI engines)
- Frontend: Static HTML + JS (Canvas) that talks to backend
- Docker Compose for easy local run (optional)

**Important**: Replace API keys and Egaroucid binary path in `.env` before enabling real AI.

## Quick start (local)
1. unzip or clone repository
2. create .env from .env.example and fill API keys
3. Backend:
   ```bash
   cd backend
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
4. Frontend:
   - Open `frontend/public/index.html` in your browser OR
   - run a simple static server: `npx serve frontend/public` or use the Docker compose included
5. Open the page and play!

## Files included
Backend:
- backend/app/main.py
- backend/app/routes.py
- backend/app/logic/board.py
- backend/app/engines/* (stubs)
- backend/requirements.txt

Frontend:
- frontend/public/index.html
- frontend/src/js/board.js
- frontend/src/js/api.js
- frontend/src/css/style.css

Docker:
- docker-compose.yml
- .env.example
- .gitignore

If you want, I can also push this to a GitHub repo for you (you must provide a repo URL or give permission), or provide exact `git` commands to create the repo and push.
