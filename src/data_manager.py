import csv
import os
from pathlib import Path
from typing import List, Dict, Tuple
import uuid

class DataManager:
    """Manages all CSV data operations for the stock tracker"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.portfolios_file = self.data_dir / "portfolios.csv"
        self.watchlists_file = self.data_dir / "watchlists.csv"
        self.watchlist_items_file = self.data_dir / "watchlist_items.csv"
        self._ensure_files_exist()
    
    def _ensure_files_exist(self):
        """Ensure all CSV files exist with proper headers"""
        self.data_dir.mkdir(exist_ok=True)
        
        if not self.portfolios_file.exists():
            with open(self.portfolios_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['stock_name', 'amount_egp'])
                writer.writeheader()
        
        if not self.watchlists_file.exists():
            with open(self.watchlists_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['watchlist_id', 'watchlist_name'])
                writer.writeheader()
        
        if not self.watchlist_items_file.exists():
            with open(self.watchlist_items_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['watchlist_id', 'stock_name', 'status'])
                writer.writeheader()
    
    # ==================== Portfolio Methods ====================
    
    def get_all_portfolio_stocks(self) -> List[Dict]:
        """Get all stocks in portfolio"""
        stocks = []
        with open(self.portfolios_file, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                stocks.append({'stock_name': row['stock_name'], 'amount_egp': float(row['amount_egp'])})
        return stocks
    
    def add_portfolio_stock(self, stock_name: str, amount_egp: float) -> bool:
        """Add or update a stock in portfolio"""
        stocks = self.get_all_portfolio_stocks()
        
        # Check if stock already exists
        stock_exists = False
        for stock in stocks:
            if stock['stock_name'].lower() == stock_name.lower():
                stock['amount_egp'] = amount_egp
                stock_exists = True
                break
        
        if not stock_exists:
            stocks.append({'stock_name': stock_name, 'amount_egp': amount_egp})
        
        self._write_portfolio_stocks(stocks)
        return True
    
    def delete_portfolio_stock(self, stock_name: str) -> bool:
        """Delete a stock from portfolio"""
        stocks = self.get_all_portfolio_stocks()
        stocks = [s for s in stocks if s['stock_name'].lower() != stock_name.lower()]
        self._write_portfolio_stocks(stocks)
        return True
    
    def _write_portfolio_stocks(self, stocks: List[Dict]):
        """Write stocks back to CSV"""
        with open(self.portfolios_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['stock_name', 'amount_egp'])
            writer.writeheader()
            for stock in stocks:
                writer.writerow({'stock_name': stock['stock_name'], 'amount_egp': stock['amount_egp']})
    
    # ==================== Watchlist Methods ====================
    
    def get_all_watchlists(self) -> List[Dict]:
        """Get all watchlists"""
        watchlists = []
        with open(self.watchlists_file, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                watchlists.append({'watchlist_id': row['watchlist_id'], 'watchlist_name': row['watchlist_name']})
        return watchlists
    
    def create_watchlist(self, watchlist_name: str) -> str:
        """Create a new watchlist and return its ID"""
        watchlist_id = str(uuid.uuid4())
        watchlists = self.get_all_watchlists()
        watchlists.append({'watchlist_id': watchlist_id, 'watchlist_name': watchlist_name})
        self._write_watchlists(watchlists)
        return watchlist_id
    
    def delete_watchlist(self, watchlist_id: str) -> bool:
        """Delete a watchlist and all its items"""
        watchlists = self.get_all_watchlists()
        watchlists = [w for w in watchlists if w['watchlist_id'] != watchlist_id]
        self._write_watchlists(watchlists)
        
        # Delete all items in this watchlist
        items = self.get_all_watchlist_items()
        items = [i for i in items if i['watchlist_id'] != watchlist_id]
        self._write_watchlist_items(items)
        return True
    
    def _write_watchlists(self, watchlists: List[Dict]):
        """Write watchlists back to CSV"""
        with open(self.watchlists_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['watchlist_id', 'watchlist_name'])
            writer.writeheader()
            for wl in watchlists:
                writer.writerow({'watchlist_id': wl['watchlist_id'], 'watchlist_name': wl['watchlist_name']})
    
    # ==================== Watchlist Items Methods ====================
    
    def get_all_watchlist_items(self) -> List[Dict]:
        """Get all watchlist items"""
        items = []
        with open(self.watchlist_items_file, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                items.append({
                    'watchlist_id': row['watchlist_id'],
                    'stock_name': row['stock_name'],
                    'status': row['status']
                })
        return items
    
    def get_watchlist_items(self, watchlist_id: str) -> List[Dict]:
        """Get all items for a specific watchlist"""
        all_items = self.get_all_watchlist_items()
        return [item for item in all_items if item['watchlist_id'] == watchlist_id]
    
    def add_watchlist_item(self, watchlist_id: str, stock_name: str, status: str) -> bool:
        """Add a stock to a watchlist"""
        items = self.get_all_watchlist_items()
        
        # Check if item already exists
        for item in items:
            if item['watchlist_id'] == watchlist_id and item['stock_name'].lower() == stock_name.lower():
                item['status'] = status
                self._write_watchlist_items(items)
                return True
        
        items.append({
            'watchlist_id': watchlist_id,
            'stock_name': stock_name,
            'status': status
        })
        self._write_watchlist_items(items)
        return True
    
    def delete_watchlist_item(self, watchlist_id: str, stock_name: str) -> bool:
        """Delete a stock from a watchlist"""
        items = self.get_all_watchlist_items()
        items = [i for i in items if not (i['watchlist_id'] == watchlist_id and i['stock_name'].lower() == stock_name.lower())]
        self._write_watchlist_items(items)
        return True
    
    def _write_watchlist_items(self, items: List[Dict]):
        """Write items back to CSV"""
        with open(self.watchlist_items_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['watchlist_id', 'stock_name', 'status'])
            writer.writeheader()
            for item in items:
                writer.writerow({
                    'watchlist_id': item['watchlist_id'],
                    'stock_name': item['stock_name'],
                    'status': item['status']
                })
    
    # ==================== Summary Methods ====================
    
    def get_all_stocks_with_watchlists(self) -> Dict[str, List[Tuple[str, str, str]]]:
        """Get all unique stocks with their watchlists and statuses
        Returns: {stock_name: [(watchlist_id, watchlist_name, status), ...]}
        """
        watchlists = {w['watchlist_id']: w['watchlist_name'] for w in self.get_all_watchlists()}
        items = self.get_all_watchlist_items()
        
        stocks_dict = {}
        for item in items:
            stock_name = item['stock_name']
            if stock_name not in stocks_dict:
                stocks_dict[stock_name] = []
            stocks_dict[stock_name].append((
                item['watchlist_id'],
                watchlists[item['watchlist_id']],
                item['status']
            ))
        
        return stocks_dict
    
    def get_watchlist_summary(self, watchlist_id: str) -> Dict:
        """Get summary data for a specific watchlist"""
        watchlists = {w['watchlist_id']: w['watchlist_name'] for w in self.get_all_watchlists()}
        items = self.get_watchlist_items(watchlist_id)
        
        summary = {
            'watchlist_name': watchlists.get(watchlist_id, ''),
            'stocks': []
        }
        
        for item in items:
            summary['stocks'].append({
                'stock_name': item['stock_name'],
                'status': item['status']
            })
        
        return summary
