# 👨‍💻 Developer Guide - Architecture, Code Structure & Customization

## 📖 Table of Contents

1. Architecture Overview
2. Project Structure
3. Technology Stack
4. Development Workflow
5. Code Conventions
6. Customization Guide
7. Performance Optimization
8. Deployment Guide
9. Debugging & Testing

---

## 🏗️ Architecture Overview

### High-Level Design

```
┌─────────────────────────────────────────┐
│        React Frontend (Port 3000)       │
│   ├─ App.jsx (Main Container)           │
│   ├─ Components/                        │
│   │  ├─ PortfolioTab.jsx               │
│   │  ├─ WatchlistTab.jsx               │
│   │  ├─ SummaryTab.jsx                 │
│   │  └─ Utilities/                     │
│   └─ Services/api.js (HTTP Client)     │
└────────────┬────────────────────────────┘
             │ HTTP Requests
             │ (CORS Enabled)
             ▼
┌─────────────────────────────────────────┐
│      FastAPI Backend (Port 8000)        │
│   ├─ main.py (REST Endpoints)           │
│   ├─ app/                               │
│   │  ├─ models.py (Pydantic Models)    │
│   │  └─ data_manager.py (CSV Handler)  │
│   └─ data/ (CSV Storage)                │
└─────────────────────────────────────────┘
```

### Data Flow

```
User Interaction
    ↓
React Component Event Handler
    ↓
Axios API Call (HTTP)
    ↓
FastAPI Route Handler
    ↓
Pydantic Model Validation
    ↓
Data Manager (CSV Read/Write)
    ↓
Response JSON
    ↓
React State Update
    ↓
Component Re-render
    ↓
UI Update (with Framer Motion)
```

---

## 📁 Project Structure

```
My_Stock_Tracker/
├── backend/
│   ├── main.py                # FastAPI application (350+ lines)
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models.py          # Pydantic models (20+ models)
│   │   └── data_manager.py    # CSV management (250+ lines)
│   ├── requirements.txt        # Python dependencies
│   └── .env                    # Environment variables
│
├── frontend/
│   ├── src/
│   │   ├── main.jsx           # React entry point
│   │   ├── App.jsx            # Main app component (150+ lines)
│   │   ├── components/
│   │   │   ├── PortfolioTab.jsx    (200+ lines)
│   │   │   ├── WatchlistTab.jsx    (250+ lines)
│   │   │   ├── SummaryTab.jsx      (200+ lines)
│   │   │   ├── LoadingSpinner.jsx
│   │   │   ├── Toast.jsx
│   │   │   └── StatsCard.jsx
│   │   ├── services/
│   │   │   └── api.js         # Axios client (50+ lines)
│   │   └── index.css          # Global Tailwind styles
│   ├── index.html             # HTML template
│   ├── tailwind.config.js      # Tailwind configuration
│   ├── vite.config.js          # Vite dev server config
│   ├── postcss.config.js       # PostCSS configuration
│   ├── package.json            # Node.js dependencies
│   └── .env                    # Environment variables
│
├── data/
│   ├── portfolios.csv          # Stock holdings
│   ├── watchlists.csv          # Watchlist definitions
│   └── watchlist_items.csv     # Recommendations
│
├── docker-compose.yml          # Service orchestration
├── Dockerfile.backend          # Python image
├── Dockerfile.frontend         # Node.js image
│
├── Documentation/
│   ├── README.md               # Project overview
│   ├── QUICKSTART.md           # Quick start guide
│   ├── WEB_APP_SETUP.md        # Detailed setup
│   ├── API_REFERENCE.md        # API endpoints (NEW)
│   ├── REACT_COMPONENTS_GUIDE.md (NEW)
│   ├── ARCHITECTURE.md         # System design
│   ├── TROUBLESHOOTING.md      # Problem solving
│   └── this file: DEVELOPER_GUIDE.md
│
└── Scripts/
    ├── run.sh / run.bat        # Start both services
    ├── run_backend.sh/.bat     # Start backend only
    └── run_frontend.sh/.bat    # Start frontend only
```

---

## 🛠️ Technology Stack

### Backend

| Layer | Technology | Purpose | Version |
|-------|-----------|---------|---------|
| Framework | FastAPI | Web framework | 0.104.1 |
| Server | Uvicorn | ASGI server | 0.24.0 |
| Validation | Pydantic | Data validation | 2.5.0 |
| Storage | CSV (pathlib) | Data persistence | Built-in |
| Python | Python | Runtime | 3.8+ |

### Frontend

| Layer | Technology | Purpose | Version |
|-------|-----------|---------|---------|
| Framework | React | UI library | 18.x |
| Build Tool | Vite | Dev server & bundler | 4.x |
| Styling | Tailwind CSS | Utility CSS | 3.4 |
| Animation | Framer Motion | Motion library | Latest |
| HTTP Client | Axios | API requests | Latest |
| Icons | Lucide React | Icon library | Latest |
| Node | Node.js | Runtime | 18+ |

### DevOps

