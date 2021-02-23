
import {createSvgDeleteButton} from './utils.js';

function delete_todo(event) {
  const id = event.currentTarget.id.split("_")[1];
  const request = new Request(`api/v1/todos/${id}/`, {
    'method': 'delete',
    'headers': {
      'content-type': 'application/json',
      'accept': 'application/json'
    }
  });
  fetch(request).then((response) => {
    if (response.ok) {
      let todo = document.querySelector(`#todo_${id}`);
      todo.parentElement.removeChild(todo);
    }
  })
}

var button = document.querySelector("button");
var input = document.querySelector("input[type='text']");

function add_todo_element(event) {
  event.preventDefault()
  let form = document.querySelector("form");
  const data = JSON.stringify(
    Object.fromEntries(new FormData(form))
  );

  const request = new Request("api/v1/todos/", {
    'method': 'post',
    'body': data,
    'headers': {
      'content-type': 'application/json',
      'accept': 'application/json'
    }
  });

  let error = document.querySelector(".submission_error");
  if (error) {
    error.classList.replace("submission_error", "hide");
  }

  fetch(request).then((response) => {

      if (response.status === 204) {
        throw new Error("Cannot create duplicate todo");
      } else if (response.status === 400) {
        throw new Error("Invalid todo!")
      }
      return response.json();
  }).then((data) => {
    if (data.length === 1) {
      const placeholder = document.querySelector("todo_placeholder");
      placeholder.parentElement.removeChild(placeholder);
    }
    let todos_container = document.querySelector(".todos_list");
    let todo_div = document.createElement("div");
    todo_div.setAttribute("class", `todo`)
    todo_div.setAttribute("id", `todo_${data.id}`)
    let p = document.createElement("p");
    p.textContent = data.item;
    let delete_button = createSvgDeleteButton();
    [delete_button, p].forEach((element) => {
      if (element.nodeName === 'svg') {
        element.id=`delete_${data.id}`
        element.addEventListener("click", delete_todo)
        element.classList.add('todo_component', 'delete');
      } else{
        element.classList.add('todo_component', 'todo_text');
      }
      todo_div.appendChild(element);
    });
    todos_container.appendChild(todo_div);
  }).catch((e) => {
    let message = document.querySelector(".message");
    message.textContent = `${e.message}`;
    message.classList.remove("hide");
    message.classList.add("submission_error");
  });
}

button.addEventListener("click", add_todo_element);
input.addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    add_todo_element(event);
  }
})
