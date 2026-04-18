# 🆘 Troubleshooting & FAQ

## ❓ Frequently Asked Questions

### Getting Started

**Q: Where do I run the application from?**
A: You can run it from anywhere, but keep the project folder intact at: `your-project-directory\`

**Q: Do I need to install anything besides Python?**
A: No! Tkinter comes with Python, and there are no other dependencies.

**Q: Can I use this on Mac/Linux?**
A: Yes! Just run `bash run.sh` instead of double-clicking `run.bat`

**Q: Where is my data stored?**
A: In three CSV files in the `data` folder: `portfolios.csv`, `watchlists.csv`, `watchlist_items.csv`

---

### Data Management

**Q: Can I edit CSV files directly in Excel?**
A: Yes! Open them in Excel, make changes, save. Just keep the column headers identical.

**Q: What happens if I delete the `data` folder?**
A: The app will recreate empty CSV files on next launch. You'll lose all data unless you have a backup.

**Q: How do I backup my data?**
A: Copy the entire `data` folder to another location, preferably with a date in the name.

**Q: Can I restore from a backup?**
A: Yes! Copy your backed-up CSV files back to the `data` folder.

**Q: What if I mess up the CSV format?**
A: Delete the file, let the app recreate it with default headers, then re-enter data manually.

---

### Portfolio Management

**Q: Can I have the same stock multiple times?**
A: No, each stock appears once. When you add it again, it updates the amount.

**Q: What if I type a stock name wrong?**
A: Delete it and add it again with the correct name.

**Q: Can I have negative amounts?**
A: No, the app validates that amounts must be positive.

**Q: How do I delete all stocks?**
A: Delete them one by one using the "🗑️ Delete Selected" button.

---

### Watchlist Management

**Q: Can I have the same stock in multiple watchlists?**
A: Yes! That's the whole point. Each entry represents one recommendation position.

**Q: Can a stock have different statuses in different watchlists?**
A: Yes! CIB can be "Hold" in one watchlist and "Buy" in another.

**Q: What's the difference between the statuses?**
A: 
- **Buy**: You want to increase/start this position
- **Hold**: Maintain current position
- **Take Profit**: Sell/reduce position
- **Invest**: Alternative recommendation for new money

**Q: Can I edit status without deleting/re-adding?**
A: Yes, delete the item and add it again with the new status.

**Q: What happens if I delete a watchlist?**
A: All stocks in that watchlist are also deleted from recommendations.

---

### Summary & Analysis

**Q: Why is my stock not showing in the summary?**
A: Make sure it's in BOTH a watchlist AND in your portfolio. Watchlist-only stocks show but with no portfolio amount.

**Q: How is the position size calculated?**
A: Each entry in a watchlist = 1x = 10,000 EGP. If a stock is in 2 watchlists, that's 2x = 20,000 EGP.

**Q: What does "Matched" mean?**
A: Your portfolio amount equals your total position recommendation (watchlists × 10,000).

**Q: What does "Mismatch" mean?**
A: Your actual amount doesn't match your recommendations exactly.

**Q: Can I view multiple stocks at once?**
A: Yes, the summary always shows all your stocks. Use filtering by watchlist to focus.

**Q: Why are some rows colored differently?**
A: Color indicates status:
- 🟢 Green: Perfect match
- 🔵 Blue: You hold more than recommended
- 🟡 Yellow: You hold less than recommended
- 🔴 Red: Not in portfolio

---

## 🐛 Troubleshooting

### Application Won't Start

**Error: "ModuleNotFoundError: No module named 'tkinter'"**
```
Solution: Install tkinter
Windows: python -m pip install tk
Mac: brew install python-tk
Linux: sudo apt-get install python3-tk
```

**Error: "Python not found"**
```
Solution: Install Python from python.org
Make sure to check "Add Python to PATH" during installation
```

**Error: "FileNotFoundError"**
```
Solution: Make sure you're in the right directory
cd your-project-directory
python src/main.py
```

---

### Data Issues

**Problem: Data doesn't save**
```
Troubleshooting:
1. Check file permissions on 'data' folder
2. Ensure CSV files are not read-only (right-click → Properties)
3. Check available disk space
4. Try running as Administrator
```

**Problem: Can't find my data**
```
Location: your-project-directory\data\
Files: portfolios.csv, watchlists.csv, watchlist_items.csv
Solution: Copy data from another location if backed up
```

**Problem: Stock amounts showing as 0**
```
Possible causes:
1. You entered text instead of numbers
2. CSV encoding is wrong
3. File didn't save properly
Solution: Re-enter the data carefully
```

**Problem: Watchlist disappeared**
```
Possible causes:
1. You deleted it
2. CSV file was corrupted
Solution: 
- Check watchlists.csv in data folder
- Restore from backup if available
- Recreate the watchlist
```

---

### Display Issues

**Problem: Table won't show any data**
```
Troubleshooting:
1. Click "🔄 Refresh" button
2. Check that data exists in CSV files
3. Try clicking on different tabs
4. Restart the application
```

**Problem: Text too small/too large**
```
Solution: This depends on your monitor resolution
The app is designed for 1400x800 minimum resolution
Try maximizing the window
```

**Problem: Colors look wrong**
```
Solution: Colors are system-dependent
The app uses standard colors that should work on all systems
If colors look off, your theme might be unusual
```

**Problem: Buttons are grayed out**
```
Solution:
- You need to select an item first
- For example, select a watchlist before clicking "Delete"
- Try clicking "🔄 Refresh" to update the interface
```

---

### Performance Issues

**Problem: App is slow**
```
Solution:
This is unlikely unless you have thousands of stocks
- CSV is a text format, not optimized for large datasets
- For > 1000 stocks, consider using a database
- Current app is optimized for < 500 stocks
```

**Problem: Takes long to open large CSV files**
```
Solution:
- This is normal for large CSV files
- If you have > 10,000 entries, consider splitting into multiple watchlists
- Or use a database-backed system
```

---

## 🔧 Advanced Troubleshooting

### CSV File Corruption

**How to check if a CSV is corrupted:**
1. Open it in a text editor (Notepad)
2. Check first line matches expected headers
3. Look for extra commas or missing quotes
4. Check for non-ASCII characters

**How to fix:**
1. Back up the corrupted file
2. Create a new CSV with correct headers
3. Manually copy data if needed
4. Test that app reads it correctly

### Reset to Factory Settings

**Complete Reset:**
```
1. Stop the application
2. Delete the entire 'data' folder
3. Start the application
4. New empty CSV files will be created
5. Sample data: Re-enter or use backup
```

**Partial Reset (Portfolio only):**
```
1. Delete 'data/portfolios.csv'
2. App will recreate it empty
3. Watchlists remain unchanged
```

**Partial Reset (Watchlists only):**
```
1. Delete 'data/watchlists.csv' and 'data/watchlist_items.csv'
2. App will recreate them empty
3. Portfolio remains unchanged
```

---

## 📋 Verification Checklist

### Before Reporting an Issue

- [ ] Python 3.7+ installed? (`python --version`)
- [ ] Tkinter available? (`python -m tkinter`)
- [ ] All files in place? (`ls your-project-directory\`)
- [ ] CSV files exist? (`ls your-project-directory\data\`)
- [ ] Tried refreshing the view? (Click 🔄)
- [ ] Tried restarting the app?
- [ ] Tried restarting your computer?
- [ ] Checked file permissions?
- [ ] Checked available disk space?
- [ ] Backed up data before making changes?

---

## 💡 Pro Tips

### Performance

✓ Keep watchlists organized by strategy
✓ Archive old watchlists instead of deleting
✓ Delete unused stocks regularly
✓ Backup data monthly

### Data Integrity

✓ Never edit CSV files while app is running
✓ Always close app before editing CSVs
✓ Keep multiple backups in different locations
✓ Test restore procedures occasionally

### Usage

✓ Use consistent stock name spelling
✓ Use meaningful watchlist names
✓ Update portfolio after each trade
✓ Check summary weekly

### Backup Strategy

```
Weekly: Copy data folder to USB
Monthly: Email backup to yourself
Quarterly: Archive old versions with dates
Location: Store backups in at least 2 places
```

---

## 🎯 When to Seek Help

### Expected Behavior (Not an Issue)

- Application takes a second to load data
- Refreshing the view takes a moment
- CSV files appear in Excel with proper columns
- Colors vary slightly between systems

### Actual Issues to Report

- Application won't start at all
- Data completely disappears
- Can't add stocks no matter what
- Errors in the console/terminal
- Application crashes without saving

### How to Report Issues

1. Describe exactly what happened
2. List steps to reproduce
3. Include error messages (copy-paste)
4. Mention your OS (Windows/Mac/Linux)
5. Provide Python version (`python --version`)
6. Attach screenshots if helpful

---

## 🔑 Key Files Reference

```
Main Application:
  src/main.py

