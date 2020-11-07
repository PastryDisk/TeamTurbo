from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def initial():
    return render_template("index.html")

@app.route('/upload_file', methods=['POST'])
def upload_file():
    return request.get_data()


if __name__ == "__main__":
    app.run(debug=True)