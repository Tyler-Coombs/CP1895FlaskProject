import os
from flask import Flask, render_template, redirect, request, abort
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/albums")
def albums():
    pass

@app.route("/update")
def update():
    pass

@app.route("/remove")
def remove():
    pass



def validate_album(stream):
    pass