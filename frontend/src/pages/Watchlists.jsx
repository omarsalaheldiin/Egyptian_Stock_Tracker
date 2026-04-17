import React,{useEffect,useState} from 'react'
import api from '../api'
import { ArrowUp, ArrowDown, PauseCircle } from 'lucide-react'

export default function Watchlists(){
  const [watchlists,setWatchlists] = useState([])
  const [recs,setRecs] = useState([])
  const [selected,setSelected] = useState(null)
  const [loading,setLoading] = useState(false)
  const [newWatch, setNewWatch] = useState({name:'', description:''})
  const [newRec, setNewRec] = useState({ticker:'', status:'Buy', recommender_name:''})

  useEffect(()=>{fetchData()},[])

  async function fetchData(){
    setLoading(true)
    try{
      const [wRes,rRes] = await Promise.all([api.get('/watchlists'), api.get('/recommendations')])
      setWatchlists(wRes.data || [])
      setRecs(rRes.data || [])
      if(wRes.data && wRes.data.length && !selected) setSelected(wRes.data[0].id)
    }finally{setLoading(false)}
  }

  const list = recs.filter(r=> r.watchlist_id === selected)

  async function addWatchlist(e){
    e && e.preventDefault()
    if(!newWatch.name) return
    await api.post('/watchlists', newWatch)
    setNewWatch({name:'', description:''})
    await fetchData()
  }

  async function deleteWatchlist(id){
    if(!confirm('Delete this watchlist?')) return
    await api.delete(`/watchlists/${id}`)
    await fetchData()
    setSelected((prev)=>{
      const first = watchlists.find(w=>w.id !== id)
      return first ? first.id : null
    })
  }

  async function addRec(e){
    e && e.preventDefault()
    if(!selected || !newRec.ticker) return
    await api.post('/recommendations', {
      watchlist_id: selected,
      ticker: newRec.ticker.toUpperCase(),
      status: newRec.status,
      recommender_name: newRec.recommender_name,
      date_added: new Date().toISOString().slice(0,10)
    })
    setNewRec({ticker:'', status:'Buy', recommender_name:''})
    await fetchData()
  }

  async function deleteRec(id){
    if(!confirm('Delete this recommendation?')) return
    await api.delete(`/recommendations/${id}`)
    await fetchData()
  }

  return (
    <div>
      <h2 className="text-xl font-semibold mb-4">Watchlist Explorer</h2>
      <div className="flex gap-6">
        <aside className="w-64 bg-slate-800/50 p-3 rounded">
          <h3 className="text-sm text-slate-300 mb-2">Watchlists</h3>
          <form onSubmit={addWatchlist} className="space-y-2 mb-3">
            <input className="w-full p-2 bg-slate-900/30 rounded" placeholder="Name" value={newWatch.name} onChange={e=>setNewWatch({...newWatch, name:e.target.value})} />
            <input className="w-full p-2 bg-slate-900/30 rounded" placeholder="Description" value={newWatch.description} onChange={e=>setNewWatch({...newWatch, description:e.target.value})} />
            <button className="w-full px-2 py-1 bg-green-600 rounded" type="submit">Add Watchlist</button>
          </form>
          <ul className="space-y-2">
            {watchlists.map(w=>(
              <li key={w.id} className={`p-2 rounded cursor-pointer ${selected===w.id ? 'bg-slate-700' : ''}`} onClick={()=>setSelected(w.id)}>
                <div className="flex justify-between items-center">
                  <div>
                    <div className="font-semibold">{w.name}</div>
                    <div className="text-xs text-slate-400">{w.description}</div>
                  </div>
                  <div className="ml-2">
                    <button className="px-2 py-1 bg-red-700 rounded text-xs" onClick={(ev)=>{ev.stopPropagation(); deleteWatchlist(w.id)}}>Delete</button>
                  </div>
                </div>
              </li>
            ))}
          </ul>
        </aside>
        <div className="flex-1">
          <h3 className="text-sm text-slate-400 mb-2">Recommendations</h3>
          {selected ? (
            <>
              <form onSubmit={addRec} className="p-3 bg-slate-800/40 rounded mb-3 grid grid-cols-1 md:grid-cols-4 gap-2">
                <input className="p-2 bg-slate-900/30 rounded" placeholder="Ticker" value={newRec.ticker} onChange={e=>setNewRec({...newRec, ticker:e.target.value})} />
                <select className="p-2 bg-slate-900/30 rounded" value={newRec.status} onChange={e=>setNewRec({...newRec, status:e.target.value})}>
                  <option>Buy</option>
                  <option>Hold</option>
                  <option>Take Profit</option>
                  <option>Sell</option>
                  <option>Invest</option>
                </select>
                <input className="p-2 bg-slate-900/30 rounded" placeholder="Recommender" value={newRec.recommender_name} onChange={e=>setNewRec({...newRec, recommender_name:e.target.value})} />
                <div className="flex"><button className="px-3 py-1 bg-green-600 rounded">Add</button></div>
              </form>
              <div className="space-y-2">
                {list.map(r=>(
                  <div key={r.id} className="p-3 bg-slate-800/40 rounded flex items-center justify-between">
                    <div>
                      <div className="font-bold">{r.ticker}</div>
                      <div className="text-xs text-slate-400">By {r.recommender_name} — {r.date_added}</div>
                    </div>
                    <div className="flex items-center space-x-3">
                      {r.status === 'Buy' && <ArrowUp className="text-green-400" />}
                      {r.status === 'Sell' && <ArrowDown className="text-red-400" />}
                      {r.status === 'Hold' && <PauseCircle className="text-amber-400" />}
                      <div className="px-3 py-1 rounded-full bg-slate-900/40 text-sm">{r.status}</div>
                      <button className="px-2 py-1 bg-red-700 rounded text-xs" onClick={()=>deleteRec(r.id)}>Delete</button>
                    </div>
                  </div>
                ))}
              </div>
            </>
          ) : (
            <div className="text-slate-500">Select a watchlist to view recommendations</div>
          )}
        </div>
      </div>
    </div>
  )
}
