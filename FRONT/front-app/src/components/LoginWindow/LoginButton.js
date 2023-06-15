import React from 'react';

const LoginButton = ({ handleLogin, buttonText }) => {
    return (
        <button onClick={() => handleLogin('', '')}>
            {buttonText}
        </button>
    );
};

export default LoginButton;
