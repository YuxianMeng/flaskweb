from flask_script import Manager
from flask_migrate import MigrateCommand
from exampleapp.wsgi import app, db


manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def gvserver(ip="0.0.0.0", port=5000):
    from gevent.pywsgi import WSGIServer
    print("gevent server staring on %s %s" % (ip, port))
    WSGIServer((ip, int(port)), app).serve_forever()


@manager.shell
def make_shell_context():
    import flaskweb
    return dict(app=app, db=db, webapp=flaskweb)


if __name__ == "__main__":
    manager.run()