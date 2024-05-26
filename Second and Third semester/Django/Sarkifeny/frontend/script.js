function postObservation() {
   const city = "Debrecen";
   const street = document.querySelector("#street");
   const observTime = document.querySelector("#observ");
   const auroraType = document.querySelector("#aurora");
   fetch("http://localhost:8000/newObservation", {
      method: "POST",
      headers: {
         "Content-Type": "application/json",
      },
      body: JSON.stringify({
         cityName: city,
         street: street.value,
         observTime: observTime.value,
         auroraType: auroraType.value,
      }),
   });
}

function getAllCities() {
   fetch("http://localhost:8000/getAllCities")
      .then((response) => response.json())
      .then((result) => {
         result.sort((a, b) => a.city.localeCompare(b.city));

         const cityInput = document.querySelector("#city");
         cityInput.innerHTML = "";

         result.forEach((city) => {
            const newElement = document.createElement("option");
            newElement.innerHTML = city.city;
            cityInput.appendChild(newElement);
         });
      });
}

getAllCities();

function deleteObservation() {
   const searchedId = document.querySelector("#obsId");
   fetch(`http://localhost:8000/deleteObservation/${searchedId.value}`, {
      method: "DELETE",
   });
}
