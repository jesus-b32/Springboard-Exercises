const baseURL = "https://deckofcardsapi.com";



// 1.
fetch(`${baseURL}/api/deck/new/draw/?count=1`)
    .then(response => response.json())
    .then(data => console.log(`${data.cards[0].value} of ${data.cards[0].suit}`));

// 2.
fetch(`${baseURL}/api/deck/new/draw/?count=1`)
    .then(response => response.json())
    .then(data => {
        console.log(data);
        return fetch(`${baseURL}/api/deck/${data.deck_id}/draw/?count=1`)
        .then(response => response.json())
    })
    .then(data => {
        console.log(data);
    })

// 3.
const button = document.querySelector('button');
const card_container = document.querySelector('#card_container');
let deckId = null;

fetch(`${baseURL}/api/deck/new/shuffle/?deck_count=1`)
.then(response => response.json())
.then(data => {
    console.log(data);
    deckId = data.deck_id;
});

button.addEventListener('click', function() {

    fetch(`${baseURL}/api/deck/${deckId}/draw/?count=1`)
        .then(response => response.json())
        .then(data => {
            console.log('cards remaining: ', data.remaining);
            let img = document.createElement("img");
            img.src = data.cards[0].image;;
            img.alt = 'card image';
            card_container.append(img);
            if (data.remaining === 0) {
                button.remove();
            }
    });
})