# Javascript interview resources

- http://www.toptal.com/javascript#hiring-guide
- http://www.toptal.com/javascript/interview-questions


/*
- difference between `==` and `===`
- What is bidirectional data binding?
- Have you used SASS? What have you used from CSS3?
- How does prototypical inheritance work?
- How does scope inheritance work in angular?
- Have you created a directive in angular?
- this, that
- What is the difference between asynchronous and synchronous language
- what is a promise
- Write an isPrime function
*/

/*
- what will be printed on the console if a user clicks the first and fourth button?
*/
var nodes = document.getElementsByTagName('button');
for (var i = 0; i < nodes.length; i++) {
   nodes[i].addEventListener('click', function() {
      console.log('You clicked element #' + i);
   });
}


/*
- What is the output
*/
var o = {
    hey: function() {
	    setTimeout(function(){this.sayHi();}, 100);
    },
    sayHi: function() {
        console.log('hi');
    }
}
o.hey();


/*
- What is the result of the following?
*/
(function () {
   console.log(1);
   setTimeout(function() { console.log(2); }, 1000);
   setTimeout(function() { console.log(3); }, 0);
   console.log(4);
})();


/*
- How does prototypical inheritance work?
*/
function o(str) {
	this.a = 'a';
}
o.prototype.b = 'b';
a = new o()

console.log(a.a);
delete a.a;
console.log(a.a);

console.log(a.b);
delete a.b;
console.log(a.b);



