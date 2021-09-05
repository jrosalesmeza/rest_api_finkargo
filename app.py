from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from  flask_httpauth import HTTPBasicAuth


            
app = Flask(__name__)


auth = HTTPBasicAuth()


#Configuramos base de datos
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:123@localhost:5432/db_finkargo'


from views import *



if __name__ == '__main__':
    app.run(debug=True, port=4000)
    