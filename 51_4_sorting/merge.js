function merge(arr1, arr2) {
  let results = [];
  //i and j are pointer for each array
  let i = 0;
  let j = 0;

  // while both array have not been exhausted
  while (i < arr1.length && j < arr2.length) {
    if (arr2[j] > arr1[i]) {
      results.push(arr1[i]);
      i++;
    } else {
      results.push(arr2[j]);
      j++;
    }
  }

  //push remainnig elements of arr1
  while (i < arr1.length) {
    results.push(arr1[i]);
    i++;
  }

  //push remainnig elements of arr2
  while (j < arr2.length) {
    results.push(arr2[j]);
    j++;
  }

  return results;
}

function mergeSort(arr) {
  //Split array into halves until you have arrays that have length of 0 or 1
  if (arr.length <= 1) return arr;
  const mid = Math.floor(arr.length / 2);
  const left = mergeSort(arr.slice(0, mid));
  const right = mergeSort(arr.slice(mid));

  return merge(left, right);
}

module.exports = { merge, mergeSort };
