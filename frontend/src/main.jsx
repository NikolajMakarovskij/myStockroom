import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './components/App';

export const API_STATIC_MEDIA = "http://localhost/static/"

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
            <App/>
    </React.StrictMode>
);


