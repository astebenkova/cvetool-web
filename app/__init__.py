from flask import Flask, render_template, request
from app.forms import ImageForm
import subprocess

app = Flask(__name__)
app.config.from_object("app.config.Config")

cvetool_path = "/home/arina/Projects/mirantis/airship/docker-image-scanner/venv/bin/cvetool"


@app.route("/", methods=["GET", "POST"])
def scan():
    scan_result = ""
    form = ImageForm()
    if request.method == "POST":
        if form.validate_on_submit():
            image = request.form["image"]
            processors = str(form.processors.data).replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
            representers = request.form["representers"]
            scan_result = subprocess.check_output("{} --path ~/nvd.db --representers {} --processors {} {}"
                                                  .format(cvetool_path, representers, processors, image),
                                                  stderr=subprocess.STDOUT, shell=True,
                                                  universal_newlines=True).replace('\n', '<br>')
        else:
            scan_result = str(form.errors)
    return render_template("results.html", form=form, message=scan_result)
