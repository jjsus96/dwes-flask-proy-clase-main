from flask import Flask, send_from_directory
from config import DevConfig
import os

app = Flask(__name__)
app.config.from_object(DevConfig)

# Changed to show the git diff command


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home():
    return '<h1>Hello world</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
