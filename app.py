from flask import Flask, render_template
from flask_restx import Api
from resources import api as data_api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app, version='1.0', title='API de Dados', description='Uma API para acessar dados do banco Oracle')

CORS(app)

@app.route('/')
def index():
    return render_template('./index.html')

api.add_namespace(data_api, path='/api')

if __name__ == '__main__':
    app.run(debug=True)
