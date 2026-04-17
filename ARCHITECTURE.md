# 📊 System Architecture & Visual Guide

## Application Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│           EGYPTIAN STOCK TRACKER APPLICATION           │
│                   (Tkinter GUI)                         │
└─────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
   ┌────▼─────┐        ┌────▼─────┐        ┌───▼────┐
   │ Portfolio │        │ Watchlist │        │Summary │
   │ Management│        │Management │        │ Window │
   └────┬─────┘        └────┬─────┘        └───┬────┘
        │                   │                   │
        │              ┌────┴─────┐              │
        │              │           │              │
        ▼              ▼           ▼              ▼
   ┌─────────────────────────────────────────────────┐
   │         DATA MANAGER (data_manager.py)          │
   │  - Read CSV files                              │
   │  - Write CSV files                             │
   │  - Manage data logic                           │
   │  - UUID generation for watchlists              │
   └────────────┬────────────────────────┬──────────┘
                │                        │
        ┌───────┴──────┐         ┌─────┴──────┐
        │              │         │            │
        ▼              ▼         ▼            ▼
   ┌─────────┐   ┌──────────┐  ┌────────────┐
   │Portfolio │   │Watchlist │  │Watchlist  │
   │s.csv    │   │s.csv     │  │Items.csv  │
   └─────────┘   └──────────┘  └────────────┘
```

## Data Flow Diagram

### Adding a Stock to Portfolio

```
User Action:
┌──────────────────────────┐
│ Enter Stock Name: "CIB"  │
│ Enter Amount: "50000"    │
│ Click: ✚ Add/Update      │
└────────────┬─────────────┘
             │
             ▼
        main.py
     _add_portfolio_stock()
             │
             ▼
      data_manager.py
   add_portfolio_stock()
             │
      ┌──────┴──────┐
      │             │
      ▼             ▼
   Check if   Write to
   exists    portfolios.csv
      │             │
      └──────┬──────┘
             │
             ▼
     ✅ Success Message
             │
             ▼
    Refresh Portfolio Table
```

### Creating a Watchlist and Adding Stocks

```
User Action 1: Create Watchlist
┌────────────────────────┐
│ Enter Name:            │
│ "Conservative"         │
│ Click: ✚ Create        │
└──────────┬─────────────┘
           │
           ▼
    DataManager
  create_watchlist()
    (Generate UUID)
           │
           ▼
    Write to
  watchlists.csv
           │
           ▼
    ✅ Watchlist Created
           │
           ▼
    Update Watchlist List

User Action 2: Add Stock to Watchlist
┌────────────────────────────┐
│ Select Watchlist           │
│ Enter Stock: "CIB"        │
│ Select Status: "Hold"      │
│ Click: ✚ Add              │
└──────────┬─────────────────┘
           │
           ▼
    DataManager
 add_watchlist_item()
           │
           ▼
    Write to
watchlist_items.csv
           │
           ▼
    ✅ Stock Added
           │
           ▼
    Refresh Items Table
```

### Displaying Summary

```
User Views Summary:
┌──────────────────────┐
│ Select View Type     │
│ ◉ Full Summary       │
└──────────┬───────────┘
           │
           ▼
  Get all stocks from
  watchlist_items.csv
           │
           ▼
  Get portfolio from
  portfolios.csv
           │
           ▼
  For each stock:
  ┌─────────────────┐
  │ Count watchlists = X │
  │ Position = X × 10000 │
  │ Compare to portfolio │
  │ Calculate variance   │
  │ Color code result    │
  └──────────┬──────┘
             ▼
    Display in Table
    (Green/Blue/Yellow/Red)
```

## Three Main Windows

### Window 1: Portfolio Management

```
╔═══════════════════════════════════════════════════╗
║ 📈 Portfolio Management                          ║
╠═══════════════════════════════════════════════════╣
║                                                   ║
║ ┌─ Add/Update Stock ────────────────────────────┐║
║ │ Stock Name: [_____________________]          │║
║ │ Amount (EGP): [___________]  [✚ Add/Update] │║
║ └──────────────────────────────────────────────┘║
║                                                   ║
║ ┌─ Your Holdings ───────────────────────────────┐║
║ │ Stock Name       │ Amount (EGP)              │║
║ ├────────────────────────────────────────────────┤║
║ │ CIB              │ 50,000.00                │║
║ │ NBKK             │ 75,000.00                │║
║ │ ORHD             │ 20,000.00                │║
║ │ ELSEWEDY         │ 15,000.00                │║
║ └──────────────────────────────────────────────┘║
║                                                   ║
║ [🗑️ Delete] [🔄 Refresh]                        ║
║                                                   ║
╚═══════════════════════════════════════════════════╝

