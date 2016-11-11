import os
from sys import executable
from subprocess import Popen

Popen(["nohup","redis-server"])
Popen(["python","worker.py"])



os.system("python manage.py runserver")
# python manage.py db init
# python manage.py db migrate
# python manage.py db upgrade
