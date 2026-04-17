# Backend — FastAPI

Prerequisites
- Python 3.10+ recommended

Local development (PowerShell)
```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn backend.app.main:app --reload --port 8000
```

Local development (bash)
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m uvicorn backend.app.main:app --reload --port 8000
```

Seed data
- CSV files are in `backend/data/`:
  - `watchlists.csv` — id, name, description
  - `recommendations.csv` — id, watchlist_id, ticker, status, recommender_name, date_added
  - `portfolio.csv` — ticker, total_shares, average_cost, current_value_pounds

Key endpoints
- `GET /api/watchlists` — list watchlists
- `POST /api/watchlists` — create
- `PUT /api/watchlists/{id}` — update
- `DELETE /api/watchlists/{id}` — delete
- `GET /api/recommendations` — list recommendations (optional `watchlist_id` query)
- `POST /api/recommendations` — create
- `PUT /api/recommendations/{id}` — update
- `DELETE /api/recommendations/{id}` — delete
- `GET /api/portfolio` — portfolio with computed `position_label` and sentiment summary
- `POST /api/portfolio` — add/update a portfolio item
- `PUT /api/portfolio/{ticker}` — update by ticker
- `DELETE /api/portfolio/{ticker}` — remove
- `GET /api/conflicts` — flags holdings with multiple Sell/Take Profit recommendations
- `GET /api/aggregator` — aggregated status across watchlists

Behavior notes
- Position Size calculation: `position_multiplier = current_value_pounds / 10000` (e.g. £50,000 => `5x`).
- Conflict engine: holdings with 2+ `Sell`/`Take Profit` recommendations are flagged as `High Priority Action`.

Development tips
- The backend allows all CORS origins for local development. Update `main.py` middleware for production.
- CSV files are simple persistence for this demo — you can migrate to a DB later by replacing the `store` module.
