# Egyptian Stock Tracker - Quick Start Guide

## First Time Setup

1. **Extract or navigate to** the My_Stock_Tracker folder
2. **Run the application:**
   - **Windows**: Double-click `run.bat`
   - **Linux/Mac**: Run `bash run.sh` in terminal
   - **Manual**: Open terminal and run `python src/main.py` from the project folder

## Main Window Tabs

### 1. Portfolio Management (📈)
- **What it does**: Tracks stocks you actually own
- **Add Stock**: Enter stock name and amount in EGP, click "✚ Add/Update"
- **Delete Stock**: Select stock and click "🗑️ Delete Selected"
- **Your data**: Saved in `data/portfolios.csv`

### 2. Watchlist Management (⭐)
- **What it does**: Create investment recommendations with multiple watchlists
- **Create Watchlist**: Enter name, click "✚ Create"
- **Add Stock**: Select watchlist → enter stock name → select status (Buy/Hold/Take Profit/Invest) → click "✚ Add"
- **Delete**: Delete individual stocks or entire watchlists
- **Note**: Each stock in a watchlist = 1x position = 10,000 EGP value
- **Your data**: Saved in `data/watchlists.csv` and `data/watchlist_items.csv`

### 3. Summary (📊)
- **What it does**: Compare your actual holdings against your recommendations

**Full Summary:**
- Shows ALL stocks sorted alphabetically
- Displays which watchlists contain each stock
- Shows what action you should take (Buy/Hold/etc.)
- Compares your actual amount vs. recommended (watchlist positions × 10,000 EGP)
- Color indicator for match status

**Individual Watchlist:**
- Select a specific watchlist
- See detailed breakdown:
  - Each stock's recommended size (10,000 EGP)
  - Your actual position
  - Difference (variance)
  - Color-coded status

## Color Meanings in Summary

| Color | Meaning |
|-------|---------|
| 🟢 Green | Your position matches recommendation |
| 🔵 Light Blue | You're holding MORE than recommended |
| 🟡 Yellow | You're holding LESS than recommended |
| 🔴 Light Red | Stock not in your portfolio |

## Example: Using the App

**Scenario**: You want to track 3 different investment strategies

1. **Create Watchlists** (Watchlist tab):
   - "Conservative" - dividend stocks, Hold status
   - "Growth" - high potential, Buy status
   - "Trading" - short term positions, Buy/Sell statuses

2. **Add Stocks** to watchlists:
   - Conservative: CIB (Hold), NBKK (Hold)
   - Growth: ORHD (Buy), ELSEWEDY (Buy)
   - Trading: GrEB (Buy)

3. **Add Your Actual Holdings** (Portfolio tab):
   - CIB: 50,000 EGP (matches 5x position in Conservative)
   - NBKK: 20,000 EGP (matches 2x position in Conservative)
   - ORHD: 10,000 EGP (matches 1x position in Growth)
   - ELSEWEDY: 15,000 EGP (1.5x position in Growth)

4. **Check Summary** (Summary tab):
   - Full view: See all stocks and which watchlists they're in
   - Compare your amounts to recommendations
   - See if you're over/under allocated

## Where Your Data is Stored

Three CSV files in the `data` folder:
- **portfolios.csv** - Your actual stock holdings
- **watchlists.csv** - Names of your watchlists
- **watchlist_items.csv** - Stocks in each watchlist with their status

You can:
- Open them in Excel for manual edits
- Backup them by copying the data folder
- Share them with others or import them to other tools

## Key Concepts

**1x Position**: A unit of measurement
- 1x position = 10,000 EGP
- If you have a stock in 2 watchlists, that's 2x = 20,000 EGP recommended
- Compare to your actual position to see if you're aligned

**Watchlist**: A collection of stocks with recommendations
- You can have as many watchlists as you want
- A stock can be in multiple watchlists with different statuses

**Status**: Your action for a stock
- **Buy**: Increase position
- **Hold**: Keep as is
- **Take Profit**: Reduce position / sell
- **Invest**: New investment opportunity

## Getting Help

- **Data not appearing?** Click "🔄 Refresh" button
- **Want to edit data directly?** Open CSV files in Excel (in `data` folder)
- **Need to start fresh?** Delete everything in the `data` folder (CSV headers will recreate)
- **Application crashes?** Check that all files have proper permissions

## Tips

✓ Use descriptive watchlist names  
✓ Update portfolio amounts regularly  
✓ Check summary weekly to monitor alignment  
✓ Use different statuses to track your investment thesis  
✓ Backup your data folder regularly  

---

**Happy tracking! 🚀**
