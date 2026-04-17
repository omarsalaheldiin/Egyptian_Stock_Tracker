from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import sys

# Add parent directory to path for data manager
sys.path.insert(0, str(Path(__file__).parent))

from app.models import (
    PortfolioStock, PortfolioCreate, PortfolioUpdate,
    WatchlistCreate, WatchlistItem, WatchlistItemCreate, WatchlistItemUpdate,
    SummaryStock, FullSummary, WatchlistSummaryItem, WatchlistSummaryResponse,
    SuccessResponse, ErrorResponse
)
from app.data_manager import DataManager

# Initialize FastAPI app
app = FastAPI(
    title="Egyptian Stock Tracker API",
    description="API for tracking Egyptian stock market positions and recommendations",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize data manager
data_manager = DataManager("data")

# ==================== PORTFOLIO ENDPOINTS ====================

@app.get("/api/portfolio", response_model=list)
async def get_portfolio():
    """Get all portfolio stocks"""
    try:
        stocks = data_manager.get_all_portfolio_stocks()
        return sorted(stocks, key=lambda x: x['stock_name'])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/portfolio", response_model=SuccessResponse)
async def add_portfolio_stock(stock: PortfolioCreate):
    """Add or update a portfolio stock"""
    try:
        if stock.amount_egp <= 0:
            raise ValueError("Amount must be positive")
        data_manager.add_portfolio_stock(stock.stock_name, stock.amount_egp)
        return SuccessResponse(success=True, message="Stock added/updated successfully")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/api/portfolio/{stock_name}", response_model=SuccessResponse)
async def delete_portfolio_stock(stock_name: str):
    """Delete a portfolio stock"""
    try:
        data_manager.delete_portfolio_stock(stock_name)
        return SuccessResponse(success=True, message="Stock deleted successfully")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ==================== WATCHLIST ENDPOINTS ====================

@app.get("/api/watchlists", response_model=list)
async def get_watchlists():
    """Get all watchlists"""
    try:
        watchlists = data_manager.get_all_watchlists()
        return sorted(watchlists, key=lambda x: x['watchlist_name'])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/watchlists", response_model=dict)
async def create_watchlist(watchlist: WatchlistCreate):
    """Create a new watchlist"""
    try:
        watchlist_id = data_manager.create_watchlist(watchlist.watchlist_name)
        return {"watchlist_id": watchlist_id, "watchlist_name": watchlist.watchlist_name}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/api/watchlists/{watchlist_id}", response_model=SuccessResponse)
async def delete_watchlist(watchlist_id: str):
    """Delete a watchlist"""
    try:
        data_manager.delete_watchlist(watchlist_id)
        return SuccessResponse(success=True, message="Watchlist deleted successfully")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/watchlists/{watchlist_id}/items", response_model=list)
async def get_watchlist_items(watchlist_id: str):
    """Get all items in a watchlist"""
    try:
        items = data_manager.get_watchlist_items(watchlist_id)
        return sorted(items, key=lambda x: x['stock_name'])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/watchlists/{watchlist_id}/items", response_model=SuccessResponse)
async def add_watchlist_item(watchlist_id: str, item: WatchlistItemCreate):
    """Add a stock to a watchlist"""
    try:
        data_manager.add_watchlist_item(watchlist_id, item.stock_name, item.status)
        return SuccessResponse(success=True, message="Stock added to watchlist")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/api/watchlists/{watchlist_id}/items/{stock_name}", response_model=SuccessResponse)
async def delete_watchlist_item(watchlist_id: str, stock_name: str):
    """Delete a stock from a watchlist"""
    try:
        data_manager.delete_watchlist_item(watchlist_id, stock_name)
        return SuccessResponse(success=True, message="Stock removed from watchlist")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ==================== SUMMARY ENDPOINTS ====================

@app.get("/api/summary/full", response_model=list)
async def get_full_summary():
    """Get full summary with all stocks and watchlists"""
    try:
        portfolio_stocks = {s['stock_name']: s['amount_egp'] 
                           for s in data_manager.get_all_portfolio_stocks()}
        stocks_with_watchlists = data_manager.get_all_stocks_with_watchlists()
        watchlists_dict = {w['watchlist_id']: w['watchlist_name'] 
                          for w in data_manager.get_all_watchlists()}
        
        summary = []
        all_stocks = sorted(set(list(portfolio_stocks.keys()) + list(stocks_with_watchlists.keys())))
        
        for stock_name in all_stocks:
            watchlist_data = stocks_with_watchlists.get(stock_name, [])
            
            watchlists_info = []
            total_positions = 0
            
            for wl_id, wl_name, status in watchlist_data:
                watchlists_info.append({
                    'watchlist_name': wl_name,
                    'status': status
                })
                total_positions += 1
            
            position_egp = total_positions * 10000
            portfolio_amount = portfolio_stocks.get(stock_name, 0)
            
            if portfolio_amount > 0:
                status = "Matched" if abs(portfolio_amount - position_egp) < 1 else f"Mismatch"
            else:
                status = "Not in Portfolio" if position_egp > 0 else "No Data"
            
            summary.append({
                'stock_name': stock_name,
                'watchlists': watchlists_info,
                'total_positions': total_positions,
                'portfolio_amount': portfolio_amount,
                'status': status
            })
        
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/summary/watchlist/{watchlist_id}", response_model=dict)
async def get_watchlist_summary(watchlist_id: str):
    """Get summary for a specific watchlist"""
    try:
        portfolio_stocks = {s['stock_name']: s['amount_egp'] 
                           for s in data_manager.get_all_portfolio_stocks()}
        watchlist_items = data_manager.get_watchlist_items(watchlist_id)
        watchlists = {w['watchlist_id']: w['watchlist_name'] 
                     for w in data_manager.get_all_watchlists()}
        
        summary_items = []
        for item in sorted(watchlist_items, key=lambda x: x['stock_name']):
            stock_name = item['stock_name']
            status = item['status']
            position_egp = 10000
            portfolio_amount = portfolio_stocks.get(stock_name, 0)
            variance = portfolio_amount - position_egp
            
            summary_items.append({
                'stock_name': stock_name,
                'status': status,
                'position_size_egp': position_egp,
                'portfolio_amount': portfolio_amount,
                'variance': variance
            })
        
        return {
            'watchlist_name': watchlists.get(watchlist_id, ''),
            'stocks': summary_items
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ==================== HEALTH CHECK ====================

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": "Egyptian Stock Tracker API",
        "version": "1.0.0",
        "docs": "/docs"
    }
