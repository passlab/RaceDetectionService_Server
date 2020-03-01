from flask import Flask, request, render_template, redirect, Response
from subprocess import PIPE, run
import flask
import os
import subprocess
import time
from werkzeug import secure_filename
UPLOAD_FOLDER = '/tmp/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def api_root():
    return render_template('index.html', val="")


# benchmark API for intellInspector
@app.route('/benchmark', methods=['POST'])
def benchmark():
    print("request received")

    # Running first command
    cmd = "sh test.sh"
    tstart = time.time()
    result = run(cmd.split(), stdout=PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    tend = time.time()
    benchmarkTime = tend - tstart
    if(result.returncode == 1):
        str = result.stderr
    else:
        str = result.stdout
    print(str)

    # Running second command

    cmd = "sh test.sh"
    tstart = time.time()
    result = run(cmd.split(), stdout=PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    tend = time.time()
    parserTime = tend - tstart
    if(result.returncode == 1):
        str = result.stderr
    else:
        str = result.stdout
    print(str)
    with open(os.path.join(app.config['UPLOAD_FOLDER'], "intellbenchmark.txt"), "w") as intellfile:
        print("Benchmark time: ", benchmarkTime, file=intellfile)
        print("Parser time: ", parserTime, file=intellfile)
    return flask.make_response(
                flask.jsonify({'res': str}), 200)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    name = ""
    if request.method == "POST":
        if 'file' in request.files:
            f = request.files['file']
            if not f:
                print("file is empty")
                name = ""
            else:
                # f.save(secure_filename(f.filename))
                filename = secure_filename(f.filename)
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                name = filename
        else:
            name = ""
        print(name)
        # cmd_list = ["pwd", "ls -l " + os.path.join(app.config['UPLOAD_FOLDER'], name)]
        cmd_list = ["export OMP_NUM_THREADS=5", "gcc -fopenmp " + os.path.join(app.config['UPLOAD_FOLDER'], name) + " -o " + os.path.join(app.config['UPLOAD_FOLDER'], "myApp"), "inspxe-cl -collect ti3 -result-dir Result  " + os.path.join(app.config['UPLOAD_FOLDER'], "myApp"), "inspxe-cl -create-suppression-file ./mySupFile -result-dir Result", "inspxe-cl -report problems -result-dir Result -report-output Result/myThreadingReport.txt"]
        for cmd in cmd_list:
            arr = cmd.split()
        
            with open(os.path.join(app.config['UPLOAD_FOLDER'], "inspectoroutput.txt"), "w") as file:
                run(arr, stdout=file, stderr=file, universal_newlines=True)

        res_path = "python3 inspector.py " + os.path.join(app.config['UPLOAD_FOLDER'], "inspectoroutput.txt")
        result = run(res_path.split(), stdout=PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        if(result.returncode == 1):
            str = result.stderr
        else:
            str = result.stdout
        print(str)
        if request.args.get('type') == 'json':
            return flask.make_response(
                    flask.jsonify({'res': str}), 200)
        else:
            return render_template('index.html', val=str.split('\n'))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
