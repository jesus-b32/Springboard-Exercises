function binarySearch (arr, val) {
    let leftIndex = 0;
    let rightIndex = arr.length - 1;

    while (leftIndex <= rightIndex){
        let middleindex = Math.floor((leftIndex + rightIndex) / 2);
        let middleValue = arr[middleindex];

        if (middleValue < val) {
            leftIndex = middleindex + 1;

        } else if(middleValue > val) {
            rightIndex = middleindex - 1;
        } else {
            return middleindex;
        }
    }
    return -1;
}

function findRotatedIndex(arr, num) {
    /* 
    Write a function called findRotatedIndex which accepts a rotated array of sorted numbers and an integer. The function should return the index of num in the array. If the value is not found, return -1.
    
    */
    let rightRotatingIndex = 0; //store index here if array rotates from right side
    let leftRotatingIndex = 0; //store index here if array rotates from right side
    let leftSortedArr; // leftside of the array where it rotates
    let rightSortedArr; // rightside of the array where it rotates

    //find the index where array rotates going from both sides
    for(let i = 0; i < arr.length; i++){
        if (arr[i] > arr[i + 1]) {
            leftRotatingIndex = i;
            rightRotatingIndex = -1;
            break;
        } else if(arr[((arr.length - 1) - i)] < arr[((arr.length - 2) - i)]) {
            rightRotatingIndex = i;
            leftRotatingIndex = -1;
            break;
        }
    }

    // slice the array into left and right accross rotation of array
    if(leftRotatingIndex !== -1){
        leftSortedArr = arr.slice(0, leftRotatingIndex + 1);
        rightSortedArr = arr.slice(leftRotatingIndex + 1);
    } else {
        leftSortedArr = arr.slice(0, arr.length - rightRotatingIndex - 1);
        rightSortedArr = arr.slice(arr.length - rightRotatingIndex - 1);
    }

    // binary search on both arrays
    let left = binarySearch(leftSortedArr, num); 
    let right = binarySearch(rightSortedArr, num); 


    if(left !== -1) {
        return left;
    } else if (right !== -1){
        return leftSortedArr.length + right;
    } else {
        return -1;
    }

}

// module.exports = findRotatedIndex

console.log(findRotatedIndex([3,4,1,2],4)) // 1
console.log(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 8)) // 2
console.log(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 3)) // 6
console.log(findRotatedIndex([37,44,66,102,10,22],14)) // -1
console.log(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 12)) // -1