$(function()
{
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data, textStatus) {
        $.each(data.results, function(index, movies) {
            $("UL#list_movies").append(`<li>${movies.title}</li>`);
        })
    });
});
