 """
ASGI config for the_weather project.

It expo ses the ASGI callable as a module-level variable named ``application``.

For more information on this file,  see
https://docs.djangoprojec t.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_weather.settings')

application = get_asgi_application()
