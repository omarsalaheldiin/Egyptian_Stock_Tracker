# Frontend — React (Vite) + Tailwind

Prerequisites
- Node.js 16+ (Node 18 recommended)

Local development (PowerShell)
```powershell
cd frontend
npm install
$env:VITE_API_BASE = "http://localhost:8000/api"
npm run dev
```

Local development (bash)
```bash
cd frontend
npm install
VITE_API_BASE="http://localhost:8000/api" npm run dev
```

Notes
- The frontend reads the API base from `VITE_API_BASE` with a fallback of `http://localhost:8000/api`.
- Dev server default: `http://localhost:5173`.
- Update `frontend/src/api.js` if you need a hard-coded base.
