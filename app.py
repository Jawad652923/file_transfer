import os
from flask import Flask,render_template,request,send_from_directory
from werkzeug.utils import secure_filename
app=Flask(__name__)


upload_folder="upload/"
if not os.path.exists(upload_folder):
    os.mkdir(upload_folder)

app.config['UPLOAD_FOLDER']= upload_folder



@app.route("/")
def index():
    return render_template('upload_file.html')

@app.route('/upload', methods=['GET','POST'])
def upload_file():
    if request.method=='POST':
        file=request.files['file']        
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        return f'file uploaded successfully'

@app.route('/download_link/<path:filename>', methods=['GET', 'POST'])
def download_link(filename):
   permitted_directory='/path/to/directoy/'
   return send_from_directory(directory=permitted_directory, filename=filename,as_attachment=True,cache_timeout=0)

if __name__=='__main__':
    app.run(debug=True)
