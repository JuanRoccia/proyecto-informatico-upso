const token = localStorage.getItem("token");
const id = localStorage.getItem("id");

function getRequestOptions() {

  const requestOptions = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      "token": token,
      "user-id": id,
    },
  };

  return requestOptions;
}

function fetchData(url, requestOptions) {
  return fetch(url, requestOptions)
    .then((response) => {
      if (response.status === 401) {
        window.location.href = "../index.html";
        return Promise.reject("Acceso no autorizado");
      }
      return response.json();
    })
    .catch((error) => console.error("Error al cargar los datos: " + error));
}

function initializeMenu() {
  const menuLinks = document.querySelectorAll(".sidebar a");

  menuLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();

      // Desactivar la clase "active" en todos los elementos
      menuLinks.forEach((menuLink) => {
        menuLink.classList.remove("active");
      });

      // Activar la clase "active" en el enlace que se hizo clic
      link.classList.add("active");

      // Obtener el atributo data-view del enlace para determinar la vista a la que redirigir
      const view = link.getAttribute("data-view");

      // Redirigir a la vista correspondiente
      if (view === "dashboard") {
        window.location.href = "dashboard.html";
      } else if (view === "clients") {
        window.location.href = "clientes.html";
      } else if (view === "products") {
        window.location.href = "products.html";
      }
      // Agrega más condiciones para otras vistas
    });
  });
}

//Función para agregar un producto

function agregarProducto() {
  var name = document.getElementById("name").value;
  var price = document.getElementById("price").value;
  var stock = document.getElementById("stock").value;
  var description = document.getElementById("description").value;
  var modal = document.getElementById("exampleModal");

  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      token: token,
      "user-id": id,
    },
    body: JSON.stringify({
      name: name,
      price: price,
      stock: stock,
      description: description,
    }),
  };

  fetch(`http://127.0.0.1:5000/user/${id}/products`, requestOptions)
    .then((response) => response.json())
    .then((data) => {
      console.log("Producto agregado:", data);
      window.location.reload();
    })
    .catch((error) => {
      
      console.error("Error al agregar el producto:", error);
    });

}


export { fetchData, initializeMenu, getRequestOptions, agregarProducto };