# 📈 Egyptian Stock Tracker - Web App

A **professional web application** for tracking your stock positions and investment recommendations in the Egyptian stock market.

**Built with**: React 18 • FastAPI • Tailwind CSS • Docker • Framer Motion

---

## 🎯 Quick Start (30 seconds)

### For First-Time Docker Users

➡️ **Read this first**: [DOCKER_BEGINNER_GUIDE.md](DOCKER_BEGINNER_GUIDE.md)  
(🕐 Takes 10 minutes, explains everything step-by-step)

### For Docker Users

```bash
docker-compose up
```

Then open: **http://localhost:3000**

---

## ✨ Features

### 📊 Portfolio Management
- ✅ Track all your stock holdings with amounts in EGP
- ✅ Add, update, delete stocks easily
- ✅ Real-time stats (total value, count, average)
- ✅ Animated card interface

### 📋 Watchlist Management
- ✅ Create multiple investment strategy watchlists
- ✅ Add stocks with 4 recommendation statuses:
  - 🟢 **Buy** - Green (Emerald)
  - 🔵 **Hold** - Blue
  - 🟡 **Take Profit** - Amber/Gold
  - 🟣 **Invest** - Violet
- ✅ Each position = 10,000 EGP
- ✅ Manage items (edit/delete)

### 📈 Summary & Analysis
- ✅ **Full Summary**: ALL stocks across all watchlists
- ✅ **Individual Analysis**: Focus on one watchlist
- ✅ **Variance Tracking**: Actual vs recommended positions
- ✅ **Color-Coded Status**:
  - 🟢 Matched - Position matches recommendation
  - 🔵 Over-allocated - You hold more than recommended
  - 🟡 Under-allocated - You hold less than recommended
  - 🔴 Missing - Stock not in portfolio

### 🎨 Professional UI
- ✅ Beautiful gradient design
- ✅ Smooth animations & transitions
- ✅ Glass morphism effects
- ✅ Fully responsive (mobile, tablet, desktop)
- ✅ Color-coded status indicators
- ✅ Toast notifications

---

## 📁 Project Structure

```
My_Stock_Tracker/
│
├── 🐳 DOCKER SETUP
│   ├── docker-compose.yml       ← Main orchestration file
│   ├── Dockerfile.backend       ← Backend container blueprint
│   ├── Dockerfile.frontend      ← Frontend container blueprint
│   └── DOCKER_BEGINNER_GUIDE.md ← Step-by-step guide (NEW USERS START HERE!)
│
├── 🔙 BACKEND (FastAPI)
│   ├── main.py                  ← REST API (350+ lines)
│   ├── app/
│   │   ├── models.py           ← Pydantic data models
│   │   └── data_manager.py     ← CSV data management
│   └── requirements.txt         ← Python dependencies
│
├── 🎨 FRONTEND (React)
│   ├── src/
│   │   ├── App.jsx             ← Main app (150+ lines)
│   │   ├── main.jsx            ← Entry point
│   │   ├── index.css           ← Global Tailwind styles
│   │   └── components/
│   │       ├── PortfolioTab.jsx      (200+ lines)
│   │       ├── WatchlistTab.jsx      (250+ lines)
│   │       ├── SummaryTab.jsx        (200+ lines)
│   │       ├── LoadingSpinner.jsx
│   │       ├── Toast.jsx
│   │       └── StatsCard.jsx
│   ├── src/services/api.js     ← Axios API client
│   ├── package.json            ← Dependencies
│   ├── tailwind.config.js      ← Tailwind config (custom theme)
│   ├── vite.config.js          ← Vite build config
│   └── index.html              ← HTML template
│
├── 💾 DATA
│   └── data/
│       ├── portfolios.csv      ← Your stock holdings
│       ├── watchlists.csv      ← Watchlist definitions
│       └── watchlist_items.csv ← Recommendations
│
├── 📚 DOCUMENTATION
│   └── docs/
│       ├── QUICKSTART.md                    ← Fast setup (5 mins)
│       ├── REACT_COMPONENTS_GUIDE.md        ← Component details
│       ├── API_REFERENCE.md                 ← API endpoints
│       ├── DEVELOPER_GUIDE.md               ← Architecture & code
│       ├── DEPLOYMENT_GUIDE.md              ← Production setup
│       ├── TROUBLESHOOTING.md               ← Problem solving
│       └── WEB_APP_SETUP.md                 ← Detailed setup
│
└── 📄 CONFIG
    ├── LICENSE
    └── .gitignore
```

