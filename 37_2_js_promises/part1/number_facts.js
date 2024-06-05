let baseURL = "http://numbersapi.com";
let favNumber = 69;
const part2 = document.querySelector('#two');
const part3 = document.querySelector('#three');


// 1.
fetch(`${baseURL}/${favNumber}?json`)
    .then(response => response.json())
    .then(data => console.log(data));

// 2.
let favNumbers = [69, 2, 10];
fetch(`${baseURL}/${favNumbers}?json`)
    .then(response => response.json())
    .then(data => {
        for (let num of favNumbers) {
            let li = document.createElement('li');
            li.textContent = data[num];
            part2.append(li);
        }
    });

// 3.
let fourNumberPromises = [];

for (let i = 1; i < 5; i++) {
    fourNumberPromises.push(
    fetch(`${baseURL}/${favNumber}?json`)
        .then(response => response.json())
    );
}

Promise.all(fourNumberPromises)
    .then(numberArr => (
        numberArr.forEach(data => {
            let li = document.createElement('li');
            li.textContent = data.text;
            part3.append(li);
        })
    )
)