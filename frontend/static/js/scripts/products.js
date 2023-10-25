import {
  fetchData,
  initializeMenu,
  getRequestOptions,
  agregarProducto
} from "../utils/utils.js";
const token = localStorage.getItem("token");
const id = localStorage.getItem("id");
document.getElementById("btn-agregar-producto").addEventListener("click", agregarProducto);

initializeMenu();
const requestOptions = getRequestOptions();

// Hacer una solicitud GET a la API
fetchData(`http://127.0.0.1:5000/user/${id}/products`, requestOptions)
  .then((data) => {
    const userTable = document.getElementById("product-table");

    // Iterar los datos y creamos filas de la tabla
    data.forEach((product, index) => {
      const row = userTable.insertRow();
      const cell1 = row.insertCell(0);
      const cell2 = row.insertCell(1);
      const cell3 = row.insertCell(2);
      const cell4 = row.insertCell(3);
      const cell5 = row.insertCell(4);

      cell1.innerHTML = index + 1;
      cell2.innerHTML = product.name;
      cell3.innerHTML = product.price;
      cell4.innerHTML = product.stock;
      cell5.innerHTML =
        '<div class="btns"><a href="#"><span class="material-symbols-sharp btn-edit" >edit</span></a> <a href="#"><span class="material-symbols-sharp btn-delete" >delete</span></a></div>';
    });
  })
  .catch((error) => console.error("Error al cargar los datos: " + error));


