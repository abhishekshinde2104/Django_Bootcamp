// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addNew(name)
{
  roster.push(name)
  //return roster
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//
function remove(name)
{
  var newRoster=[]
  for(var i=0;i<roster.length;i++)
  {
    if(name === roster[i])
    {
      continue
    }
    newRoster.push(roster[i])
  }
  roster=newRoster
}

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function display()
{
  /*for(var i=0;i< roster.length;i++)
  {
    console.log(roster[i])
  }*/
    console.log(roster)
}


// Start by asking if they want to use the web app
var ask=prompt("Do you want to perform : 1)Yes 2)No")

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
if(ask==1)
{
  while(opt!==4)
  {
    var opt=prompt("Which operation to perform : 1)Add 2)Remove 3)Display 4)quit")
    if(opt == 1){
      var name=prompt("Enter the name")
      addNew(name)
    }else if(opt == 2){
      var name=prompt("Enter name to remove")
      remove(name)
    }else if(opt == 3){
      display()
    }
  }
}
alert("Done successfully")
