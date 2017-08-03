from flask import Flask
from flask_dropzone import Dropzone
from flask_bootstrap import Bootstrap


app = Flask(__name__)

app.config.from_object('config')
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024
app.config['UPLOAD_FOLDER'] = 'app/static/tmp'

bootstrap = Bootstrap(app)
dropzone = Dropzone(app)


from app import views
