// hw16
const numArr = [4, 5, 6, 7];
console.log(numArr.findIndex(function(value){
    return primeCheck(value);
}));

function primeCheck(value){
    if (value <= 1){
        return false;
    }
    
    for (let i = 2; i <= Math.floor(Math.sqrt(value)); i++){
        if (value % i == 0){
            return false;
        }
    }
    
    return true;
}


// hw17
const userArr = [{role: "a"}, {role: "a"}, {role: "Admin"}]
console.log(userArr.findIndex(function(value){
    return value.role.toLowerCase() === "admin"
}))


// hw18
const itemArr = [{overdue: false}, {overdue: true}, {overdue: false}]
console.log(itemArr.findIndex(function(value){
    return value.overdue === true
}))


// hw19
const itemArr2 = [{inStock: false}, {inStock: true}, {inStock: true}]
console.log(itemArr2.findIndex(function(value){
    return value.inStock === false;
}))


// hw20
function manualFindIndex(iterable, userFunc){
    for (let i=0; i<iterable.length; i++){
        if (userFunc(iterable[i])){
            return iterable[i]
        }
    }

    return -1
}


// hw21
console.log("Hello world!".indexOf("l"))


// hw22
console.log(numArr.indexOf(6))


// hw23
console.log("hello hello".indexOf("ll"))


// hw 24
console.log(itemArr.indexOf({overdue: true}))


// hw25
function manualIndexOf(iterable, value){
    for (let i=0; i<iterable.length; i++){
        if (userFunc(iterable[i]) === value){
            return i
        }
    }

    return -1
}


// hw26
console.log("david".lastIndexOf("d"))


// hw27
function isPrime(num) {
    if (num <= 1) return false;
    if (num === 2) return true;
    if (num % 2 === 0) return false;
    for (let i = 3; i <= Math.sqrt(num); i += 2) {
        if (num % i === 0) return false;
    }
    return true;
}

function lastIndexOfPrime(arr) {
    const primes = arr.filter(isPrime);
    if (primes.length === 0) return -1;
    
    const lastPrime = primes[primes.length - 1]; 
    return arr.lastIndexOf(lastPrime); 
}

const numArr2 = [4, 5, 6, 7];
console.log(lastIndexOfPrime(numArr2));


// hw28
const strArr = ["a", "b", "c", "a", "b", "c"]
console.log(strArr.lastIndexOf("c"))


// hw29
const obj1 = {isActive: true};
const obj2 = {isActive: false};
const obj3 = {isActive: true};

const userArr2 = [obj1, obj2, obj3]
console.log(userArr2.lastIndexOf(obj3))


// hw30
function manualIndexOf(iterable, value){
    for (let i=iterable.length - 1; i>= 0; i--){
        if (userFunc(iterable[i]) === value){
            return i
        }
    }

    return -1
}