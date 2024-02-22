function countZeroes(arr) {
    /*  
    Given an array of 1s and 0s which has all 1s first followed by all 0s, write a function called countZeroes, 
    which returns the number of zeroes in the array.
    */
  if(arr[0] === 0) {
    return arr.length;
  } else if(arr[arr.length - 1] === 1) {
    return 0;
  } else {
    for(let i = 0; i < arr.length; i++) {
        // find index where 0's start
        if (arr[i] === 0) {
            return arr.length - i;
        // 
        } else if(arr[((arr.length - 1) - i)] === 1) {
            return i;
        }
    }
  }
}

console.log(countZeroes([1, 1, 1, 1, 0, 0])) //2) index = 2 and length = 6
console.log(countZeroes([1, 0, 0, 0, 0])) //4)
console.log(countZeroes([0, 0, 0])) //3)
console.log(countZeroes([1, 1, 1, 1])) //0)

// module.exports = countZeroe