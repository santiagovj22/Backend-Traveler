import logging
from flask_restx import Api
from flask import Flask
from flask_cors import CORS
from settings import DB_URI

from controllers.tours_controller import init_tours_controller

# Init flask app
app = Flask(__name__)

# Configuration from .env
app.config['MONGO_URI'] = DB_URI

# Handling Logs
LOG_FILENAME = './logs/app.log'
logging.basicConfig(level=logging.DEBUG,
                    filename=LOG_FILENAME,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app.logger.debug('Server on port..')

# Configure api
api = Api(app, validate = True,
               title = 'Traveler API',
               description = 'Api Using flask-restx models Layer')

# Configure cors
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})

# Configure controller
init_tours_controller(app, api)

# Launch app local mode
if __name__ == "__main__":
    app.run(debug=True)
