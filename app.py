from gather import create_app
from gather.utils.exts import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


# 创建flask应用对象
app = create_app("develop")
manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()
