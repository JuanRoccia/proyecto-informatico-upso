// register.js

export function registerUser() {
    const name = document.getElementById("name").value;
    const username = document.getElementById("reg-username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("reg-password").value;
  
    const messageElement = document.getElementById("reg-message");
    messageElement.innerHTML = "";
  
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
          messageElement.innerHTML = "Registro fallido";
        }
      })
      .catch((error) => {
        console.error("Error en la solicitud:", error);
      });
  }
  