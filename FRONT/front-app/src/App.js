import React, { useState } from 'react';
import EditorComponent from './components/Editor/EditorComponent';
import LoginWindowComponent from './components/LoginWindow/LoginWindowComponent';
import './App.css';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [token, setToken] = useState('');

  const handleLogin = (token) => {
    setIsLoggedIn(true);
    setToken(token);
  };

  return (
      <div className="app">
        {isLoggedIn ? (
            <EditorComponent token={token}/>
        ) : (
            <LoginWindowComponent handleLogin={handleLogin} />
        )}
      </div>
  );
}

export default App;