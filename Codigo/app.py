from flask import Flask
from routes.home import home_bp
import os

app = Flask(__name__)

app.register_blueprint(home_bp)

if __name__ == "__main__":
    port = int(os.getenv('PORT'), '5000')
    app.run(host='0.0.0.0', port=port)