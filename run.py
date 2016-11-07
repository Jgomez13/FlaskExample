import os
#os.system("redis-server")
#os.system("python worker.py")
os.system("redis-server && python worker.py && python manage.py runserver")
# python manage.py db init
# python manage.py db migrate
# python manage.py db upgrade
