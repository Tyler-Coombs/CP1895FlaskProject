"use strict";

$(document).ready( () => {
    const genrePattern = /^[A-Za-z ]*$/;
    const userNamePattern = /^[A-Za-z0-9]*$/;

    $("#update_form").submit(
        evt => {
            let isValid = true;

            let albumCover = $("#album_cover").val();
            if (albumCover == "") {
                $("#album_cover").next().text("No files selected.");
                isValid = false;
            } else {
                $("#album_cover").next().text("");
            }

            let albumTitle = $("#album_title").val().trim();
            if (albumTitle == "") {
                $("#album_title").next().text("This field is required.");
                isValid = false;
            } else {
                $("#album_title").next().text("");
            }


            let albumArtist = $("#album_artist").val().trim();
            if (albumArtist == "") {
                $("#album_artist").next().text("This field is required.");
                isValid = false;
            } else {
                $("#album_artist").next().text("");
            }


            let genre = $("#genre").val().trim();
            if (genre == "") {
                $("#genre").next().text("This field is required.");
                isValid = false;
            } else if (!genrePattern.test(genre)) {
                $("#genre").next().text("Please use only alphabetical letters. Genres for a multi-genre album may be separated using a blank space.");
                isValid = false;
            } else {
                $("#genre").next().text("");
            }

            if (isValid == false) {
                evt.preventDefault();
            }
        }
    )

    $("#remove_form").submit(
        evt => {
            let isValid = true;

            let albumTitle = $("#album_title").val();
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

            let userName = $("#user_name").val().trim();
            if (userName == "") {
                $("#login_error").text("Please enter a user name to log in.");
                isValid = false;
            } else if (!userNamePattern.test(userName)) {
                $("#login_error").text("Username must consist of only numbers and letters.");
                isValid = false;
            }
            $("#user_name").val(userName);

            if (isValid == false) {
                evt.preventDefault();
            }
        }
    )
})