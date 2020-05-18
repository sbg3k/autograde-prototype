import otter
import time
import os
import inspect
import sys
from flask import Flask, render_template, request, json, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
app.config.from_object(os.environ['APP_SETTINGS'])
UPLOAD_FOLDER = os.environ['UPLOAD_FOLDER']

def allowed_file(filename):
	return '.' in filename and \
		   filename.split('.')[-1].lower() == os.environ['ALLOWED_EXTENSION']
	

@app.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		# check if the post request has the file part
		
		if 'file' not in request.files:
			return "Incomplete Request"
		
		file = request.files['file']
		print(file)
		
		file.filename = request.form['name'].replace(".", "") + '.py'
		
		# if user does not select file, browser also
		# submit an empty part without filename
		
		if file.filename == '':
			return 'No selected file'
		scores = 1
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(UPLOAD_FOLDER[:2], filename))
			try:
				nen = globals()
				exec('from ' + filename[:-3] + ' import *', globals())
				print("executing...", "[", request.form['name'], "]")
				nan = globals()
				print({i for i in nan if i not in nen})
				score = {}
				tests = os.listdir(UPLOAD_FOLDER)
				for i in tests:
					if allowed_file(i):
						score[i] = str(otter.Notebook(UPLOAD_FOLDER[2:]).check(i.split('.')[0]))
			
			
				files = []
				for i in score:
					print(i)
					print(score[i])
					if 'All tests passed!' in score[i]:
						files.append(i)
			
				scores = 0
				for i in files:
					print(i)
					with open(UPLOAD_FOLDER + '/' + i) as f:
						a = f.read()
						if '"points":' in a:
							b = a.split('\n')[2]
							c = b.split(":")[1]
							d = c.replace(",", "")
							scores += int(d)
							print(d)
				
				

				exec('import ' + filename[:-3] + ' as ma', globals())
				for name, data in inspect.getmembers(ma):
					if name.startswith('_'):
						continue
					if name in globals():
						print(name, ['deleting...'])
						del globals()[name]
				if ma in globals(): del globals()[ma]
				for i in nan:
					if i not in nen:
						print(i, ["deleting..."])
						del globals()[i]
				with open(os.path.join(UPLOAD_FOLDER[:2], filename), "r") as f:
					print(f.read())
					f.close()
				os.remove(os.path.join(UPLOAD_FOLDER[:2], filename))
				if scores == 0: scores = 1
				return jsonify({"name":request.form['name'], "score":scores})
			except Exception as e:
				exec('import ' + filename[:-3] + ' as ma', globals())
				for name, data in inspect.getmembers(ma):
					if name.startswith('_'):
						continue
					if name in globals():
						print(name, ['deleting...'])
						del globals()[name]
				if ma in globals(): del globals()[ma]
				for i in nan:
					if i not in nen:
						print(i, ["deleting..."])
						del globals()[i]
				with open(os.path.join(UPLOAD_FOLDER[:2], filename), "r") as f:
					print(f.read())
					f.close()
				os.remove(os.path.join(UPLOAD_FOLDER[:2], filename))
				print(e)
				scores = 1
				return jsonify({"name":request.form['name'], "score":scores})
				return "Oops! an error occured."
	
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

if __name__ == '__main__':
    app.run(threaded=True, debug=True)
