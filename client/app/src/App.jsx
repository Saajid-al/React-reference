import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <h1>
      Job Tracker
    </h1>
    <div> 
      <input type="text" placeholder='Enter Job URL' />
      <input type="number" placeholder='Applied Date' />
      <button>Submit Job</button>
    </div>
    </>
  )
}

export default App
