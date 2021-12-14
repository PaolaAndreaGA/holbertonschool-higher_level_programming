# Classes

Classes are a template for creating objects. They encapsulate data with code to work on that data. Classes in JS are built on prototypes but also have some syntax and semantics that are not shared with ES5 class-like semantics.

## [Defining classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#defining_classes "Permalink to Defining classes")

Classes are in fact "special  [functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)", and just as you can define  [function expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function)  and  [function declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function), the class syntax has two components:  [class expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class)  and  [class declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class).

### [Class declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#class_declarations "Permalink to Class declarations")

One way to define a class is using a  **class declaration**. To declare a class, you use the  `class`  keyword with the name of the class ("Rectangle" here).

```
class Rectangle {
  constructor(height, width) {
      this.height = height;
          this.width = width;
	    }
	    }

```

Copy to Clipboard

#### Hoisting

An important difference between  **function declarations**  and  **class declarations**  is that while functions can be called in code that appears before they are defined, classes must be defined before they can be constructed. Code like the following will throw a  [`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError):

```
const p = new Rectangle(); // ReferenceError

class Rectangle {}

```

Copy to Clipboard

This occurs because while the class is  [hoisted](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)  its values are not initialized.

### [Class expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#class_expressions "Permalink to Class expressions")

A  **class expression**  is another way to define a class. Class expressions can be named or unnamed. The name given to a named class expression is local to the class's body. However, it can be accessed via the  [`name`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name)  property.

```
// unnamed
let Rectangle = class {
  constructor(height, width) {
      this.height = height;
          this.width = width;
	    }
	    };
	    console.log(Rectangle.name);
	    // output: "Rectangle"

// named
let Rectangle = class Rectangle2 {
  constructor(height, width) {
      this.height = height;
          this.width = width;
	    }
	    };
	    console.log(Rectangle.name);
	    // output: "Rectangle2"

```

Copy to Clipboard

**Note:**  Class  **expressions**  must be declared before they can be used (they are subject to the same hoisting restrictions as described in the  [class declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#class_declarations)  section).

## [Class body and method definitions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#class_body_and_method_definitions "Permalink to Class body and method definitions")

The body of a class is the part that is in curly brackets  `{}`. This is where you define class members, such as methods or constructor.

### [Strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#strict_mode "Permalink to Strict mode")

The body of a class is executed in  [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode), i.e., code written here is subject to stricter syntax for increased performance, some otherwise silent errors will be thrown, and certain keywords are reserved for future versions of ECMAScript.

### [Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#constructor "Permalink to Constructor")

The  [constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor)  method is a special method for creating and initializing an object created with a  `class`. There can only be one special method with the name "constructor" in a class. A  [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)  will be thrown if the class contains more than one occurrence of a  `constructor`  method.

A constructor can use the  `super`  keyword to call the constructor of the super class.

### [Static initialization blocks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#static_initialization_blocks "Permalink to Static initialization blocks")

[Class  `static`  initialization blocks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Class_static_initialization_blocks)  allow flexible initialization of  [class  `static`  properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#static_methods_and_properties)  including the evaluation of statements during initialization, and granting access to private scope.

Multiple static blocks can be declared, and these can be interleaved with the declaration of static properties and methods (all static items are evaluated in declaration order).

### [Prototype methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#prototype_methods "Permalink to Prototype methods")

See also  [method definitions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions).

```
class Rectangle {
  constructor(height, width) {
      this.height = height;
          this.width = width;
	    }
	      // Getter
	        get area() {
		    return this.calcArea();
		      }
		        // Method
			  calcArea() {
			      return this.height * this.width;
			        }
				}

const square = new Rectangle(10, 10);

console.log(square.area); // 100

```

Copy to Clipboard

### [Generator methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#generator_methods "Permalink to Generator methods")

See also  [Iterators and generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators).

```
class Polygon {
  constructor(...sides) {
      this.sides = sides;
        }
	  // Method
	    *getSides() {
	        for(const side of this.sides){
		      yield side;
		          }
			    }
			    }

const pentagon = new Polygon(1,2,3,4,5);

console.log([...pentagon.getSides()]); // [1,2,3,4,5]

```

Copy to Clipboard

### [Static methods and properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#static_methods_and_properties "Permalink to Static methods and properties")

The  [static](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)  keyword defines a static method or property for a class. Static members (properties and methods) are called without instantiating their class and  **cannot**  be called through a class instance. Static methods are often used to create utility functions for an application, whereas static properties are useful for caches, fixed-configuration, or any other data you don't need to be replicated across instances.

```
class Point {
  constructor(x, y) {
      this.x = x;
          this.y = y;
	    }

  static displayName = "Point";
    static distance(a, b) {
        const dx = a.x - b.x;
	    const dy = a.y - b.y;

    return Math.hypot(dx, dy);
      }
      }

const p1 = new Point(5, 5);
const p2 = new Point(10, 10);
p1.displayName; // undefined
p1.distance;    // undefined
p2.displayName; // undefined
p2.distance;    // undefined

console.log(Point.displayName);      // "Point"
console.log(Point.distance(p1, p2)); // 7.0710678118654755

```

Copy to Clipboard

### [Binding  `this`  with prototype and static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#binding_this_with_prototype_and_static_methods "Permalink to Binding this with prototype and static methods")

When a static or prototype method is called without a value for  [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this), such as by assigning the method to a variable and then calling it, the  `this`  value will be  `undefined`  inside the method. This behavior will be the same even if the  [`"use strict"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)  directive isn't present, because code within the  `class`  body's syntactic boundary is always executed in strict mode.

