from os import environ

from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from routes import routes


app = Flask(__name__)
app.config.from_object(environ.get('CONFIG_OBJECT'))

migrate = Migrate(app, db)
api = Api(app)

# Create initial db instance
with app.app_context():
    db.init_app(app)

# Add routes
[api.add_resource(*route) for route in routes]

if __name__ == '__main__':
    app.run()
