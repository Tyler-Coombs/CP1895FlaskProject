"use strict";

$(document).ready( () => {
    const genrePattern = /^[A-Za-z]+$/;

    $("#add_album").submit(
        evt => {
            let isValid = true;

            let albumTitle = $("#album_title").val().trim();
            if (albumTitle == "") {
                alert("This field is required.");
                isValid = false;
            }
            $("#album_title").val(albumTitle);

            let albumArtist = $("#album_artist").val().trim();
            if (albumArtist) == "") {
                alert("This field is required.");
                isValid = false;
            }
            $("#album_artist").val(albumArtist);

            let genre = $("#genre").val().trim();
            if (genre == "") {
                alert("This field is required.");
                isValid = false;
            } else if (!genrePattern.test(genre)) {
                alert("Please use only alphabetical letters. Genres for a multi-genre album may be separated using a blank space.")
                isValid = false;
            }

            if (isValid == false) {
                evt.preventDefault();
            }
        }
    )

    $("#remove_album").submit(
        evt => {
            let isValid = true;

            let albumTitle = $("#album_title").val().trim();
            if (albumTitle == "") {
                alert("This field is required.");
                isValid = false;
            }
            $("#album_title").val(albumTitle);

            if (isValid == false) {
                evt.preventDefault();
            }
        }
    )
})