---

## 🚀 Getting Started

### Step 1: Install Docker (If Not Already Installed)

**Windows 10/11**: 
- Download [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop)
- Install and restart computer
- Verify: Open Command Prompt and type `docker --version`

**Mac**:
- Download [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop)
- Install and drag to Applications
- Verify: Open Terminal and type `docker --version`

**Linux** (Ubuntu/Debian):
```bash
sudo apt-get install docker.io docker-compose
docker --version
```

📖 **Need detailed help?** → [DOCKER_BEGINNER_GUIDE.md](DOCKER_BEGINNER_GUIDE.md)

---

### Step 2: Run the Project

1. **Open Terminal/Command Prompt**
2. **Navigate** to project folder:
   ```bash
   cd D:\Projects\My_Stock_Tracker
   ```
3. **Start the app**:
   ```bash
   docker-compose up
   ```
4. **Wait** for messages:
   ```
   backend  | INFO:     Application startup complete
   frontend | VITE v5.x.x  ready in xxx ms
   ```
5. **Open browser** to: **http://localhost:3000**

---

### Step 3: Stop the App

In the same terminal where `docker-compose up` is running:

Press: **Ctrl+C**

---

## 🌐 Access Points

| Service | URL | Purpose |
|---------|-----|---------|
| **Frontend** | http://localhost:3000 | The app you use |
| **Backend API** | http://localhost:8000 | API server |
| **API Docs** | http://localhost:8000/docs | Interactive API testing |

---

## 💻 Technology Stack

### Backend
- **Framework**: FastAPI 0.104.1
- **Server**: Uvicorn
- **Validation**: Pydantic
- **Language**: Python 3.11
- **Container**: Docker

### Frontend
- **Framework**: React 18
- **Build Tool**: Vite 4
- **Styling**: Tailwind CSS 3.4
- **Animation**: Framer Motion
- **HTTP Client**: Axios
- **Icons**: Lucide React
- **Package Manager**: npm
- **Container**: Docker

### Data Storage
- **Format**: CSV files
- **Location**: `/data` folder
- **Persistence**: Survives container restarts

---

## 📊 API Endpoints

### Portfolio Management
- `GET /api/portfolio` - Get all stocks
- `POST /api/portfolio` - Add/update stock
- `DELETE /api/portfolio/{stock_name}` - Delete stock

### Watchlist Management
- `GET /api/watchlists` - Get all watchlists
- `POST /api/watchlists` - Create watchlist
- `DELETE /api/watchlists/{id}` - Delete watchlist

### Watchlist Items
- `GET /api/watchlists/{id}/items` - Get items
- `POST /api/watchlists/{id}/items` - Add item
- `PUT /api/watchlists/{id}/items/{stock}` - Update item
- `DELETE /api/watchlists/{id}/items/{stock}` - Delete item

### Summary
- `GET /api/summary/full` - Full summary
- `GET /api/summary/watchlist/{id}` - Watchlist summary

📖 Full API docs: http://localhost:8000/docs (when running)

---

## 🎮 Usage Example

### 1. Add a Stock
1. Click **Portfolio** tab
2. Click **Add Stock**
3. Enter: `ETELECOM`
4. Enter Amount: `30000`
5. Click **Add**
6. ✅ Stock appears in list

### 2. Create a Watchlist
1. Click **Watchlist** tab
2. Enter name: `Tech Stocks`
3. Click **Create**
4. Click on created watchlist
5. Add the stock above as "Buy"
6. ✅ Stock added to watchlist

### 3. View Summary
1. Click **Summary** tab
2. See analysis of your holdings vs recommendations
3. Switch between Full and Individual views

---

## ⚙️ Configuration

### Environment Variables

**Backend** (.env in `/backend`):
```env
DEBUG=False
SECRET_KEY=your-secret-key
CORS_ORIGINS=http://localhost:3000
```

