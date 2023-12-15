$('form').on('submit', function(event) {
    event.preventDefault();
    const movie = $('#title').val();
    const rating = $('#rating').val();
    $('#whole-container').append($('<div>'));
    $('#whole-container div:last-child').append($('<div>', {text: `${movie} has rating of ${rating}`}), $('<button type="button" class="delete-button">Delete</button>'));
});

$('#whole-container').on('click', '.delete-button', function(event) {
    $(event.target.parentElement).remove();
})