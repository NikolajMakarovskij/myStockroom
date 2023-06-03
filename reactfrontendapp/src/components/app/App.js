import './App.css';
import axios from 'axios';
import React, {Component, } from "react";
import Header from "../appHeader/Header";
import Home from "../appHome/Home";

if (window.location.origin === "http://localhost:3000") {
  axios.defaults.baseURL = "http://127.0.0.1:8010";
} else {
  axios.defaults.baseURL = window.location.origin;
}

class App extends Component {
    state = {
      news: '12345'
    }
  

  }
  


export default App;

