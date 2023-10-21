const todoList = document.querySelector('.list__wrapper');
const submitButton = document.querySelector('.submit__button');
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

submitButton.addEventListener('click', addNewTodo);






