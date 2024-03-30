import {useState} from "react";
import styles from "./ColorPicker.module.css";

export default function ColorPicker() {
   const [color, setColor] = useState("#FFFFFF");

   function handleColorChange(e) {
      setColor(e.target.value);
   }

   return (
      <div className={styles.color_picker_container}>
         <h1>Color Picker</h1>
         <div className={styles.color_display} style={{backgroundColor: color}}>
            <p>Selected Color: {color}</p>
         </div>
         <label>Select a color:</label>
         <input type="color" value={color} onChange={handleColorChange} />
      </div>
   );
}
