export default function ProfilePicture() {
   const imageUrl = "./src/assets/Fülöp-Zsolt_CV-photo.jpg";
   const handleClick = (e) => (e.target.style.display = "none");
   return <img onClick={(e) => handleClick(e)} src={imageUrl} width="200px"></img>;
}