```
class Animal {
  speak() {
      return this;
        }
	  static eat() {
	      return this;
	        }
		}

let obj = new Animal();
obj.speak(); // the Animal object
let speak = obj.speak;
speak(); // undefined

Animal.eat() // class Animal
let eat = Animal.eat;
eat(); // undefined

```

Copy to Clipboard

If we rewrite the above using traditional function-based syntax in non–strict mode, then  `this`  method calls are automatically bound to the initial  `this`  value, which by default is the  [global object](https://developer.mozilla.org/en-US/docs/Glossary/Global_object). In strict mode, autobinding will not happen; the value of  `this`  remains as passed.

```
function Animal() { }

Animal.prototype.speak = function() {
  return this;
  }

Animal.eat = function() {
  return this;
  }

let obj = new Animal();
let speak = obj.speak;
speak(); // global object (in non–strict mode)

let eat = Animal.eat;
eat(); // global object (in non-strict mode)

```

Copy to Clipboard

### [Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#instance_properties "Permalink to Instance properties")

Instance properties must be defined inside of class methods:

```
class Rectangle {
  constructor(height, width) {
      this.height = height;
          this.width = width;
	    }
	    }

```

Copy to Clipboard

### [Field declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#field_declarations "Permalink to Field declarations")

#### Public field declarations

With the JavaScript field declaration syntax, the above example can be written as:

```
class Rectangle {
  height = 0;
    width;
      constructor(height, width) {
          this.height = height;
	      this.width = width;
	        }
		}

```

Copy to Clipboard

By declaring fields up-front, class definitions become more self-documenting, and the fields are always present.

As seen above, the fields can be declared with or without a default value.

See  [public class fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields)  for more information.

#### Private field declarations

Using private fields, the definition can be refined as below.

```
class Rectangle {
  #height = 0;
    #width;
      constructor(height, width) {
          this.#height = height;
	      this.#width = width;
	        }
		}

```

Copy to Clipboard

It's an error to reference private fields from outside of the class; they can only be read or written within the class body. By defining things that are not visible outside of the class, you ensure that your classes' users can't depend on internals, which may change from version to version.

**Note:**  Private fields can only be declared up-front in a field declaration.

Private fields cannot be created later through assigning to them, the way that normal properties can.

For more information, see  [private class features](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_class_fields).

## [Sub classing with  `extends`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#sub_classing_with_extends "Permalink to Sub classing with extends")

The  [`extends`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)  keyword is used in  _class declarations_  or  _class expressions_  to create a class as a child of another class.

```
class Animal {
  constructor(name) {
      this.name = name;
        }

  speak() {
      console.log(`${this.name} makes a noise.`);
        }
	}

class Dog extends Animal {
  constructor(name) {
      super(name); // call the super class constructor and pass in the name parameter
        }

  speak() {
      console.log(`${this.name} barks.`);
        }
	}

let d = new Dog('Mitzie');
d.speak(); // Mitzie barks.

```

Copy to Clipboard

If there is a constructor present in the subclass, it needs to first call super() before using "this".

One may also extend traditional function-based "classes":

```
function Animal (name) {
  this.name = name;
  }

Animal.prototype.speak = function () {
  console.log(`${this.name} makes a noise.`);
  }

class Dog extends Animal {
  speak() {
      console.log(`${this.name} barks.`);
        }
	}

let d = new Dog('Mitzie');
d.speak(); // Mitzie barks.

// For similar methods, the child's method takes precedence over parent's method

```

Copy to Clipboard

Note that classes cannot extend regular (non-constructible) objects If you want to inherit from a regular object, you can instead use  [`Object.setPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf):

```
const Animal = {
  speak() {
      console.log(`${this.name} makes a noise.`);
        }
	};

class Dog {
  constructor(name) {
      this.name = name;
        }
	}

// If you do not do this you will get a TypeError when you invoke speak
Object.setPrototypeOf(Dog.prototype, Animal);

let d = new Dog('Mitzie');
d.speak(); // Mitzie makes a noise.

```

Copy to Clipboard

## [Species](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#species "Permalink to Species")

You might want to return  [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)  objects in your derived array class  `MyArray`. The species pattern lets you override default constructors.

For example, when using methods such as  [`map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)  that returns the default constructor, you want these methods to return a parent  `Array`  object, instead of the  `MyArray`  object. The  [`Symbol.species`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/species)  symbol lets you do this:

```
class MyArray extends Array {
  // Overwrite species to the parent Array constructor
    static get [Symbol.species]() { return Array; }
    }

let a = new MyArray(1,2,3);
let mapped = a.map(x => x * x);

console.log(mapped instanceof MyArray); // false
console.log(mapped instanceof Array);   // true

```

Copy to Clipboard

## [Super class calls with  `super`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#super_class_calls_with_super "Permalink to Super class calls with super")

The  [`super`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)  keyword is used to call corresponding methods of super class. This is one advantage over prototype-based inheritance.

```
class Cat {
  constructor(name) {
      this.name = name;
        }

  speak() {
      console.log(`${this.name} makes a noise.`);
        }
	}

class Lion extends Cat {
  speak() {
      super.speak();
          console.log(`${this.name} roars.`);
	    }
	    }

let l = new Lion('Fuzzy');
l.speak();
// Fuzzy makes a noise.
// Fuzzy roars.

```

Copy to Clipboard

## [Mix-ins](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#mix-ins "Permalink to Mix-ins")

Abstract subclasses or  _mix-ins_  are templates for classes. An ECMAScript class can only have a single superclass, so multiple inheritance from tooling classes, for example, is not possible. The functionality must be provided by the superclass.

A function with a superclass as input and a subclass extending that superclass as output can be used to implement mix-ins in ECMAScript:

```
let calculatorMixin = Base => class extends Base {
  calc() { }
  };

let randomizerMixin = Base => class extends Base {
  randomize() { }
  };

```

Copy to Clipboard

A class that uses these mix-ins can then be written like this:

```
class Foo { }
class Bar extends calculatorMixin(randomizerMixin(Foo)) { }

```

Copy to Clipboard

## [Re-running a class definition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#re-running_a_class_definition "Permalink to Re-running a class definition")

A class can't be redefined. Attempting to do so produces a  `SyntaxError`.

If you're experimenting with code in a web browser, such as the Firefox Web Console (**Tools**  >  **Web Developer**  >  **Web Console**) and you 'Run' a definition of a class with the same name twice, you'll get a  `SyntaxError: redeclaration of let ClassName;`. (See further discussion of this issue in  [bug 1428672](https://bugzilla.mozilla.org/show_bug.cgi?id=1428672).) Doing something similar in Chrome Developer Tools gives you a message like  `Uncaught SyntaxError: Identifier 'ClassName' has already been declared at <anonymous>:1:1`.