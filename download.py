import os
from flask import Flask, render_template, send_from_directory, current_app
import subprocess as sp

app = Flask(__name__,template_folder="template")

@app.route("/")
def home():
    return render_template("download.html")

@app.route("/download")
def change():
    downdir = os.path.join(current_app.root_path, app.instance_path, 'downloads')
    return send_from_directory(directory=downdir, path="instance\\downloads", filename="data.csv", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)    