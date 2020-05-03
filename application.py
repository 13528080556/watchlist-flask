
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager


class Application(Flask):

    def __init__(self,
                 import_name,
                 static_url_path=None,
                 static_folder='static',
                 static_host=None,
                 host_matching=False,
                 subdomain_matching=False,
                 template_folder="templates",
                 instance_path=None,
                 instance_relative_config=False,
                 root_path=None):
        super().__init__(import_name, static_url_path, static_folder, static_host, host_matching,
                         subdomain_matching, template_folder, instance_path, instance_relative_config, root_path)
        self.config.from_pyfile('config/base_setting.py')
        if 'ops_config' in os.environ:
            self.config.from_pyfile('config/{}'.format(os.environ['ops_config']))
        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__)
manager = Manager(app)
