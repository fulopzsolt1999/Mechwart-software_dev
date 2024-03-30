import {useState} from "react";
export default function MyComponent() {
   const [name, setName] = useState("Guest");
   const [quantity, setQuantity] = useState(1);
   const [comment, setComment] = useState("");
   const [payment, setPayment] = useState("");
   const [shipping, setShipping] = useState("Delivery");

   function handleNameChange(e) {
      setName(e.target.value);
   }
   function handleQuantityChange(e) {
      setQuantity(e.target.value);
   }
   function handleCommentChange(e) {
      setComment(e.target.value);
   }
   function handlePaymentChange(e) {
      setPayment(e.target.value);
   }
   function handleShippingChange(e) {
      setShipping(e.target.value);
   }

   return (
      <div>
         <input value={name} onChange={handleNameChange} />
         <p>Name: {name}</p>
         <hr />
         <input value={quantity} onChange={handleQuantityChange} type="number" />
         <p>Quantity: {quantity}</p>
         <hr />
         <textarea
            value={comment}
            onChange={handleCommentChange}
            placeholder="Enter delivery instructions"
         />
         <p>Comment: {comment}</p>
         <hr />
         <select value={payment} onChange={handlePaymentChange}>
            <option value="">Select an option</option>
            <option value="Visa">Visa</option>
            <option value="Mastercard">Mastercard</option>
            <option value="Giftcard">Giftcard</option>
         </select>
         <p>Payment: {payment}</p>
         <hr />
         <label>
            <input
               type="radio"
               value="Pick Up"
               checked={shipping === "Pick up"}
               onChange={handleShippingChange}
            />
            Pick up
         </label>
         <br />
         <label>
            <input
               type="radio"
               value="Delivery"
               checked={shipping === "Delivery"}
               onChange={handleShippingChange}
            />
            Delivery
         </label>
         <p>Shipping: {shipping}</p>
      </div>
   );
}