CSV Output:
stock_name,amount_egp
CIB,50000.0
NBKK,75000.0
ORHD,20000.0
ELSEWEDY,15000.0
```

### Window 2: Watchlist Management

```
╔════════════════════════════════════════════════════════╗
║ ⭐ Watchlist Management                              ║
╠════════════════════════════════════════════════════════╣
║                                                        ║
║ ┌─ Create New Watchlist ─────────────────────────────┐║
║ │ Watchlist Name: [___________________] [✚ Create] │║
║ └────────────────────────────────────────────────────┘║
║                                                        ║
║ ┌─ Watchlists ──────┬─ Stocks in Watchlist ─────────┐║
║ │ • Conservative     │ Stock: [__________] (Status)│║
║ │ • Growth           │ [✚ Add]                     │║
║ │ • Dividend Focused │                             │║
║ │                    │ Stock Name  │ Status        │║
║ │                    ├─────────────────────────────┤║
║ │                    │ CIB         │ Hold          │║
║ │                    │ NBKK        │ Hold          │║
║ │                    └──────────────────────────────┘║
║ │                                                    ║
║ │                    [🗑️ Delete Item]              ║
║ └────────────────────────────────────────────────────┘║
║                                                        ║
║ [🗑️ Delete Watchlist] [🔄 Refresh]                   ║
║                                                        ║
╚════════════════════════════════════════════════════════╝

CSV Output:
watchlists.csv:
watchlist_id,watchlist_name
wl-001,Conservative Portfolio
wl-002,Growth Stocks
wl-003,Dividend Focused

watchlist_items.csv:
watchlist_id,stock_name,status
wl-001,CIB,Hold
wl-001,NBKK,Hold
wl-002,ORHD,Buy
wl-002,ELSEWEDY,Buy
```

### Window 3: Summary & Analysis

```
╔═══════════════════════════════════════════════════════════╗
║ 📊 Summary & Analysis                                    ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║ ◉ View Full Summary    ○ View Individual Watchlist      ║
║   [Select: Conservative ▼]                             ║
║                                                           ║
║ ┌─ Stock Summary ──────────────────────────────────────┐║
║ │ Stock │ Conservative│ Growth     │ Total│Portfolio │  ║
║ ├───────┼─────────────┼────────────┼──────┼──────────┤  ║
║ │ CIB   │ Hold (1x)   │ Buy (1x)   │ 2x   │ 50,000  │  ║
║ │ NBKK  │ Hold (1x)   │ -          │ 1x   │ 75,000  │  ║
║ │ ORHD  │ -           │ Buy (1x)   │ 1x   │ 20,000  │  ║
║ │ ELSE  │ -           │ Buy (1x)   │ 1x   │ 15,000  │  ║
║ └───────┴─────────────┴────────────┴──────┴──────────┘  ║
║                                                           ║
║ [🔄 Refresh]                                            ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝

Color Indicators:
🟢 Green  = Matched (portfolio = positions × 10,000)
🔵 Blue   = Over-allocated (portfolio > positions × 10,000)
🟡 Yellow = Under-allocated (portfolio < positions × 10,000)
🔴 Red    = Not in portfolio (stock not owned)
```

## CSV File Relationships

```
┌──────────────────────────────┐
│     watchlists.csv           │
├──────────────────────────────┤
│ watchlist_id│watchlist_name  │
├──────────────────────────────┤
│ wl-001      │Conservative    │
│ wl-002      │Growth          │
└───────┬──────────────────────┘
        │
        │ References via watchlist_id
        ▼
