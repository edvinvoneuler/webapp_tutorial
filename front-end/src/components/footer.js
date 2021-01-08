import React, {Component} from 'react';
import {CtxConsumer} from '../index';

class Footer extends Component {

    state = {
        name: 'Edvin',
        age: 27
    };

    componentDidMount(){
        this.setState({name: "Edvin"})
    }

    createAlert(){
        alert('Hello, I am an alert.')
    };

    changed = (evt) => {
        //this.setState({name: evt})
        console.log('changed', evt.target.value)
        this.setState({name: evt.target.value})
    };

    render(){
        return (
            <div>
                <h1>hello I am a footer</h1>
                <CtxConsumer>
                    {value => (value.animals.map( animal => {return <p key={animal}>{animal}</p> }))}
                </CtxConsumer>
            </div>
        )
    }
}

export default Footer