function addNewAttraction() {
   const city = document.querySelector("#city");
   const attraction_name = document.querySelector("#attraction_name");
   const short_desc = document.querySelector("#short_desc");
   const avg_rate = document.querySelector("#avg_rate");
   const opening_hours = document.querySelector("#opening_hours");
   fetch("http://localhost:8000/newAttraction", {
      method: "POST",
      headers: {
         "Content-Type": "application/json",
      },
      body: JSON.stringify({
         city: city.value,
         attraction_name: attraction_name.value,
         short_desc: short_desc.value,
         avg_rate: Number(avg_rate.value),
         opening_hours: opening_hours.value,
      }),
   });
}

function getAllAttractions() {
   fetch("http://localhost:8000/getAllAttractions")
      .then((response) => response.json())
      .then((result) => {
         const cityInput = document.querySelector("#city");
         let allCitiNames = [];
         let allCityObj = [];
         result.forEach((attraction) => {
            allCityObj.push(attraction.city);
            allCitiNames.push(attraction.city.name);
         });
         allCitiNames.sort();
         for (const city of allCitiNames) {
            const newElement = document.createElement("option");
            newElement.innerHTML = city;
            newElement.setAttribute("value", city);
            cityInput.appendChild(newElement);
         }
         document.querySelector("select").addEventListener("change", () => {
            const countryInput = document.querySelector("#country");
            countryInput.value = "";
            const selectedOption = document.querySelector("select").value;
            if (selectedOption !== "default") {
               const selectedCity = allCityObj.find((city) => city.name === selectedOption);
               countryInput.value = selectedCity.country.name;
               document.querySelector("button").removeAttribute("disabled");
            } else {
               document.querySelector("button").setAttribute("disabled", true);
            }
         });
      });
}

getAllAttractions();

function compare(a, b) {
   if (a.last_nom < b.last_nom) {
      return -1;
   }
   if (a.last_nom > b.last_nom) {
      return 1;
   }
   return 0;
}
