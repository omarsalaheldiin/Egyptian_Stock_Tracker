# 🔌 Backend API Reference - Complete Endpoint Documentation

## Base URL
- **Development**: `http://localhost:8000`
- **Production**: `https://your-domain.com`

---

## Health Check

### GET /
**Description**: Welcome message
```bash
curl http://localhost:8000/
```
**Response**:
```json
{
  "message": "Egyptian Stock Tracker API - FastAPI Backend"
}
```

### GET /health
**Description**: Health check endpoint
```bash
curl http://localhost:8000/health
```
**Response**:
```json
{
  "status": "ok"
}
```

---

## 📊 Portfolio Endpoints

### GET /api/portfolio
**Description**: Get all portfolio stocks
```bash
curl http://localhost:8000/api/portfolio
```
**Response**:
```json
{
  "data": [
    {
      "stock_name": "ETELECOM",
      "amount_egp": 30000
    },
    {
      "stock_name": "SWDY",
      "amount_egp": 20000
    }
  ],
  "count": 2
}
```

### POST /api/portfolio
**Description**: Add or update a stock
```bash
curl -X POST http://localhost:8000/api/portfolio \
  -H "Content-Type: application/json" \
  -d '{
    "stock_name": "ETELECOM",
    "amount_egp": 30000
  }'
```
**Request Body**:
```json
{
  "stock_name": "string (required)",
  "amount_egp": "number (required)"
}
```
**Response**:
```json
{
  "message": "Stock added/updated successfully",
  "stock": {
    "stock_name": "ETELECOM",
    "amount_egp": 30000
  }
}
```

### DELETE /api/portfolio/{stock_name}
**Description**: Delete a stock from portfolio
```bash
curl -X DELETE http://localhost:8000/api/portfolio/ETELECOM
```
**Response**:
```json
{
  "message": "Stock deleted successfully",
  "deleted_stock": "ETELECOM"
}
```

---

## 📋 Watchlist Endpoints

### GET /api/watchlists
**Description**: Get all watchlists
```bash
curl http://localhost:8000/api/watchlists
```
**Response**:
```json
{
  "data": [
    {
      "watchlist_id": "abc123",
      "watchlist_name": "Tech Stocks",
      "items_count": 3
    }
  ],
  "count": 1
}
```

### POST /api/watchlists
**Description**: Create a new watchlist
```bash
curl -X POST http://localhost:8000/api/watchlists \
  -H "Content-Type: application/json" \
  -d '{
    "watchlist_name": "Tech Stocks"
  }'
```
**Request Body**:
```json
{
  "watchlist_name": "string (required)"
}
```
**Response**:
```json
{
  "message": "Watchlist created successfully",
  "watchlist": {
    "watchlist_id": "abc123",
    "watchlist_name": "Tech Stocks"
  }
}
```

### DELETE /api/watchlists/{watchlist_id}
**Description**: Delete a watchlist
```bash
curl -X DELETE http://localhost:8000/api/watchlists/abc123
```
**Response**:
```json
{
  "message": "Watchlist deleted successfully",
  "deleted_id": "abc123"
}
```

---

## 📌 Watchlist Items Endpoints

### GET /api/watchlists/{watchlist_id}/items
**Description**: Get items in a watchlist
```bash
curl http://localhost:8000/api/watchlists/abc123/items
```
**Response**:
```json
{
  "watchlist_id": "abc123",
  "watchlist_name": "Tech Stocks",
  "items": [
    {
      "stock_name": "ETELECOM",
      "status": "Buy"
    },
    {
      "stock_name": "SWDY",
      "status": "Hold"
    }
  ]
}
```

### POST /api/watchlists/{watchlist_id}/items
**Description**: Add item to watchlist
```bash
curl -X POST http://localhost:8000/api/watchlists/abc123/items \
  -H "Content-Type: application/json" \
  -d '{
    "stock_name": "ETELECOM",
    "status": "Buy"
  }'
```
**Request Body**:
```json
{
  "stock_name": "string (required)",
  "status": "Buy | Hold | Take Profit | Invest (required)"
}
```
**Response**:
```json
{
  "message": "Item added to watchlist successfully",
  "item": {
    "stock_name": "ETELECOM",
    "status": "Buy"
  }
}
```

### PUT /api/watchlists/{watchlist_id}/items/{stock_name}
**Description**: Update watchlist item status
```bash
curl -X PUT http://localhost:8000/api/watchlists/abc123/items/ETELECOM \
  -H "Content-Type: application/json" \
  -d '{
    "status": "Hold"
  }'
```
**Request Body**:
```json
{
  "status": "Buy | Hold | Take Profit | Invest (required)"
}
```
**Response**:
```json
{
  "message": "Item updated successfully",
  "item": {
    "stock_name": "ETELECOM",
    "status": "Hold"
  }
}
```

