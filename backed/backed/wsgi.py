# """
# WSGI config for backed project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
# """

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backed.settings')

# application = get_wsgi_application()

import os
import sys
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# ✅ Add this line to include the outer 'backed/' directory in sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backed.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(os.path.dirname(__file__), 'staticfiles'))