| Tool | Purpose | Version |
|------|---------|---------|
| Docker | Containerization | Latest |
| docker-compose | Orchestration | Latest |
| Git | Version control | Latest |

---

## 🔄 Development Workflow

### 1. Local Development

**Start Backend**:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

**Start Frontend** (new terminal):
```bash
cd frontend
npm install
npm run dev
```

**Access**:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

### 2. File Watching

- **Backend**: Uvicorn auto-reloads on `.py` file changes
- **Frontend**: Vite hot-reloads on `.jsx`, `.css`, `.js` changes

### 3. Making Changes

1. Edit file in your IDE
2. Save (Ctrl+S)
3. See changes instantly in browser
4. Check browser console (F12) for errors

### 4. Testing

**Manual Testing**:
- Create stocks in Portfolio
- Create watchlists
- Verify data persists

**API Testing**:
- Use http://localhost:8000/docs (Swagger UI)
- Use curl from terminal
- Use Postman desktop app

### 5. Committing Changes

```bash
git add .
git commit -m "Feature: [description]"
git push
```

---

## 📝 Code Conventions

### Backend (Python)

**File Naming**:
```
main.py              # Main entry point
models.py            # Data models (Pydantic)
data_manager.py      # Data access layer
utils.py             # Utility functions
```

**Function Naming**:
```python
# Use snake_case
def get_portfolio()
def create_watchlist()
def delete_stock()
```

**Class Naming**:
```python
# Use PascalCase
class PortfolioStock
class WatchlistItem
class SummaryResponse
```

**Type Hints**:
```python
# Always use type hints
def get_portfolio() -> List[PortfolioStock]:
    ...

def create_stock(stock: PortfolioCreate) -> PortfolioStock:
    ...
```

**Docstrings**:
```python
def add_stock(stock_name: str, amount_egp: float) -> bool:
    """Add or update a stock in portfolio.
    
    Args:
        stock_name: Name of the stock (e.g., 'ETELECOM')
        amount_egp: Amount in Egyptian Pounds
    
    Returns:
        True if successful, False otherwise
    """
```

### Frontend (React/JavaScript)

**File Naming**:
```
App.jsx              # Capitalized for components
api.js               # Lowercase for utilities
index.css            # Lowercase for styles
```

**Component Naming**:
```javascript
// PascalCase for components
function PortfolioTab() {}
export default PortfolioTab

// camelCase for hooks/functions
const handleAddStock = () => {}
const fetchPortfolio = () => {}
```

**Props & State**:
```javascript
// Descriptive names
const [stocks, setStocks] = useState([])
const [isLoading, setIsLoading] = useState(false)
const [error, setError] = useState(null)

// Props
<PortfolioTab 
  stocks={stocks}
  onAddStock={handleAdd}
  isLoading={isLoading}
/>
```

**CSS Classes**:
```javascript
// Use Tailwind with semantic names
className="flex items-center justify-between bg-gradient-to-r from-blue-500 to-blue-600 rounded-lg shadow-md p-4"
```

---

## 🎨 Customization Guide

### 1. Change Color Scheme

Edit `frontend/tailwind.config.js`:

```javascript
colors: {
  primary: {
    50: '#f0f7ff',
    100: '#e0efff',
    500: '#0ea5e9',  // Change this
    600: '#0284c7',  // And this
    700: '#0369a1',
  },
  accent: {
    emerald: '#10b981',  // Success - Change if needed
    amber: '#f59e0b',    // Warning - Change if needed
    rose: '#ef4444',     // Danger - Change if needed
    violet: '#8b5cf6',   // Info - Change if needed
  }
}
```

Then restart frontend: `npm run dev`

### 2. Add New Status Type

**Backend (main.py)**:
```python
# In POST watchlist items validation
status = status  # Currently: "Buy", "Hold", "Take Profit", "Invest"

# Add new status like "Allocate"
# Update the CSV reader/writer to handle it
```

**Frontend (WatchlistTab.jsx)**:
```javascript
const statuses = [
  { value: 'Buy', label: 'Buy', color: 'emerald' },
  { value: 'Hold', label: 'Hold', color: 'blue' },
  { value: 'Take Profit', label: 'Take Profit', color: 'amber' },
  { value: 'Invest', label: 'Invest', color: 'violet' },
  { value: 'Allocate', label: 'Allocate', color: 'pink' },  // NEW
]
```

### 3. Modify Position Size

**Backend (data_manager.py)**:
```python
# Currently 1 position = 10,000 EGP
POSITION_SIZE = 10000  # Change this value
```

**Frontend (SummaryTab.jsx)**:
```javascript
// Comment showing position size
// Update in calculations if needed
const recommendedAmount = status === 'Buy' ? 10000 : 0  // 10000 is position size
```

### 4. Add New API Endpoint

**Backend (main.py)**:
```python
@app.get("/api/new-endpoint")
def new_endpoint():
    """New endpoint description"""
    return {"data": "result"}
```

**Frontend (services/api.js)**:
```javascript
export const myAPI = {
  newEndpoint: async () => {
    return api.get('/new-endpoint')
  }
}

// Then use in component:
const response = await myAPI.newEndpoint()
```

