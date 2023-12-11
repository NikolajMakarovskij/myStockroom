import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './components/App';
import reportWebVitals from './reportWebVitals';
import 'bootstrap/dist/css/bootstrap.min.css'

export const API_URL = "http://172.18.0.4:8010/workplace/api/v1/room/"
export const API_STATIC_MEDIA = "http://172.18.0.9/static/"

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <App/>
    </React.StrictMode>
);

reportWebVitals();
