import React, { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Plus, Trash2, Edit2, DollarSign } from 'lucide-react'
import { portfolioAPI } from '../services/api'
import Toast from './Toast'
import LoadingSpinner from './LoadingSpinner'

export default function PortfolioTab() {
  const [stocks, setStocks] = useState([])
  const [loading, setLoading] = useState(true)
  const [toast, setToast] = useState(null)
  const [formData, setFormData] = useState({ stock_name: '', amount_egp: '' })

  useEffect(() => {
    loadPortfolio()
  }, [])

  const loadPortfolio = async () => {
    try {
      setLoading(true)
      const res = await portfolioAPI.getAll()
      setStocks(res.data || [])
    } catch (error) {
      showToast('Failed to load portfolio', 'error')
      console.error(error)
    } finally {
      setLoading(false)
    }
  }

  const handleAddStock = async () => {
    if (!formData.stock_name.trim() || !formData.amount_egp) {
      showToast('Please fill all fields', 'warning')
      return
    }

    try {
      await portfolioAPI.add({
        stock_name: formData.stock_name,
        amount_egp: parseFloat(formData.amount_egp)
      })
      showToast('Stock added successfully', 'success')
      setFormData({ stock_name: '', amount_egp: '' })
      loadPortfolio()
    } catch (error) {
      showToast('Failed to add stock', 'error')
    }
  }

  const handleDelete = async (stockName) => {
    if (window.confirm(`Delete ${stockName}?`)) {
      try {
        await portfolioAPI.delete(stockName)
        showToast('Stock deleted', 'success')
        loadPortfolio()
      } catch (error) {
        showToast('Failed to delete stock', 'error')
      }
    }
  }

  const showToast = (message, type) => {
    setToast({ message, type })
  }

  const totalValue = stocks.reduce((sum, s) => sum + s.amount_egp, 0)

  if (loading) return <LoadingSpinner />

  return (
    <div className="space-y-6">
      {/* Stats */}
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="grid grid-cols-1 sm:grid-cols-3 gap-4"
      >
        <div className="glass rounded-lg p-4 border-l-4 border-primary-500">
          <p className="text-gray-600 text-sm">Total Value</p>
          <p className="text-2xl font-bold text-primary-600">{totalValue.toLocaleString()} EGP</p>
        </div>
        <div className="glass rounded-lg p-4 border-l-4 border-accent-emerald">
          <p className="text-gray-600 text-sm">Total Stocks</p>
          <p className="text-2xl font-bold text-accent-emerald">{stocks.length}</p>
        </div>
        <div className="glass rounded-lg p-4 border-l-4 border-accent-violet">
          <p className="text-gray-600 text-sm">Avg per Stock</p>
          <p className="text-2xl font-bold text-accent-violet">
            {stocks.length > 0 ? (totalValue / stocks.length).toLocaleString() : 0} EGP
          </p>
        </div>
      </motion.div>

      {/* Add Form */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1 }}
        className="glass rounded-lg p-6 border border-gray-200"
      >
        <h3 className="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
          <Plus size={20} className="text-primary-500" />
          Add Stock to Portfolio
        </h3>
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <input
            type="text"
            placeholder="Stock Name"
            value={formData.stock_name}
            onChange={(e) => setFormData({ ...formData, stock_name: e.target.value })}
            className="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
          />
          <input
            type="number"
            placeholder="Amount (EGP)"
            value={formData.amount_egp}
            onChange={(e) => setFormData({ ...formData, amount_egp: e.target.value })}
            className="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
          />
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={handleAddStock}
            className="bg-gradient-to-r from-primary-500 to-primary-600 text-white font-semibold py-2 px-6 rounded-lg hover:shadow-lg transition-all"
          >
            <Plus size={18} className="inline mr-2" />
            Add Stock
          </motion.button>
        </div>
      </motion.div>

      {/* Stocks List */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.2 }}
        className="glass rounded-lg p-6 border border-gray-200"
      >
        <h3 className="text-lg font-bold text-gray-800 mb-4">Your Holdings</h3>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <AnimatePresence>
            {stocks.map((stock, idx) => (
              <motion.div
                key={stock.stock_name}
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0, scale: 0.9 }}
                transition={{ delay: idx * 0.05 }}
                whileHover={{ y: -5 }}
                className="glass rounded-lg p-4 border border-gray-200 hover:border-primary-400 group"
              >
                <div className="flex items-start justify-between mb-3">
                  <h4 className="font-bold text-gray-800 group-hover:text-primary-600 transition-colors">
                    {stock.stock_name}
                  </h4>
                  <motion.button
                    whileHover={{ scale: 1.1 }}
                    whileTap={{ scale: 0.9 }}
                    onClick={() => handleDelete(stock.stock_name)}
                    className="text-accent-rose opacity-0 group-hover:opacity-100 transition-opacity"
                  >
                    <Trash2 size={18} />
                  </motion.button>
                </div>
                <div className="flex items-center gap-2 text-2xl font-bold text-primary-600">
                  <DollarSign size={24} />
                  {stock.amount_egp.toLocaleString()}
                </div>
                <p className="text-xs text-gray-500 mt-2">EGP</p>
              </motion.div>
            ))}
          </AnimatePresence>
        </div>
        {stocks.length === 0 && (
          <motion.div
            animate={{ opacity: [0.5, 1, 0.5] }}
            transition={{ duration: 2, repeat: Infinity }}
            className="text-center py-8 text-gray-400"
          >
            No stocks yet. Add your first stock!
          </motion.div>
        )}
      </motion.div>

      {toast && <Toast {...toast} onClose={() => setToast(null)} />}
    </div>
  )
}
