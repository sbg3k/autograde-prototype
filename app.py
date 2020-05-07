import otter
import time
import os
import sys
from flask import Flask, render_template, request, json, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
app.config.from_object(os.environ['APP_SETTINGS'])
UPLOAD_FOLDER = json.loads(os.environ['UPLOAD_FOLDER'])

def allowed_file(filename):
	return '.' in filename and \
		   filename.split('.')[-1].lower() == os.environ['ALLOWED_EXTENSION']

def allowed_level(level):
	return level in UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		# check if the post request has the file part
		
		if 'file' not in request.files:
			return "Incomplete Request"
		
		# confirms if the level is Beginner or Intermediate
		if not allowed_level(request.form['level']):
			return "Invalid level"
		
		file = request.files['file']
		print(file)
		
		file.filename = request.form['name'].replace(".", "") + '.py'
		
		# if user does not select file, browser also
		# submit an empty part without filename
		
		if file.filename == '':
			return 'No selected file'
		
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(UPLOAD_FOLDER[request.form['level']][:2], filename))
			if True:
				exec('from ' + filename[:-3] + ' import *', globals())
				print("executing...", "[", request.form['name'], "]")
				with open(os.path.join(UPLOAD_FOLDER[request.form['level']][:2], filename)) as f:
					data = f.read().replace('\n', '')
					print(data)
					print("import" in data)
					if "import" in f.read():
						return jsonify({"name":request.form['name'], "score":1})
				score = {}
				tests = os.listdir(UPLOAD_FOLDER[request.form['level']])
				print(tests)
				for i in tests:
					if allowed_file(i):
						print(i)
						score[i] = str(otter.Notebook(UPLOAD_FOLDER[request.form['level']][2:]).check(i.split('.')[0]))
			
			
				files = []
				for i in score:
					if 'All tests passed!' in score[i]:
						files.append(i)
			
				scores = 0
				for i in files:
					print(i)
					with open(UPLOAD_FOLDER[request.form['level']] + '/' + i) as f:
						a = f.read()
						if '"points":' in a:
							b = a.split('\n')[2]
							c = b.split(":")[1]
							d = c.replace(",", "")
							scores += int(d)
							print(d)
						f.close()
				
				os.remove(os.path.join(UPLOAD_FOLDER[request.form['level']][:2], filename))
				if scores == 0: scores = 1
				return jsonify({"name":request.form['name'], "score":scores})
			
	
	return '''
	<!doctype html>
	<title>Upload new File</title>
	<h1>Upload new File</h1>
	<form method=post enctype=multipart/form-data>
	  <input type=file name=file>
	  <input type=text name=name placeholder="Email">
	  <input type=text name=level placeholder="beginner or intermediate (lowercase)">
	  <input type=submit value=Upload>
	</form>
	'''

@app.route('/test-upload/', methods=['GET', 'POST'])
def upload_test():
	if request.method == 'POST' and request.form['password'] == os.environ['PASS']:
		# check if the post request has the file part
		
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		
		if not allowed_level(request.form['level']):
			return "Invalid level"
		
		file = request.files['file']
		
		# if user does not select file, browser also
		# submit an empty part without filename
		
		if file.filename == '':
			return redirect(request.url)
		
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(UPLOAD_FOLDER[request.form['level']], filename))
			return "Testcase {} successfully uploaded".format(filename)
			
	return '''
	<!doctype html>
	<title>Upload Testcase</title>
	<h1>Upload Testcase</h1>
	<form method=post enctype=multipart/form-data>
	  <input type=file name=file>
	  <input type=text name=level placeholder="beginner or intermediate">
	  <input type=password name=password placeholder="password">
	  <input type=submit value=Upload>
	</form>
	'''
@app.route('/delete/', methods=['GET', 'POST'])
def delete_test():
	if request.method == 'POST' and request.form['password'] == os.environ['PASS']:
		if not allowed_level(request.form['level']):
			return "Invalid level"
		for filename in os.listdir(UPLOAD_FOLDER[request.form['level']]):
			if allowed_file(filename):
				os.remove(os.path.join(UPLOAD_FOLDER[request.form['level']], filename))
		return "Testcases successfully deleted"
			
	return '''
	<!doctype html>
	<title>Delete Yesterday's Testcases</title>
	<h1>Delete Yesterday's Testcases</h1>
	<form method=post enctype=multipart/form-data>
	  <input type=text name=level placeholder="beginner or intermediate">
	  <input type=password name=password placeholder="password">
	  <input type=submit value=Delete>
	</form>
	'''

if __name__ == '__main__':
    app.run(threaded=True, debug=True)
