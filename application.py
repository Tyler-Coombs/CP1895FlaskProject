import sqlite3
from contextlib import closing
import imghdr
import os
from flask import Flask, render_template, redirect, request, abort
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'static/album_covers'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.jfif']

conn = sqlite3.connect("albums.db", check_same_thread=False)


@app.route("/home")
@app.route("/")
def index():
    heading = "Tyler's Top 5"
    return render_template("index.html", heading=heading)


@app.route("/albums")
def albums():
    heading = "Tyler's Top 5"
    with closing(conn.cursor()) as c:
        query = "SELECT * from Albums"
        c.execute(query)
        results = c.fetchall()
        images = []
        for result in results:
            images.append((result[1], result[2], result[3], result[4]))
    return render_template("albums.html", images=images, heading=heading)


@app.route("/update")
def update():
    heading = "Update"
    return render_template("update.html", heading=heading)


@app.route("/update", methods=['post'])
def getFormData():
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
            query = f"INSERT into Albums(album_title, artist, genre, cover_path) Values(?,?,?,?)"
            c.execute(query, (album_title, artist, genre, filename))
            conn.commit()
    return redirect("albums")


@app.route("/remove")
def remove():
    heading = "Remove An Album"
    return render_template("remove.html", heading=heading)


@app.route("/remove", methods=['post'])
def getFormData():
    album_title = request.values["album_title"]
    with closing(conn.cursor()) as c:
        query = f"DELETE from Albums WHERE album_title=?"
        c.execute(query, album_title)
        conn.commit()
    return redirect("albums")


def validate_album(stream):
    pass