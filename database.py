from app import db #? import db from our App instance

# DATABASE MODEL
#? this class will create db model in sqlalchemy for Sqlite database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username  = db.Column(db.String(80), unique=True, nullable=False) 
    email =  db.Column(db.String(80), unique=True, nullable=False) 
    password = db.Column(db.String(80)) 
    def __repr__(self):
        return f'<User {self.username}>'
    

