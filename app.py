
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


#Configuramos base de datos
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:123@localhost:5432/db_finkargo'


db= SQLAlchemy(app)


db.init_app(app)


from views import *



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=4000)