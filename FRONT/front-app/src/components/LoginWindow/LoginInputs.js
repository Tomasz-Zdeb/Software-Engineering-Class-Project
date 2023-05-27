import React, {useState} from 'react';

const LoginInputs = ({handleLogin, handleRegister, buttonText}) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = e => {
        e.preventDefault();
        handleLogin(email, password);
    };

    return (
        <form>
            <div>
                <label>Email:</label>
                <input
                    className="form-control"
                    type="email"
                    name="email"
                    value={email}
                    onChange={e => setEmail(e.target.value)}
                    required
                />
            </div>
            <div>
                <label>Hasło:</label>
                <input
                    className="form-control"
                    type="password"
                    name="password"
                    value={password}
                    onChange={e => setPassword(e.target.value)}
                    required
                />
            </div>
            <button className="btn btn-primary mb-3 mt-2" onClick={() => handleLogin(email, password)}>
                {buttonText}
            </button>
            <button className="btn btn-primary mb-3 mt-2" onClick={() => handleRegister(email, email, password)}>
                Zarejestruj
            </button>
        </form>
    );
};

export default LoginInputs;
