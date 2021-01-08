import React, {Component} from 'react';

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

        const animals = ['cat', 'dog', 'horse'];

        return (
            <div>
                { animals.map( animal => { return <p>animal</p>}) }
                <input value={this.state.name} onChange={this.changed} type="text"></input>
                <h2 onClick={this.createAlert}>
                    {this.props.signature}
                </h2>

                { this.state.age === 27 ? "yes" : "no" }

            </div>
        )
    }
}

export default Footer