//Grabs restart button
var restart = document.querySelector("#b")

//Grabs all the td elemnts in list
var squares = document.querySelectorAll('td')


//Clear all the squares

function clearBoard(){
  for(var i=0;i<squares.length;i++)
  {
    squares[i].textContent='';
  }
}

restart.addEventListener('click',clearBoard)
//so this will execute the function clearBoard upon clicking on Restart Btn

//Check the square marker
function changeMarker(){
  if (this.textContent===''){
    this.textContent='X';
  }
  else if (this.textContent === 'X') {
    this.textContent = 'O';
  }
  else {
    this.textContent ='';
 }
}

//For loop to add event listeners to all squares
for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener('click',changeMarker)
}


//REPETITIVE SOLUTION
//SUPPOSE CELLS HAVE IDS
/*
var cellOne=document.querySelector("#one")

cellOne.addEventListener('click',function(){
if (cellOne.textContent===''){
  cellOne.textContent='X'
}
else if (cellOne.textContent === 'X') {
  cellOne.textContent = 'O'
}
else {
  cellOne.textContent =''
}

})
*/
