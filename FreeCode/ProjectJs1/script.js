const character = "#";
const count = 8;
const rows = [];

function padRow(){
  
}


for (let i = 0; i < count; i = i + 1) {
  rows.push(character.repeat(i + 1))
}

let result = ""

for (const row of rows) {
  result = result + row + "\n";
}

console.log(result);


function padRow() {

}
padRow();


const call = padRow();
console.log(call);
console.log("this is the output of the call variable that was assigned the value of func")


