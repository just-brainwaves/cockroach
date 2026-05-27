/**
 * Module  : apps.desktop.src.App
 * Purpose : Root application shell. Defines top-level routing between
 *           the five main pages, renders persistent sidebar navigation,
 *           and hosts the global command palette (Cmd+K).
 * Layer   : Desktop — Application Shell
 */
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Dashboard   from './pages/Dashboard'
import Explorer    from './pages/Explorer'
import Architecture from './pages/Architecture'
import Runtime     from './pages/Runtime'
import Investigate from './pages/Investigate'

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/"              element={<Dashboard />} />
        <Route path="/explorer"      element={<Explorer />} />
        <Route path="/architecture"  element={<Architecture />} />
        <Route path="/runtime"       element={<Runtime />} />
        <Route path="/investigate"   element={<Investigate />} />
      </Routes>
    </BrowserRouter>
  )
}
