from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import personal.channels.routing
import logging

logging.warning("ROUTING!!!!!!!!!!!!!!!!!!")
logging.warning(personal.channels.routing.websocket_urlpatterns)

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            personal.channels.routing.websocket_urlpatterns
        )
    ),
})