// main.js

// Limpia el localStorage al cargar la página
document.addEventListener("DOMContentLoaded", function () {
  localStorage.removeItem("token");
  localStorage.removeItem("username");
  localStorage.removeItem("id");
});

function iniciarSesion() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

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
        // messageElement.innerHTML = 'Bienvenido ' + resp.username;
        window.location.href = "./templates/dashboard.html";
      } else {
        console.log("Error en el inicio de sesión");
      }
    })
    .catch((error) => {
      console.error("Error en la solicitud:", error);
    });
}

// Función para registrarse
function registerUser() {
  const name = document.getElementById("name").value;
  const username = document.getElementById("username").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const requestOptions = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      name: name,
      username: username,
      password: password,
      email: email,
    }),
  };

  fetch("http://127.0.0.1:5000/user/register", requestOptions)
    .then((res) => res.json())
    .then((resp) => {
      console.log(resp);

      if (resp.username) {
        window.location.href = "../index.html";
      } else {
        console.log("Error en el registro");
      }
    })
    .catch((error) => {
      console.error("Error en la solicitud:", error);
    });
}

document.addEventListener("DOMContentLoaded", function () {
  const formLogin = document.getElementById("form-login");
  if (formLogin) {
    formLogin.addEventListener("submit", function (event) {
      event.preventDefault();
      // Llama a la función de inicio de sesión
      iniciarSesion();
    });
  }

  const formRegister = document.getElementById("form-register");
  if (formRegister) {
    formRegister.addEventListener("submit", function (event) {
      event.preventDefault();
      // Llama a la función de registro
      registerUser();
    });
  }
});
