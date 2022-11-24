from ast import Div
from tkinter import Menu
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/inicio')
def home_page():
    return render_template ('home.html')
