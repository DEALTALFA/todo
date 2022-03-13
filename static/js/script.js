const SERVER_URI = 'http://localhost:4000';
const fetchOptions = {
  method: 'POST',
  mode: 'cors',
  headers: {
    'Content-Type': 'application/json',
  },
};
let dummyData = [
  {
    id: 1,
    todoText: 'Learning Javascript',
    completed: false,
  },
  {
    id: 2,
    todoText: 'Learning Git',
    completed: true,
  },
  {
    id: 3,
    todoText: 'Learning Bash',
    completed: true,
  },
  {
    id: 4,
    todoText: 'Learning Digital Marketing',
    completed: true,
  },
];

const todoList = document.querySelector('#todolist');
const createInput = document.querySelector('#createInput');
const createBtn = document.querySelector('#createBtn');

let currentInput = '';
createInput.addEventListener('change', () => {
  currentInput = createInput.value;
});

async function createTodo() {
  const value = createInput.value;
  await fetch(`${SERVER_URI}/create`, {
    ...fetchOptions,
    body: JSON.stringify({
      msg:{todoText: value,
        id: Math.floor(Math.random() * 1000),
        completed: false,}
    }),
  });
  fetchFromServer();
}
createBtn.addEventListener('click', createTodo);
async function changeById(id, current) {
  const response = await fetch(SERVER_URI, {
    ...fetchOptions,
    body: JSON.stringify({
      id,
      current,
    }),
  }).then((response) => response.json());
  dummyData = response;
  renderedList();
}

async function fetchFromServer() {
  const data = await fetch(`${SERVER_URI}/getAll`).then((res) => res.json());
  dummyData = data;
  renderedList();
}

async function deleteById(id) {
  const data = await fetch(`${SERVER_URI}/delete`, {
    ...fetchOptions,
    body: JSON.stringify({
      id,
    }),
  }).then((res) => res.json());
  dummyData = data;
  renderedList();
}

function renderedList() {
  todoList.innerHTML = '';
  dummyData.map((e) => {
    const doc = document.createElement('div');
    const p = document.createElement('p');
    const todoText = document.createTextNode(e.todoText);
    p.appendChild(todoText);
    const input = document.createElement('input');
    input.type = 'checkbox';
    input.checked = e.completed;
    input.setAttribute('data-id', e.id);
    input.onchange = () => {
      console.log(`changed ${input.getAttribute('data-id')}`);
    };
    const insideDoc = document.createElement('div');
    insideDoc.classList.add('flex-inside');
    const delBtn = document.createElement('button');
    delBtn.classList.add('del_button');
    delBtn.setAttribute('data-id', e.id);
    delBtn.appendChild(document.createTextNode(`\u2715`));
    delBtn.onclick = () => {
      deleteById(e.id);
    };
    doc.appendChild(p);
    insideDoc.appendChild(input);
    insideDoc.appendChild(delBtn);
    doc.appendChild(insideDoc);
    doc.classList.add('todo');
    todoList.appendChild(doc);
  });
}

renderedList();
