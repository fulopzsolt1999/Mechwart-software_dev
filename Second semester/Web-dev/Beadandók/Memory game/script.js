document.addEventListener("DOMContentLoaded", function () {
   // Card data
   const cardData = [
      {
         frontImage: "imgs/side_img.jpg",
         backImage: "imgs/Arnold_Schwarzenegger.jpg",
      },
      {
         frontImage: "imgs/side_img.jpg",
         backImage: "imgs/Arnold_Schwarzenegger.jpg",
      },
      {
         frontImage: "imgs/side_img.jpg",
         backImage: "imgs/Bodybuilder_Larry_Scott_first_winner.jpg",
      },
      {
         frontImage: "imgs/side_img.jpg",
         backImage: "imgs/Bodybuilder_Larry_Scott_first_winner.jpg",
      },
      {
         frontImage: "imgs/side_img.jpg",
         backImage: "imgs/DEREK-LUNSFORD_2023_winner.jpg",
      },
      {
         frontImage: "imgs/side_img.jpg",
         backImage: "imgs/DEREK-LUNSFORD_2023_winner.jpg",
      },
      {
         frontImage: "imgs/side_img.jpg",
         backImage: "imgs/Jay_Cutler.jpg",
      },
      {
         frontImage: "imgs/side_img.jpg",
         backImage: "imgs/Jay_Cutler.jpg",
      },
      {
         frontImage: "imgs/side_img.jpg",
         backImage: "imgs/Lee_Haney_1984_1991.JPG",
      },
      {
         frontImage: "imgs/side_img.jpg",
         backImage: "imgs/Lee_Haney_1984_1991.JPG",
      },
      {
         frontImage: "imgs/side_img.jpg",
         backImage: "imgs/Phil-Heath.png",
      },
      {
         frontImage: "imgs/side_img.jpg",
         backImage: "imgs/Phil-Heath.png",
      },
      {
         frontImage: "imgs/side_img.jpg",
         backImage: "imgs/Roney_Coleman_1998_2005.webp",
      },
      {
         frontImage: "imgs/side_img.jpg",
         backImage: "imgs/Roney_Coleman_1998_2005.webp",
      },
      {
         frontImage: "imgs/side_img.jpg",
         backImage: "imgs/Sergio_Oliva.jpg",
      },
      {
         frontImage: "imgs/side_img.jpg",
         backImage: "imgs/Sergio_Oliva.jpg",
      },
   ];

   // Set an array to store the last 2 selected images
   var storeClickedCards = [];

   // Set a variable to count how many pairs did the user found
   var count = 0;

   // Get the card container element
   const cardContainer = document.getElementById("cardContainer");

   // Shuffle the array of card data
   shuffleArray(cardData);
   function shuffleArray(array) {
      for (let i = array.length - 1; i > 0; i--) {
         const j = Math.floor(Math.random() * (i + 1));
         [array[i], array[j]] = [array[j], array[i]];
      }
   }

   // Create div elements and give the pictures to it
   cardData.forEach((cardInfo) => {
      const cardElement = document.createElement("div");
      cardElement.className = "card";

      const cardInner = document.createElement("div");
      cardInner.className = "card-inner";

      const frontFace = document.createElement("div");
      frontFace.className = "card-face front";
      frontFace.innerHTML = `<img src="${cardInfo.frontImage}" alt="Front Image">`;

      const backFace = document.createElement("div");
      backFace.className = "card-face back";
      backFace.innerHTML = `<img src="${cardInfo.backImage}" alt="Back Image">`;

      cardInner.addEventListener("click", handleCardClick);

      cardInner.appendChild(frontFace);
      cardInner.appendChild(backFace);
      cardElement.appendChild(cardInner);

      cardContainer.appendChild(cardElement);
   });

   // Handle click events on cards
   function handleCardClick(event) {
      const clickedCard = event.currentTarget;
      clickedCard.style.transform = "rotateY(180deg)";
      clickedCard.classList.add("periodicUnclickable");
      storeClickedCards.push(clickedCard);
      if (storeClickedCards.length === 2) {
         if (
            storeClickedCards[0].querySelector(".back img").src ===
            storeClickedCards[1].querySelector(".back img").src
         ) {
            count += 1;
            storeClickedCards[0].classList.add("unclickable");
            storeClickedCards[1].classList.add("unclickable");
            storeClickedCards = [];
         } else {
            document.querySelectorAll(".card-inner:not(.periodicUnclickable)").forEach((card) => {
               card.classList.add("periodicUnclickable");
            });
            setTimeout(() => {
               storeClickedCards[0].style.transform = "";
               storeClickedCards[1].style.transform = "";
               document.querySelectorAll(".card-inner.periodicUnclickable").forEach((card) => {
                  card.classList.remove("periodicUnclickable");
               });
               storeClickedCards = [];
            }, 1000);
         }
      }
      if (count === cardData.length / 2) {
         setTimeout(() => {
            handleWinCondition();
         }, 200);
      }
   }

   // Handle win, and show restart button
   function handleWinCondition() {
      window.alert("Congratulations! You Win!");
      restartGame();
   }

   // Handle restart game
   function restartGame() {
      const resetButton = document.getElementById("btn");
      resetButton.style.opacity = "1";
      resetButton.classList.remove("unclickable");
      resetButton.addEventListener("click", () => {
         location.reload();
      });
   }
});
