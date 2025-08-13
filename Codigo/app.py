from flask import Flask
from routes.home import home_bp
from routes.login import login_bp
import os

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(login_bp)


if __name__ == "__main__":
    port = int(os.getenv('PORT') or '5000')
    app.debug = os.getenv('FLASK_DEBUG') or True
    app.run(host='0.0.0.0', port=port)