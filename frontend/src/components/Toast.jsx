import React from 'react'
import { motion } from 'framer-motion'
import { AlertCircle, CheckCircle, Info, X } from 'lucide-react'

export default function Toast({ type = 'info', message, onClose }) {
  const bgColor = {
    success: 'bg-accent-emerald/10 border-accent-emerald text-accent-emerald',
    error: 'bg-accent-rose/10 border-accent-rose text-accent-rose',
    info: 'bg-primary-500/10 border-primary-500 text-primary-600',
    warning: 'bg-accent-amber/10 border-accent-amber text-accent-amber',
  }[type]

  const Icon = {
    success: CheckCircle,
    error: AlertCircle,
    info: Info,
    warning: AlertCircle,
  }[type]

  React.useEffect(() => {
    const timer = setTimeout(onClose, 4000)
    return () => clearTimeout(timer)
  }, [onClose])

  return (
    <motion.div
      initial={{ x: 400, opacity: 0 }}
      animate={{ x: 0, opacity: 1 }}
      exit={{ x: 400, opacity: 0 }}
      className={`fixed bottom-4 right-4 border rounded-lg p-4 shadow-lg flex items-center gap-3 glass ${bgColor}`}
    >
      <Icon size={20} />
      <p className="flex-1">{message}</p>
      <button onClick={onClose} className="hover:opacity-70">
        <X size={18} />
      </button>
    </motion.div>
  )
}
