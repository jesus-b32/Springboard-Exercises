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
    let rightRotatingIndex = 0;
    let leftRotatingIndex = 0;
    let leftSortedArr;
    let rightSortedArr;


    for(let i = 0; i < arr.length; i++){
        if (arr[i] > arr[i + 1]) {
            leftRotatingIndex = i;
            break;
        } else if(arr[((arr.length - 1) - i)] < arr[((arr.length - 2) - i)]) { //1
            rightRotatingIndex = i;
            break;
        }
    }

    // for(let i = 0; i < arr.length; i++){
    //     if (arr[i] > arr[i + 1]) {
    //         leftRotatingIndex = i;
    //         break;
    //     } else if(arr[((arr.length - 1) - i)] < arr[((arr.length - 2) - i)]) { //1
    //         rightRotatingIndex = i;
    //         break;
    //     }
    // }


    if(leftRotatingIndex){
        leftSortedArr = arr.slice(0, leftRotatingIndex + 1);
        rightSortedArr = arr.slice(leftRotatingIndex + 1);
    } else {
        leftSortedArr = arr.slice(0, arr.length - rightRotatingIndex);
        rightSortedArr = arr.slice(arr.length - rightRotatingIndex - 1);
    }

    console.log('left Array: ', leftSortedArr);
    console.log('right Array: ', rightSortedArr);

    let left = binarySearch(leftSortedArr);
    let right = binarySearch(rightSortedArr);

    if(left) {
        return left;
    } else {
        return leftSortedArr.length + right;
    }

}

// module.exports = findRotatedIndex

console.log(findRotatedIndex([3,4,1,2],4)) // 1
console.log(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 8)) // 2
console.log(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 3)) // 6
console.log(findRotatedIndex([37,44,66,102,10,22],14)) // -1
console.log(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 12)) // -1