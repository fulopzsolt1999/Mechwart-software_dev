import picture from "../assets/Fülöp-Zsolt_CV-photo.jpg";

function Card() {
   return (
      <div className="card">
         <img className="card-img" src={picture} alt="my-img" />
         <h2 className="card-title">My name</h2>
         <p className="card-text">I learn junior frontend develping.</p>
      </div>
   );
}

export default Card;
