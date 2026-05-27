/**
 * Module  : apps.desktop.src.main
 * Purpose : React application entry point. Mounts App into #root,
 *           wraps with QueryClientProvider (async data), and initialises
 *           Tauri event listeners for native OS callbacks.
 * Layer   : Desktop — Bootstrap
 */
import React from 'react'
import ReactDOM from 'react-dom/client'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import App from './App'
import './index.css'

const queryClient = new QueryClient()

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <App />
    </QueryClientProvider>
  </React.StrictMode>
)
