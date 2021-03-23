import React from 'react';

function TestList(props){
    const test_vals = [
        {id: 1, value: "banana"},
        {id:2, value: "potato"},
        {id: 3, value: "orange"}
    ]
    return (
        <div>
            {
                test_vals.map( item => {
                    return (
                        <div key={item.id}>
                            <p>{item.value}</p>
                        </div>
                    )
                })
            }
        </div>
    )
}

export default TestList;