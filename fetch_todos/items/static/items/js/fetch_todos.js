
var button = document.querySelector("button");

button.addEventListener("click", (event) => {
  let form = document.querySelector("form");
  const data = JSON.stringify(
    Object.fromEntries(new FormData(form))
  );

  console.log(data);
  const request = new Request("api/v1/todos/", {
    'method': 'post',
    'body': data,
    'headers': {
      'content-type': 'application/json',
      'accept': 'application/json'
    }
  });
  console.log(request);
  fetch(request).then((response) => {
    return response.json();
  }).then((data) => {
    let p = document.querySelector(".todo_placeholder");
    p.parentElement.removeChild(p);
    let box = document.querySelector(".todos_box");

    for (let i = 0; i < data.length; i++) {
      let p = document.createElement("p");
      p.textContent = data[i].item;
      box.appendChild(p);
    }
  })
})
