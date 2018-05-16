from flask import Flask
from db import create_execute

app = Flask(__name__)

execute = create_execute('dbname=grocerydb')

import api

if __name__ == '__main__':
    app.run()
