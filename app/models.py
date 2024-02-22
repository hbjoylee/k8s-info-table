from app import db
from datetime import datetime


class K8sInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(64), index=True)
    k8sver = db.Column(db.String(15), index=False)
    expire_date = db.Column(db.String(120), index=False)
    posted = db.Column(db.DateTime, default=datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0))

    def __repr__(self):
        return 'URL: {}'.format(self.url)

    def to_dict(self):
        return {
            'url': self.url,
            'k8sver': self.k8sver,
            'expire_date': self.expire_date,
            'posted': self.posted
        }
