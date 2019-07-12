import React from 'react';
import '@babel/polyfill';
import PropTypes from 'prop-types';

function Todo({title, isCompleted}) {
    return (
        <div>
            <h1>{title}</h1>
            <p>{isCompleted.toString()}</p>
        </div>
    )
}

Todo.propTypes = {
    title: PropTypes.string.isRequired,
    isCompleted: PropTypes.bool.isRequired
}

export default Todo;