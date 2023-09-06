import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import ListaPersonas from './Componentes/ListaPersonas';
import "bootstrap/dist/css/bootstrap.min.css";
import Navbar from './Componentes/Navbar';



const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>

    <div>
      <Navbar />
      <div className='container my-4'>
        <ListaPersonas />
      </div>
    </div>
  </React.StrictMode>,

);


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals

reportWebVitals()
