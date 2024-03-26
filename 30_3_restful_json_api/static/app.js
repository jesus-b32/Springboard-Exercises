const cupcakeForm = document.querySelector('#new_cupcake_form');
const cupcakeList = document.querySelector('#cupcake_list');
const BASE_URL = "http://127.0.0.1:5000/api";


/** given data about a cupcake, generate html */
function generateCupcakeHTML(cupcake) {
    return `
        <li data-cupcake-id="${cupcake.id}">
            ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
            <img class="img-fluid w-25"
            src="${cupcake.image}"
            alt="no image">
            <button class="btn btn-danger btn-sm delete_button">X</button>
        </li>
    `;
}


// Use Giphy API to retrive a GIF using a search term. Also will handel any error if encountered
async function showCupcakeList () {
    try {
        const response = await axios.get(`${BASE_URL}/cupcakes`);

        for (let cupcake of response.data.cupcakes) {
            let newCupcake = generateCupcakeHTML(cupcake);
            cupcakeList.innerHTML += newCupcake;
        }
    } catch(e) {
        alert('There was an issue showCupcakeList. Try again later.');
    }
}



// get search term from user input submit, send to API, and apend the GIF recieved from API
async function cupcakeFormHandler(e) {
    e.preventDefault();

    const flavor = document.querySelector('#flavor').value;
    const size = document.querySelector('#size').value;
    const rating = document.querySelector('#rating').value;
    const image = document.querySelector('#image').value;

    const response = await axios.post(`${BASE_URL}/cupcakes`, {
        flavor,
        size,
        rating,
        image
    });

    const cupcake = generateCupcakeHTML(response.data.cupcake);
    cupcakeList.innerHTML += cupcake;
}


// Use Giphy API to retrive a GIF using a search term. Also will handel any error if encountered
async function deleteCupcake (e) {
    e.preventDefault();

    if(!(e.target.classList.contains('delete_button'))) {
        return
    }

    const cupcake_id = e.target.parentElement.dataset.cupcakeId;

    try {
        const response = await axios.delete(`${BASE_URL}/cupcakes/${cupcake_id}`);

        e.target.parentElement.remove();
    } catch(e) {
        alert('There was an issue with deleteCupcake. Try again later.');
    }
}

showCupcakeList();
cupcakeForm.addEventListener('submit', cupcakeFormHandler);
cupcakeList.addEventListener('click', deleteCupcake);