let baseURL = "http://numbersapi.com";
let favNumber = 69;
const part2 = document.querySelector('#two');
const part3 = document.querySelector('#three');


// 1.
async function numFact(favNumber) {
    const response = await fetch(`${baseURL}/${favNumber}?json`);
    const num_data = await response.json();
    console.log(num_data);
}

numFact(favNumber);

// 2.
let favNumbers = [69, 2, 10];

async function numsFact(numArr) {
    const response = await fetch(`${baseURL}/${numArr}?json`);
    const num_data = await response.json();
    for (let num of numArr) {
        let li = document.createElement('li');
        li.textContent = num_data[num];
        part2.append(li);
    }    
}

numsFact(favNumbers); 

// 3.
async function numsFourFacts(favNumber) {
    let fourNumFacts = []

    for (let i=1; i<5; i++) {
        const response = await fetch(`${baseURL}/${favNumber}?json`);
        const num_fact = await response.json();
        fourNumFacts.push(num_fact);
    }

    for (let facts of fourNumFacts) {
        let li = document.createElement('li');
        li.textContent = facts.text;
        part3.append(li);
    }  
}

numsFourFacts(favNumber); 