import UserGreeting from "./Cond Rendering/UserGreeting.jsx";

function App() {
   return (
      <>
         <UserGreeting isLoggedIn={true} username="BroCode" />
      </>
   );
}

export default App;