**Frontend** (.env in `/frontend`):
```env
VITE_API_URL=http://localhost:8000
VITE_APP_NAME=Stock Tracker
```

### Tailwind Theme Customization

Edit `frontend/tailwind.config.js`:
```javascript
colors: {
  primary: '#0ea5e9',      // Change primary color
  accent: {
    emerald: '#10b981',
    amber: '#f59e0b',
    rose: '#ef4444',
    violet: '#8b5cf6'
  }
}
```

Then restart: `docker-compose up --build`

---

## 🆘 Troubleshooting

### Common Issues

| Problem | Solution |
|---------|----------|
| "docker: command not found" | Install Docker Desktop and restart computer |
| "Port 3000 already in use" | `docker-compose down` then `docker-compose up` |
| "Cannot connect to localhost:3000" | Wait for "ready in" message in terminal |
| App loads but no data | Check `data/` folder exists |
| Very slow first run | Normal! First run builds images (2-5 mins) |

📖 More help: [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)

---

## 📚 Documentation

| Document | Purpose | For |
|----------|---------|-----|
| **[DOCKER_BEGINNER_GUIDE.md](DOCKER_BEGINNER_GUIDE.md)** | Complete Docker setup guide | Everyone (first time) |
| [docs/QUICKSTART.md](docs/QUICKSTART.md) | Quick start reference | Experienced users |
| [docs/API_REFERENCE.md](docs/API_REFERENCE.md) | All API endpoints | Developers |
| [docs/REACT_COMPONENTS_GUIDE.md](docs/REACT_COMPONENTS_GUIDE.md) | UI component details | Frontend devs |
| [docs/DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md) | Architecture & code | Backend devs |
| [docs/DEPLOYMENT_GUIDE.md](docs/DEPLOYMENT_GUIDE.md) | Production setup | DevOps/Admins |
| [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) | Problem solving | Everyone |

---

## 🎯 Docker Commands Cheat Sheet

```bash
# Start the app
docker-compose up

# Start in background
docker-compose up -d

# Stop everything
docker-compose down

# View logs
docker-compose logs

# View specific service logs
docker-compose logs backend
docker-compose logs frontend

# Rebuild after code changes
docker-compose up --build

# Clean rebuild (clear cache)
docker-compose up --build --force-recreate
```

---

## 🔒 Data & Security

- ✅ All data stored locally in `/data` folder (CSV files)
- ✅ No external API calls
- ✅ No data sent to cloud
- ✅ Data persists after container stops
- ✅ Safe to use online or offline

---

## 💡 Tips & Tricks

### Tip 1: Check API Interactively
Visit http://localhost:8000/docs while app is running to test API endpoints

### Tip 2: View Logs Separately
```bash
# Terminal 1: Run app
docker-compose up

# Terminal 2: Tail logs
docker-compose logs -f
```

### Tip 3: Rebuild on Code Changes
```bash
docker-compose up --build
```

### Tip 4: Clean Everything
```bash
docker-compose down
docker system prune -a
docker-compose up
```

---

## ✅ What You Get

- ✅ Production-ready web application
- ✅ Professional design with animations
- ✅ 12 REST API endpoints
- ✅ Complete documentation
- ✅ Docker containerization
- ✅ Data persistence
- ✅ Responsive design
- ✅ Error handling & validation
- ✅ Ready to customize
- ✅ Ready to deploy

---

## 📞 Support

### If Something Goes Wrong

1. Check [DOCKER_BEGINNER_GUIDE.md](DOCKER_BEGINNER_GUIDE.md) - Common fixes section
2. Check [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) - All issues documented
3. Check terminal output - Most errors explained there
4. Google the error message - Usually has solutions

---

## 🎉 Ready to Start?

**First time users**: Start with [DOCKER_BEGINNER_GUIDE.md](DOCKER_BEGINNER_GUIDE.md)

**Experienced Docker users**: Just run:
```bash
docker-compose up
```

**Questions?** Check [docs/QUICKSTART.md](docs/QUICKSTART.md) or [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file

---

## 🙏 Version

**Current**: 2.0 (Web App with Docker)  
**Status**: ✅ Production Ready  
**Last Updated**: April 2026

---

**Happy tracking! 📈**
