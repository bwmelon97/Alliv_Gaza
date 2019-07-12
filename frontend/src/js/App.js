import React, {Component} from 'react';
import '../css/App.css';
import Todo from './TodoList.js';
import '@babel/polyfill';

class App extends Component {

    state = {}

    componentDidMount() {
        this._getTodoList();
    }

    _getTodoList = async () => {
        const TodoList = await this._fetchTodoList();
        this.setState({
            TodoList
        })
    }

    _fetchTodoList = () => {
        return fetch('http://127.0.0.1:8000/todo/test/')
        .then(res => res.json())
        .catch(err => console.log(err))
    }

    _renderTodoList = () => {
        const TodoList = this.state.TodoList.map( todo => {
            return < Todo 
                title={todo.todo_content}
                isCompleted={todo.is_completed}
            />
        }) 

        return TodoList;
    }

    render() {
        const { TodoList } = this.state;
        return (
            <div>
                { TodoList ? this._renderTodoList() : 'loading' }
            </div>
        )
    }
}

export default App;