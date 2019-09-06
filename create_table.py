from gather import create_app
from gather.utils.exts import db


app = create_app("develop")
with app.app_context():
    db.create_all()