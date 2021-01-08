import React, { useEffect, useState } from 'react';

const Numbers = () => {
    const [numbers, setNumbers] = useState(['one', 'two', 'three'])
    const [letters, setLetters] = useState(['a', 'b', 'c'])
    
    const addNumber = () => {
        setNumbers([...numbers, 'four'])
    }

    const addLetter = () => {
        setLetters([...letters, 'd'])
    }
    
    useEffect ( () => {
        console.log('useEffect triggered');
    },[numbers]);

    return (
        <div>
            <h1>Numbers</h1>
            { numbers.map( num => {
                return <h4 key={num}>{num}</h4>})}
             <button onClick={addNumber}>Add a Number</button>

             <h1>Letters</h1>
            { letters.map( letter => {
                return <h4 key={letter}>{letter}</h4>})}
        <button onClick={addLetter}>Add a Letter</button>
        </div>
    )
};

export default Numbers;