var headOne = document.querySelector("#one");
var headTwo= document.querySelector("#two");
var headThree = document.querySelector("#three");
console.log("COnnected");

headOne.addEventListener("mouseover", function(){
  headOne.textContent = "Mouse Currently Over";
  headOne.style.color = "red";
});

headOne.addEventListener("mouseout", function(){
  headOne.textContent = "Hover Over ME!";
  headOne.style.color = "black";
});


headTwo.addEventListener("click", function(){
  headTwo.textContent ="Clicked ON";
  headTwo.style.color = "blue";
});

headThree.addEventListener("dblclick", function(){
  headThree.textContent = "I was double clicked!";
  headThree.style.color ="red";
});
