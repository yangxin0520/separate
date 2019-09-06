from gather import create_app
from gather.utils.exts import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


# 创建flask应用对象
app = create_app("develop")

app.template_folder = 'static/html'
from flask import request, render_template, jsonify
@app.route('/test_post', methods=['POST', 'GET'])
def test_post():
    if request.method  == 'GET':
        return render_template('test_post.html')
    elif request.method == 'POST' :
       return jsonify('ok')

manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()
