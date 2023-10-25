// login.js

function iniciarSesion() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const messageElement = document.getElementById("message");
  messageElement.innerHTML = "";

  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: "Basic " + btoa(username + ":" + password),
    },
  };

  fetch("http://127.0.0.1:5000/user/login", requestOptions)
    .then((res) => res.json())
    .then((resp) => {
      console.log(resp);

      if (resp.token) {
        localStorage.setItem("token", resp.token);
        localStorage.setItem("username", resp.username);
        localStorage.setItem("id", resp.id);
        const token = localStorage.getItem("token");
        const id = localStorage.getItem("id");
        // messageElement.innerHTML = 'Bienvenido ' + resp.username;
        window.location.href = "./templates/dashboard.html";
      } else {
        messageElement.innerHTML = "Inicio de sesión fallido";
      }
    })
    .catch((error) => {
      console.error("Error en la solicitud:", error);
    });
}
console.log(token, id);
export { iniciarSesion, token, id };
