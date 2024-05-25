function getData() {
   fetch("http://127.0.0.1:8000/")
      .then((response) => response.json())
      .then((result) => {
         result.forEach((element) => {
            document.querySelector("#result").innerHTML += `
               <tr>
                  <td>${element.varos}</td>
                  <td>${element.utca}</td>
                  <td>${element.ertek}</td>
                  <td>${element.idopont}</td>
               </tr>
            `;
         });
      });
}

getData();
