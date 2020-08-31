var hot =false
var temp =10

var user_temp = prompt("Enter the Temperatureof your city : ");


if(user_temp > 80)
{
  //hot=true //this way we can re-assign the variable
  console.log("Hot outside");
}else if (user_temp <= 80 && temp>=50){
  console.log("Average temperature outside");
}else if (user_temp < 50 && user_temp >=32){
  console.log("It`s pretty cold out");
}else {
  console.log("Its very cold outside");
}
//console.log(hot);
