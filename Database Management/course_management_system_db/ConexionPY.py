import os

from dash import Dash, html, dcc
import plotly.express as px
import psycopg2
try:
    connection = psycopg2.connect(host = os.environ.get('DB_HOST', 'localhost'),
                                  user = os.environ.get('DB_USER', 'postgres'),
                                  password = os.environ['DB_PASSWORD'],
                                  database = os.environ.get('DB_NAME', 'Proyecto'),
                                  port = os.environ.get('DB_PORT', '5433'))
    print('Conexión exitosa')
    cursor = connection.cursor()
    cursor.execute('select * from materia;')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print('Conexión finalizada')