import {useState} from "react";
import styles from "./Counter.module.css";
export default function Counter() {
   const [count, setCount] = useState(0);
   const increment = () => {
      setCount((c) => c + 1);
   };
   const decrement = () => {
      setCount((c) => c - 1);
   };
   const reset = () => {
      setCount(0);
   };
   return (
      <div className={styles.counter_container}>
         <p className={styles.count_display}>{count}</p>
         <button className={styles.counter_button} onClick={decrement}>
            Decrement
         </button>
         <button className={styles.counter_button} onClick={increment}>
            Increment
         </button>
         <button className={styles.counter_button} onClick={reset}>
            Reset
         </button>
      </div>
   );
}
