import { fetchData, initializeMenu, getRequestOptions } from '../utils/utils.js';
const token = localStorage.getItem("token");
const id = localStorage.getItem("id");

initializeMenu();
const requestOptions = getRequestOptions();

fetchData(`http://127.0.0.1:5000/user/${id}/clients`, requestOptions)
  .then((data) => {
    const userTable = document.getElementById("user-table");
    
    // Iterar los datos y creamos filas de la tabla
    data.forEach((user, index) => {
      const row = userTable.insertRow();
      const cell1 = row.insertCell(0);
      const cell2 = row.insertCell(1);
      const cell3 = row.insertCell(2);
      const cell4 = row.insertCell(3);
      const cell5 = row.insertCell(4);

      cell1.innerHTML = index + 1;
      cell2.innerHTML = user.name;
      cell3.innerHTML = user.surname;
      cell4.innerHTML = user.address;
      cell5.innerHTML = user.email;
    });
  })
  .catch((error) => console.error("Error al cargar los datos: " + error));