### 5. Add New React Component

**Create file** `frontend/src/components/MyComponent.jsx`:

```javascript
import { motion } from 'framer-motion'
import React, { useState, useEffect } from 'react'

function MyComponent() {
  const [data, setData] = useState([])
  
  useEffect(() => {
    // Load data
  }, [])
  
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="p-4"
    >
      {/* Component JSX */}
    </motion.div>
  )
}

export default MyComponent
```

**Use in App.jsx**:
```javascript
import MyComponent from './components/MyComponent'

// In App.jsx render:
<MyComponent />
```

---

## ⚡ Performance Optimization

### Backend Optimizations

1. **Add Caching**:
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_calculation():
    # Results cached
    pass
```

2. **Async Operations**:
```python
@app.get("/api/fast-endpoint")
async def fast_endpoint():
    # Non-blocking
    pass
```

3. **Pagination**:
```python
@app.get("/api/portfolio")
def get_portfolio(skip: int = 0, limit: int = 100):
    # Return limited results
    pass
```

### Frontend Optimizations

1. **Code Splitting**:
```javascript
import { lazy, Suspense } from 'react'

const PortfolioTab = lazy(() => import('./components/PortfolioTab'))

<Suspense fallback={<LoadingSpinner />}>
  <PortfolioTab />
</Suspense>
```

2. **Memoization**:
```javascript
import { memo } from 'react'

const StockCard = memo(({ stock }) => (
  // Component
))
```

3. **useCallback**:
```javascript
const handleAdd = useCallback((stock) => {
  // Handler
}, [dependencies])
```

---

## 🚀 Deployment Guide

### Production Build

**Frontend**:
```bash
cd frontend
npm run build
# Creates optimized /dist folder
```

**Backend**:
- Already production-ready with Uvicorn
- Use gunicorn for multiple workers:
```bash
pip install gunicorn
gunicorn -w 4 main:app
```

### Docker Deployment

```bash
# Build images
docker-compose build

# Run services
docker-compose up -d

# Check status
docker-compose ps
```

### Environment Variables

**Backend (.env)**:
```
DATABASE_URL=sqlite:///./data/stocks.db
DEBUG=False
CORS_ORIGINS=https://yourdomain.com
```

**Frontend (.env)**:
```
VITE_API_URL=https://api.yourdomain.com
VITE_APP_NAME=Stock Tracker
```

---

## 🐛 Debugging & Testing

### Browser DevTools

1. **Open DevTools**: F12
2. **Console**: Ctrl+Shift+J (see errors)
3. **Network**: Ctrl+Shift+E (monitor API calls)
4. **Application**: Storage → Local Storage (see cached data)

### Backend Debugging

```python
# Add debug prints
print(f"DEBUG: {variable}")

# Use Python debugger
import pdb
pdb.set_trace()  # Execution pauses here
```

### API Testing

**Using Swagger UI**:
1. Go to http://localhost:8000/docs
2. Try endpoints interactively
3. See request/response examples

**Using curl**:
```bash
curl -X GET http://localhost:8000/api/portfolio
curl -X POST http://localhost:8000/api/portfolio \
  -H "Content-Type: application/json" \
  -d '{"stock_name":"ETELECOM","amount_egp":30000}'
```

### Unit Testing (Future)

```python
# backend/test_main.py
import pytest
from main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_get_portfolio(client):
    response = client.get("/api/portfolio")
    assert response.status_code == 200
```

---

## 📊 Code Quality

### Backend
- Follow PEP 8 style guide
- Use type hints everywhere
- Write docstrings for functions
- Handle exceptions properly

### Frontend
- Use ESLint for code quality
- Use Prettier for formatting
- Follow React best practices
- Components should be reusable

### Both
- Keep functions small and focused
- Use meaningful variable names
- Comment complex logic
- DRY principle (Don't Repeat Yourself)

---

## 🔗 Related Documentation

- [QUICKSTART.md](QUICKSTART.md) - 2-minute setup
- [API_REFERENCE.md](API_REFERENCE.md) - All endpoints
- [REACT_COMPONENTS_GUIDE.md](REACT_COMPONENTS_GUIDE.md) - UI details
- [ARCHITECTURE.md](ARCHITECTURE.md) - System design
- [WEB_APP_SETUP.md](WEB_APP_SETUP.md) - Detailed setup
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Problem solving

---

## 💡 Pro Tips

1. **Keep dependencies updated**: `npm update`, `pip install --upgrade -r requirements.txt`
2. **Use `.gitignore`**: Exclude `node_modules`, `venv`, `.env` files
3. **Make small commits**: Easier to debug and review
4. **Write tests early**: Catches bugs before production
5. **Monitor performance**: Use browser DevTools regularly
6. **Document changes**: Keep README updated
7. **Backup data**: Always backup CSV files before major updates

---

**Happy coding! 🎉**

For questions or issues, check TROUBLESHOOTING.md or review relevant API/component documentation.
