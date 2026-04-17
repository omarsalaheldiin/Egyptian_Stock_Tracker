import React from 'react'
import { Routes, Route, Link } from 'react-router-dom'
import Portfolio from './pages/Portfolio'
import Watchlists from './pages/Watchlists'
import Aggregator from './pages/Aggregator'

export default function App(){
  return (
    <div className="min-h-screen p-6 bg-slate-900">
      <header className="mb-6 flex items-center justify-between">
        <h1 className="text-2xl font-bold text-white">Stock Intelligence System</h1>
        <nav className="space-x-4">
          <Link to="/" className="text-slate-300 hover:text-white">Portfolio</Link>
          <Link to="/watchlists" className="text-slate-300 hover:text-white">Watchlists</Link>
          <Link to="/aggregator" className="text-slate-300 hover:text-white">Aggregator</Link>
        </nav>
      </header>
      <main>
        <Routes>
          <Route path="/" element={<Portfolio />} />
          <Route path="/watchlists" element={<Watchlists />} />
          <Route path="/aggregator" element={<Aggregator />} />
        </Routes>
      </main>
    </div>
  )
}
