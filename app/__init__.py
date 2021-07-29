from flask import Flask, render_template, request
from app.forms import ImageForm
import subprocess

app = Flask(__name__)
app.config.from_object("app.config.Config")

cvetool_path = "/home/intern1/Projects/mirantis/airship/docker-image-scanner/venv/bin/cvetool"

@app.route("/", methods=["GET", "POST"])
def scan():
    scan_result = ""
    form = ImageForm()
    if request.method == "POST":
      if form.validate_on_submit():
          image = request.form["image"]
          processors = request.form["processors"]
  #        scan_result = subprocess.check_output("{} --path ~/nvd.db --representers HumanMirrored {}".format(cvetool_path, image), stderr=subprocess.STDOUT, shell=True, universal_newlines=True).replace('\n', '<br>')
          scan_result = subprocess.check_output("{} --path ~/nvd.db --representers DetailedHTML {} --processors {}".format(cvetool_path, image, processors), stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
    return render_template("results.html", form=form, message=scan_result)
