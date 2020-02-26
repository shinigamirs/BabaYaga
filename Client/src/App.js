import React, { useState, useEffect } from 'react';
import logo from './logo512.png';
import './App.css';

import { ReadCard } from "./libs";
import { fetchUserFromId, logoutUser } from "./services";

const readCard = new ReadCard();

function App() {
  const [authenticatedUser, setAuthenticatedUser] = useState(null);
  const [statusText, setStatusText] = useState(false);

  async function startCardScanning() {
    setStatusText("scanning");
    const userId = await readCard.read();
    setStatusText(null);

    setStatusText("authenticating")
    const result = await fetchUserFromId(userId);
    setStatusText(null);

    setAuthenticatedUser(result.user);
  }

  async function logout() {
    setStatusText("logging out")
    const result = await logoutUser(authenticatedUser.id);
    setStatusText(null);

    setAuthenticatedUser(null);
  }

  useEffect(() => {

  })


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        {!statusText && !authenticatedUser && <>
          <p>
            Scan your ID to get started <br />
          </p>
          <a
            className="App-link"
            target="_blank"
            rel="noopener noreferrer"
            onClick={startCardScanning}
          >
            Get Started
          </a>
        </>
        }
        {
          statusText && <p>{statusText}...</p>
        }
        {
          !statusText && authenticatedUser && <>
            <p>Hi, {authenticatedUser.name}</p>
            <a
              className="App-link"
              target="_blank"
              rel="noopener noreferrer"
              onClick={logout}
            >
              logout
            </a>
          </>
        }
      </header>
    </div>
  );
}

export default App;
