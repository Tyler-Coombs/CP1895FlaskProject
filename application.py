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
    return render_template("index.html")


@app.route("/albums")
def albums():
    with closing(conn.cursor()) as c:
        query = "SELECT * from Albums"
        c.execute(query)
        results = c.fetchall()
        images = []
        for result in results:
            images.append((result[1], result[2], result[3], result[4]))
    return render_template("albums.html", images=images)


@app.route("/update")
def update():
    return render_template("update.html")


@app.route("/remove")
def remove():
    return render_template("remove.html")


def validate_album(stream):
    pass