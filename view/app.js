const todoList = document.querySelector('.list__wrapper');
const submitButton = document.querySelector('.submit__button');
const BASE_URL = 'http://127.0.0.1:5000/'


const getResponse = async (params) => {
    const { endpointUrl, method, body, errorMessage } = params
    try {
              const response = await fetch(BASE_URL + endpointUrl,
            {
                method: method,
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    "Access-Control-Origin": "*"
                },
                body: JSON.stringify(body),
            })    
        if (!response.ok) {
            throw new Error(errorMessage);
        }
        const data = await response.json();
        return data;
    } catch (err) {
        console.log(err);
    }
}

const getAllTodos = async () => {
    try {
        const response = await fetch(BASE_URL, {       headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    "Access-Control-Origin": "*"
                },})
    if (!response.ok) {
        throw new Error('Could not fetch todos!');
    }
        const todos = await response.json();
        return todos;
    } catch (err) {
        console.log(err);
    }
}

const getTodoById = async (todoId) => {
           try {
        const response = await fetch(BASE_URL + `id/${todoId['todo_id']}`, {       headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    "Access-Control-Origin": "*"
                },})
    if (!response.ok) {
        throw new Error('Could not fetch this one!');
    }
        const todo = await response.json();
        console.log(todo)
    } catch (err) {
        console.log(err);
    }
}

const postNewTodo = (newTodo) => {
    const params = {
        endpointUrl: 'add_todo',
        method: 'POST',
        body: newTodo,
        errorMessage: 'Could not add new todo!'
    }
    getResponse(params)
}

const deleteTodo = (todoId) => {
    const params = {
        endpointUrl: '/',
        method: 'DELETE',
        body: todoId,
        errorMessage: 'Could not delete todo!'
    }
    getResponse(params)
}


const createTodoElem = async () => {
    const todos = await getAllTodos();
    if (todos) {
        for (const todo of todos) {
            const todoElem = document.createElement('li')
            todoElem.classList.add('list__elem')
            todoElem.insertAdjacentHTML(
                'afterbegin',
                `<h3 class="list__elem-title">${todo['title']}</h3>
                <p class="list__elem-desc">${todo.description}</p>
                <div class="list__elem-just-between">
                    <h4 class="list__elem-status">${todo.status}</h4>
                    <p class="list__elem-date">${todo.deadline}</p>
                </div>
                <div class="list__elem-just-between">
                    <a href='#' data-id="update-${todo.todo_id}">
                        <img class="list__elem-img" src='../assets/update.png' alt='update' data-id="update-${todo.todo_id}"/>
                    </a>
                    <button data-id="delete-${todo.todo_id}" >
                        <img class="list__elem-img" src='../assets/delete.png' alt='delete' data-id="delete-${todo.todo_id}"/>
                    </button>
                </div>
            `)
        todoList.append(todoElem)
    }
    }
}

createTodoElem();

const addNewTodo = (e) => {
    e.preventDefault();
    const form = document.querySelector('.form__control');
    const formError = document.querySelector('.form__error')
    const title = form[0].value.trim();
    const description = form[1].value.trim();
    const status = form[2].value.trim();
    const deadline = form[3].value.trim();
    if (title !== '' && description !== '' && status !== '' && deadline !== '') {
        formError.classList.remove('active')
        const newTodo = { title, description, status, deadline }
        postNewTodo(newTodo);
        form[0].value = '';
        form[1].value = '';
        form[2].value = '';
        form[3].value = '';
    } else {
        formError.classList.add('active')
    }
}

const handleDeleteTodo = (e) => {
    if (e.target.getAttribute('data-id').includes('delete')) {
        const todoId = { todo_id: +(e.target.getAttribute('data-id').slice(7)) }
        deleteTodo(todoId);
        while (todoList.lastElementChild) {
        todoList.removeChild(todoList.lastElementChild);
        }
        createTodoElem();
    } else {
        return
    }
}

const handleUpdateTodo = (e) => {
    if (e.target.getAttribute('data-id').includes('update')) {
        const todoId = { todo_id: +(e.target.getAttribute('data-id').slice(7)) }
        console.log(todoId)
        getTodoById(todoId);
    } else {
        return
    }
}

if (submitButton) submitButton.addEventListener('click', addNewTodo);
todoList.addEventListener('click', handleDeleteTodo);
todoList.addEventListener('click', handleUpdateTodo)






