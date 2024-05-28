document.querySelector("#get_data").addEventListener("click", () => {
   if (document.querySelector("#get_data").innerHTML === "Mutasd") {
      fetch("http://localhost:8000/getAllAttractions")
         .then((response) => response.json())
         .then((result) => {
            document.querySelector(".table").removeAttribute("hidden");
            document.querySelector("#get_data").innerHTML = "Rejtsd el";
            const tBody = document.querySelector("tbody");

            let attractions = result.map((attraction) => ({
               id: attraction.id,
               name: attraction.name,
               country: attraction.city.country.name,
               city: attraction.city.name,
               short_description: attraction.short_description,
               average_rate: attraction.average_rate,
               opening_hours: attraction.opening_hours,
            }));

            for (let i = 0; i < attractions.length; i++) {
               const row = tBody.insertRow();
               const cellId = row.insertCell(0);
               const cellName = row.insertCell(1);
               const cellCountry = row.insertCell(2);
               const cellCity = row.insertCell(3);
               const cellDesc = row.insertCell(4);
               const cellRate = row.insertCell(5);
               const cellOpen = row.insertCell(6);
               cellId.textContent = attractions[i].id;
               cellName.textContent = attractions[i].name;
               cellCountry.textContent = attractions[i].country;
               cellCity.textContent = attractions[i].city;
               cellDesc.textContent = attractions[i].short_description;
               cellRate.textContent = attractions[i].average_rate;
               cellOpen.textContent = attractions[i].opening_hours;
            }
         });
   } else {
      document.querySelector(".table").setAttribute("hidden", true);
      document.querySelector("#get_data").innerHTML = "Mutasd";
   }
});
