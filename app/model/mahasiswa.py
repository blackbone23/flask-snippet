from app import db
from datetime import datetime
from app.model.dosen import Dosen


class Mahasiswa(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nidn = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    alamat = db.Column(db.String(250), nullable=False)
    dosen_satu = db.Column(db.BigInteger, db.ForeignKey(Dosen.id, ondelete='CASCADE')) # when use cascade, if you delete 1 dosen then mahasiswa that related to dosen will be deleted
    dosen_dua = db.Column(db.BigInteger, db.ForeignKey(Dosen.id, ondelete='CASCADE')) # when use cascade, if you delete 1 dosen then mahasiswa that related to dosen will be deleted


    def __repr__(self):
        return '<Mahasiswa {}>'.format(self.name)