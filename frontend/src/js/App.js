import React, {Component} from 'react';
import '../css/App.css';
import Todo from './TodoList.js';

class App extends Component {

    state = {}

    componentDidMount() {
        console.log('DidMount')
        this._getTodoList();
    }

    _getTodoList = async () => {
        // const TodoList = [
        //     {
        //         title : 'coding',
        //         isCompleted : true
        //     },
        //     {
        //         title : 'reading',
        //         isCompleted : false
        //     },
        //     {
        //         title : 'play the guitar',
        //         isCompleted : false
        //     }
        // ]

        console.log('get')

        const TodoList = await this._fetchTodoList();

        this.setState({
            TodoList
        })
    }

    _fetchTodoList = () => {

        console.log('fetch')

        return fetch('http://127.0.0.1:8000/todo/test/')
        .then(res => res.json())
        .catch(err => console.log(err))
    }

    _renderTodoList = () => {
        const TodoList = this.state.TodoList.map( todo => {
            return < Todo 
                title={todo.title}
                isCompleted={todo.isCompleted}
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

// import React, {Component} from 'react';
// import '../css/App.css';
// import Todo from './TodoList.js';

// class App extends Component {

//     state = {}

//     componentDidMount() {
//         setTimeout(() => {
//             this._getTodoList();
//         }, 3000);
//     }

//     _getTodoList = () => {
//         const TodoList = [
//             {
//                 title : 'coding',
//                 isCompleted : true
//             },
//             {
//                 title : 'reading',
//                 isCompleted : false
//             },
//             {
//                 title : 'play the guitar',
//                 isCompleted : false
//             }
//         ]

//         this.setState({
//             TodoList
//         })
//     }

//     _fetchTodoList = () => {
//         return 'It will be used later.'
//     }

//     _renderTodoList = () => {
//         const TodoList = this.state.TodoList.map( todo => {
//             return < Todo 
//                 title={todo.title}
//                 isCompleted={todo.isCompleted}
//             />
//         }) 

//         return TodoList;
//     }

//     render() {
//         const { TodoList } = this.state;

//         return (
//             <div>
//                 { TodoList ? this._renderTodoList() : 'loading' }
//             </div>
//         )
//     }
// }

// export default App;