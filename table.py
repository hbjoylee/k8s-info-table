from app import app, db
from app.models import K8sInfo


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, K8sInfo=K8sInfo)
