from flask import Flask, request, render_template, redirect
from subprocess import PIPE, run
import requests
from werkzeug import secure_filename
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html', val="")



@app.route("/uploader", methods=['GET', 'POST'])
def uploader():
    if request.method == "POST":
        if 'file' in request.files:
            f = request.files['file']
            if not f:
                print("file is empty")
                return render_template('index.html', val={"Please insert the file"})
                name = ""
            else:
                f.save(secure_filename(f.filename))
                name = f.filename
            name = f.filename
        else:
            name = ""
        print(name)
        as_dict = request.form.getlist('racedetection')
        print(as_dict)
        res_archer = ""
        res_inspector = ""
        res_tsan = ""
        res = ""
        if not as_dict:
            print("nothing")
            res_archer = callArcher(name)
            res_inspector = callIntellInspector(name)
            res_tsan = callTsan(name)
            res = res_archer.text + res_inspector.text + res_tsan.text
        else:
            for rd in as_dict:
                if(rd == "archer"):
                    print("archer")
                    res_archer = callArcher(name)
                    res += res_archer.text
                    print(res_archer.text)
                if(rd == "intellspector"):
                    print("intellspector")
                    res_inspector = callIntellInspector(name)
                    res += res_inspector.text
                    print(res_inspector.text)
                if(rd == "tsan"):
                    print("tsan")
                    res_tsan = callTsan(name)
                    res += res_tsan.text
                    print(res_tsan.text)
        
        return render_template('index.html', val=res.split('\n'))


def callArcher(name):
    url = 'http://0.0.0.0:5001/upload?type=json'
    files = {'file': open(name, 'rb')}
    r = requests.post(url, files=files)
    return r


def callIntellInspector(name):
    url = 'http://0.0.0.0:5002/upload?type=json'
    files = {'file': open(name, 'rb')}
    r = requests.post(url, files=files)
    return r


def callTsan(name):
    url = 'http://0.0.0.0:5003/upload?type=json'
    files = {'file': open(name, 'rb')}
    r = requests.post(url, files=files)
    return r


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
