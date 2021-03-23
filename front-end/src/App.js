import React, { useState, useEffect } from 'react';
import GameList from './components/GameList'
import './App.css';
import GameDetails from './components/GameDetails';

function App() {

  const [games, setGames] = useState([]);
  const [selectedGame, setSelectedGame] = useState(null)

  useEffect(()=>{
    fetch("http://127.0.0.1:8000/api/games/", { method: 'GET',headers: { 
        'Content-Type': 'application/json', 
        'authorization': 'Token bcc7b517ed315284f990b3044c75fded6bc5ed76',
      }
    }).then( resp => resp.json())
    .then( resp => setGames(resp))
    .catch( error => console.log(error))
  }, [])

  const gameClicked = (game) => {
    setSelectedGame(game)
  };

  return (
    <div className="App">
      <header className="App-header">
          <h1>Hello this is an app</h1>
      </header>
      <div className="layout">
            <GameList games={games} gameClicked={gameClicked}/>
            <GameDetails game={selectedGame}/>
      </div>
    </div>
  );
}

export default App;
