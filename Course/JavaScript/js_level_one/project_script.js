var fname = prompt("Hello .. Enter your first name : ");
var lname = prompt("Enter your last name : ");
var age = prompt("Whats your age :")
var height = prompt("Enter your height in cm : ")
var petname = prompt("Enter your pet name : ")

var condition1 = false
var condition2 = false
var condition3 = false
var condition4 = false
var final_cond = false

if(fname[0] === lname[0])
{
  condition1=true;
}

if(age<=30 && age>20)
{
  condition2=true;
}

if(height<=170)
{
  condition3=true
}

var len=petname.length
len--;
if(petname[len])
{
  condition4=true;
}



if(condition1===true && condition2===true && condition3===true && condition4===true  )
{
  final_cond= true
}

if(final_cond === true)
{
  console.log("You have passed the spy test")
}else{
  console.log("There is nothing here ")
}