Data Management:
  src/data_manager.py

Your Data:
  data/portfolios.csv
  data/watchlists.csv
  data/watchlist_items.csv

Documentation:
  README.md              - Full guide
  QUICKSTART.md          - Quick reference
  FEATURE_DEMO.md        - Detailed walkthrough
  ARCHITECTURE.md        - System design
  INSTALLATION.md        - Setup verification
  TROUBLESHOOTING.md     - This file
```

---

## 📞 Contacts & Resources

### Python Help
- Official: https://www.python.org/
- Tkinter Docs: https://docs.python.org/3/library/tkinter.html
- Tutorials: https://www.python.org/doc/

### CSV Format
- RFC 4180: https://tools.ietf.org/html/rfc4180
- Wikipedia: https://en.wikipedia.org/wiki/Comma-separated_values

### Stock Market (Egypt)
- EGX: https://www.egx.com.eg/ (Egyptian Exchange)
- General investing: Your preferred financial resource

---

## ✨ Final Notes

- **This application uses local CSV files only** - No internet connection needed
- **All data stays on your computer** - No cloud storage or internet transmission
- **Completely free and open** - No license restrictions
- **Editable source code** - Modify as needed for your preferences
- **No ads or tracking** - Your data is yours only

---

**Need more help? Check out README.md or QUICKSTART.md**

**Happy tracking! 🚀📈**
