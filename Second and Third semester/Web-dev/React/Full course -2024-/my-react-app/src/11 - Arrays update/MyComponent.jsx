import {useState} from "react";
import "./MyComponent.css";
export default function MyComponent() {
   const [foods, setFoods] = useState(["pizza", "burger", "fries"]);

   function handleAddFood() {
      const newFood = document.querySelector("#foodInput").value;
      document.querySelector("#foodInput").value = "";

      setFoods((f) => [...f, newFood]);
   }
   function handleRemoveFood(index) {
      setFoods(foods.filter((_, i) => i !== index));
   }

   return (
      <div>
         <h2>List of Food</h2>
         <ul>
            {foods.map((food, index) => (
               <li key={index} onClick={() => handleRemoveFood(index)}>
                  {food}
               </li>
            ))}
         </ul>
         <input type="text" id="foodInput" placeholder="Enter food name" />
         <button onClick={handleAddFood}>Add Food</button>
      </div>
   );
}
