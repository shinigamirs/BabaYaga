import React, { useState, useEffect } from 'react';
import logo from './logo512.png';
import './App.css';

import { ReadCard, ReadBarcode } from "./libs";
import { fetchUserFromId, logoutUser, issueBook, returnBook } from "./services";

const readCard = new ReadCard();
const readBarcode = new ReadBarcode();

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

  async function startBarcodeScanning() {
    setStatusText("scanning barcode");
    const bookId = await readBarcode.read();
    setStatusText(null);
    return bookId;
  }

  async function startIssuingBook() {
    const bookId = await startBarcodeScanning();

    setStatusText("issuing book")
    const result = await issueBook(authenticatedUser.id, bookId);
    setAuthenticatedUser({
      ...authenticatedUser,
      issuedCount: result.issuedCount,
    });
    setStatusText(null);
  }

  async function startReturningBook() {
    const bookId = await startBarcodeScanning();

    setStatusText("returning book")
    const result = await returnBook(authenticatedUser.id, bookId);
    setAuthenticatedUser({
      ...authenticatedUser,
      issuedCount: result.issuedCount,
    });

    setStatusText(null);
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
            <div>You have {authenticatedUser.issuedCount} books on you :)</div>
            <p>
              <a
                className="App-link"
                target="_blank"
                rel="noopener noreferrer"
                onClick={startIssuingBook}
              >
                issue book
              </a>
              &nbsp;-&nbsp;
              <a
                className="App-link"
                target="_blank"
                rel="noopener noreferrer"
                onClick={startReturningBook}
              >
                return book
              </a>
              &nbsp;-&nbsp;
              <a
                className="App-link"
                target="_blank"
                rel="noopener noreferrer"
                onClick={logout}
              >
                logout
              </a>
            </p>
          </>
        }
      </header>
    </div>
  );
}

export default App;
