import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './components/app/App';
import reportWebVitals from './reportWebVitals';
import 'bootstrap/dist/css/bootstrap.css'

export const API_URL_ROOM = "http://localhost/workplace/api/v1/room/"
export const API_STATIC_MEDIA = "http://0.0.0.0/public"

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
    <React.StrictMode>
        <App/>
    </React.StrictMode>
);

reportWebVitals();
