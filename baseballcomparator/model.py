import flask
import psycopg2
from configparser import ConfigParser
from psycopg2 import extras

def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            cursor = cursor_factory(conn)
            return cursor
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def cursor_factory(conn):
    """Allow for cursor to return entries as dictionaries."""
    curs = conn.cursor(cursor_factory=extras.RealDictCursor)