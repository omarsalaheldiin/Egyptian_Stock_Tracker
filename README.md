# Egyptian Stock Tracker 📈

A professional desktop application for tracking your stock positions and recommendations in the Egyptian stock market.

## Features

### 📈 Portfolio Management
- Track all your actual stock holdings with their current values in EGP
- Add, update, or delete stocks from your portfolio
- View all holdings in an organized table

### ⭐ Watchlist Management
- Create multiple watchlists for different investment strategies
- Add stocks to watchlists with recommendations (Buy, Hold, Take Profit, Invest)
- Each watchlist represents a 1x position (equivalent to 10,000 EGP)
- Easily manage and update your recommendations

### 📊 Summary & Analysis
**Full Summary View:**
- View all stocks sorted alphabetically
- See which watchlists contain each stock
- View the recommendation status for each watchlist
- Compare your actual position value against your 1x position recommendations
- Identify mismatches between recommendations and actual holdings

**Individual Watchlist View:**
- Focus on a specific watchlist
- See detailed position analysis
- Track variance between recommended position size (10,000 EGP per position) and your actual holdings
- Color-coded status indicators:
  - 🟢 **Match**: Your position matches the recommendation
  - 🔵 **Over**: You hold more than recommended
  - 🟡 **Under**: You hold less than recommended
  - 🔴 **Missing**: Stock not in your portfolio

## Project Structure

```
My_Stock_Tracker/
├── data/                          # Data storage (CSV files)
│   ├── portfolios.csv            # Your actual stock holdings
│   ├── watchlists.csv            # Your watchlist definitions
│   └── watchlist_items.csv       # Stocks in each watchlist
├── src/
│   ├── main.py                   # Main application GUI
│   └── data_manager.py           # Data management and CSV operations
├── requirements.txt              # Python dependencies
├── run.bat                        # Windows launcher
├── run.sh                         # Linux/Mac launcher
└── README.md                      # This file
```

## CSV File Format

### portfolios.csv
```csv
stock_name,amount_egp
CIB,50000
NBKK,75000
```

### watchlists.csv
```csv
watchlist_id,watchlist_name
1a2b3c4d,Conservative Portfolio
5e6f7g8h,Growth Portfolio
```

### watchlist_items.csv
```csv
watchlist_id,stock_name,status
1a2b3c4d,CIB,Hold
1a2b3c4d,NBKK,Buy
5e6f7g8h,ORHD,Buy
```

## Installation & Setup

### Requirements
- Python 3.7+
- tkinter (usually comes with Python)

### Windows
1. Double-click `run.bat` to launch the application

### Linux/Mac
1. Run in terminal:
   ```bash
   bash run.sh
   ```

### Manual Run
1. Navigate to the `src` folder:
   ```bash
   cd src
   python main.py
   ```

## Usage Guide

### Adding Stocks to Your Portfolio
1. Go to **Portfolio Management** tab
2. Enter stock name and amount in EGP
3. Click **✚ Add/Update**
4. Your holdings appear in the table below

### Creating and Managing Watchlists
1. Go to **Watchlist Management** tab
2. Enter watchlist name in "Create New Watchlist" section
3. Click **✚ Create**
4. Select your watchlist from the left panel
5. Add stocks with their recommendations:
   - Enter stock name
   - Select status (Buy/Hold/Take Profit/Invest)
   - Click **✚ Add**

### Viewing Your Summary
1. Go to **Summary** tab
2. Choose view type:
   - **View Full Summary**: See all stocks and their presence across all watchlists
   - **View Individual Watchlist**: Focus on one watchlist with detailed position analysis

### Position Sizing
- Each watchlist item represents **1x position = 10,000 EGP**
- If you have 3 Buy recommendations for a stock across watchlists = 30,000 EGP recommended position
- Compare your actual position to these recommendations in the Summary tab

## Understanding the Summary View

### Full Summary Columns:
- **Stock Name**: Name of the stock (alphabetically sorted)
- **[Watchlist Names]**: Status in each watchlist (Buy, Hold, Take Profit, Invest)
- **Total Positions**: Sum of all 1x positions for this stock
- **Portfolio Amount (EGP)**: Your actual holding
- **Portfolio Status**: Comparison result (Matched/Mismatch/Not in Portfolio)

### Individual Watchlist Columns:
- **Stock Name**: Name of the stock
- **Status**: Your recommendation status
- **Position Size (EGP)**: Recommended size (10,000 per stock)
- **Your Position (EGP)**: Your actual holding
- **Variance**: Difference between your position and recommendation

## Data Storage

All data is stored in CSV format in the `data` folder:
- Easy to backup
- Can be opened with Excel or any spreadsheet application
- Can be easily imported/exported to other systems

### Backing Up Your Data
Simply copy the `data` folder to your backup location.

### Restoring Data
Copy your backed-up CSV files back to the `data` folder.

## Color Scheme & Professional Design

The application features:
- **Professional color palette**: Blues (#1e3a8a, #2563eb) for main actions
- **Green highlights**: Success and matched positions
- **Amber/Red indicators**: Warnings and mismatches
- **Clean typography**: Using Segoe UI for Windows
- **Organized layout**: Tabbed interface for easy navigation
- **Alternating row colors**: For better readability

## Tips & Best Practices

1. **Use meaningful watchlist names**: "Aggressive Growth", "Dividend Stocks", "Short Term Trading"
2. **Update regularly**: Keep your portfolio amounts current
3. **Use different statuses**: Help you track your investment thesis for each recommendation
4. **Check summary frequently**: Monitor alignment between recommendations and actual positions
5. **Backup your data**: Regularly copy your `data` folder

## Troubleshooting

**App won't start:**
- Ensure Python is installed and in your PATH
- Check that tkinter is available (usually pre-installed with Python)

**Data not saving:**
- Make sure the `data` folder exists and is writable
- Check file permissions

**Can't see my stocks in summary:**
- Make sure you've added stocks to both Portfolio and Watchlists
- Try refreshing the view

## Future Enhancements

Potential features for future versions:
- Chart/graph visualizations
- Historical tracking
- Price integration
- Export to Excel reports
- Multi-user support
- Database backend (instead of CSV)

## License

This project is provided as-is for personal use.

---

**Happy investing! 🎯📈**
