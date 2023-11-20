from app.model.user import User
from app.model.gambar import Gambar
from app import response, app, db, uploadconfig
from flask import request
from flask_jwt_extended import *
import datetime
import os
import uuid
from werkzeug.utils import secure_filename

# upload file
def upload():
    try:
        title = request.form.get('title')

        # if there is no file to upload
        if 'file' not in request.files:
            return response.badRequest([], 'file is not available')
        
        file = request.files['file']

        # if filename is empty
        if file.filename == '':
            return response.badRequest([], 'filename is empty')
        
        if file and uploadconfig.allowed_files(file.filename):
            uid = uuid.uuid4()
            filename = secure_filename(file.filename)
            renamefile = 'Flask-'+str(uid)+filename # rename file with secure filename and uuid

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], renamefile)) #save to upload path

            uploads = Gambar(title=title, pathname=renamefile)

            db.session.add(uploads)
            db.session.commit()

            return response.success({
                'title': title,
                'pathname': renamefile,
            }, 'success upload file')
        
        else :
            return response.badRequest([], 'file is not allowed')
        
    except Exception as e:
        print('failed to upload file', e)

# add
def createAdmin():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        level = 1

        users = User(name=name, email=email, level=level)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.success([], 'success add admin')
    
    except Exception as e:
        print('failed to add data admin', e)

def singleObject(data):
    data = {
        'id': data.id,
        'name': data.name,
        'email': data.email,
        'level': data.level,
    }

    return data

def login():
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if not user:
            return response.badRequest([], 'user not found')
        
        if not user.checkPassword(password):
            return response.badRequest([], 'wrong password')
        
        data = singleObject(user)

        expires = datetime.timedelta(days=7)
        expires_refresh = datetime.timedelta(days=10)

        access_token = create_access_token(data, fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)

        return response.success({
            'data': data,
            'access_token': access_token,
            'refresh_token': refresh_token
        }, 'login success')

    except Exception as e:
        print('failed to do login', e)