┌──────────────────────────────────────┐
│    watchlist_items.csv               │
├──────────────────────────────────────┤
│ watchlist_id│stock_name│status      │
├──────────────────────────────────────┤
│ wl-001      │CIB       │Hold        │
│ wl-001      │NBKK      │Hold        │
│ wl-002      │ORHD      │Buy         │
└──────────────────────────────────────┘
        │
        │ References via stock_name
        ▼
┌──────────────────────────┐
│  portfolios.csv          │
├──────────────────────────┤
│ stock_name│amount_egp    │
├──────────────────────────┤
│ CIB        │50000        │
│ NBKK       │75000        │
│ ORHD       │20000        │
└──────────────────────────┘
```

## Summary Calculation Logic

```
For each unique stock:

STEP 1: Get all watchlist entries for this stock
    SELECT * FROM watchlist_items WHERE stock_name = "CIB"
    Result: 2 entries (Conservative: Hold, Growth: Buy)

STEP 2: Calculate total positions (1x per entry)
    Total Positions = 2 × 10,000 = 20,000 EGP

STEP 3: Get actual portfolio amount
    SELECT amount_egp FROM portfolios WHERE stock_name = "CIB"
    Result: 50,000 EGP

STEP 4: Compare and determine status
    Portfolio Amount - Recommended Amount = Variance
    50,000 - 20,000 = 30,000 (OVER-ALLOCATED)
    
    Color code:
    IF variance == 0    → 🟢 Green (Matched)
    IF variance > 0     → 🔵 Blue (Over)
    IF variance < 0     → 🟡 Yellow (Under)
    IF stock_not_found  → 🔴 Red (Missing)
```

## File Modification Flow

```
User Action → GUI Function → DataManager → CSV File
                                  ↓
                          CSV Row Read/Write
                                  ↓
                          In-Memory List
                                  ↓
                          Logic Processing
                                  ↓
                          Return to GUI
                                  ↓
                          Display to User
                                  ↓
                          Save Changes to Disk
```

## Status Color Scheme

```
Professional Color Palette:
────────────────────────────────────

Primary Colors:
  🔵 #1e3a8a - Deep Blue (Header, Main)
  🔵 #2563eb - Bright Blue (Buttons, Accents)

Status Colors:
  🟢 #10b981 - Green (Success, Matched)
  🟡 #f59e0b - Amber (Warning, Under)
  🔴 #ef4444 - Red (Danger, Over)

Background:
  ⚪ #f8fafc - Light Slate (Main background)
  ⚪ #ffffff - White (Table background)

Text:
  ⚫ #1e293b - Dark Slate (Headers)
  ⚫ #0f172a - Very Dark (Table content)
```

## Position Sizing Reference

```
Understanding 1x Position:
────────────────────────────────────

Definition: 1x Position = 10,000 EGP

Examples:
  1 Watchlist Entry = 1x = 10,000 EGP
  2 Watchlist Entries = 2x = 20,000 EGP
  3 Watchlist Entries = 3x = 30,000 EGP

Real Example - CIB Stock:
  In Watchlist 1 (Conservative) = 1x = 10,000
  In Watchlist 2 (Growth) = 1x = 10,000
  In Watchlist 3 (Dividend) = 1x = 10,000
  ─────────────────────────────────────────
  Total Recommendation = 3x = 30,000 EGP

Your Portfolio: 50,000 EGP
Result: +20,000 EGP over recommendation
```

## System Flow Diagram

```
┌─────────────────────┐
│  Application Start  │
└──────────┬──────────┘
           │
           ▼
    ┌─────────────────┐
    │ Initialize GUI  │
    │ 3 Tab Windows   │
    └──────┬──────────┘
           │
           ▼
    ┌──────────────────────┐
    │  DataManager Init    │
    │  Check CSV Files     │
    │  Create if missing   │
    └──────┬───────────────┘
           │
           ▼
    ┌─────────────────────────────────────┐
    │  Application Running                │
    │  User can:                          │
    │  - View tabs                        │
    │  - Enter data                       │
    │  - Save to CSV                      │
    │  - View summaries                   │
    └──────┬────────────────────────────┘
           │
           ▼
    ┌────────────────────┐
    │  All data saved    │
    │  in CSV files      │
    │  Persistent        │
    └────────────────────┘
```

---

**This visual guide illustrates the complete system architecture and data flow.**
