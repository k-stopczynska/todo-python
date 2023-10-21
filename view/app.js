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

createTodoElem()




