import React, {useEffect, useState} from 'react'
import api from '../api'

const Badge = ({label, type})=>{
  const classes = {
    buy:'text-green-400 bg-green-900/20 ring-1 ring-green-500/30 shadow-[0_0_8px_rgba(34,197,94,0.12)]',
    sell:'text-red-400 bg-red-900/20 ring-1 ring-red-500/30 shadow-[0_0_8px_rgba(239,68,68,0.12)]',
    neutral: 'text-amber-400 bg-amber-900/20 ring-1 ring-amber-500/30'
  }
  return <span className={`px-3 py-1 rounded-full text-sm font-semibold ${classes[type]||classes.neutral}`}>{label}</span>
}

export default function Portfolio(){
  const [items,setItems] = useState([])
  const [loading,setLoading] = useState(false)
  const [showAdd,setShowAdd] = useState(false)
  const [form,setForm] = useState({ticker:'', total_shares:'', average_cost:'', current_value_pounds:''})
  const [editing,setEditing] = useState(null)
  const [editForm,setEditForm] = useState({})
  const [conflicts,setConflicts] = useState(new Set())

  useEffect(()=>{fetchData(); fetchConflicts()},[])

  async function fetchData(){
    setLoading(true)
    try{
      const res = await api.get('/portfolio')
      setItems(res.data || [])
    }finally{setLoading(false)}
  }

  async function fetchConflicts(){
    try{
      const res = await api.get('/conflicts')
      const set = new Set((res.data || []).map(c=>c.ticker))
      setConflicts(set)
    }catch(e){/* ignore */}
  }

  async function addHolding(e){
    e && e.preventDefault()
    if(!form.ticker) return
    await api.post('/portfolio', {
      ticker: form.ticker.toUpperCase(),
      total_shares: Number(form.total_shares) || 0,
      average_cost: Number(form.average_cost) || 0,
      current_value_pounds: Number(form.current_value_pounds) || 0,
    })
    setForm({ticker:'', total_shares:'', average_cost:'', current_value_pounds:''})
    setShowAdd(false)
    await fetchData()
    await fetchConflicts()
  }

  function startEdit(item){
    setEditing(item.ticker)
    setEditForm({
      total_shares: item.total_shares,
      average_cost: item.average_cost,
      current_value_pounds: item.current_value_pounds
    })
  }

  async function saveEdit(ticker){
    await api.put(`/portfolio/${ticker}`, {
      ticker,
      total_shares: Number(editForm.total_shares) || 0,
      average_cost: Number(editForm.average_cost) || 0,
      current_value_pounds: Number(editForm.current_value_pounds) || 0,
    })
    setEditing(null)
    await fetchData()
    await fetchConflicts()
  }

  async function deleteHolding(ticker){
    if(!confirm(`Delete holding ${ticker}?`)) return
    await api.delete(`/portfolio/${ticker}`)
    await fetchData()
    await fetchConflicts()
  }

  function positionType(mult){
    if(mult >= 3) return 'buy'
    if(mult >= 1) return 'neutral'
    return 'sell'
  }

  return (
    <div>
      <h2 className="text-xl font-semibold mb-4">Command Center — Portfolio</h2>

      <div className="mb-4 flex items-center justify-between">
        <div className="text-slate-300">Manage your holdings and monitor conflicts</div>
        <div>
          <button className="px-3 py-1 rounded bg-slate-700 text-slate-100" onClick={()=>setShowAdd(s => !s)}>{showAdd ? 'Close' : 'Add Holding'}</button>
        </div>
      </div>

      {showAdd && (
        <form onSubmit={addHolding} className="mb-4 p-4 bg-slate-800/50 rounded grid grid-cols-1 md:grid-cols-4 gap-3">
          <input className="p-2 bg-slate-900/30 rounded" placeholder="Ticker" value={form.ticker} onChange={e=>setForm({...form, ticker:e.target.value})} />
          <input className="p-2 bg-slate-900/30 rounded" placeholder="Total shares" value={form.total_shares} onChange={e=>setForm({...form, total_shares:e.target.value})} />
          <input className="p-2 bg-slate-900/30 rounded" placeholder="Average cost" value={form.average_cost} onChange={e=>setForm({...form, average_cost:e.target.value})} />
          <div className="flex gap-2">
            <input className="p-2 bg-slate-900/30 rounded flex-1" placeholder="Current value (GBP)" value={form.current_value_pounds} onChange={e=>setForm({...form, current_value_pounds:e.target.value})} />
            <button className="px-3 py-1 rounded bg-green-600" type="submit">Add</button>
          </div>
        </form>
      )}

      {loading && <div className="text-slate-400 mb-4">Loading...</div>}

      <div className="grid gap-4">
        {items.map(it=>{
          const mult = parseFloat(it.position_multiplier) || 0
          return (
            <div key={it.ticker} className="p-4 bg-slate-800/60 rounded-lg flex items-center justify-between">
              <div>
                <div className="flex items-center space-x-3">
                  <div className="text-2xl font-bold">{it.ticker}</div>
                  <div className="text-sm text-slate-400">Owned: {it.total_shares} | Avg cost: £{it.average_cost}</div>
                  {conflicts.has(it.ticker) && <span className="ml-2 px-2 py-1 rounded bg-red-900 text-red-300 text-xs font-semibold">High Priority Action</span>}
                </div>
                <div className="text-sm text-slate-300 mt-2">Market Sentiment: {it.sentiment_summary || 'None'}</div>
              </div>
              <div className="flex items-center space-x-4">
                <div className="text-center mr-4">
                  <div className="text-sm text-slate-400">Position</div>
                  <div className="text-3xl font-extrabold">{it.position_label}</div>
                </div>
                <Badge label={it.position_label} type={positionType(mult)} />
                <div className="flex flex-col items-end ml-4">
                  {editing === it.ticker ? (
                    <div className="flex gap-2">
                      <input className="p-1 w-20 rounded bg-slate-900/30" value={editForm.total_shares} onChange={e=>setEditForm({...editForm, total_shares:e.target.value})} />
                      <input className="p-1 w-20 rounded bg-slate-900/30" value={editForm.average_cost} onChange={e=>setEditForm({...editForm, average_cost:e.target.value})} />
                      <input className="p-1 w-24 rounded bg-slate-900/30" value={editForm.current_value_pounds} onChange={e=>setEditForm({...editForm, current_value_pounds:e.target.value})} />
                      <button className="px-2 py-1 bg-green-600 rounded" onClick={()=>saveEdit(it.ticker)}>Save</button>
                      <button className="px-2 py-1 bg-slate-700 rounded" onClick={()=>setEditing(null)}>Cancel</button>
                    </div>
                  ) : (
                    <div className="flex gap-2">
                      <button className="px-2 py-1 bg-slate-700 rounded" onClick={()=>startEdit(it)}>Edit</button>
                      <button className="px-2 py-1 bg-red-700 rounded" onClick={()=>deleteHolding(it.ticker)}>Delete</button>
                    </div>
                  )}
                </div>
              </div>
            </div>
          )
        })}
      </div>
    </div>
  )
}
