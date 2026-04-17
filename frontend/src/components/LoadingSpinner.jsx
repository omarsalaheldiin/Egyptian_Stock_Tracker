import React from 'react'
import { motion } from 'framer-motion'

export default function LoadingSpinner() {
  return (
    <div className="flex items-center justify-center p-8">
      <motion.div
        animate={{ rotate: 360 }}
        transition={{ duration: 1, repeat: Infinity, ease: 'linear' }}
        className="w-12 h-12 border-4 border-primary-200 border-t-primary-500 rounded-full"
      />
      <span className="ml-3 text-primary-600 font-semibold">Loading...</span>
    </div>
  )
}

export function LoadingOverlay() {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50"
    >
      <motion.div
        animate={{ scale: [1, 1.1, 1] }}
        transition={{ duration: 0.6, repeat: Infinity }}
        className="bg-white rounded-lg p-8 shadow-lg"
      >
        <motion.div
          animate={{ rotate: 360 }}
          transition={{ duration: 1, repeat: Infinity, ease: 'linear' }}
          className="w-16 h-16 border-4 border-primary-200 border-t-primary-500 rounded-full mx-auto"
        />
        <p className="mt-4 text-gray-600 font-medium text-center">Processing...</p>
      </motion.div>
    </motion.div>
  )
}
