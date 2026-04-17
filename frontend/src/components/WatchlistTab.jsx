import React, { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Plus, Trash2, TrendingUp, Star } from 'lucide-react'
import { watchlistAPI } from '../services/api'
import Toast from './Toast'
import LoadingSpinner from './LoadingSpinner'

const STATUS_COLORS = {
  'Buy': 'from-accent-emerald to-emerald-700',
  'Hold': 'from-primary-500 to-primary-600',
  'Take Profit': 'from-accent-amber to-amber-700',
  'Invest': 'from-accent-violet to-violet-700',
}

const STATUS_BADGE = {
  'Buy': 'bg-accent-emerald/10 text-accent-emerald border-accent-emerald/20',
  'Hold': 'bg-primary-500/10 text-primary-700 border-primary-500/20',
  'Take Profit': 'bg-accent-amber/10 text-accent-amber border-accent-amber/20',
  'Invest': 'bg-accent-violet/10 text-accent-violet border-accent-violet/20',
}

export default function WatchlistTab() {
  const [watchlists, setWatchlists] = useState([])
  const [selectedWatchlist, setSelectedWatchlist] = useState(null)
  const [items, setItems] = useState([])
  const [loading, setLoading] = useState(true)
  const [toast, setToast] = useState(null)
  const [newWatchlistName, setNewWatchlistName] = useState('')
  const [newItemData, setNewItemData] = useState({ stock_name: '', status: 'Buy' })

  useEffect(() => {
    loadWatchlists()
  }, [])

  useEffect(() => {
    if (selectedWatchlist) {
      loadWatchlistItems()
    }
  }, [selectedWatchlist])

  const loadWatchlists = async () => {
    try {
      setLoading(true)
      const res = await watchlistAPI.getAll()
      setWatchlists(res.data || [])
      if (!selectedWatchlist && res.data?.length > 0) {
        setSelectedWatchlist(res.data[0])
      }
    } catch (error) {
      showToast('Failed to load watchlists', 'error')
    } finally {
      setLoading(false)
    }
  }

  const loadWatchlistItems = async () => {
    try {
      const res = await watchlistAPI.getItems(selectedWatchlist.watchlist_id)
      setItems(res.data || [])
    } catch (error) {
      showToast('Failed to load items', 'error')
    }
  }

  const handleCreateWatchlist = async () => {
    if (!newWatchlistName.trim()) {
      showToast('Enter a watchlist name', 'warning')
      return
    }
    try {
      await watchlistAPI.create({ watchlist_name: newWatchlistName })
      showToast('Watchlist created', 'success')
      setNewWatchlistName('')
      loadWatchlists()
    } catch (error) {
      showToast('Failed to create watchlist', 'error')
    }
  }

  const handleAddItem = async () => {
    if (!newItemData.stock_name.trim() || !newItemData.status) {
      showToast('Fill all fields', 'warning')
      return
    }
    try {
      await watchlistAPI.addItem(selectedWatchlist.watchlist_id, {
        stock_name: newItemData.stock_name,
        status: newItemData.status
      })
      showToast('Stock added to watchlist', 'success')
      setNewItemData({ stock_name: '', status: 'Buy' })
      loadWatchlistItems()
    } catch (error) {
      showToast('Failed to add item', 'error')
    }
  }

  const handleDeleteItem = async (stockName) => {
    if (!window.confirm(`Remove ${stockName}?`)) return
    try {
      await watchlistAPI.deleteItem(selectedWatchlist.watchlist_id, stockName)
      showToast('Stock removed', 'success')
      loadWatchlistItems()
    } catch (error) {
      showToast('Failed to remove stock', 'error')
    }
  }

  const handleDeleteWatchlist = async () => {
    if (!window.confirm('Delete watchlist and all items?')) return
    try {
      await watchlistAPI.delete(selectedWatchlist.watchlist_id)
      showToast('Watchlist deleted', 'success')
      setSelectedWatchlist(null)
      loadWatchlists()
    } catch (error) {
      showToast('Failed to delete watchlist', 'error')
    }
  }

  const showToast = (message, type) => {
    setToast({ message, type })
  }

  if (loading) return <LoadingSpinner />

  return (
    <div className="space-y-6">
      {/* Create Watchlist */}
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="glass rounded-lg p-6 border border-gray-200"
      >
        <h3 className="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
          <Star size={20} className="text-accent-amber" />
          Create New Watchlist
        </h3>
        <div className="flex gap-3">
          <input
            type="text"
            placeholder="Watchlist name (e.g., Growth Stocks)"
            value={newWatchlistName}
            onChange={(e) => setNewWatchlistName(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleCreateWatchlist()}
            className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
          />
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={handleCreateWatchlist}
            className="bg-gradient-to-r from-accent-amber to-amber-700 text-white font-semibold py-2 px-6 rounded-lg hover:shadow-lg"
          >
            <Plus size={18} className="inline mr-2" />
            Create
          </motion.button>
        </div>
      </motion.div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Watchlists List */}
        <motion.div
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.1 }}
          className="glass rounded-lg p-6 border border-gray-200"
        >
          <h3 className="text-lg font-bold text-gray-800 mb-4">Your Watchlists</h3>
          <div className="space-y-2">
            <AnimatePresence>
              {watchlists.map((wl) => (
                <motion.button
                  key={wl.watchlist_id}
                  initial={{ opacity: 0, x: -10 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ opacity: 0, x: -10 }}
                  onClick={() => setSelectedWatchlist(wl)}
                  className={`w-full text-left p-3 rounded-lg transition-all ${
                    selectedWatchlist?.watchlist_id === wl.watchlist_id
                      ? 'bg-gradient-to-r from-primary-500 to-primary-600 text-white shadow-lg'
                      : 'bg-gray-100 text-gray-800 hover:bg-gray-200'
                  }`}
                >
                  <div className="font-semibold">{wl.watchlist_name}</div>
                  <div className="text-xs opacity-70 mt-1">{items.length} stocks</div>
                </motion.button>
              ))}
            </AnimatePresence>
          </div>
        </motion.div>

        {/* Watchlist Items */}
        {selectedWatchlist && (
          <motion.div
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.2 }}
            className="lg:col-span-2 glass rounded-lg p-6 border border-gray-200"
          >
            <div className="flex items-center justify-between mb-6">
              <h3 className="text-lg font-bold text-gray-800">{selectedWatchlist.watchlist_name}</h3>
              <motion.button
                whileHover={{ scale: 1.1 }}
                whileTap={{ scale: 0.95 }}
                onClick={handleDeleteWatchlist}
                className="text-accent-rose hover:bg-accent-rose/10 p-2 rounded-lg"
              >
                <Trash2 size={20} />
              </motion.button>
            </div>

            {/* Add Item */}
            <div className="mb-6 pb-6 border-b border-gray-200">
              <p className="text-sm font-semibold text-gray-600 mb-3">Add Stock</p>
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                <input
                  type="text"
                  placeholder="Stock name"
                  value={newItemData.stock_name}
                  onChange={(e) => setNewItemData({ ...newItemData, stock_name: e.target.value })}
                  className="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
                />
                <select
                  value={newItemData.status}
                  onChange={(e) => setNewItemData({ ...newItemData, status: e.target.value })}
                  className="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
                >
                  <option>Buy</option>
                  <option>Hold</option>
                  <option>Take Profit</option>
                  <option>Invest</option>
                </select>
                <motion.button
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                  onClick={handleAddItem}
                  className="bg-gradient-to-r from-primary-500 to-primary-600 text-white font-semibold py-2 px-4 rounded-lg hover:shadow-lg"
                >
                  <Plus size={16} className="inline mr-2" />
                  Add
                </motion.button>
              </div>
            </div>

            {/* Items List */}
            <div className="space-y-3">
              <p className="text-sm font-semibold text-gray-600">Stocks in Watchlist</p>
              <AnimatePresence>
                {items.map((item, idx) => (
                  <motion.div
                    key={item.stock_name}
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -10 }}
                    transition={{ delay: idx * 0.05 }}
                    whileHover={{ x: 5 }}
                    className="flex items-center justify-between p-3 bg-gray-50 rounded-lg group hover:bg-gray-100 transition-colors"
                  >
                    <div>
                      <p className="font-semibold text-gray-800">{item.stock_name}</p>
                      <span className={`inline-block mt-1 px-2 py-1 rounded-full text-xs font-semibold border ${STATUS_BADGE[item.status]}`}>
                        {item.status}
                      </span>
                    </div>
                    <motion.button
                      whileHover={{ scale: 1.1 }}
                      whileTap={{ scale: 0.95 }}
                      onClick={() => handleDeleteItem(item.stock_name)}
                      className="text-accent-rose opacity-0 group-hover:opacity-100 transition-opacity"
                    >
                      <Trash2 size={18} />
                    </motion.button>
                  </motion.div>
                ))}
              </AnimatePresence>
              {items.length === 0 && (
                <div className="text-center py-8 text-gray-400">No stocks in this watchlist yet</div>
              )}
            </div>
          </motion.div>
        )}
      </div>

      {toast && <Toast {...toast} onClose={() => setToast(null)} />}
    </div>
  )
}
