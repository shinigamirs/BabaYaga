import React, { useState, useEffect } from 'react';
import logo from './logo512.png';
import './App.css';

const pyshell = new window.PythonShell("lib/dummy.py");

function App() {
  const [count, setCount] = useState(0)

  function updateCount(message) {
    // received a message sent from the Python script (a simple "print" statement)
    setCount(parseInt(message))
  }

  useEffect(() => {
    pyshell.on('message', updateCount);

    return () => pyshell.removeListener('message', updateCount);
  })


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Scan your ID to get started <br />
          <h6>Python clock has fired {count} times. Check out lib/dummy.py.</h6>
        </p>
        <a
          className="App-link"
          target="_blank"
          rel="noopener noreferrer"
        >
          Get Started
        </a>
      </header>
    </div>
  );
}

export default App;
