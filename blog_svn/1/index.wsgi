# import sys
# import os.path
  
# os.environ['DJANGO_SETTINGS_MODULE'] = 'my_blog.settings'
# sys.path.append(os.path.join(os.path.dirname(__file__), 'my_blog'))
  
# root = os.path.dirname(__file__)
# sys.path.insert(0, os.path.join(root, 'site-packages'))
# application = sae.create_wsgi_app(wsgi.application)


import sae
from my_blog import wsgi
application = sae.create_wsgi_app(wsgi.application)
