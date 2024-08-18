import flask
import psycopg2
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

    curs = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    curs.execute(
        "SELECT * FROM players;"
    )

    record = curs.fetchone()
    print(record)
    return flask.jsonify(**record), 200