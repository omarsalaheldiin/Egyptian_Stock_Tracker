from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from . import store
from .schemas import WatchlistCreate, RecommendationCreate, PortfolioItemCreate
from typing import List

app = FastAPI(title="Stock Intelligence System API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

store.ensure_data_files()


@app.get("/api/watchlists")
def list_watchlists():
    return store.list_watchlists().to_dict(orient="records")


@app.post("/api/watchlists")
def create_watchlist(payload: WatchlistCreate):
    wl = store.create_watchlist(payload.dict())
    return wl


@app.put("/api/watchlists/{watchlist_id}")
def update_watchlist(watchlist_id: int, payload: WatchlistCreate):
    updated = store.update_watchlist(watchlist_id, payload.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Watchlist not found")
    return updated


@app.delete("/api/watchlists/{watchlist_id}")
def delete_watchlist(watchlist_id: int):
    ok = store.delete_watchlist(watchlist_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Watchlist not found")
    return {"ok": True}


@app.get("/api/recommendations")
def list_recommendations(watchlist_id: int = None):
    df = store.list_recommendations()
    if watchlist_id is not None:
        df = df[df["watchlist_id"] == int(watchlist_id)]
    return df.to_dict(orient="records")


@app.post("/api/recommendations")
def create_recommendation(payload: RecommendationCreate):
    rec = store.create_recommendation(payload.dict())
    return rec


@app.put("/api/recommendations/{rec_id}")
def update_recommendation(rec_id: int, payload: RecommendationCreate):
    updated = store.update_recommendation(rec_id, payload.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Recommendation not found")
    return updated


@app.delete("/api/recommendations/{rec_id}")
def delete_recommendation(rec_id: int):
    ok = store.delete_recommendation(rec_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Recommendation not found")
    return {"ok": True}


@app.get("/api/portfolio")
def get_portfolio():
    portfolio = store.read_portfolio()
    recommendations = store.list_recommendations()
    result = []
    for _, row in portfolio.iterrows():
        ticker = row['ticker']
        current_value = float(row['current_value_pounds']) if row['current_value_pounds'] != "" else 0.0
        position_multiplier = current_value / 10000.0 if current_value else 0.0
        recs = recommendations[recommendations['ticker'].str.upper() == ticker.upper()]
        sentiment_counts = recs['status'].value_counts().to_dict()
        sentiment_list = [f"{count} {status}" for status, count in sentiment_counts.items()]
        sentiment_summary = ", ".join(sentiment_list) if sentiment_list else ""
        position_label = f"{position_multiplier:.2f}x" if abs(position_multiplier - int(position_multiplier)) > 1e-6 else f"{int(position_multiplier)}x"
        result.append({
            'ticker': ticker,
            'total_shares': row['total_shares'],
            'average_cost': row['average_cost'],
            'current_value_pounds': row['current_value_pounds'],
            'position_multiplier': position_multiplier,
            'position_label': position_label,
            'sentiment_summary': sentiment_summary
        })
    return result


@app.post("/api/portfolio")
def add_portfolio_item(payload: PortfolioItemCreate):
    item = store.create_portfolio_item(payload.dict())
    return item


@app.put("/api/portfolio/{ticker}")
def update_portfolio_item(ticker: str, payload: PortfolioItemCreate):
    updated = store.update_portfolio_item(ticker, payload.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Portfolio item not found")
    return updated


@app.delete("/api/portfolio/{ticker}")
def delete_portfolio_item(ticker: str):
    ok = store.delete_portfolio_item(ticker)
    if not ok:
        raise HTTPException(status_code=404, detail="Portfolio item not found")
    return {"ok": True}


@app.get("/api/conflicts")
def get_conflicts():
    portfolio = store.read_portfolio()
    recommendations = store.list_recommendations()
    conflicts = []
    for _, row in portfolio.iterrows():
        ticker = row['ticker']
        recs = recommendations[recommendations['ticker'].str.upper() == ticker.upper()]
        negative_count = recs[recs['status'].isin(['Sell', 'Take Profit'])].shape[0]
        if negative_count >= 2:
            conflicts.append({
                'ticker': ticker,
                'total_negative_recs': int(negative_count),
                'action': 'High Priority Action'
            })
    return conflicts


@app.get("/api/aggregator")
def get_aggregator():
    recs = store.list_recommendations()
    if recs.empty:
        return []
    grouped = recs.groupby('ticker')['status'].value_counts().unstack(fill_value=0)
    out = []
    for ticker in grouped.index:
        row = grouped.loc[ticker].to_dict()
        prevailing = max(row.items(), key=lambda x: x[1])[0] if row else ""
        total = int(sum(row.values()))
        out.append({
            'ticker': ticker,
            'counts': row,
            'total': total,
            'prevailing': prevailing
        })
    return out


if __name__ == "__main__":
    uvicorn.run("backend.app.main:app", host="0.0.0.0", port=8000, reload=True)
