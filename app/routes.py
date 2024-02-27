from app import app, db
from app.models import K8sInfo
from flask import render_template, request, jsonify
from datetime import datetime
import ipaddress
import sys


@app.route('/feed', methods=['POST'])
def feed():
    if request.method == 'POST':
        try:
            # Get JSON data from the request
            data = request.get_json()
            # Display the received JSON data in the browser
            save_to_db(data)
            return jsonify({'Success': 'OK'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'Unsupported method, POST ONLY'}), 405


def is_date_valid(data, key, datetime_format):
    valid = False
    try:
        datetime.strptime(data[key], datetime_format)
        valid = True
    except ValueError:
        print("Incorrect data format, should be " + datetime_format)
    except Exception:
        print("Exception: " + str(Exception))

    return valid


def if_ip_valid(ip):
    valid = False
    try:
        ipaddress.ip_address(ip)
        valid = True
    except ValueError:
        print("address/netmask is invalid: %s" + ip)
    return valid


def save_to_db(data):
    datetime_fmt = '%Y-%m-%d %H:%M:%S'
    exist = K8sInfo.query.filter_by(url=data['url']).first()
    if exist is not None:
        exist.k8sver = data['k8sver']
        exist.expire_date = data['expire']
        if is_date_valid(data, 'posted', datetime_fmt):
            exist.posted = datetime.strptime(data['posted'], datetime_fmt)
        if if_ip_valid(data['ipaddress']):
            exist.ipaddress = data['ipaddress']
        db.session.commit()
    else:
        k8sinfo = None
        if is_date_valid(data, 'posted', datetime_fmt) and if_ip_valid(data['ipaddress']):
            k8sinfo = K8sInfo(url=data['url'], k8sver=data['k8sver'], ipaddress=data['ipaddress'],
                              expire_date=data['expire'],
                              posted=datetime.strptime(data['posted'], datetime_fmt))
        else:
            k8sinfo = K8sInfo(url=data['url'], k8sver=data['k8sver'], expire_date=data['expire'],
                              ipaddress=data['ipaddress'])

        db.session.add(k8sinfo)
        db.session.commit()


@app.route('/')
def index():
    k8sinfo = K8sInfo.query.all()
    return render_template('basic.html', k8sinfo=k8sinfo, title='Kubernetes Cluster Information')
