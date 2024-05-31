document.querySelector("#show_data").addEventListener("click", () => {
   if (document.querySelector("#show_data").innerHTML === "Mutasd") {
      document.querySelector(".table").removeAttribute("hidden");
      document.querySelector("#delete_btn").removeAttribute("hidden");
      document.querySelector("#show_data").innerHTML = "Rejtsd el";
      fetchAllData();
   } else {
      document.querySelector(".table").setAttribute("hidden", true);
      document.querySelector("#delete_btn").setAttribute("hidden", true);
      document.querySelector("#show_data").innerHTML = "Mutasd";
   }
});

function fetchAllData() {
   fetch("http://localhost:8000/getAllAttractions")
      .then((response) => response.json())
      .then((result) => {
         let attractions = result.map((attraction) => ({
            id: attraction.id,
            name: attraction.name,
            country: attraction.city.country.name,
            city: attraction.city.name,
            short_description: attraction.short_description,
            average_rate: attraction.average_rate,
            opening_hours: attraction.opening_hours,
         }));

         const tBody = document.querySelector("tbody");
         tBody.innerHTML = "";

         for (let i = 0; i < attractions.length; i++) {
            const row = tBody.insertRow();
            const cellName = row.insertCell(0);
            const cellCountry = row.insertCell(1);
            const cellCity = row.insertCell(2);
            const cellDesc = row.insertCell(3);
            const cellRate = row.insertCell(4);
            const cellOpen = row.insertCell(5);
            const radioInput = row.insertCell(6);
            cellName.textContent = attractions[i].name;
            cellCountry.textContent = attractions[i].country;
            cellCity.textContent = attractions[i].city;
            cellDesc.textContent = attractions[i].short_description;
            cellRate.textContent = attractions[i].average_rate;
            cellOpen.textContent = attractions[i].opening_hours;
            radioInput.innerHTML = `<input name='delete' type='radio' value=${attractions[i].id}>`;
         }
      });
}

document.querySelector("#delete_btn").addEventListener("click", () => {
   const selectedItem = document.querySelector("input[name='delete']:checked").value;

   fetch(`http://localhost:8000/deleteAttraction/${selectedItem}`, {
      method: "DELETE",
   }).then(() => {
      fetchAllData();
   });
});
