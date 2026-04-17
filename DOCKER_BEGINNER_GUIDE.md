# 🐳 Docker Desktop Beginner Guide - Step-by-Step Instructions

> **For people who have never used Docker before**

---

## 📚 Table of Contents

1. [What is Docker?](#what-is-docker)
2. [Prerequisites](#prerequisites)
3. [Install Docker](#install-docker)
4. [Understanding the Project](#understanding-the-project)
5. [Running the Project](#running-the-project)
6. [Verify Everything Works](#verify-everything-works)
7. [Using the Application](#using-the-application)
8. [Stopping the Application](#stopping-the-application)
9. [Common Issues & Fixes](#common-issues--fixes)
10. [What's Happening Behind the Scenes](#whats-happening-behind-the-scenes)

---

## 🎯 What is Docker?

### Simple Explanation

Think of Docker as a **sandwich maker's kit**:
- Without Docker: You need to buy all ingredients separately, prepare your kitchen, and hope everything works
- With Docker: You get a **pre-packaged kit** with everything you need inside. You just open it and it works!

In technical terms:
- **Docker Container**: A package containing your application + all dependencies
- **Docker Image**: The blueprint/recipe for the container
- **Docker Desktop**: The GUI application that runs containers on your computer

### Why Use Docker?

✅ **Works on any computer** (Windows, Mac, Linux)  
✅ **No installation hassles** (everything pre-packaged)  
✅ **Identical to production** (same environment everywhere)  
✅ **Easy to share** (one command to run)  
✅ **Easy to stop** (clean removal)  

---

## ✅ Prerequisites

Before starting, you need:

### 1. **Your Computer Requirements**
- [ ] Windows 10/11 Pro, Enterprise, or Education (Home edition needs update)
- [ ] OR Mac 2010+ with Intel or Apple Silicon
- [ ] OR Any Linux distribution
- [ ] 4GB+ RAM (8GB recommended)
- [ ] 10GB free disk space
- [ ] Reliable internet connection

### 2. **Check Your Windows Version** (Windows Users Only)

**If on Windows 10/11 Home:**
1. Right-click Start Menu → Settings
2. Go to System → About
3. Look for "Edition" - if it says "Home", you need to update

**Upgrade path for Windows Home**:
- **Option A** (Easy): Use WSL 2 with Docker Desktop (recommended)
  - Docker Desktop now works with Home edition using WSL 2
  - See installation guide below

- **Option B** (Upgrade): Buy Windows 11 Pro ($99-199)

### 3. **Check Your Disk Space**

**Windows**:
1. Open File Explorer
2. Right-click C: drive
3. Click Properties
4. Check "Free space" is at least 10GB

**Mac/Linux**:
```bash
df -h /
```
Look for "Available" column - should show at least 10GB

---

## 🐳 Install Docker Desktop

### **Windows Installation**

#### Step 1: Download Docker Desktop

1. Go to: https://www.docker.com/products/docker-desktop
2. Click **"Download for Windows"**
3. You'll get `Docker Desktop Installer.exe`

#### Step 2: Install

1. **Double-click** `Docker Desktop Installer.exe`
2. Allow administrator access when prompted
3. Click **Install** and wait (2-5 minutes)
4. When done, click **Close**
5. **Restart your computer** (very important!)

#### Step 3: First Launch

1. After restart, go to **Start Menu**
2. Search for "Docker"
3. Click **Docker Desktop**
4. Wait for it to fully load (you'll see a whale icon 🐋 in taskbar)
5. First load takes 1-2 minutes
6. You should see "Docker Desktop is running" ✅

#### Step 4: Verify Installation

1. Open **Command Prompt** or **PowerShell**
2. Type:
```bash
docker --version
```
3. Should show: `Docker version 24.x.x` (or similar)

If you see version number: ✅ **Installation successful!**

---

### **Mac Installation**

#### Step 1: Download Docker Desktop

1. Go to: https://www.docker.com/products/docker-desktop
2. Click **"Download for Mac"**
3. Choose based on your Mac:
   - **Intel Macs**: Click "Intel Chip"
   - **Apple Silicon Macs** (M1, M2, M3): Click "Apple Silicon"

#### Step 2: Install

1. Find the **DMG file** (usually in Downloads)
2. **Double-click** to open it
3. Drag **Docker.app** to **Applications** folder
4. Wait for copy to complete (1-2 minutes)

#### Step 3: First Launch

1. Open **Applications** folder
2. Find **Docker.app**
3. **Double-click** to launch
4. Enter your Mac password when prompted (for privileged access)
5. Wait for Docker to fully load (1-2 minutes)
6. You'll see whale icon 🐋 at top menu bar

#### Step 4: Verify Installation

1. Open **Terminal** (Cmd+Space, type "Terminal")
2. Type:
```bash
docker --version
```
3. Should show: `Docker version 24.x.x` (or similar)

If you see version number: ✅ **Installation successful!**

---

### **Linux Installation** (Ubuntu/Debian)

```bash
# Install Docker
sudo apt-get update
sudo apt-get install docker.io docker-compose

# Add your user to docker group (so you don't need sudo)
sudo usermod -aG docker $USER

# Log out and back in, then verify:
docker --version
```

---

## 📁 Understanding the Project

### Project Structure

```
My_Stock_Tracker/
│
├── 🔧 DOCKER FILES (Important!)
│   ├── docker-compose.yml     ← Main file that runs everything
│   ├── Dockerfile.backend     ← Blueprint for backend
│   └── Dockerfile.frontend    ← Blueprint for frontend
│
├── 🔙 BACKEND (Python API)
│   ├── main.py               ← FastAPI application
│   ├── app/
│   │   ├── models.py        ← Data structures
│   │   └── data_manager.py  ← Data storage
│   └── requirements.txt      ← Dependencies
│
├── 🎨 FRONTEND (React App)
│   ├── src/
│   │   ├── App.jsx          ← Main app
│   │   └── components/      ← UI components
│   ├── package.json         ← Dependencies
│   └── tailwind.config.js   ← Styling config
│
├── 💾 DATA FOLDER
│   └── data/                ← Your portfolio data (CSV files)
│
└── 📚 DOCUMENTATION
    └── docs/                ← Guides and references
```

### What Will Run?

When you run this project with Docker:

1. **Backend Service** (Python FastAPI)
   - Runs on: http://localhost:8000
   - Purpose: Handles business logic, stores data
   - Uses: Python, FastAPI, Pydantic

2. **Frontend Service** (React)
   - Runs on: http://localhost:3000
   - Purpose: User interface, what you see in browser
   - Uses: React, Tailwind CSS, Framer Motion

3. **Data Storage**
   - Uses: CSV files in `data/` folder
   - Your data persists after stopping

---

## 🚀 Running the Project - Step by Step

### Step 1: Ensure Docker Desktop is Running

**Windows/Mac**:
- Look for whale icon 🐋 in taskbar/menu bar
- If not there, open **Docker Desktop** application

**Linux**:
- Docker runs in background automatically

### Step 2: Open Terminal/Command Prompt

**Windows (Easiest)**:
1. In File Explorer, go to: `D:\Projects\My_Stock_Tracker`
2. Click address bar at top
3. Type: `powershell`
4. Press Enter
5. A PowerShell window opens in that folder ✅

**Or Manual**:
1. Open Command Prompt or PowerShell
2. Type:
```bash
cd D:\Projects\My_Stock_Tracker
```

**Mac**:
1. Open Terminal (Cmd+Space, type "Terminal")
2. Type:
```bash
cd /path/to/My_Stock_Tracker
```

**Linux**:
1. Open Terminal
2. Type:
```bash
cd ~/path/to/My_Stock_Tracker
```

### Step 3: Start the Project

In your terminal/command prompt, type:

```bash
docker-compose up
```

Then press **Enter**.

> **Note**: First time will take 2-5 minutes to download and build. Subsequent times are faster (5-10 seconds).

### Step 4: Wait for "Ready" Messages

You'll see lots of text scrolling. **Wait until you see**:

```
backend  | INFO:     Application startup complete
frontend | VITE v5.x.x  ready in xxx ms
```

When you see both messages: ✅ **Everything is running!**

### Step 5: Open Your Browser

1. Open your favorite browser (Chrome, Firefox, Safari, Edge)
2. Go to: **http://localhost:3000**
3. You should see the **Stock Tracker app** 🎉

---

## ✅ Verify Everything Works

### Test 1: Frontend Loads

**Step 1**: Open http://localhost:3000 in your browser

**Success Looks Like**:
- Header says "Egyptian Stock Tracker"
- Three tabs visible: Portfolio, Watchlist, Summary
- Colorful design with gradients

**If it doesn't work**:
- Wait 10 more seconds (first load can be slow)
- Refresh the page (Ctrl+R or Cmd+R)
- Check the terminal for error messages

### Test 2: Backend Works

**Step 1**: In a NEW terminal (keep docker-compose one running), type:

```bash
curl http://localhost:8000/health
```

**Success Looks Like**:
```json
{"status":"ok"}
```

**If error**: Make sure `docker-compose up` is still running in other terminal

### Test 3: Add Sample Data

**Step 1**: In the app (browser), click **Portfolio** tab

**Step 2**: Click "Add Stock" button

**Step 3**: Fill in:
- Stock Name: `ETELECOM`
- Amount in EGP: `30000`

**Step 4**: Click "Add" button

**Success Looks Like**:
- Stock appears in the list below
- Toast notification appears

---

## 🎮 Using the Application

### Portfolio Tab

**What it does**: Track your stock holdings

**How to use**:
1. Click "Add Stock" button
2. Enter stock name (e.g., ETELECOM)
3. Enter amount in EGP (e.g., 30000)
4. Click "Add"
5. Stock appears in the list

**Features**:
- ✅ See total value, count, average
- ✅ Update existing stocks (click → edit → update)
- ✅ Delete stocks (click delete button)

### Watchlist Tab

**What it does**: Create investment recommendations

**How to use**:
1. Click "Create Watchlist"
2. Enter name (e.g., "Tech Stocks")
3. Click create
4. Click on created watchlist
5. Add stocks with status (Buy/Hold/Take Profit/Invest)
6. Click "Add to Watchlist"

### Summary Tab

**What it does**: Compare your holdings vs recommendations

**How to use**:
1. Click "Full Summary" to see all stocks
2. Click "Individual" to analyze one watchlist
3. Select a watchlist from dropdown
4. See variance analysis

---

## 🛑 Stopping the Application

### Method 1: In Terminal (Cleanest)

1. Go back to the terminal with `docker-compose up` running
2. Press: **Ctrl+C** (hold Ctrl and press C)
3. Wait for clean shutdown (5-10 seconds)
4. Terminal will return to normal prompt

### Method 2: From Docker Desktop GUI

**Windows/Mac**:
1. Open Docker Desktop app
2. Go to **Containers** tab
3. Find your project
4. Click **Stop** button

---

## 🆘 Common Issues & Fixes

### Issue 1: "docker: command not found"

**Cause**: Docker not installed or not restarted after installation

**Fix**:
1. Restart your computer
2. After restart, open Docker Desktop
3. Wait for it to fully load
4. Try again

### Issue 2: "Cannot connect to Docker daemon"

**Cause**: Docker Desktop isn't running

**Fix**:
1. **Windows/Mac**: Open Docker Desktop application
2. Wait for whale icon 🐋 to appear
3. Try again

### Issue 3: "Port 3000 already in use"

**Cause**: Another app using port 3000

**Fix**:
1. Stop `docker-compose up` (press Ctrl+C)
2. Type:
```bash
docker-compose down
```
3. Start again:
```bash
docker-compose up
```

### Issue 4: "Port 8000 already in use"

**Cause**: Another app using port 8000

**Fix**:
1. Stop `docker-compose up` (press Ctrl+C)
2. Type:
```bash
docker-compose down
```
3. Start again:
```bash
docker-compose up
```

### Issue 5: Browser shows "Cannot reach localhost:3000"

**Cause**: Services still loading or not started

**Fix**:
1. Check terminal for "ready in" message
2. Wait 10 more seconds
3. Refresh browser (Ctrl+R or Cmd+R)
4. Make sure `docker-compose up` is still running

### Issue 6: App loads but data doesn't save

**Cause**: Data folder permissions

**Fix**:
1. Stop Docker (Ctrl+C)
2. Make sure `data/` folder exists and has permissions
3. Restart: `docker-compose up`

### Issue 7: First run very slow (5+ minutes)

**Normal behavior!** First run downloads and builds everything. Subsequent runs are 5-10 seconds.

---

## 📊 What's Happening Behind the Scenes

### When You Run `docker-compose up`

```
1. Docker reads docker-compose.yml
   ↓
2. Creates two containers:
   ├─ Backend container (Python + FastAPI)
   └─ Frontend container (Node.js + React)
   ↓
3. Starts both services simultaneously
   ├─ Backend listens on port 8000
   └─ Frontend runs dev server on port 3000
   ↓
4. Frontend connects to Backend API
   ↓
5. App ready at http://localhost:3000
```

### Container Details

**Backend Container**:
- Image: Python 3.11 slim
- Purpose: Runs FastAPI API server
- Port: 8000
- Restarts on errors

**Frontend Container**:
- Image: Node 20 alpine
- Purpose: Runs React dev server
- Port: 3000
- Hot-updates on code changes

**Data Storage**:
- Your CSV files stored in `data/` folder
- Persists after container stops
- Not lost when you stop Docker

### Cleanup at Stop

When you press Ctrl+C:
```
1. Sends shutdown signal to containers
   ↓
2. Services gracefully shut down (5-10 sec)
   ↓
3. Containers stop & removed
   ↓
4. Data folder remains safe
   ↓
5. Next time: Much faster (cached images)
```

---

## 🎯 Quick Reference

### Commands You'll Use

```bash
# Start the app
docker-compose up

# Stop the app (in terminal)
Ctrl+C

# Clean stop (from another terminal)
docker-compose down

# View logs (another terminal)
docker-compose logs

# View only backend logs
docker-compose logs backend

# View only frontend logs
docker-compose logs frontend
```

### URLs to Remember

| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:8000 |
| API Docs | http://localhost:8000/docs |

---

## 💡 Pro Tips

### Tip 1: Keep Docker Desktop Running
Leave Docker Desktop open while developing. It uses minimal resources and keeps things running smoothly.

### Tip 2: First Run Takes Time
First run downloads images (~500MB+). Don't worry, subsequent runs are much faster once cached.

### Tip 3: Check Docker Dashboard
**Windows/Mac**: Docker Desktop has a dashboard showing:
- Running containers
- CPU/Memory usage
- Logs
- Network info

### Tip 4: Save Your Data
Your data in `data/` folder is safe and persists. Stopping Docker won't delete it.

### Tip 5: Performance
- Docker uses minimal CPU when idle
- RAM usage: ~500MB - 1GB
- Safe to use on laptops regularly

---

## 🔗 Helpful Resources

| Resource | Purpose |
|----------|---------|
| [Docker Official Docs](https://docs.docker.com/) | Complete Docker documentation |
| [Docker Hub](https://hub.docker.com/) | Image repository |
| [Interactive API Docs](http://localhost:8000/docs) | Test API endpoints live |

---

## ✨ You're Done!

You now have:
✅ Docker installed and working
✅ Project running successfully
✅ Backend API running (port 8000)
✅ Frontend app running (port 3000)
✅ Data stored safely

**Next Steps**:
1. Add your portfolio data
2. Create watchlists
3. Explore the app features
4. Customize as needed

---

## 🆘 Still Having Issues?

### Check Terminal Output

Look for error messages in the terminal. Most issues are explained there. Take a screenshot of the error and:
1. Google the error message
2. Check [docs/TROUBLESHOOTING.md](./docs/TROUBLESHOOTING.md)
3. Restart Docker Desktop and try again

### Common Checks

- [ ] Docker Desktop running (whale icon visible)
- [ ] Terminal opened in correct folder: `My_Stock_Tracker`
- [ ] Ran `docker-compose up` (not `docker compose` without dash)
- [ ] Waited for both services to show "ready" messages
- [ ] Opened http://localhost:3000 (not https)
- [ ] Tried refreshing browser
- [ ] Checked no other apps using ports 3000/8000

---

**Happy tracking! 📈**

For more detailed information, see:
- [docs/README.md](./docs/README.md) - Full project overview
- [docs/QUICKSTART.md](./docs/QUICKSTART.md) - Quick start alternative
- [docs/TROUBLESHOOTING.md](./docs/TROUBLESHOOTING.md) - Detailed problem-solving

