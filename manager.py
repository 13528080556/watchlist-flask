
from flask_script import Server

from application import manager, app
import www

manager.add_command('runserver', Server(host='0.0.0.0', port=app.config['PORT']))


def main():
    manager.run()


if __name__ == '__main__':
    main()
