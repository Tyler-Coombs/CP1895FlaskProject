import sqlite3
from contextlib import closing
import imghdr
import os
from flask import Flask, flash, render_template, redirect, request, abort, session, send_from_directory
from flask_session import Session
from werkzeug.utils import secure_filename
from datetime import timedelta

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'venv/static/images'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.jfif', '.jpeg']
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

conn = sqlite3.connect("venv/albums.db", check_same_thread=False)


def validate_album(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


@app.route("/home")
@app.route("/")
def index():
    heading2 = "Welcome"
    if not session.get("name"):
        return render_template("index.html", heading2=heading2)
    else:
        user = session["name"]
        return render_template("index.html", heading2=heading2, user=user)


@app.route("/login", methods=["POST", "GET"])
def login():
    heading2 = "User Login"
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html", heading2=heading2)


@app.route("/logout")
def logout():
    session["name"] = None
    logout_message = "Thank you for logging out. Please visit again!"
    return render_template("message.html", message=logout_message)


@app.route("/albums")
def albums():
    if not session.get("name"):
        user_name1 = "secret_admin"
        heading2 = "Login to create your own."
        heading3 = "Here is what I've been listening to:"
        with closing(conn.cursor()) as c:
            query = f"SELECT * from Albums WHERE user_name = ?"
            c.execute(query, (user_name1,))
            results = c.fetchall()
            albums = []
            for result in results:
                albums.append((result[1], result[2], result[3], result[4]))
        return render_template("albums.html", albums=albums, heading2=heading2, heading3=heading3)
    else:
        user_name1 = "secret_admin"
        heading2 = "Create your own with 'Add Album'"
        heading3 = "Here is what I've been listening to:"
        with closing(conn.cursor()) as c:
            query = f"SELECT * from Albums WHERE user_name = ?"
            c.execute(query, (user_name1,))
            results = c.fetchall()
            albums = []
            for result in results:
                albums.append((result[1], result[2], result[3], result[4]))
        return render_template("albums.html", albums=albums, heading2=heading2, heading3=heading3)


@app.route("/userAlbums")
def userAlbums():
    if not session.get("name"):
        message1 = "Please log in first."
        return render_template("message.html", message=message1)
    else:
        heading2 = "Add to your list using the 'Add Album' link in the Nav bar."
        heading3 = "What you've been listening to: "
        with closing(conn.cursor()) as c:
            query = f"SELECT * from Albums WHERE user_name = ?"
            c.execute(query, (session.get("name"),))
            results = c.fetchall()
            albums = []
            for result in results:
                albums.append((result[1], result[2], result[3], result[4]))
        return render_template("albums.html", albums=albums, heading2=heading2, heading3=heading3)


@app.route("/update")
def update():
    if not session.get("name"):
        return render_template("login.html", )
    else:
        title = "Update"
        heading2 = "Create your own favorites list!"
        return render_template("update.html", title=title, heading2=heading2)


@app.route("/update", methods=['POST'])
def getUpdateFormData():
    uploaded_file = request.files["album_cover"]
    filename = secure_filename(uploaded_file.filename)
    album_title = request.values["album_title"]
    artist = request.values["album_artist"]
    genre = request.values["genre"]
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']: # or \
                #file_ext != validate_album(uploaded_file.stream):
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        with closing(conn.cursor()) as c:
            query = f"INSERT into Albums(album_title, artist, genre, cover_path, user_name) Values(?,?,?,?,?)"
            c.execute(query, (album_title, artist, genre, filename, session.get("name")))
            conn.commit()
    return redirect("userAlbums")


@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


@app.route("/remove")
def remove():
    if not session.get("name"):
        return redirect("/login")
    else:
        title = "Remove"
        heading2 = "Which album would you like to remove from your list?"
        return render_template("remove.html", title=title, heading2=heading2)


@app.route("/remove", methods=['POST'])
def getRemoveFormData():
    albumTitle = request.values["album_title"]
    with closing(conn.cursor()) as c:
        query = f"DELETE from Albums WHERE album_title = ? AND user_name = ?"
        c.execute(query, (albumTitle, session.get("name"),))
        conn.commit()
    return redirect("albums")


@app.route("/message")
def message():
    return render_template("message.html")




