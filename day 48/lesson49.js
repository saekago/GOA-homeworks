var myName = "nika"
myName = "saba"
console.log(myName)

let myHobby = "programming"
myHobby = "fencing"
console.log(myHobby)

const myGroup = "group 77"
console.log(myGroup)

// I გზა
console.log("hello, my name is " + myName + ".")
console.log("hello, my hobby is " + myHobby + ".")
console.log("hello, my name is " + myName + " and my hobby is " + myHobby + ".")
// II გზა
console.log(`hello, my name is ${myName} and my hobby is ${myHobby}.`)

let age = 16
// I გზა
age = age + 4 // 20
// II გზა
age += 4 // 24
age -= 4 // 20
age *= 2 // 40
age /= 2 // 20
age ++ // + 1 = 21 // increment
age -- // = 1 = 20 // decrement
console.log(age)

console.log(typeof myName) // string
console.log(typeof myHobby) // string
console.log(typeof age) // number
let hobby = false
console.log(typeof hobby) // boolean
console.log(typeof "hello") // string
console.log(typeof 16) // number
console.log(typeof true) // boolean

// Math object
console.log(Math.PI)
console.log(Math.E)
console.log(Math.floor(Math.random() * 10)) // .floor ამრგვალებს რიცხვს დაბლა
console.log(Math.round(Math.random() * 10)) // .round ამრგვალებს რიცხვს მაღლა

random = Math.random() * 10
console.log(Math.round(random))