from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa

from app import response, app, db
from flask import request
import math
from flask import jsonify, make_response

# get all
def index():
    try:
        dosen = Dosen.query.all()
        data = formatarray(dosen)
        return response.success(data, 'success')
    except Exception as e:
        print('failed to show all data dosen', e)

def formatarray(datas):
    array = []

    for i in datas:
        array.append(singleObject(i))
    return array

def singleObject(data):
    data = {
        'id': data.id,
        'nidn': data.nidn,
        'name': data.name,
        'phone': data.phone,
        'alamat': data.alamat,
    }

    return data

# get by id
def detail(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        mahasiswa = Mahasiswa.query.filter((Mahasiswa.dosen_satu == id) | (Mahasiswa.dosen_dua == id))
        
        if not dosen:
            return response.badRequest([], 'Dosen not found')
        
        datamahasiswa = formatMahasiswa(mahasiswa)
        
        data = singleDetailMahasiswa(dosen, datamahasiswa)
        return response.success(data, 'success')

    except Exception as e:
        print('failed to detail data dosen', e)

def singleDetailMahasiswa(dosen, mahasiswa):
    data = {
        'id': dosen.id,
        'nidn': dosen.nidn,
        'name': dosen.name,
        'phone': dosen.phone,
        'alamat': dosen.alamat,
        'mahasiswa': mahasiswa,
    }
    return data

def formatMahasiswa(data):
    array = []

    for i in data:
        array.append(singleMahasiswa(i))
    return array

def singleMahasiswa(data):
    data = {
        'id': data.id,
        'nidn': data.nidn,
        'name': data.name,
        'phone': data.phone,
    }
    return data

# add
def save():
    try:
        nidn = request.form.get('nidn')
        name = request.form.get('name')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')

        dosen = Dosen(nidn=nidn, name=name, phone=phone, alamat=alamat)
        db.session.add(dosen)
        db.session.commit()

        return response.success([], 'success add dosen')
    
    except Exception as e:
        print('failed to add data dosen', e)

# update
def update(id):
    try:
        nidn = request.form.get('nidn')
        name = request.form.get('name')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')

        input = [
            {
                'nidn': nidn,
                'name': name,
                'phone': phone,
                'alamat': alamat,
            }
        ]

        dosen = Dosen.query.filter_by(id=id).first()

        dosen.nidn = nidn
        dosen.name = name
        dosen.phone = phone
        dosen.alamat = alamat

        db.session.commit()

        return response.success(input, 'success update dosen data')

    except Exception as e:
        print('failed to update data dosen', e)

# delete
def delete(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()

        if not dosen:
            return response.badRequest([], 'dosen not found')
        
        db.session.delete(dosen)
        db.session.commit()

        return response.success([], 'success delete dosen data')
        

    except Exception as e:
        print('failed to delete data dosen', e)

# pagination
def get_pagination(clss, start, limit):
    # get all data 
    results = clss.query.all()
    # change format
    data = formatarray(results)
    # count all data
    count = len(data)
    total_page = math.ceil(count / limit)

    result_pagination = clss.query.paginate(page=start, error_out=False, max_per_page=limit)

    obj = {}

    if total_page < start:
        obj['success'] = False
        obj['message'] = 'page is off limit'
        return obj
    else:
        obj['success'] = True
        obj['current_page'] = start
        obj['per_page'] = limit
        obj['total'] = count
        obj['total_page'] = total_page

        obj['results'] = formatarray(result_pagination)
        return obj
    

# paging function
def paginate():
    start = request.args.get('start')
    limit = request.args.get('limit')

    try:
        if start == None or limit == None:
            return jsonify(get_pagination(
                Dosen,
                start=request.args.get('start', 1),
                limit=request.args.get('limit', 3),
            ))
        else:
            return jsonify(get_pagination(
                Dosen,
                start=int(start),
                limit=int(limit),
            ))
    
    except Exception as e:
        print('failed to paginate', e)


