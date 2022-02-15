$(function () {
    $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, status) {
        if (status === 'success') {
            let movie = data.results;
            for (let i in movie){
                $('UL#list_movies').append('<li>' + movie[i].title + '</li>');
            }
        }
    });
});
