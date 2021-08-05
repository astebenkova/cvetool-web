from flask import Flask, render_template, request
from app.forms import ImageForm
import subprocess

app = Flask(__name__)
app.config.from_object("app.config.Config")


@app.route("/", methods=["GET", "POST"])
def scan():
    scan_result = ""
    error = ""
    form = ImageForm()
    if request.method == "POST":
        if form.validate_on_submit():
            image = request.form["image"]
            processors = str(form.processors.data).replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
            representers = request.form["representers"]
            try:
                scan_result = subprocess.check_output("cvetool --path /etc/cvetool/nvd.db --representers {} --processors {} {}"
                                                      .format(representers, processors, image),
                                                      stderr=subprocess.STDOUT, shell=True,
                                                      universal_newlines=True)
                if representers == "HumanMirrored":
                    scan_result = scan_result.replace('\n', '<br>')
            except subprocess.CalledProcessError:
                error = "Ooops, seems your image is incorrect or no processors were specified."
        else:
            error = str(form.errors)

    return render_template("results.html", form=form, message=scan_result, error=error)
