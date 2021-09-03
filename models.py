from app import db



class Nationality(db.Model):
    __tablename__ ='finkargo_nationality'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False, unique=True)


class User(db.Model):

    __tablename__ = 'finkargo_user'

    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(80),nullable=False)
    nationality=db.column(db.Integer,db.ForeignKey('finkargo_nationality.id'))

    def __init__(self,name,nationality):
        self.name=name
        self.nationality=nationality


