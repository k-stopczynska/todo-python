const todoLists = document.querySelectorAll('.list__wrapper');
const submitButton = document.querySelector('.submit__button');
const form = document.querySelector('.form__control');
const formError = document.querySelector('.form__error');
const BASE_URL = 'http://127.0.0.1:5000/';

//TODO: refactor this fn for get requests
const getResponse = async (params) => {
    const { endpointUrl, method, body, errorMessage } = params
    try {
              const response = await fetch(BASE_URL + endpointUrl,
            {
                method: method,
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    "Access-Control-Origin": "*",
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

const getTodoByStatus = async (status) => {
     try {
         const response = await fetch(BASE_URL + `status/${status}`, {
             headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Access-Control-Origin': '*',
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
        const response = await fetch(BASE_URL + `id/${todoId['todo_id']}`, {
            headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Access-Control-Origin': '*',
                },})
    if (!response.ok) {
        throw new Error('Could not fetch this one!');
    }
        const todo = await response.json();
        return todo
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

const updateExistingTodo = (todoToUpdate) => {
    const params = {
        endpointUrl: 'update_todo',
        method: 'PUT',
        body: todoToUpdate,
        errorMessage: 'Could not update this todo!'
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


const renderTodosByStatus = async () => {
    const todoListTodo = document.querySelector('.list__wrapper-todo');
    const todoListPending = document.querySelector('.list__wrapper-pending');
    const todoListDone = document.querySelector('.list__wrapper-done');
    const todoTodos = await getTodoByStatus('todo');
    const pendingTodos = await getTodoByStatus('pending');
    const doneTodos = await getTodoByStatus('done');
    if (todoTodos) {
       createTodoElem(todoTodos, todoListTodo)
    }
    if (pendingTodos) {
       createTodoElem(pendingTodos, todoListPending)
    }
    if (doneTodos) {
       createTodoElem(doneTodos, todoListDone)
    }
}

const createTodoElem = (todos, list) => {
     for (const todo of todos) {
            const todoElem = document.createElement('li')
            todoElem.classList.add('list__elem')
            const date = new Date(todo.deadline)
            todoElem.insertAdjacentHTML(
                'afterbegin',
                `<h3 class="list__elem-title">${todo['title']}</h3>
                <p class="list__elem-desc">${todo.description}</p>
                <div class="list__elem-just-between">
                    <h4 class="list__elem-status">${todo.status}</h4>
                    <p class="list__elem-date">${date.toJSON().split('T')[0]}</p>
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
        list.append(todoElem)
    }
}

if (window.location.href === "http://localhost:5500/view/index.html") renderTodosByStatus();

const submitForm = (e) => {
    e.preventDefault();
    const title = form[0].value.trim();
    const description = form[1].value.trim();
    const status = form[2].value.trim();
    const deadline = form[3].value.trim();
    if (title !== '' && description !== '' && status !== '' && deadline !== '') {
        formError.classList.remove('active')
        const newTodo = { title, description, status, deadline }
        const todo_id = JSON.parse(localStorage.getItem('id'))['todo_id']
        const todoToUpdate = {todo_id, title, description, status, deadline }
        if (window.location.href === "http://localhost:5500/view/add_todo.html") {
            postNewTodo(newTodo);
        } else {
            updateExistingTodo(todoToUpdate)
        }
        form[0].value = '';
        form[1].value = '';
        form[2].value = '';
        form[3].value = '';
        window.location.href = "http://localhost:5500/view/index.html"
    } else {
        formError.classList.add('active')
    }
}

const handleDeleteTodo = (e) => {
    if (e.target.getAttribute('data-id').includes('delete')) {
        const todoId = { todo_id: +(e.target.getAttribute('data-id').slice(7)) }
        deleteTodo(todoId);
        for (list of todoLists) {
            while (list.lastElementChild) {
        list.removeChild(list.lastElementChild);
        }
        }
       
       renderTodosByStatus();
    } else {
        return
    }
}

const prepopulateForm = async (id) => {
    const todoToUpdate = await getTodoById(id);
    const { title, description, status, deadline } = todoToUpdate[0];
    date = new Date(deadline)
    form[0].value = title;
    form[1].value = description;
    form[2].value = status;
    form[3].value = date.toJSON().split('T')[0];
}

const handleUpdateTodo = (e) => {
    if (e.target.getAttribute('data-id').includes('update')) {
        const todoId = { todo_id: +(e.target.getAttribute('data-id').slice(7)) };
        localStorage.setItem('id', JSON.stringify(todoId));
        window.location.href = "http://localhost:5500/view/update_todo.html"; 
    } else {
        return
    } 
}

if (window.location.href === "http://localhost:5500/view/update_todo.html") {
    const todoToUpdateId = JSON.parse(localStorage.getItem('id'));
    prepopulateForm(todoToUpdateId)
}

if (submitButton) submitButton.addEventListener('click', submitForm);
if (todoLists) todoLists.forEach((list) => list.addEventListener('click', handleDeleteTodo));
if (todoLists) todoLists.forEach((list) => list.addEventListener('click', handleUpdateTodo));






