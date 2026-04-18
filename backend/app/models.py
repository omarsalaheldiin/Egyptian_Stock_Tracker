from pydantic import BaseModel, Field
from typing import List, Optional

# Portfolio Models
class PortfolioStock(BaseModel):
    stock_name: str
    amount_egp: float

class PortfolioCreate(BaseModel):
    stock_name: str
    amount_egp: float

class PortfolioUpdate(BaseModel):
    stock_name: str
    amount_egp: float

# Watchlist Models
class WatchlistCreate(BaseModel):
    watchlist_name: str

class WatchlistItem(BaseModel):
    watchlist_id: str
    watchlist_name: str

class WatchlistItemCreate(BaseModel):
    stock_name: str = Field(..., min_length=1)
    status: str = Field(..., min_length=1)

class WatchlistItemUpdate(BaseModel):
    stock_name: str
    status: str

# Summary Models
class SummaryStock(BaseModel):
    stock_name: str
    watchlists: List[dict]  # [{watchlist_name, status}, ...]
    total_positions: int
    portfolio_amount: float
    status: str

class FullSummary(BaseModel):
    stocks: List[SummaryStock]

class WatchlistSummaryItem(BaseModel):
    stock_name: str
    status: str
    position_size_egp: float
    portfolio_amount: float
    variance: float

class WatchlistSummaryResponse(BaseModel):
    watchlist_name: str
    stocks: List[WatchlistSummaryItem]

# Response Models
class SuccessResponse(BaseModel):
    success: bool
    message: str
    data: Optional[dict] = None

class ErrorResponse(BaseModel):
    error: bool
    message: str
