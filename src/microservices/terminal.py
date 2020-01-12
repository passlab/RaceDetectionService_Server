from flask import Flask, request, render_template
from subprocess import PIPE, run
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        arr = task_content.split()
        result = run(arr, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        if(result.returncode == 1):
            str = result.stderr
        else:
            str = result.stdout
        print(str)
        return render_template('index.html', val=str.split('\n'))
    else:
        return render_template('index.html', val="")


if __name__ == "__main__":
    app.run(debug=True)
