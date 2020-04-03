// ==============
// 1 what is immutability? why is it useful?
// Talked about
// - pure functions
// - strings
// - side effects
// - functional programming
// - in place sorting

// ==============
// 2 describe web authentication and how it works
// - salt + secret
// - rainbow attack
// - plain text
// - captcha
// - JWT
// - https
// - password complexity

// ==============
// 3 scope with set timeout
// Without running what will the below print

function asdf() {
  if (true) {
    var x = 10;
    let y = 20;
  }
  var z = 30;
  console.log("x", x);
  setTimeout(() => console.log("y", y), 10);
  console.log("z", z);
  return () => {
    console.log("y", y);
  };
}

// ==============
// 4 function Person evaluate class
// Without running what will the below print
// follow up how would you fix it
function Person(name) {
  this.name = name;
}
Person.sayHi = () => {
  console.log("this.name", this.name);
};

var john = new Person("john");
john.sayHi();

// ==============
// 5 pairs with sum

function hasPairsWithSum(array, sum) {
  // implement
}

hasPairsWithSum([1, 2, 2, 3, 4, 5], 8); // true because 5 + 3 => 8
hasPairsWithSum([1, 2], 8); // false no pair of numbers add up to 8

// ==============
// 6 balance brackets

function checkBrackets(string) {}

checkBrackets("(something)"); // valid
checkBrackets("()"); // valid
checkBrackets("something()("); // invalid
checkBrackets(")something("); // invalid

// Follow up: what if we had multiple brackets

checkBrackets("[({blah})]"); // valid
checkBrackets("[{(blah})]"); // invalid

// ==============
// 7 implement Promise.last
// it takes an array of promises but only returns the result of the slowest promise
// all the other promises are ignored
Promise.last([promise1, promise2, promise3]);
