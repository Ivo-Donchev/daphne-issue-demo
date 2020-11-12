from django.conf.urls import url

from channels.routing import ProtocolTypeRouter, URLRouter

from .consumers import MyConsumer


application = ProtocolTypeRouter({
    'websocket': URLRouter(
        [
            url(r'^ws/$', MyConsumer.as_asgi()),
        ]
    )
})
