from app import db
from datetime import datetime


class Gambar(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    pathname = db.Column(db.String(150), nullable=False)


    def __repr__(self):
        return '<Gambar {}>'.format(self.name)