import React from 'react';

function GameList(props){

    const gameClicked = (game) => (evt) => {
        props.gamelicked(game)
    };

    return (
        <div>
            { props.games && props.games.map( game =>{
                return (
                    console.log(game.id),
                    <div key={"MEEP MOOP" + game.id}>
                        <h2 onClick={gameClicked(game)}>{ game.name }</h2>
                    </div>
                )
              })}        
        </div>
    )
};

export default GameList;