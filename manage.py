# -*- encoding=UTF-8 -*-


from nowstgram import app, db
from flask_script import Manager
from nowstgram.models import User

manager = Manager(app)


@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0, 100):
        db.session.add(User('User' + str(i), 'a' + str(i)))
    db.session.commit()


if __name__ == '__main_':
    manager.run()
