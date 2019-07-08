import React from 'react';

function Todo({title, isCompleted}) {
    return (
        <div>
            <h1>{title}</h1>
            <p>{isCompleted.toString()}</p>
        </div>
    )
}

export default Todo;