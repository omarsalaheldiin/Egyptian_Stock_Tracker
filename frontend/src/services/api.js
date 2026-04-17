import axios from 'axios'

const API_BASE = '/api'

const api = axios.create({
  baseURL: API_BASE,
  headers: {
    'Content-Type': 'application/json',
  }
})

// Portfolio endpoints
export const portfolioAPI = {
  getAll: () => api.get('/portfolio'),
  add: (data) => api.post('/portfolio', data),
  delete: (stockName) => api.delete(`/portfolio/${encodeURIComponent(stockName)}`),
}

// Watchlist endpoints
export const watchlistAPI = {
  getAll: () => api.get('/watchlists'),
  create: (data) => api.post('/watchlists', data),
  delete: (id) => api.delete(`/watchlists/${id}`),
  getItems: (id) => api.get(`/watchlists/${id}/items`),
  addItem: (id, data) => api.post(`/watchlists/${id}/items`, data),
  deleteItem: (id, stockName) => api.delete(`/watchlists/${id}/items/${encodeURIComponent(stockName)}`),
}

// Summary endpoints
export const summaryAPI = {
  getFull: () => api.get('/summary/full'),
  getWatchlist: (id) => api.get(`/summary/watchlist/${id}`),
}

export default api
