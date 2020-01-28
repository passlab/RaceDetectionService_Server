from flask import Flask, request, render_template, redirect
from subprocess import PIPE, run
from werkzeug import secure_filename
import Flask_Archer
import Flask_IntelInspector
import Flask_TSan
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    # if request.method == 'POST':
    #     task_content = request.form['content']
    #     arr = task_content.split()
    #     result = run(arr, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    #     if(result.returncode == 1):
    #         str = result.stderr
    #     else:
    #         str = result.stdout
    #     print(str)
    #     return render_template('index.html', val=str.split('\n'))
    # else:
    return render_template('index.html', val="")



@app.route("/uploader", methods=['GET', 'POST'])
def uploader():
    if request.method == "POST":
        f = request.files['file']
        if not f:
            print("file is empty")
        else:
            f.save(secure_filename(f.filename))
        print(f.filename)
        as_dict = request.form.getlist('racedetection')
        print(as_dict)
        str1 = ""
        str2 = ""
        str3 = ""
        if not as_dict:
            str1 = Flask_Archer.archer(f.filename)
            str2 = Flask_IntelInspector.intellinspector(f.filename)
            str3 = Flask_TSan.tsan(f.filename)
        else:
            for rd in as_dict:
                if(rd == "archer"):
                    str1 = Flask_Archer.archer(f.filename)
                if(rd == "intellspector"):
                    str2 = Flask_IntelInspector.intellinspector(f.filename)
                if(rd == "tsan"):
                    str3 = Flask_TSan.tsan(f.filename)
        res = str1 + str2 + str3
        return render_template('index.html', val=res.split('\n'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
