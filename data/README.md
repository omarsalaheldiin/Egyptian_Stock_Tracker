# Data Directory

This directory contains your personal portfolio and watchlist data in CSV format.

⚠️ **IMPORTANT: This folder is NOT committed to Git for security reasons.**

## Files

- `portfolios.csv` - Your current stock holdings
- `watchlists.csv` - Your investment watchlists  
- `watchlist_items.csv` - Stocks in each watchlist

## Setup Instructions

On first run, copy the example files:

```bash
cp portfolios.csv.example portfolios.csv
cp watchlists.csv.example watchlists.csv
cp watchlist_items.csv.example watchlist_items.csv
```

Then edit each file with your actual data.

## File Format

### portfolios.csv
```
stock_name,amount_egp
ETELECOM,50000.0
CIB,75000.0
```

### watchlists.csv
```
watchlist_id,watchlist_name
550e8400-e29b-41d4-a716-446655440000,Technology
```

### watchlist_items.csv
```
watchlist_id,stock_name,status
550e8400-e29b-41d4-a716-446655440000,ETELECOM,Buy
```

## Security

✅ These CSV files are in `.gitignore`  
✅ Your personal data will never be committed to Git  
✅ Safe to push to public repositories  
