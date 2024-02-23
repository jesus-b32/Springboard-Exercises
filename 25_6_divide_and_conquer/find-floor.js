
//modifyed binary search where the left and right indexed values are return when val not found or middle index value is returned
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
            return arr[middleindex];
        }
    }
    return [arr[leftIndex], arr[rightIndex]];
}



function findFloor(arr, num) {
    /* 
    Write a function called findFloor which accepts a sorted array and a value x, and returns the floor of x in the array. The floor of x in an array is the largest element in the array which is smaller than or equal to x. If the floor does not exist, return -1.
    
    */
    if(num < arr[0]) {// floor does not exist
        return -1;
    } else if(arr[arr.length - 1] < num){ //floor is the last element
        return arr[arr.length - 1];
    } else{
        let targetVals = binarySearch(arr, num);

        if(targetVals instanceof Array){ // logic for when num not found in arr
            let floorOne = Math.abs(num - targetVals[0]); 
            let floorTwo = Math.abs(num - targetVals[1]);
            if(floorOne < floorTwo) { // use to check targetVals[0] is closer to num
                return targetVals[0];
            } else {
                return targetVals[1];
            }
        } else { // floor is num
            return targetVals;
        }

    }
}

// module.exports = findFloor

console.log(findFloor([1,2,8,10,10,12,19], 9)) // 8
console.log(findFloor([1,2,8,10,10,12,19], 20)) // 19
console.log(findFloor([1,2,8,10,10,12,19], 0)) // -1