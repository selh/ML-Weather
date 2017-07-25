from flask import Flask, render_template
from flask_dropzone import Dropzone
from flask_bootstrap import Bootstrap
import pickle
import numpy as np


app = Flask(__name__)

bootstrap = Bootstrap(app)
dropzone = Dropzone(app)

from app import views
