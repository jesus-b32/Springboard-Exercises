console.log("Let's get this party started!");

const gifForm = document.querySelector('#gif_form');
const searchButton = document.querySelector('#searchBtn');
const removeButton = document.querySelector('#removeBtn');

function gifSearchHandler(e) {
    e.preventDefault();
    const gifSearch = document.querySelector('#searchBar');
    let input = gifSearch.value;
    // run aysnc function that uses user input to search for a gif
    getGIFs(input);
    gifSearch.value = '';
}


async function getGIFs (searchTerm) {
    console.log(searchTerm);
    const result = await axios.get('http://api.giphy.com/v1/gifs/search', {params: {q: searchTerm, api_key: '7i1v2G2AELzzTnZPvjNV5I4FKYMP3hA5'}});
    console.log(result);
    const gif = document.querySelector('#gif');
    gif.src = result.data.data[0].images.original.url; //outputs the same GIF when using the same search term; use math random to randomize the index of data
}


gifForm.addEventListener('submit', gifSearchHandler);