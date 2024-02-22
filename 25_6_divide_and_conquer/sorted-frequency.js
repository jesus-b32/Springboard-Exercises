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

function sortedFrequency(arr, num) {
    /*  
    Given a sorted array and a number, write a function called sortedFrequency that counts the occurrences of the number in the array
    */
    
    //check if num exist in arr
    let index = binarySearch(arr, num);
    if(index == -1){
        return index;
    }

    let leftIndex = index;
    let rightIndex = index;

    // find the start index and the end index of the subset arr of num
    while (arr[leftIndex] === num) {
        leftIndex--;
        if(leftIndex === -1) {
            break;
        }
    }
    while (arr[rightIndex] === num) {
        rightIndex++;
        if(rightIndex === arr.length) {
            break;
        }
    }

    // calculate the ferequency of num 
    return (rightIndex - leftIndex) - 1;
}

// module.exports = sortedFrequency
// console.log(binarySearch([1,1,2,2,2,2,3],1)) // 2

console.log(sortedFrequency([1,1,2,2,2,2,3],2)) // 4    
console.log(sortedFrequency([1,1,2,2,2,2,3],3)) // 1
console.log(sortedFrequency([1,1,2,2,2,2,3],1)) // 2
console.log(sortedFrequency([1,1,2,2,2,2,3],4)) // -1