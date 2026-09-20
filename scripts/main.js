const myImage = document.querySelector("img");

myImage.addEventListener("click", () => {
  const mySrc = myImage.getAttribute("src");
  if (mySrc === "images/The_Mid_Offs_4.png") {
    myImage.setAttribute("src", "images/ranked_logo.png");
  } else {
    myImage.setAttribute("src", "images/The_Mid_Offs_4.png");
  }
});

let myButton = document.querySelector("button");
let myHeading = document.querySelector("h1");

function setUserName() {
  const myName = prompt("Please enter your ingame name to compare to the Mid-Offs players.");
  if (!myName) {
    setUserName();
  } else {
    localStorage.setItem("name", myName);
    myHeading.textContent = `Let's track some Mid-Offs, ${myName}`;
  }
}

if (!localStorage.getItem("name")) {
  setUserName();
} else {
  const storedName = localStorage.getItem("name");
  myHeading.textContent = `Let's track some Mid-Offs, ${storedName}`;
}

myButton.addEventListener("click", () => {
  setUserName();
});