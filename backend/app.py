from flask import Flask, render_template
from routes import api

def create_app():
    app = Flask(__name__, template_folder='frontend/templates', static_folder='frontend/static')
    app.register_blueprint(api)
    return app

if __name__ == '__main__':
    app = create_app()
    
    @app.route('/')
    def index():
        return render_template('main.html')

    app.run(debug=True)
