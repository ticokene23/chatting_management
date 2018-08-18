from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import personal.channels.routing as personal
import chat.channels.routing as chat
import itertools
import logging

# logging.warning(personal.channels.routing.websocket_urlpatterns)
routers = personal.websocket_urlpatterns + chat.websocket_urlpatterns
application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
        	routers
        ),

    ),
})