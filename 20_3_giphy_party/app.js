const gifForm = document.querySelector('#gif_form');
const removeButton = document.querySelector('#removeBtn');

// append GIF URL to DOM
function appendGif (gifURL) {
    const gifContainer = document.querySelector('#gif_container');
    const img = document.createElement('img');
    img.src = gifURL;
    gifContainer.append(img);
}

// Use Giphy API to retrive a GIF using a search term. Also will handel any error if encountered
async function getGifURL (searchTerm) {
    try {
        let randomIndex = Math.floor(Math.random()*50);
        const result = await axios.get('https://api.giphy.com/v1/gifs/search', {params: {q: searchTerm, api_key: '7i1v2G2AELzzTnZPvjNV5I4FKYMP3hA5'}});
        return result.data.data[randomIndex].images.fixed_height.url;
    } catch(e) {
        alert('There was an issue. Try again later.');
    }
}

// get search term from user input submit, send to API, and apend the GIF recieved from API
async function gifSearchHandler(e) {
    e.preventDefault();
    const gifSearch = document.querySelector('#searchBar');
    const gif = await getGifURL(gifSearch.value); 
    appendGif(gif);
    gifSearch.value = '';
}

// remove all GIFS when remove  button is clicked on
function removeGifsHandler (e) {
    const gifContainer = document.querySelector('#gif_container');
    gifContainer.innerHTML = '';
}


gifForm.addEventListener('submit', gifSearchHandler);
removeButton.addEventListener('click', removeGifsHandler);