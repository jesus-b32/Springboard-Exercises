const baseURL = "https://deckofcardsapi.com";



// 1.
async function drawCard() {
    const response = await fetch(`${baseURL}/api/deck/new/draw/?count=1`);
    const data = await response.json();
    console.log(`${data.cards[0].value} of ${data.cards[0].suit}`);
}

drawCard();

// 2.
async function drawTwoCard() {
    const response = await fetch(`${baseURL}/api/deck/new/draw/?count=1`);
    const data = await response.json();
    console.log(`${data.cards[0].value} of ${data.cards[0].suit}`);

    const response2 = await fetch(`${baseURL}/api/deck/${data.deck_id}/draw/?count=1`);
    const data2 = await response2.json();
    console.log(`${data2.cards[0].value} of ${data2.cards[0].suit}`);    
}

drawTwoCard();



// 3.
const button = document.querySelector('button');
const card_container = document.querySelector('#card_container');
let deckId = null;

async function shuffleCards() {
    const response = await fetch(`${baseURL}/api/deck/new/shuffle/?deck_count=1`);
    const data = await response.json();
    console.log(data);
    deckId = data.deck_id;
}
shuffleCards();


async function newCard (e) {
    const response = await fetch(`${baseURL}/api/deck/${deckId}/draw/?count=1`);
    const data = await response.json();
    // console.log('cards remaining: ', data.remaining);
    let img = document.createElement("img");
    img.src = data.cards[0].image;;
    img.alt = 'card image';
    card_container.append(img);
    if (data.remaining === 0) {
        button.remove();
    }    
}

button.addEventListener('click', newCard);