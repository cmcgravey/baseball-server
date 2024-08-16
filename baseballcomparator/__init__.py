import flask

app = flask.Flask(__name__)

app.config.from_object('baseballcomparator.config')

app.config.from_envvar('BASEBALLCOMPARATOR_SETTINGS', silent=True)

import baseballcomparator.api
import baseballcomparator.model