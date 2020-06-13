
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
	with open("database.txt", mode = 'a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data['message']
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database1.csv', 'a', newline='') as csvfile:
		email = data["email"]
		subject = data["subject"]
		message = data['message']
		writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow([email,subject,message])

# form submission
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
		   data = request.form.to_dict()
		   write_to_file(data)
		   write_to_csv(data)
		   return redirect('/thankyou.html')
		except:
			return 'Did not save to database'
	else:
		return "something went wrong"


'''
<form action="/submit_form" method="post" 		#add action & method in form lable

<input name="email" type="email"				# give name variable
<textarea name="message" class="form-control" 	##


'''

'''
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/works.html')
def works():
	return render_template('works.html')

@app.route('/about.html')
def about():
	return render_template('about.html')

@app.route('/contact.html')
def contact():
	return render_template('contact.html')

@app.route('/components.html')
def components():
	return render_template('components.html')

'''

'''
python -m venv d:/trail_venv 		#create venv

trail_venv\Scripts\activate.bat		#activate venve

pip insatll flask 					#install flask

$env:FLASK_APP = "server.py"		#link the py filr to flask app
set FLASK_APP=p1_server.py

$env:FLASK_ENV = "development"		#turn debug mode on
set FLASK_ENV=development

flask run 							#run  or start server
'''

