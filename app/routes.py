from app import app, response
from app.controller import DosenController
from app.controller import UserController
from flask import request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


@app.route('/')
def index():
    return "Hello Flask"

# example route protect with jwt
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return response.success(current_user, 'sukses')

@app.route('/createadmin', methods=['POST'])
def createadmins():
    return UserController.createAdmin()

@app.route('/login', methods={'POST'})
def login():
    return UserController.login()
    
@app.route('/dosen', methods=['GET', 'POST'])
@jwt_required()
def dosens():
    if request.method == 'GET':
        return DosenController.index()
    if request.method == 'POST':
        return DosenController.save()

@app.route('/dosen/<id>', methods=['GET', 'PUT', 'DELETE'])
def dosensDetail(id):
    if request.method == 'GET':
        return DosenController.detail(id)
    if request.method == 'PUT':
        return DosenController.update(id)
    if request.method == 'DELETE':
        return DosenController.delete(id)
    
@app.route('/upload-file', methods=['POST'])
def uploads():
    if request.method == 'POST':
        return UserController.upload()

# pagination route
@app.route('/api/dosen/page', methods=['GET'])
def pagination():
    return DosenController.paginate()