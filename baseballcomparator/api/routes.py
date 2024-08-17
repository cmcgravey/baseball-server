import flask
import baseballcomparator

@baseballcomparator.app.route('/')
def show_routes():
    context = {
        "/players/": "retrieve one player record"
    }
    return flask.jsonify(**context), 200

@baseballcomparator.app.route('/players/')
def fetch_one_player():
    config = baseballcomparator.model.load_config()
    conn = baseballcomparator.model.connect(config)

    curs = conn.cursor()

    curs.execute(
        "SELECT * FROM players;"
    )

    record = curs.fetchone()
    print(record)
    return flask.jsonify(**record), 200