from flask import Flask
from src.routes.user import user_bp

app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)