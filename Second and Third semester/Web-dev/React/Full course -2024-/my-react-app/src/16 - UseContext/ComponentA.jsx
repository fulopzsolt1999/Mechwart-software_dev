import {useState, createContext} from "react";
import "./Component.css";
import ComponentB from "./ComponentB.jsx";

export const UserContext = createContext();

export default function ComponentA() {
   const [user, setUser] = useState("KrémesPuffancs");

   return (
      <div className="box">
         <h1>ComponentA</h1>
         <h2>{`Hello ${user}`}</h2>
         <UserContext.Provider value={user}>
            <ComponentB />
         </UserContext.Provider>
      </div>
   );
}
