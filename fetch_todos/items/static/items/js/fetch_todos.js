
var button = document.querySelector("#submit");

button.addEventListener("click", (event) => {
  console.log("Hi");
  let form = document.querySelector("form")
  const data = new FormData(form);
  console.log(data);
})
