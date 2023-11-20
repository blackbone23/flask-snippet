from app import db
from datetime import datetime


class Dosen(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nidn = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    alamat = db.Column(db.String(250), nullable=False)


    def __repr__(self):
        return '<Dosen {}>'.format(self.name)