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


const createTodoElem = async () => {
    const todos = await getAllTodos();
    if (todos) {
        for (const todo of todos) {
            const todoElem = document.createElement('li')
            todoElem.insertAdjacentHTML('afterbegin', `<h3>${todo['title']}</h3>
            <p>${todo.description}</p>
            <h4>${todo.status}</h4><span>${todo.deadline}</span>`)
        todoList.append(todoElem)
    }
    }
}

createTodoElem()




