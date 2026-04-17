import React, { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { TrendingUp, Wallet, Star, BarChart3, Menu, X, Github } from 'lucide-react'
import PortfolioTab from './components/PortfolioTab'
import WatchlistTab from './components/WatchlistTab'
import SummaryTab from './components/SummaryTab'
import './index.css'

const TABS = [
  { id: 'portfolio', label: 'Portfolio', icon: Wallet },
  { id: 'watchlist', label: 'Watchlist', icon: Star },
  { id: 'summary', label: 'Summary', icon: BarChart3 },
]

export default function App() {
  const [activeTab, setActiveTab] = useState('portfolio')
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)

  return (
    <div className="min-h-screen bg-gradient-to-br from-violet-50 via-blue-50 to-pink-50">
      {/* Header */}
      <motion.header
        initial={{ y: -100 }}
        animate={{ y: 0 }}
        transition={{ type: 'spring', stiffness: 100 }}
        className="glass sticky top-0 z-40 border-b border-gray-200 shadow-soft"
      >
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between">
            <motion.div
              whileHover={{ scale: 1.05 }}
              className="flex items-center gap-3"
            >
              <motion.div
                animate={{ rotate: 360 }}
                transition={{ duration: 4, repeat: Infinity, ease: 'linear' }}
                className="bg-gradient-to-r from-primary-500 to-accent-violet p-2 rounded-lg"
              >
                <TrendingUp size={28} className="text-white" />
              </motion.div>
              <div>
                <h1 className="text-2xl font-bold bg-gradient-to-r from-primary-600 to-accent-violet bg-clip-text text-transparent">
                  Stock Tracker
                </h1>
                <p className="text-xs text-gray-500">Egyptian Market</p>
              </div>
            </motion.div>

            {/* Desktop Navigation */}
            <nav className="hidden md:flex items-center gap-2">
              {TABS.map((tab) => {
                const Icon = tab.icon
                return (
                  <motion.button
                    key={tab.id}
                    whileHover={{ scale: 1.05 }}
                    whileTap={{ scale: 0.95 }}
                    onClick={() => setActiveTab(tab.id)}
                    className={`flex items-center gap-2 px-4 py-2 rounded-lg font-semibold transition-all ${
                      activeTab === tab.id
                        ? 'bg-gradient-to-r from-primary-500 to-primary-600 text-white shadow-lg'
                        : 'text-gray-700 hover:bg-gray-100'
                    }`}
                  >
                    <Icon size={18} />
                    {tab.label}
                  </motion.button>
                )
              })}
            </nav>

            {/* Mobile Menu Button */}
            <motion.button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="md:hidden p-2 hover:bg-gray-100 rounded-lg transition-colors"
              whileHover={{ scale: 1.1 }}
              whileTap={{ scale: 0.95 }}
            >
              {mobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
            </motion.button>
          </div>

          {/* Mobile Navigation */}
          <AnimatePresence>
            {mobileMenuOpen && (
              <motion.nav
                initial={{ opacity: 0, y: -10 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -10 }}
                className="md:hidden mt-4 flex flex-col gap-2"
              >
                {TABS.map((tab) => {
                  const Icon = tab.icon
                  return (
                    <motion.button
                      key={tab.id}
                      onClick={() => {
                        setActiveTab(tab.id)
                        setMobileMenuOpen(false)
                      }}
                      className={`flex items-center gap-2 px-4 py-2 rounded-lg font-semibold transition-all w-full ${
                        activeTab === tab.id
                          ? 'bg-gradient-to-r from-primary-500 to-primary-600 text-white'
                          : 'text-gray-700 hover:bg-gray-100'
                      }`}
                    >
                      <Icon size={18} />
                      {tab.label}
                    </motion.button>
                  )
                })}
              </motion.nav>
            )}
          </AnimatePresence>
        </div>
      </motion.header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
        >
          {activeTab === 'portfolio' && <PortfolioTab />}
          {activeTab === 'watchlist' && <WatchlistTab />}
          {activeTab === 'summary' && <SummaryTab />}
        </motion.div>
      </main>

      {/* Footer */}
      <motion.footer
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5 }}
        className="border-t border-gray-200 mt-12 py-6 text-center text-gray-600 text-sm"
      >
        <p>© 2026 Egyptian Stock Tracker • Built with ❤️ for traders</p>
      </motion.footer>
    </div>
  )
}
