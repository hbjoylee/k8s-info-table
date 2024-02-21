from app import app, db
from app.models import K8sInfo
from flask import render_template, request, jsonify


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


def save_to_db(data):
    exist = K8sInfo.query.filter_by(url=data['url']).first()
    if exist is not None:
        exist.k8sver = data['k8sver']
        exist.expire_date = data['expire']
        db.session.commit()
    else:
        k8sinfo = K8sInfo(url=data['url'], k8sver=data['k8sver'], expire_date=data['expire'])
        db.session.add(k8sinfo)
        db.session.commit()


@app.route('/')
def index():
    k8sinfo = K8sInfo.query.all()
    return render_template('basic.html', k8sinfo=k8sinfo, title='Kubernetes Cluster Information')
