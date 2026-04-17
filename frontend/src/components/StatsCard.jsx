import React from 'react'
import { motion } from 'framer-motion'
import { TrendingUp, TrendingDown, BarChart3 } from 'lucide-react'

export default function StatsCard({ title, value, icon: Icon, color = 'blue', trend, subtext }) {
  const colorClasses = {
    blue: 'from-primary-500 to-primary-600',
    green: 'from-accent-emerald to-emerald-700',
    amber: 'from-accent-amber to-amber-700',
    rose: 'from-accent-rose to-rose-700',
    violet: 'from-accent-violet to-violet-700',
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      whileHover={{ y: -5 }}
      className={`bg-gradient-to-br ${colorClasses[color]} rounded-lg p-6 text-white shadow-lg`}
    >
      <div className="flex items-start justify-between">
        <div>
          <p className="text-white/80 text-sm font-medium">{title}</p>
          <motion.h3
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.2 }}
            className="text-3xl font-bold mt-2"
          >
            {typeof value === 'number' ? value.toLocaleString() : value}
          </motion.h3>
          {subtext && <p className="text-white/70 text-xs mt-1">{subtext}</p>}
        </div>
        <motion.div
          animate={{ rotate: [0, 5, -5, 0] }}
          transition={{ duration: 3, repeat: Infinity }}
          className="bg-white/20 p-3 rounded-lg"
        >
          <Icon size={24} className="text-white" />
        </motion.div>
      </div>
      {trend && (
        <div className="mt-4 flex items-center gap-1 text-sm">
          {trend > 0 ? (
            <>
              <TrendingUp size={16} />
              <span>+{trend}%</span>
            </>
          ) : (
            <>
              <TrendingDown size={16} />
              <span>{trend}%</span>
            </>
          )}
        </div>
      )}
    </motion.div>
  )
}
