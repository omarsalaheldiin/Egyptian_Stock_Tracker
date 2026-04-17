from pydantic import BaseModel
from typing import Optional


class WatchlistCreate(BaseModel):
    name: str
    description: Optional[str] = ""


class RecommendationCreate(BaseModel):
    watchlist_id: int
    ticker: str
    status: str
    recommender_name: str
    date_added: Optional[str] = None


class PortfolioItemCreate(BaseModel):
    ticker: str
    total_shares: float
    average_cost: float
    current_value_pounds: float
