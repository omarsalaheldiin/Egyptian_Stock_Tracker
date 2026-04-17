# 🌍 Deployment Guide - Production Setup & Hosting

## Table of Contents

1. Pre-Deployment Checklist
2. Production Build
3. Deployment Options
4. Production Configuration
5. Monitoring & Maintenance
6. Scaling Guide
7. Backup & Recovery

---

## ✅ Pre-Deployment Checklist

### Code Quality
- [ ] All features tested locally
- [ ] No console errors in DevTools
- [ ] No backend errors in logs
- [ ] All endpoints working
- [ ] Data persists across restarts

### Security
- [ ] Remove debug mode
- [ ] Set `DEBUG=False` in backend
- [ ] Generate secure SECRET_KEY
- [ ] Update CORS origins (not `*`)
- [ ] Use HTTPS in production
- [ ] Validate all user inputs

### Performance
- [ ] Frontend optimized (npm run build)
- [ ] API response times acceptable
- [ ] Database queries efficient
- [ ] No memory leaks
- [ ] Images/assets compressed

### Documentation
- [ ] README up to date
- [ ] API documentation complete
- [ ] Deployment steps documented
- [ ] Environment variables documented

### Data
- [ ] Backup CSV files
- [ ] Test data migration
- [ ] Verify data integrity
- [ ] Plan data archival strategy

---

## 🏗️ Production Build

### Frontend Build

```bash
cd frontend

# Build optimized production bundle
npm run build

# Creates /dist folder with optimized files
# Output: ~100-200 KB gzipped
```

**What's optimized**:
- Minified JavaScript
- CSS bundled and minified
- Unused code removed (tree-shaking)
- Images optimized
- Code split by routes

### Backend Setup

```bash
cd backend

# Create production environment
python -m venv venv-prod
source venv-prod/bin/activate

# Install production dependencies
pip install -r requirements.txt
pip install gunicorn  # Production ASGI server

# Test build
gunicorn -w 4 main:app --bind 0.0.0.0:8000
```

---

## 🚀 Deployment Options

### Option 1: Docker (Recommended)

**Advantages**:
- Consistent across environments
- Easy scaling
- Built-in isolation
- Fast deployment

**Deploy to VPS**:

```bash
# On your local machine
docker-compose build

# Push to registry (Docker Hub, etc.)
docker tag my-stock-app:latest yourusername/my-stock-app:latest
docker push yourusername/my-stock-app:latest

# On production server
docker pull yourusername/my-stock-app:latest
docker-compose up -d
```

**Production docker-compose.yml**:
```yaml
version: '3.8'

services:
  backend:
    image: yourusername/my-stock-app:latest
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - WORKERS=4
    volumes:
      - data:/app/data
    restart: always

  frontend:
    image: yourusername/my-stock-frontend:latest
    ports:
      - "80:80"
      - "443:443"
    restart: always

volumes:
  data:
```

---

### Option 2: VPS (Manual)

**Requirements**:
- Ubuntu 22.04 LTS or similar
- Python 3.10+
- Node.js 18+
- Nginx (reverse proxy)
- PostgreSQL (optional, for scalability)

**Setup Steps**:

1. **SSH to Server**:
```bash
ssh root@your-server-ip
```

2. **Install Dependencies**:
```bash
apt update && apt upgrade
apt install python3-pip python3-venv nodejs npm nginx postgresql
```

3. **Clone Repository**:
```bash
cd /var/www
git clone https://github.com/yourusername/my-stock-app.git
cd my-stock-app
```

4. **Setup Backend**:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

5. **Setup Frontend**:
```bash
cd ../frontend
npm install
npm run build
```

6. **Configure Nginx**:
```nginx
server {
    listen 80;
    server_name yourdomain.com;
    
    # Frontend
    location / {
        root /var/www/my-stock-app/frontend/dist;
        try_files $uri /index.html;
    }
    
    # API proxy
    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

7. **Start Services**:
```bash
# Backend with gunicorn
cd /var/www/my-stock-app/backend
gunicorn -w 4 -b 0.0.0.0:8000 main:app

# Or use systemd (see below)
```

---

### Option 3: Heroku

**Advantages**:
- Free tier available
- Easy git-based deployment
- Automatic scaling

**Deploy**:

1. Create `Procfile`:
```
web: gunicorn main:app
```

2. Push to Heroku:
```bash
heroku login
heroku create my-stock-app
git push heroku main
```

---

### Option 4: AWS/GCP/Azure

**Services**:
- Container hosting (ECS, Cloud Run, Container Instances)
- Managed databases
- Static hosting (S3, Cloud Storage, Blob Storage)
- CDN for frontend

**Setup** (example with AWS ECS):
1. Build Docker image
2. Push to ECR
3. Create ECS task definition
4. Deploy service
5. Configure load balancer
6. Setup auto-scaling

---

## ⚙️ Production Configuration

### Environment Variables

**Backend (.env)**:
```env
# Security
DEBUG=False
SECRET_KEY=your-very-secure-random-key-here
CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com

# Database
DATABASE_URL=postgresql://user:pass@db-host:5432/stocks

# Server
WORKERS=4
LOG_LEVEL=info
```

**Frontend (.env)**:
```env
VITE_API_URL=https://api.yourdomain.com
VITE_APP_NAME=Stock Tracker
```

### SSL/TLS Certificate

**Using Let's Encrypt (Free)**:

```bash
# Install Certbot
apt install certbot python3-certbot-nginx

# Generate certificate
certbot certonly --standalone -d yourdomain.com

# Configure Nginx for SSL
# Certbot can do this automatically:
certbot --nginx
```

### Database Migration (Optional)

If scaling beyond CSV:

```bash
# Switch from CSV to PostgreSQL
pip install sqlalchemy psycopg2-binary

