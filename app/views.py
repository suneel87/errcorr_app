import os
import cv2
from flask import render_template

UPLOAD_FOLDER = 'static/upload'

def index():
    return render_template('index.html')

def app():
    return render_template('app.html')

def genderapp():
    return render_template('gender.html')
