function addNum(num1,num2)
{
  console.log(num1+ num2);
}

function hello(name='Default')
{
  console.log("Hello "+name)
}

function formal(name="Sam" , title="Sir")
{
  return(title+" "+name);
}

function timesFive(numInput)
{
  //numInput and result have local scope
  var result= numInput*5
  return result
}

//Global scope

var v = 'Global variable'
var stuff = 'Global stuff'

function func(stuff)
{
  console.log(v)
  stuff = 'Reassign stuff inside func'
  console.log(stuff)
}

console.log(stuff8f)
