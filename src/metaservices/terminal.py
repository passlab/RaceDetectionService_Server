from flask import Flask, request, render_template, jsonify
from subprocess import PIPE, run
import requests
import os
import time
from werkzeug import secure_filename
UPLOAD_FOLDER = '/tmp/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html', val="")


# Benchmark API


@app.route("/benchmark", methods=['GET', 'POST'])
def benchmark():
    if request.method == "POST":
        result = ""
        content = request.get_json(force=True)
        tstart = time.time()
        for service in content["list"]:
            if (service == "archer"):
                print("archer")
                result_archer = archerBenchmark()
                result += result_archer.text
            if (service == "intellspector"):
                print("intellspector")
                result_intel = intellspectorBenchmark()
                result += result_intel.text
            if (service == "tsan"):
                print("tsan")
                result_tsan = tsanBenchmark()
                result += result_tsan.text
            if (service == "romp"):
                print("romp")
                result_romp = rompBenchmark()
                result += result_romp.text
        tend = time.time()
        print(tend - tstart)
        print(result)
        return jsonify(result)


@app.route("/uploader", methods=['GET', 'POST'])
def uploader():
    if request.method == "POST":
        if 'file' in request.files:
            f = request.files['file']
            if not f:
                print("file is empty")
                return render_template('index.html',
                                       val={"Please insert the file"})
                name = ""
            else:
                # f.save(secure_filename(f.filename))
                filename = secure_filename(f.filename)
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                name = filename
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
            res_romp = callRomp(name)
            res = res_archer.text + res_inspector.text + res_tsan.text + res_romp.text
        else:
            for rd in as_dict:
                if (rd == "archer"):
                    print("archer")
                    res_archer = callArcher(name)
                    res += res_archer.text
                    print(res_archer.text)
                if (rd == "intellspector"):
                    print("intellspector")
                    res_inspector = callIntellInspector(name)
                    res += res_inspector.text
                    print(res_inspector.text)
                if (rd == "tsan"):
                    print("tsan")
                    res_tsan = callTsan(name)
                    res += res_tsan.text
                    print(res_tsan.text)
                if (rd == "romp"):
                    print("romp")
                    res_romp = callRomp(name)
                    res += res_romp.text
                    print(res_romp.text)

        return render_template('index.html', val=res.split('\n'))


def callArcher(name):
    url = 'http://0.0.0.0:5001/upload?type=json'
    files = {
        'file': open(os.path.join(app.config['UPLOAD_FOLDER'], name), 'rb')
    }
    r = requests.post(url, files=files)
    return r


def callIntellInspector(name):
    url = 'http://0.0.0.0:5002/upload?type=json'
    files = {
        'file': open(os.path.join(app.config['UPLOAD_FOLDER'], name), 'rb')
    }
    r = requests.post(url, files=files)
    return r


def callTsan(name):
    url = 'http://0.0.0.0:5003/upload?type=json'
    files = {
        'file': open(os.path.join(app.config['UPLOAD_FOLDER'], name), 'rb')
    }
    r = requests.post(url, files=files)
    return r


def callRomp(name):
    url = 'http://0.0.0.0:5004/upload?type=json'
    files = {
        'file': open(os.path.join(app.config['UPLOAD_FOLDER'], name), 'rb')
    }
    r = requests.post(url, files=files)
    return r


def archerBenchmark():
    url = 'http://0.0.0.0:5001/benchmark?type=json'
    r = requests.post(url)
    return r


def intellspectorBenchmark():
    url = 'http://0.0.0.0:5002/benchmark?type=json'
    r = requests.post(url)
    return r


def tsanBenchmark():
    url = 'http://0.0.0.0:5003/benchmark?type=json'
    r = requests.post(url)
    return r


def rompBenchmark():
    url = 'http://0.0.0.0:5004/benchmark?type=json'
    r = requests.post(url)
    return r


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
