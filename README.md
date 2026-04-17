# Stock Intelligence System

Full-stack demo combining a FastAPI backend (CSV-backed) with a React (Vite) frontend styled with Tailwind (dark theme).

Repository layout
- `backend/` — FastAPI app, CSV data store, and seed data under `backend/data/`.
- `frontend/` — Vite + React app, Tailwind CSS styles.

Quick start (Windows PowerShell)
```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn backend.app.main:app --reload --port 8000

# in a separate terminal:
cd frontend
npm install
$env:VITE_API_BASE = "http://localhost:8000/api"
npm run dev
```

Quick start (macOS / Linux)
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m uvicorn backend.app.main:app --reload --port 8000

# in a separate terminal:
cd frontend
npm install
VITE_API_BASE="http://localhost:8000/api" npm run dev
```

Ports & URLs
- Backend API: `http://localhost:8000/api`
- Frontend: `http://localhost:5173`

Where to look
- Backend app entry: [backend/app/main.py](backend/app/main.py)
- CSV persistence: [backend/app/store.py](backend/app/store.py)
- Frontend entry: [frontend/src/main.jsx](frontend/src/main.jsx)
- Frontend pages: [frontend/src/pages](frontend/src/pages)

Notes
- Position size calculation: `position_multiplier = current_value_pounds / 10000` (e.g. £50,000 => `5x`).
- Conflict engine endpoint: `GET /api/conflicts` flags holdings with multiple `Sell`/`Take Profit` recommendations.
- The frontend reads `VITE_API_BASE` (fallback `http://localhost:8000/api`).

Contributing
- Feel free to open issues or PRs. For production usage migrate CSV persistence to a real database and tighten CORS/security.

License
- See [LICENSE](LICENSE)
