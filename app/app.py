from flask import Flask, render_template, g, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import json
import requests
import dateparser
from operator import itemgetter



# CREATE APPLICATION OBJECT

app = Flask(__name__)

# # CONFIG
# import os
# app.config.from_object(os.environ["APP_SETTINGS"])

#CREATE THE SQLALCHEMY OBJECT

# db = SQLAlchemy(app)
# from models import *
# now = datetime.now()


@app.route('/')
@app.route('/index')
def index():
	hello = "hello"
	return render_template("index.html", title='Home', hello=hello)

@app.route('/getlessonplan', methods=['POST'])
def get_lesson_plan():
	one = request.form.get("one")
	two = request.form.get("two")
	three = request.form.get("three")
	four = request.form.get("four")
	five = request.form.get("five")
	six = request.form.get("six")
	location = request.form.get("location")

	lesson_plan = calculate_lesson_plan(one, two, three, four, five, six, location)

	return render_template("lessonplan.html", lesson_plan='lesson_plan')



if __name__ == '__main__':

	app.run(host='127.0.0.1', port=5001)