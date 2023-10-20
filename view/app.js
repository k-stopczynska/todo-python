const todoList = document.querySelector('.list__wrapper');
const BASE_URL = 'http://127.0.0.1:5000/'

const getAllTodos = async () => {
    try {
        const response = await fetch(BASE_URL)
        console.log(response);
    if (!response.ok) {
        throw new Error('Could not fetch todos!');
    }
        const todos = await response.json();
        console.log(todos);
    } catch (err) {
        console.log(err);
    }
    
}

getAllTodos()