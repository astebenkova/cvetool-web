from app import app
from flask.cli import FlaskGroup
from flask_bootstrap import Bootstrap

cli = FlaskGroup(app)
Bootstrap(app)

if __name__ == "__main__":
    cli(debug=True)
