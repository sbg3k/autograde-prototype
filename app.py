import otter
import time
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename

class mark:
	def __init__(self, filename):
		exec('from ' + filename.split('.')[0] + ' import main', globals())
		self.main = main

UPLOAD_FOLDER = './hidden-tests'
ALLOWED_EXTENSION = 'py'
PASS = 'lcv:>?;W5QD<,js8oKyE4q`nN"z$M.?ts4#zd3o^n+9bk%6q$1@1P+P6uD^fY0z.>'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PASS'] = PASS

def allowed_file(filename):
	return '.' in filename and \
		   filename.split('.')[1].lower() == ALLOWED_EXTENSION


@app.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		# check if the post request has the file part
		
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		
		file = request.files['file']
		file.filename = request.form['name'] + '.py'
		
		# if user does not select file, browser also
		# submit an empty part without filename
		
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'][:2], filename))
			try:
				main = mark(filename).main
			
			
				score = {}
				tests = os.listdir('./hidden-tests')
				for i in tests:
					if allowed_file(i):
						score[i] = str(otter.Notebook("hidden-tests").check(i.split('.')[0]))
			
			
				files = []
				for i in score:
					if 'All tests passed!' in score[i]:
						files.append(i)
			
				scores = 0
				for i in files:
					with open('./hidden-tests/' + i) as f:
						a = f.read()
						if '"points":' in a:
							b = a.split('\n')[2]
							c = b.split(": ")[1]
							d = c.replace(",", "")
							scores += int(d)
				
				
				os.remove(os.path.join(app.config['UPLOAD_FOLDER'][:2], filename))
				return jsonify({"name":filename.replace(".py", ""), "score":scores})
			except:
				return '''Check your file, it does not follow the requirements'''
	
	return '''
	<!doctype html>
	<title>Upload new File</title>
	<h1>Upload new File</h1>
	<form method=post enctype=multipart/form-data>
	  <input type=file name=file>
	  <input type=text name=name>
	  <input type=submit value=Upload>
	</form>
	'''

@app.route('/test-upload/', methods=['GET', 'POST'])
def upload_test():
	if request.method == 'POST' and request.form['password'] == app.config['PASS']:
		# check if the post request has the file part
		
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		
		file = request.files['file']
		
		# if user does not select file, browser also
		# submit an empty part without filename
		
		if file.filename == '':
			return redirect(request.url)
		
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return "Testcase {} successfully uploaded".format(filename)
			
	return '''
	<!doctype html>
	<title>Upload new File</title>
	<h1>Upload new File</h1>
	<form method=post enctype=multipart/form-data>
	  <input type=file name=file>
	  <input type=password name=password>
	  <input type=submit value=Upload>
	</form>
	'''


if __name__ == '__main__':
    app.run(threaded=True, debug=True)
