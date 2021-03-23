import React from 'react';

function GameList(props){

    const gameClicked = (game) => (evt) => {
        console.log("CLICK")
        props.gameClicked(game)
    };

    return (
        <div>
            { props.games && props.games.map( game =>{
                return (
                    <div key={"key: " + game.id}>
                        <h2 onClick={gameClicked(game)}>{ game.name }</h2>
                    </div>
                )
              })}        
        </div>
    )
};

export default GameList;