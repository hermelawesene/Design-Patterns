import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import Observer from './Observer.jsx'
import Composite from './Composite.jsx'
import Factory from './Factory.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
    <Observer/>
    <Composite />
    <Factory />
  </StrictMode>,
)
