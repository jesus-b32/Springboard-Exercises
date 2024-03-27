const cupcakeForm = document.querySelector('#new_cupcake_form');
const cupcakeList = document.querySelector('#cupcake_list');
const BASE_URL = "http://127.0.0.1:5000/api";


/** Generate html using cupcake data*/
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


/** Display the cupcake list stored in database*/
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



/** Store cupcake form data and send a post request to add this new cupcake to database. Also add the new cupcake to html page*/
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


/** Delete a cupcake when a delete button is clicked on and submit a DELETE request. Remove that cupcake from HTML page*/
async function deleteCupcake (e) {
    e.preventDefault();

    if(!(e.target.classList.contains('delete_button'))) {
        return
    }

    const cupcake_id = e.target.parentElement.dataset.cupcakeId;

    try {
        await axios.delete(`${BASE_URL}/cupcakes/${cupcake_id}`);

        e.target.parentElement.remove();
    } catch(e) {
        alert('There was an issue with deleteCupcake. Try again later.');
    }
}

/** Display cupcake list and listen for form submission and delete button clicks*/
showCupcakeList();
cupcakeForm.addEventListener('submit', cupcakeFormHandler);
cupcakeList.addEventListener('click', deleteCupcake);