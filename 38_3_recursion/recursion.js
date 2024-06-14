// Write a function that finds the product of an array of numbers:
function product(nums, i=0) {
    if (i === nums.length) return 1;

    return nums[i] * product(nums, i+1);
}

console.log('product: ', product([2, 3, 4]))   // 24


// Given a list of words, return the length of the longest:
function longest(words, i=0) {
    if (i === words.length) {
        return 0;
    }
    else {
        let currentWordLength = words[i].length;
        let restOfWordsLength = longest(words, i+1);
        return Math.max(currentWordLength, restOfWordsLength);
    }
}


console.log('longest word: ', longest(["hello", "hi", "hola"])); //5



// Write a function that returns a string of every other character:
function everyOther(word, i=0) {
    if (i >= word.length) return '';

    return word[i] + everyOther(word, i+2);
}

console.log('Every Other Character: ', everyOther("hello")); // "hlo"



// Write a function that returns true/false depending on whether passed-in string is a palindrome:
function isPalindrome(word, i=0) {
    // let reverseWord = word.split('').reverse().join('');

    if (i === word.length) return true;

    if(word[i] === word[word.length - (i+1)]) {
        return isPalindrome(word, i+1);
    } else {
        return false;
    }
}

console.log('Is Palindrome?: ', isPalindrome("tacocat")); //true
console.log('Is Palindrome?: ', isPalindrome("tacodog")); //false



// Given an array and a string, return the index of that string in the array (or -1 if not present):
function findIndex(arr, str, i=0) {
    if (i === arr.length) return -1;

    if (arr[i] === str) {
        return i;
    } else {
        return findIndex(arr, str, i+1);
    }
}

let animals = ["duck", "cat", "pony"];
console.log('Find Index: ', findIndex(animals, "cat")); // 1
console.log('Find Index: ', findIndex(animals, "porcupine")); // -1


// Return a copy of a string, reversed:
function revString(word, i=0) {
    if (i === word.length) return '';

    return revString(word, i+1) + word[i];
}

console.log('Reverse String: ', revString("porcupine")) // 'enipucrop'



// Given an object, return an array of all the values in the object that are strings:
function gatherStrings(obj) {
    let result = [];
    for (let key in obj) {
        if (typeof obj[key] === 'string') {
            result.push(obj[key]);
        } else if (typeof obj[key] === 'object' && obj[key] !== null) {
            result = result.concat(gatherStrings(obj[key]));
        }
    }
    return result;
}


let nestedObj = {
    firstName: "Lester",
    favoriteNumber: 22,
    moreData: {
        lastName: "Testowitz"
    },
    funFacts: {
        moreStuff: {
            anotherNumber: 100,
            deeplyNestedString: {
                almostThere: {
                    success: "you made it!"
                }
            }
        },
        favoriteString: "nice!"
    }
};
console.log('Gather Strings: ', gatherStrings(nestedObj)); // ["Lester", "Testowitz", "you made it!", "nice!"];