const _ = {
    each : (obj) => {
        return obj.name;
    }
}


let myObj = {
    "name": "Bob"
}


let name1 = _.each(myObj);


// Arrow functions are the same things anonymous functions

function outer(bar) {
    this.bar = bar;
    var that = this;
    function inner(baz) {
        this.baz = baz * that.bar;
    }
    return inner;
}



let tester = function(bar) {
    this.bar = bar;
    var that = this;
    function inner(baz) {
        return this.baz = baz * that.bar;
    }
}

tester(args);



function Person(){
    this.age = 0;
  
    setInterval(() => {
      this.age++; // |this| properly refers to the Person object
    }, 1000);
  }
  
  var p = new Person();

let person = (age = 0) => {
    this.age = age;

    setInterval(() => {
        this.age++;
    }, 1000);

    let p = new Person();
}

let dog = {
    age: 10,
    bark: (times) => {
        let bark = "bow wow";
        for (let i = 0; i < times; i++) {
            console.log(bark);
        }
    }
}

let Person = class {
    constructor(age) {
      this.age = age;
    }

    getOlder() {
        this.age ++;
        return this.age;
    }

};