### DELETE /api/watchlists/{watchlist_id}/items/{stock_name}
**Description**: Delete item from watchlist
```bash
curl -X DELETE http://localhost:8000/api/watchlists/abc123/items/ETELECOM
```
**Response**:
```json
{
  "message": "Item deleted from watchlist successfully",
  "deleted_item": {
    "watchlist_id": "abc123",
    "stock_name": "ETELECOM"
  }
}
```

---

## 📈 Summary Endpoints

### GET /api/summary/full
**Description**: Get complete summary across all watchlists
```bash
curl http://localhost:8000/api/summary/full
```
**Response**:
```json
{
  "summary_type": "full",
  "stocks": [
    {
      "stock_name": "ETELECOM",
      "watchlists": [
        {
          "watchlist_name": "Tech Stocks",
          "status": "Buy"
        }
      ],
      "total_positions": 3,
      "portfolio_amount": 30000,
      "status": "Matched"
    }
  ],
  "total_stocks": 1,
  "total_positions": 3
}
```

### GET /api/summary/watchlist/{watchlist_id}
**Description**: Get summary for specific watchlist
```bash
curl http://localhost:8000/api/summary/watchlist/abc123
```
**Response**:
```json
{
  "summary_type": "watchlist",
  "watchlist_id": "abc123",
  "watchlist_name": "Tech Stocks",
  "stocks": [
    {
      "stock_name": "ETELECOM",
      "status": "Buy",
      "recommended_positions": 1,
      "recommended_amount": 10000,
      "your_positions": 3,
      "your_amount": 30000,
      "variance": 20000
    }
  ],
  "total_variance": 20000
}
```

---

## 🔴 Error Responses

### 400 Bad Request
```json
{
  "detail": "Invalid input data"
}
```

### 404 Not Found
```json
{
  "detail": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error"
}
```

---

## 💾 Data Models

### PortfolioStock
```json
{
  "stock_name": "string",
  "amount_egp": "number (positive)"
}
```

### WatchlistItem
```json
{
  "stock_name": "string",
  "status": "Buy | Hold | Take Profit | Invest"
}
```

### SummaryStock
```json
{
  "stock_name": "string",
  "watchlists": [],
  "total_positions": "number",
  "portfolio_amount": "number",
  "status": "Matched | Mismatch | Not in Portfolio"
}
```

---

## 🔄 Request/Response Format

All requests and responses use JSON format.

### Headers Required
```
Content-Type: application/json
```

### Response Structure
Success:
```json
{
  "message": "string",
  "data": {}
}
```

---

## 📊 Status Codes

| Code | Meaning |
|------|---------|
| 200  | OK - Request succeeded |
| 201  | Created - Resource created |
| 400  | Bad Request - Invalid input |
| 404  | Not Found - Resource missing |
| 500  | Server Error - Internal error |

---

## 🧪 Example Workflow

### 1. Check API Health
```bash
curl http://localhost:8000/health
```

### 2. Add Stock to Portfolio
```bash
curl -X POST http://localhost:8000/api/portfolio \
  -H "Content-Type: application/json" \
  -d '{"stock_name": "ETELECOM", "amount_egp": 30000}'
```

### 3. Get Portfolio
```bash
curl http://localhost:8000/api/portfolio
```

### 4. Create Watchlist
```bash
curl -X POST http://localhost:8000/api/watchlists \
  -H "Content-Type: application/json" \
  -d '{"watchlist_name": "Tech Stocks"}'
```

### 5. Add Item to Watchlist
```bash
curl -X POST http://localhost:8000/api/watchlists/abc123/items \
  -H "Content-Type: application/json" \
  -d '{"stock_name": "ETELECOM", "status": "Buy"}'
```

### 6. Get Full Summary
```bash
curl http://localhost:8000/api/summary/full
```

---

## 🔌 Interactive API Documentation

When running the backend, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

These provide interactive API testing interfaces!

---

## 🚀 CORS Configuration

The API is configured to accept requests from:
- `http://localhost:3000` (React frontend in development)
- `http://localhost` (other local services)

Modify `main.py` to adjust for production domains.

---

## 📝 Notes

- **Position Size**: 1 position = 10,000 EGP
- **Statuses**: Buy, Hold, Take Profit, Invest
- **Data Storage**: CSV files in `/data` folder
- **Persistence**: Changes saved to CSV immediately
- **Thread Safe**: Safe for concurrent requests

---

**FastAPI Backend - Production Ready**
