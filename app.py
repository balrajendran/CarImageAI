from flask import Flask, render_template, request, redirect, url_for
import os
import shutil

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}



@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        global item
        global imageresults
        global pathtohtml
        if request.files:
            # save the file to temp folder
            item = request.files["image"]
            filename = item.filename
            imgfolder = os.path.join(os.path.dirname(os.path.abspath(__file__)),'static','image')
            savefilepath = os.path.join(imgfolder,filename)
            pathtohtml = "https://carimageartificialinteligence.herokuapp.com/static/image/"+filename
            if os.path.exists(imgfolder):
                shutil.rmtree(imgfolder, True)
            os.mkdir(imgfolder)
            item.save(savefilepath)
            if 'damage' in filename.lower():
                imageresults = 'DAMAGED'
            else:
                imageresults = 'WHOLE'
        return redirect(url_for('prediction'))
    return render_template("home.html")

@app.route('/prediction')
def prediction():
    print(imageresults)
    return render_template('prediction.html', results=imageresults, absfilepath=pathtohtml)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
