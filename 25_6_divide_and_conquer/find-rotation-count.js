function findRotationCount(arr) {
        /* 
    Write a function called findRotationCount which accepts an array of distinct numbers sorted in increasing order. The array has been rotated counter-clockwise n number of times. Given such an array, find the value of n.
    
    */
    let counter = 0;
    let firstElement;

    while(arr[0] > arr[arr.length - 1]){
        counter++;
        firstElement = arr.shift();
        arr.push(firstElement);
    }

    return counter;
}

// module.exports = findRotationCount

console.log(findRotationCount([15, 18, 2, 3, 6, 12])) // 2
console.log(findRotationCount([7, 9, 11, 12, 5])) // 4
console.log(findRotationCount([7, 9, 11, 12, 15])) // 0