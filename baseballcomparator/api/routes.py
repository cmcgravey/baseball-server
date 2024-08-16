import flask
import baseballcomparator

@baseballcomparator.app.route('/')
def show_routes():
    config = baseballcomparator.model.load_config()
    conn = baseballcomparator.model.connect(config)

    curs = conn.cursor()

    curs.execute(
        "SELECT * FROM players;"
    )

    record = curs.fetchone()
    return flask.jsonify(**record), 200