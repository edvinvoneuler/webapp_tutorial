import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCoffee } from '@fortawesome/free-solid-svg-icons'


function render_rating(rating){
    var i;
    var output = [];
    for(i=0;i<rating;i++){
        output.push(<FontAwesomeIcon icon={faCoffee}/>)
    }
    return output
};

function GameDetails(props){
    if (props.game){
        return (
            <div>
                {/* <FontAwesomeIcon icon={faCoffee}/> */}
                <h2>{props.game.name}</h2>
                <div>{render_rating(props.game.avg_rating).map( star => {return star})}</div>
            </div>
        )
    }
    else {
        return null
    }
};

export default GameDetails;