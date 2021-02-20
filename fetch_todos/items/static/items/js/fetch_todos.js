function createSvgDeleteButton() {
  let svg = document.createElementNS("http://www.w3.org/2000/svg", 'svg');
  svg.setAttribute("width", "45px");
  svg.setAttribute("height", "45px");
  svg.setAttribute("class", "delete_button");
  let line1 = document.createElementNS("http://www.w3.org/2000/svg", 'line');
  line1.setAttribute('x1', "10");
  line1.setAttribute('y1', "10");
  line1.setAttribute('x2', "40");
  line1.setAttribute('y2', "40");
  line1.setAttribute("stroke", "red");
  line1.setAttribute("stroke-width", '10')
  let line2 = document.createElementNS("http://www.w3.org/2000/svg", 'line');
  line2.setAttribute('x1', "40");
  line2.setAttribute('y1', "10");
  line2.setAttribute('x2', "10");
  line2.setAttribute('y2', "40");
  line2.setAttribute("stroke", "red");
  line2.setAttribute("stroke-width", '10')
  svg.appendChild(line1);
  svg.appendChild(line2);
  return svg;
}


var button = document.querySelector("button");
var input = document.querySelector("input[type='text']")
function add_todo_element(event) {
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

  let previous_error = document.querySelector(".message");
  if (previous_error) {
    previous_error.textContent = "";
    previous_error.classList.remove("submission_error")
  }

  fetch(request).then((response) => {

      if (response.status === 204) {
        throw new Error("Cannot create duplicate todo");
      }
      return response.json();
  }).then((data) => {
    if (data.length === 1) {
      const placeholder = document.querySelector("todo_placeholder");
      placeholder.parentElement.removeChild(placeholder);
    }
    let todos_container = document.querySelector(".todos_list");
    let todo_div = document.createElement("div");
    todo_div.setAttribute("class", "todo")
    let p = document.createElement("p");
    p.textContent = data.item;
    let delete_button = createSvgDeleteButton();
    [delete_button, p].forEach((element) => {
      if (element.nodeName === 'svg') {
        element.id=`todo_${data.id}`
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
    message.classList.add("submission_error");
  });
}

button.addEventListener("click", add_todo_element);
input.addEventListener("keypress", function(event) {
  if (event.key === "Enter")
    console.log("Hey");
})
