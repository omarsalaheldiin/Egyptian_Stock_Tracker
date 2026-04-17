import os
from pathlib import Path
import pandas as pd
from typing import Dict, Any

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"
WATCHLISTS_CSV = DATA_DIR / "watchlists.csv"
RECOMMENDATIONS_CSV = DATA_DIR / "recommendations.csv"
PORTFOLIO_CSV = DATA_DIR / "portfolio.csv"


def ensure_data_files():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not WATCHLISTS_CSV.exists() or WATCHLISTS_CSV.stat().st_size == 0:
        pd.DataFrame(columns=["id", "name", "description"]).to_csv(WATCHLISTS_CSV, index=False)
    if not RECOMMENDATIONS_CSV.exists() or RECOMMENDATIONS_CSV.stat().st_size == 0:
        pd.DataFrame(columns=["id", "watchlist_id", "ticker", "status", "recommender_name", "date_added"]).to_csv(RECOMMENDATIONS_CSV, index=False)
    if not PORTFOLIO_CSV.exists() or PORTFOLIO_CSV.stat().st_size == 0:
        pd.DataFrame(columns=["ticker", "total_shares", "average_cost", "current_value_pounds"]).to_csv(PORTFOLIO_CSV, index=False)


def _read_csv(path: Path, dtype: Dict[str, Any] = None) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path, dtype=dtype)
    except Exception:
        return pd.read_csv(path)


def _write_csv(path: Path, df: pd.DataFrame):
    df.to_csv(path, index=False)


### Watchlists ###
def list_watchlists() -> pd.DataFrame:
    df = _read_csv(WATCHLISTS_CSV)
    if df.empty:
        return pd.DataFrame(columns=["id", "name", "description"])
    return df


def create_watchlist(data: Dict[str, Any]) -> Dict[str, Any]:
    df = list_watchlists()
    next_id = int(df["id"].max()) + 1 if not df.empty else 1
    row = {"id": next_id, "name": data.get("name", ""), "description": data.get("description", "")}
    df = df.append(row, ignore_index=True) if not df.empty else pd.DataFrame([row])
    _write_csv(WATCHLISTS_CSV, df)
    return row


def update_watchlist(watchlist_id: int, data: Dict[str, Any]) -> Dict[str, Any] | None:
    df = list_watchlists()
    if df.empty or int(watchlist_id) not in df["id"].values:
        return None
    df.loc[df["id"] == int(watchlist_id), ["name", "description"]] = [data.get("name", ""), data.get("description", "")]
    _write_csv(WATCHLISTS_CSV, df)
    return df[df["id"] == int(watchlist_id)].iloc[0].to_dict()


def delete_watchlist(watchlist_id: int) -> bool:
    df = list_watchlists()
    if df.empty or int(watchlist_id) not in df["id"].values:
        return False
    df = df[df["id"] != int(watchlist_id)]
    _write_csv(WATCHLISTS_CSV, df)
    return True


### Recommendations ###
def list_recommendations() -> pd.DataFrame:
    df = _read_csv(RECOMMENDATIONS_CSV)
    if df.empty:
        return pd.DataFrame(columns=["id", "watchlist_id", "ticker", "status", "recommender_name", "date_added"])
    # normalize tickers
    df["ticker"] = df["ticker"].astype(str).str.upper()
    return df


def create_recommendation(data: Dict[str, Any]) -> Dict[str, Any]:
    df = list_recommendations()
    next_id = int(df["id"].max()) + 1 if not df.empty else 1
    row = {
        "id": next_id,
        "watchlist_id": int(data.get("watchlist_id", 0)),
        "ticker": str(data.get("ticker", "")).upper(),
        "status": data.get("status", ""),
        "recommender_name": data.get("recommender_name", ""),
        "date_added": data.get("date_added") or ""
    }
    df = df.append(row, ignore_index=True) if not df.empty else pd.DataFrame([row])
    _write_csv(RECOMMENDATIONS_CSV, df)
    return row


def update_recommendation(rec_id: int, data: Dict[str, Any]) -> Dict[str, Any] | None:
    df = list_recommendations()
    if df.empty or int(rec_id) not in df["id"].values:
        return None
    df.loc[df["id"] == int(rec_id), ["watchlist_id", "ticker", "status", "recommender_name", "date_added"]] = [
        int(data.get("watchlist_id", 0)), str(data.get("ticker", "")).upper(), data.get("status", ""), data.get("recommender_name", ""), data.get("date_added", "")
    ]
    _write_csv(RECOMMENDATIONS_CSV, df)
    return df[df["id"] == int(rec_id)].iloc[0].to_dict()


def delete_recommendation(rec_id: int) -> bool:
    df = list_recommendations()
    if df.empty or int(rec_id) not in df["id"].values:
        return False
    df = df[df["id"] != int(rec_id)]
    _write_csv(RECOMMENDATIONS_CSV, df)
    return True


### Portfolio ###
def read_portfolio() -> pd.DataFrame:
    df = _read_csv(PORTFOLIO_CSV)
    if df.empty:
        return pd.DataFrame(columns=["ticker", "total_shares", "average_cost", "current_value_pounds"])
    df["ticker"] = df["ticker"].astype(str).str.upper()
    return df


def create_portfolio_item(data: Dict[str, Any]) -> Dict[str, Any]:
    df = read_portfolio()
    ticker = str(data.get("ticker", "")).upper()
    row = {
        "ticker": ticker,
        "total_shares": float(data.get("total_shares", 0)),
        "average_cost": float(data.get("average_cost", 0)),
        "current_value_pounds": float(data.get("current_value_pounds", 0)),
    }
    if not df.empty and ticker in df["ticker"].values:
        df.loc[df["ticker"] == ticker, ["total_shares", "average_cost", "current_value_pounds"]] = [row["total_shares"], row["average_cost"], row["current_value_pounds"]]
    else:
        df = df.append(row, ignore_index=True) if not df.empty else pd.DataFrame([row])
    _write_csv(PORTFOLIO_CSV, df)
    return row


def update_portfolio_item(ticker: str, data: Dict[str, Any]) -> Dict[str, Any] | None:
    df = read_portfolio()
    ticker = ticker.upper()
    if df.empty or ticker not in df["ticker"].values:
        return None
    df.loc[df["ticker"] == ticker, ["total_shares", "average_cost", "current_value_pounds"]] = [float(data.get("total_shares", 0)), float(data.get("average_cost", 0)), float(data.get("current_value_pounds", 0))]
    _write_csv(PORTFOLIO_CSV, df)
    return df[df["ticker"] == ticker].iloc[0].to_dict()


def delete_portfolio_item(ticker: str) -> bool:
    df = read_portfolio()
    ticker = ticker.upper()
    if df.empty or ticker not in df["ticker"].values:
        return False
    df = df[df["ticker"] != ticker]
    _write_csv(PORTFOLIO_CSV, df)
    return True
