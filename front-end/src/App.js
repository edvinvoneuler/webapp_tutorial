import React, { useState } from 'react';
import './App.css';

function App() {

  const [games, setGames] = useState([]);

  return (
    <div className="App">
      <header className="App-header">
          <h1>Hello this is an app</h1>
      </header>
      <div className="layout">
            <div>
              { games.map( game =>{
                return <h2>{ game }</h2>
              })}
            </div>
            <div>Two</div>
      </div>
    </div>
  );
}

export default App;
