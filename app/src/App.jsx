import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

import DepartureBoard from './components/DepartureBoard.jsx';

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <DepartureBoard />
    </>
  )
}

export default App
