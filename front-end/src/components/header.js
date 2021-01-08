import React from 'react';

function Header(props){
    return (
            <React.Fragment>
                <h1>Welcome to this fantastic website</h1>
                <h2 onClick={props.myAlert}>{props.info}</h2>
            </React.Fragment>
        )
};

export { Header };