# Modify data_manager.py to use SQLAlchemy instead of CSV
# Update database connection string
```

---

## 📊 Monitoring & Maintenance

### Health Checks

```bash
# Check backend health
curl https://api.yourdomain.com/health

# Monitor logs
docker logs -f backend

# Check resource usage
docker stats
```

### Logging

**Backend Logs** (main.py):
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info("Application started")
```

**View Logs**:
```bash
tail -f app.log
```

### Performance Monitoring

**Backend**:
```bash
# Monitor database queries
pip install django-extensions  # or similar

# Monitor resource usage
pip install py-spy
py-spy record -o profile.svg -- gunicorn main:app
```

**Frontend**:
- Use Sentry for error tracking
- Use Google Analytics for usage metrics
- Use Lighthouse for performance audits

### Backup Strategy

```bash
#!/bin/bash
# backup.sh - Daily backup script

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backups/stock-app"

# Backup data folder
tar -czf $BACKUP_DIR/data_$DATE.tar.gz data/

# Backup database (if using PostgreSQL)
pg_dump stocks_db > $BACKUP_DIR/db_$DATE.sql

# Remove old backups (keep 30 days)
find $BACKUP_DIR -mtime +30 -delete

echo "Backup completed: $DATE"
```

**Schedule with cron**:
```bash
crontab -e
# Add: 0 2 * * * /path/to/backup.sh
```

---

## 📈 Scaling Guide

### Single Server (Current)
- Handles ~100+ concurrent users
- CSV data storage
- Single backend instance

### Multi-Server (When needed)

1. **Load Balancer**:
```
         [nginx]
        /      \
   [backend1]  [backend2]
        \      /
    [PostgreSQL]
```

2. **Database Migration**:
```bash
# Migrate from CSV to PostgreSQL
ALTER TABLE portfolios ADD ...
CREATE INDEXES ...
```

3. **Cache Layer** (Redis):
```python
import redis

cache = redis.Redis(host='localhost')

@app.get("/api/portfolio")
def get_portfolio():
    cached = cache.get('portfolio')
    if cached:
        return json.loads(cached)
    # ... fetch from DB
    cache.set('portfolio', json.dumps(data), ex=3600)
    return data
```

---

## 🔄 Continuous Deployment

### GitHub Actions Example

**.github/workflows/deploy.yml**:
```yaml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Build Docker image
        run: docker-compose build
      
      - name: Push to registry
        run: |
          docker tag backend:latest myregistry/backend:latest
          docker push myregistry/backend:latest
      
      - name: Deploy to server
        run: |
          ssh -i $SSH_KEY user@server "cd app && docker-compose pull && docker-compose up -d"
```

---

## 🛡️ Security Hardening

### Backend Security

1. **Input Validation**:
```python
from pydantic import validator

class PortfolioCreate(BaseModel):
    stock_name: str
    amount_egp: float
    
    @validator('stock_name')
    def validate_stock_name(cls, v):
        if len(v) < 2 or len(v) > 20:
            raise ValueError('Stock name must be 2-20 characters')
        return v.upper()
```

2. **Rate Limiting**:
```bash
pip install slowapi

from slowapi import Limiter

limiter = Limiter(key_func=get_remote_address)

@app.get("/api/portfolio")
@limiter.limit("100/minute")
def get_portfolio():
    pass
```

3. **HTTPS Only**:
```python
# Redirect HTTP to HTTPS
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app.add_middleware(TrustedHostMiddleware, allowed_hosts=["yourdomain.com"])
```

### Frontend Security

1. **Content Security Policy**:
```html
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'self'; script-src 'self' 'unsafe-inline';">
```

2. **XSS Prevention** (React does this automatically)
3. **CORS Restrictions**: Already configured in backend

---

## 📋 Post-Deployment Checklist

- [ ] Frontend loads without errors
- [ ] API endpoints responding
- [ ] HTTPS working (no mixed content warnings)
- [ ] Data persisting across requests
- [ ] Database backups scheduled
- [ ] Monitoring tools active
- [ ] Error notifications configured
- [ ] Performance acceptable
- [ ] User authentication ready (if needed)
- [ ] Terms of Service & Privacy Policy displayed

---

## 🆘 Common Deployment Issues

### Blank Page on Frontend
```bash
# Check nginx configuration
nginx -t

# Check backend is accessible
curl http://localhost:8000/health

# Check CORS settings
```

### 502 Bad Gateway
```bash
# Backend not running
docker logs backend

# Or check gunicorn
ps aux | grep gunicorn
```

### Data Not Persisting
```bash
# Check data volume
docker volume ls
docker volume inspect my-stock-app_data

# Verify permissions
ls -la /backups/data/
```

### Slow Performance
```bash
# Check resource usage
docker stats

# Optimize queries
# Add caching layer
# Scale to multiple instances
```

---

## 📚 Deployment Commands Reference

```bash
# Build for production
npm run build
docker-compose build

# Deploy
docker-compose up -d
docker-compose restart

# Monitor
docker-compose logs -f
docker-compose ps

# Backup
tar -czf backup-$(date +%Y%m%d).tar.gz data/

# Update
git pull
docker-compose build --no-cache
docker-compose up -d
```

---

## 🎯 Performance Targets

Target metrics for production:

| Metric | Target |
|--------|--------|
| Frontend Load Time | < 2 seconds |
| API Response Time | < 200ms |
| Uptime | 99.9% |
| Concurrent Users | 100+ |
| Database Query Time | < 50ms |

---

**Deployment Complete! 🚀**

For more information, see:
- [WEB_APP_SETUP.md](WEB_APP_SETUP.md) - Local setup
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Problem solving
- [ARCHITECTURE.md](ARCHITECTURE.md) - System design
