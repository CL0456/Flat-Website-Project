from flask import Flask as F
from flask import render_template as RT
app = F(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return RT("home.html")

app.run()