import os
from flask import Flask, render_template, request
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = '../data/uploads'

@app.route('/')
def initial():
    return render_template("index.html")

@app.route('/upload_file', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return "File Uploaded :)"


if __name__ == "__main__":
    app.run(debug=True)