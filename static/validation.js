"use strict";

$(document).ready( () => {
    const genrePattern = /^[A-Za-z]+$/;

    $("#update_form").submit(
        evt => {
            let isValid = true;

            let albumTitle = $("#album_title").val().trim();
            if (albumTitle == "") {
                $("#album_title").next().text("This field is required.");
                isValid = false;
            }
            $("#album_title").val(albumTitle);

            let albumArtist = $("#album_artist").val().trim();
            if (albumArtist == "") {
                $("#album_artist").next().text("This field is required.");
                isValid = false;
            }
            $("#album_artist").val(albumArtist);

            let genre = $("#genre").val().trim();
            if (genre == "") {
                $("#genre").next().text("This field is required.");
                isValid = false;
            } else if (!genrePattern.test(genre)) {
                $("#genre").next().text("Please use only alphabetical letters. Genres for a multi-genre album may be separated using a blank space.");
                isValid = false;
            }

            if (isValid == false) {
                evt.preventDefault();
            }
        }
    )

    $("#remove_form").submit(
        evt => {
            let isValid = true;

            let albumTitle = $("#album_title").val().trim();
            if (albumTitle == "") {
                $("#album_title").next().text("This field is required.");
                isValid = false;
            }
            $("#album_title").val(albumTitle);

            if (isValid == false) {
                evt.preventDefault();
            }
        }
    )

    $("#login_form").submit(
        evt => {
            let isValid = true;

            let userName = $("#user_name").val().trim()
            if (userName == "") {
                $("#login_error").text("Please enter a user name to log in.");
                isValid = false;
            }
            $("#user_name").val(userName);

            if (isValid == false) {
                evt.preventDefault();
            }
        }
    )
})