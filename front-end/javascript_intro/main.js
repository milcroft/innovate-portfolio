// single line comments

/*
multiLine
Comment
*/

//! DATA TYPES

let dataType = 'this is a string'; // string data type
dataType = 123; // integer data type
dataType = 12.34; // float data type
dataType = true; // boolean data type

//! VARIABLES
console.log('Hello World');

var myFirstName = 'Darren'; // 'var' is used for legacy code

const mySurname = 'Nickerson'; // 'const cannot be updated

let myJob = 'Software Developer';

console.log(myJob);

//! IF STATEMENTS

if (myJob === 'Software Developer') {
  console.log('Job: Software Devleoper');
} else if (myJob === 'SQL Develper') {
  console.log('Job: SQL Develper');
} else {
  console.log(`Job: unknown`);
}

if (myFirstName === 'Darren' && mySurname === 'Nickers') {
  console.log('His name is Darren Nickerson');
} else {
  console.log('I dont know his name');
}

if (myJob === 'Software Developer' || myJob === 'SQL Developer') {
  console.log('Programmer');
} else {
  console.log('Not known');
}

//! FUNCTIONS
// normal function
function myFunction() {
  console.log('This is a JavaScript function!');
}

myFunction();

// arrow function
hello = (user) => {
  console.log(`hello ${user}`);
};

hello('darren');

//! STRING INTERPOLATION

console.log(`His name is ${myFirstName} ${mySurname}.`);

//! ARRAYS

let innovateInstructores = ['Jordan', 'Katy'];

console.log(innovateInstructores[0]);

//! LOOP

// for loop
let text = '';

for (let i = 0; i <= 10; i++) {
  text += ' The number is ' + i + ' ';
}
console.log(text);

// while loop

let i = 0;

while (i < 10) {
  text += ' The number is ' + i + '';
  i++;
}

console.log(text);

// ! SWITCH STATEMENT

let fruit = 'apple';

switch (fruit) {
  case 'grape':
    console.log('grape');
    break;
  case 'orange':
    console.log('orange');
    break;
  case 'apple':
    console.log('apple');
    break;
  default:
    console.log('Do not like that fruit');
}
