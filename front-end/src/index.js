import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {Header} from './components/header';
import Footer from './components/footer';
import { Route, BrowserRouter } from 'react-router-dom';

const context = React.createContext()
export const CtxConsumer = context.Consumer;

const animals = ['fish', 'snake', 'cow'];

const routing = (
  <BrowserRouter>
    <context.Provider value={{animals: animals}}>
      <div>
        <Route exact path="/" component={App}></Route>
        <Route path="/header" component={Header}></Route>
        <Route path="/footer" component={Footer}></Route>
      </div>
    </context.Provider>
  </BrowserRouter>
)

ReactDOM.render(routing, document.getElementById('root'));

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
