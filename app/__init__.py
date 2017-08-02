import os

from flask import Flask, render_template
from flask_dropzone import Dropzone
from flask_bootstrap import Bootstrap



app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024

app.config.from_object('config')
app.config['UPLOAD_FOLDER'] = 'app/static/tmp'

bootstrap = Bootstrap(app)
dropzone = Dropzone(app)


from app import views
