import os
from flask import Flask,render_template,request,send_file,redirect,url_for
from werkzeug.utils import secure_filename
app=Flask(__name__)


upload_folder="upload/"
if not os.path.exists(upload_folder):
    os.mkdir(upload_folder)

app.config['UPLOAD_FOLDER']= upload_folder



@app.route("/index")
def index():
    return render_template('upload_file.html')

@app.route('/upload', methods=['GET','POST'])
def upload_file():
    if request.method=='POST':
        file=request.files['file']   
        file_name=request.args.get('file')    
        print(file_name) 
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        return render_template('download_link.html',name=file.filename)
    # return redirect(url_for('index'))



# @app.route('/download/<filename>')
# def download_link(filename):

    

if __name__=='__main__':
    app.run(debug=True)








