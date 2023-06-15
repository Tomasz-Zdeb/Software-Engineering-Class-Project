import React, {useState} from 'react';
import LoginInputs from './LoginInputs';

const LoginWindowComponent = ({handleLogin}) => {
    const [errorMessage, setErrorMessage] = useState('');

    const handleRequest = (url, method, data) => {
        return fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
            .then(response => {
                if (response.status === 200) {
                    setErrorMessage('');
                    return response.json();
                } else if (response.status === 403) {
                    setErrorMessage('Błędne dane logowania');
                    alert('Błędne dane logowania');
                } else {
                    setErrorMessage('Wystąpił nieznany błąd');
                    alert('Wystąpił nieznany błąd');
                }
            })
            .catch(error => {
                console.error('Błąd logowania/rejestracji:', error);
            });
    };

    const handleLoginRequest = (email, password) => {
        const data = {email, password};
        handleRequest('http://localhost:5000/login', 'POST', data)
            .then(data => {
                handleLogin(data['access_token']);
            });
    };

    const handleRegisterRequest = (name, email, password) => {
        const data = {name, email, password};
        handleRequest('http://localhost:5000/register', 'POST', data)
            .then(data => {
                handleLogin(data['access_token']);
            });
    };

    return (
        <div className="login-window rounded-4  d-flex align-items-center justify-content-center">
            <div><h2>Logowanie do aplikacji</h2></div>
            {errorMessage && <p className="error-message">{errorMessage}</p>}
            <LoginInputs handleLogin={handleLoginRequest} handleRegister={handleRegisterRequest}
                         buttonText={"Zaloguj"}/>
        </div>
    );
};

export default LoginWindowComponent;
