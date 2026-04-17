import React,{useEffect,useState} from 'react'
import api from '../api'

export default function Aggregator(){
  const [data,setData] = useState([])
  const [filter,setFilter] = useState('')
  const [ownedFilter,setOwnedFilter] = useState(false)
  const [owned,setOwned] = useState([])
  const [query,setQuery] = useState('')

  useEffect(()=>{fetchData()},[])
  async function fetchData(){
    const [aRes,pRes] = await Promise.all([api.get('/aggregator'), api.get('/portfolio')])
    setData(aRes.data || [])
    setOwned((pRes.data || []).map(i=>i.ticker))
  }

  const filtered = data.filter(item=>{
    if(filter && item.prevailing !== filter) return false
    if(ownedFilter && !owned.includes(item.ticker)) return false
    if(query && !item.ticker.toLowerCase().includes(query.toLowerCase())) return false
    return true
  })

  return (
    <div>
      <h2 className="text-xl font-semibold mb-4">Global Aggregator</h2>
      <div className="flex gap-4 mb-4 items-center">
        <input className="p-2 bg-slate-800/50 rounded" placeholder="Search ticker" value={query} onChange={e=>setQuery(e.target.value)} />
        <select value={filter} onChange={e=>setFilter(e.target.value)} className="bg-slate-800/50 p-2 rounded">
          <option value="">All statuses</option>
          <option value="Buy">Buy</option>
          <option value="Sell">Sell</option>
          <option value="Hold">Hold</option>
          <option value="Take Profit">Take Profit</option>
          <option value="Invest">Invest</option>
        </select>
        <label className="flex items-center gap-2">
          <input type="checkbox" checked={ownedFilter} onChange={e=>setOwnedFilter(e.target.checked)} />
          <span className="text-slate-400">Stocks I Own</span>
        </label>
      </div>
      <div className="space-y-2">
        {filtered.map(it=>(
          <div key={it.ticker} className="p-3 bg-slate-800/50 rounded flex justify-between">
            <div>
              <div className="font-bold">{it.ticker}</div>
              <div className="text-xs text-slate-400">Total mentions: {it.total}</div>
            </div>
            <div className="text-right">
              <div className="text-sm text-slate-300">Prevailing: <span className="font-semibold">{it.prevailing}</span></div>
              <div className="text-xs text-slate-400">{JSON.stringify(it.counts)}</div>
            </div>
          </div>
        ))}
        {filtered.length === 0 && <div className="text-slate-500">No results</div>}
      </div>
    </div>
  )
}
