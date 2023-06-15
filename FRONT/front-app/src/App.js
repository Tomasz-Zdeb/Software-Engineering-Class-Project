import React, {useEffect, useState} from 'react';
import EditorComponent from './components/Editor/EditorComponent';
import LoginWindowComponent from './components/LoginWindow/LoginWindowComponent';
import './App.css';

function App() {
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [token, setToken] = useState('');

    const handleLogin = (newToken) => {
        setIsLoggedIn(true);
        setToken(newToken);
        localStorage.setItem('token', newToken);
    };


    useEffect(() => {
        const cachedToken = localStorage.getItem('token');
        if (cachedToken) {
            setIsLoggedIn(true);
            setToken(cachedToken);
        }
    }, []);


    return (
        <div className="app">
            {isLoggedIn ? (
                <EditorComponent token={token} setToken={setToken} setIsLoggedIn={setIsLoggedIn}/>
            ) : (
                <LoginWindowComponent handleLogin={handleLogin}/>
            )}
        </div>
    );
}

export default App;