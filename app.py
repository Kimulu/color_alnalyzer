from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import colorgram

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded'
    file = request.files['file']
    if file.filename == '':
        return 'No file selected'
    filename = secure_filename(file.filename)
    file.save(filename)
    colors = colorgram.extract(filename, 6)
    return render_template('result.html', colors=colors)

if __name__ == '__main__':
    app.run(debug=True)
