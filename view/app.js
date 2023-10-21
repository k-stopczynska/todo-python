const todoList = document.querySelector('.list__wrapper');
const BASE_URL = 'http://127.0.0.1:5000/'

const getAllTodos = async () => {
    try {
        const response = await fetch(BASE_URL)
    if (!response.ok) {
        throw new Error('Could not fetch todos!');
    }
        const todos = await response.json();
        return todos;
    } catch (err) {
        console.log(err);
    }
}

const newTodo = {title: 'add new todo', description: 'test you api endpoint adding new todo', status: 'pending', deadline: '2023-10-22'}

const postNewTodo = async (newTodo) => {
    const todo = JSON.stringify(newTodo);
    try {
        const response = await fetch(BASE_URL + 'add_todo',
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    "Access-Control-Origin": "*"
                },
                body: todo
            })
        if (!response.ok) {
            throw new Error('Could not add new todo!');
        }
        const addedTodo = await response.json();
        return addedTodo;
    } catch (err) {
        console.log(err);
    }
}

postNewTodo(newTodo);


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
                    <a href='/update__todo'>
                        <img class="list__elem-img" src='../assets/update.png' alt='update'/>
                    </a>
                    <button>
                        <img class="list__elem-img" src='../assets/delete.png' alt='delete'/>
                    </button>
                </div>
            `)
        todoList.append(todoElem)
    }
    }
}

createTodoElem();






