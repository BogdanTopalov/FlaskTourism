from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from constants import CONFIG
from db import db
from routes import routes

app = Flask(__name__)
app.config.from_object(CONFIG['CONFIG_OBJECT'])

migrate = Migrate(app, db)
api = Api(app)
CORS(app)

# Create initial db instance
with app.app_context():
    db.init_app(app)

# Add routes
[api.add_resource(*route) for route in routes]

if __name__ == '__main__':
    app.run()
