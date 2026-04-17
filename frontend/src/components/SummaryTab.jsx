import React, { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { BookOpen, BarChart3, TrendingUp } from 'lucide-react'
import { summaryAPI, watchlistAPI } from '../services/api'
import Toast from './Toast'
import LoadingSpinner from './LoadingSpinner'

const STATUS_COLORS = {
  'Matched': 'from-accent-emerald to-emerald-700',
  'Mismatch': 'from-accent-amber to-amber-700',
  'Not in Portfolio': 'from-accent-rose to-rose-700',
  'No Data': 'from-gray-400 to-gray-500',
}

const VARIANCE_COLOR = (variance) => {
  if (variance === 0) return 'bg-accent-emerald/10 text-accent-emerald border-accent-emerald/20'
  if (variance > 0) return 'bg-primary-500/10 text-primary-700 border-primary-500/20'
  return 'bg-accent-amber/10 text-accent-amber border-accent-amber/20'
}

export default function SummaryTab() {
  const [viewType, setViewType] = useState('full')
  const [summary, setSummary] = useState([])
  const [watchlists, setWatchlists] = useState([])
  const [selectedWatchlist, setSelectedWatchlist] = useState(null)
  const [loading, setLoading] = useState(true)
  const [toast, setToast] = useState(null)

  useEffect(() => {
    loadSummary()
    loadWatchlists()
  }, [])

  useEffect(() => {
    if (viewType === 'full') {
      loadFullSummary()
    }
  }, [viewType])

  const loadWatchlists = async () => {
    try {
      const res = await watchlistAPI.getAll()
      setWatchlists(res.data || [])
      if (res.data?.length > 0) {
        setSelectedWatchlist(res.data[0])
      }
    } catch (error) {
      showToast('Failed to load watchlists', 'error')
    }
  }

  const loadSummary = async () => {
    try {
      setLoading(true)
      await loadFullSummary()
    } finally {
      setLoading(false)
    }
  }

  const loadFullSummary = async () => {
    try {
      const res = await summaryAPI.getFull()
      setSummary(res.data || [])
    } catch (error) {
      showToast('Failed to load summary', 'error')
    }
  }

  const loadWatchlistSummary = async () => {
    try {
      const res = await summaryAPI.getWatchlist(selectedWatchlist.watchlist_id)
      setSummary(res.data?.stocks || [])
    } catch (error) {
      showToast('Failed to load watchlist summary', 'error')
    }
  }

  useEffect(() => {
    if (viewType === 'watchlist' && selectedWatchlist) {
      loadWatchlistSummary()
    }
  }, [viewType, selectedWatchlist])

  const showToast = (message, type) => {
    setToast({ message, type })
  }

  if (loading) return <LoadingSpinner />

  return (
    <div className="space-y-6">
      {/* View Options */}
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="glass rounded-lg p-6 border border-gray-200"
      >
        <h3 className="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
          <BarChart3 size={20} className="text-primary-500" />
          View Options
        </h3>
        <div className="flex flex-col sm:flex-row gap-4">
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={() => setViewType('full')}
            className={`flex-1 py-3 px-4 rounded-lg font-semibold transition-all ${
              viewType === 'full'
                ? 'bg-gradient-to-r from-primary-500 to-primary-600 text-white shadow-lg'
                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
            }`}
          >
            📊 Full Summary
          </motion.button>
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={() => setViewType('watchlist')}
            className={`flex-1 py-3 px-4 rounded-lg font-semibold transition-all ${
              viewType === 'watchlist'
                ? 'bg-gradient-to-r from-primary-500 to-primary-600 text-white shadow-lg'
                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
            }`}
          >
            ⭐ Individual Watchlist
          </motion.button>
        </div>

        {viewType === 'watchlist' && (
          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className="mt-4"
          >
            <label className="block text-sm font-semibold text-gray-700 mb-2">Select Watchlist</label>
            <select
              value={selectedWatchlist?.watchlist_id || ''}
              onChange={(e) => {
                const wl = watchlists.find(w => w.watchlist_id === e.target.value)
                setSelectedWatchlist(wl)
              }}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
            >
              {watchlists.map(wl => (
                <option key={wl.watchlist_id} value={wl.watchlist_id}>
                  {wl.watchlist_name}
                </option>
              ))}
            </select>
          </motion.div>
        )}
      </motion.div>

      {/* Summary Table */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.2 }}
        className="glass rounded-lg overflow-hidden border border-gray-200"
      >
        <div className="overflow-x-auto">
          {viewType === 'full' ? (
            <table className="w-full">
              <thead className="bg-gradient-to-r from-primary-500 to-primary-600 text-white">
                <tr>
                  <th className="px-6 py-3 text-left text-sm font-semibold">Stock</th>
                  <th className="px-6 py-3 text-left text-sm font-semibold">Watchlists</th>
                  <th className="px-6 py-3 text-center text-sm font-semibold">Total Pos</th>
                  <th className="px-6 py-3 text-right text-sm font-semibold">Portfolio (EGP)</th>
                  <th className="px-6 py-3 text-center text-sm font-semibold">Status</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-200">
                <AnimatePresence>
                  {summary.map((stock, idx) => (
                    <motion.tr
                      key={stock.stock_name}
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      exit={{ opacity: 0, x: -20 }}
                      transition={{ delay: idx * 0.05 }}
                      className="hover:bg-gray-50 transition-colors"
                    >
                      <td className="px-6 py-4 font-semibold text-gray-800">{stock.stock_name}</td>
                      <td className="px-6 py-4">
                        <div className="flex flex-wrap gap-2">
                          {stock.watchlists?.map((wl, i) => (
                            <span key={i} className="inline-block px-2 py-1 bg-primary-100 text-primary-700 text-xs rounded-full font-semibold">
                              {wl.watchlist_name}: {wl.status}
                            </span>
                          ))}
                        </div>
                      </td>
                      <td className="px-6 py-4 text-center font-bold text-primary-600">{stock.total_positions}x</td>
                      <td className="px-6 py-4 text-right font-semibold text-gray-800">{stock.portfolio_amount.toLocaleString()}</td>
                      <td className="px-6 py-4 text-center">
                        <span className={`inline-block px-3 py-1 rounded-full text-xs font-semibold bg-gradient-to-r ${STATUS_COLORS[stock.status]} text-white`}>
                          {stock.status}
                        </span>
                      </td>
                    </motion.tr>
                  ))}
                </AnimatePresence>
              </tbody>
            </table>
          ) : (
            // Watchlist Summary
            <table className="w-full">
              <thead className="bg-gradient-to-r from-primary-500 to-primary-600 text-white">
                <tr>
                  <th className="px-6 py-3 text-left text-sm font-semibold">Stock</th>
                  <th className="px-6 py-3 text-left text-sm font-semibold">Status</th>
                  <th className="px-6 py-3 text-right text-sm font-semibold">Recommended (EGP)</th>
                  <th className="px-6 py-3 text-right text-sm font-semibold">Your Position (EGP)</th>
                  <th className="px-6 py-3 text-right text-sm font-semibold">Variance (EGP)</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-200">
                <AnimatePresence>
                  {summary.map && summary.map((item, idx) => (
                    <motion.tr
                      key={item.stock_name}
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      exit={{ opacity: 0, x: -20 }}
                      transition={{ delay: idx * 0.05 }}
                      className={`hover:bg-gray-50 transition-colors ${
                        item.variance === 0 ? 'bg-accent-emerald/5' :
                        item.variance > 0 ? 'bg-primary-500/5' : 'bg-accent-amber/5'
                      }`}
                    >
                      <td className="px-6 py-4 font-semibold text-gray-800">{item.stock_name}</td>
                      <td className="px-6 py-4">
                        <span className={`inline-block px-2 py-1 rounded-full text-xs font-semibold border ${
                          item.status === 'Buy' ? 'bg-accent-emerald/10 text-accent-emerald border-accent-emerald/20' :
                          item.status === 'Hold' ? 'bg-primary-500/10 text-primary-700 border-primary-500/20' :
                          item.status === 'Take Profit' ? 'bg-accent-amber/10 text-accent-amber border-accent-amber/20' :
                          'bg-accent-violet/10 text-accent-violet border-accent-violet/20'
                        }`}>
                          {item.status}
                        </span>
                      </td>
                      <td className="px-6 py-4 text-right font-semibold text-gray-800">{item.position_size_egp.toLocaleString()}</td>
                      <td className="px-6 py-4 text-right font-semibold text-gray-800">{item.portfolio_amount.toLocaleString()}</td>
                      <td className={`px-6 py-4 text-right font-bold ${
                        item.variance === 0 ? 'text-accent-emerald' :
                        item.variance > 0 ? 'text-primary-600' : 'text-accent-amber'
                      }`}>
                        {item.variance > 0 ? '+' : ''}{item.variance.toLocaleString()}
                      </td>
                    </motion.tr>
                  ))}
                </AnimatePresence>
              </tbody>
            </table>
          )}
        </div>
        {summary.length === 0 && (
          <div className="text-center py-12 text-gray-400">
            No data to display. Add stocks to your portfolio and watchlists first!
          </div>
        )}
      </motion.div>

      {toast && <Toast {...toast} onClose={() => setToast(null)} />}
    </div>
  )
}
