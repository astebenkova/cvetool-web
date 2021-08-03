import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SESSION_SECRET_KEY") or "dummy-session-secret-key"
