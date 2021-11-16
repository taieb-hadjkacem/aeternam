from flask import Flask, render_template, request , redirect, url_for
import base64

app = Flask(__name__)
app.config['UPLOAD_PATH']='static'

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/colorize')
def colorize():
    return render_template("colorize.html")

@app.route('/colorize', methods=['POST'])
def upload_file():
    f = request.files['file']
    image_b64 = base64.b64encode(f.read()).decode('utf-8')
    return render_template("colorize.html", file=image_b64)



if __name__ == '__main__':
    app.run(debug= True)