import sqlite3
from contextlib import closing
import imghdr
import os
from flask import Flask, render_template, redirect, request, abort, session
from werkzeug.utils import secure_filename
from datetime import timedelta

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'static/album_covers'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.jfif']
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "gordie"
app.permanent_session_lifetime = timedelta(hours=12)

conn = sqlite3.connect("albums.db", check_same_thread=False)


@app.route("/home")
@app.route("/")
def index():
    heading = "Tyler's Top 5"
    heading2 = "Fall 2021"
    if "user" in session:
        user = session["user"]
        return render_template("index.html", heading=heading, heading2=heading2)
    else:
        return render_template("index.html", heading=heading, heading2=heading2)


@app.route("/login", methods=["POST", "GET"])
def login():
    heading = "Tyler's Top 5"
    heading2 = "User Login"
    heading3 = "You are now logged in."
    if request.method == "POST":
        session.permanent = True
        user = request.form["name"]
        session["user"] = user
        return redirect("/home")
    else:
        if "user" in session:
            return redirect("/home")

        return render_template("login.html", heading=heading, heading2=heading2)


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")



@app.route("/albums")
def albums():
    heading = "Tyler's Top 5"
    heading2 = "Here is what I've been listening to:"
    with closing(conn.cursor()) as c:
        query = "SELECT * from Albums"
        c.execute(query)
        results = c.fetchall()
        images = []
        for result in results:
            images.append((result[1], result[2], result[3], result[4]))
    return render_template("albums.html", images=images, heading=heading, heading2=heading2)


@app.route("/update")
def update():
    logged_in = False
    if "user" in session:
        logged_in = True
    if logged_in:
        title = "Update"
        heading = "Update"
        heading2 = "Add your favorite!"
        return render_template("update.html", heading=heading, title=title, heading2=heading2)
    else:
        heading = "Tyler's Top 5"
        heading2 = "You must log in to add an album."
        return render_template("index.html", heading=heading, heading2=heading2)


@app.route("/update", methods=['POST'])
def getUpdateFormData():
    uploaded_file = request.files["file"]
    filename = secure_filename(uploaded_file.filename)
    album_title = request.values["album_title"]
    artist = request.values["album_artist"]
    genre = request.values["genre"]
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        with closing(conn.cursor()) as c:
            query = '''INSERT into Albums(album_title, artist, genre, cover_path) Values(?,?,?,?)'''
            c.execute(query, (album_title, artist, genre, filename))
            conn.commit()
    return redirect("albums")


@app.route("/remove")
def remove():
    logged_in = False
    if "user" in session:
        logged_in = True
    if logged_in:
        title = "Remove"
        heading2 = "Which album is not on your list?"
        heading = "Remove An Album"
        return render_template("remove.html", heading=heading, title=title, heading2=heading2)
    else:
        heading = "Tyler's Top 5"
        heading2 = "You must log in to remove an album."
        return render_template("index.html", heading=heading, heading2=heading2)


@app.route("/remove", methods=['POST'])
def getRemoveFormData():
    album_title = request.values["album_title"]
    with closing(conn.cursor()) as c:
        query = '''DELETE from Albums WHERE album_title=?'''
        c.execute(query, album_title)
        conn.commit()
    return redirect("albums")


def validate_album(stream):
    pass