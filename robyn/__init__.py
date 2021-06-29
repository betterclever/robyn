from .robyn import Server
from asyncio import iscoroutinefunction

class Robyn:
    """This is the python wrapper for the Robyn binaries.
    """
    def __init__(self) -> None:
        self.server = Server()

    def add_route(self, route_type, endpoint, handler):
        handler = {
            "is_async": iscoroutinefunction(handler),
            "handler": handler
        }
        self.server.add_route(route_type, endpoint, handler)

    def start(self):
        self.server.start()

    def get(self, endpoint):
        def inner(handler):
            self.add_route("GET", endpoint, handler)
        return inner
    
    def post(self, endpoint):
        def inner(handler):
            self.add_route("POST", endpoint, handler)
        return inner

    def put(self, endpoint):
        def inner(handler):
            self.add_route("PUT", endpoint, handler)
        return inner

    def update(self, endpoint):
        def inner(handler):
            self.add_route("UPDATE", endpoint, handler)
        return inner

    def delete(self, endpoint):
        def inner(handler):
            self.add_route("DELETE", endpoint, handler)
        return inner

    def patch(self, endpoint):
        def inner(handler):
            self.add_route("PATCH", endpoint, handler)
        return inner

    @staticmethod
    async def mount_asgi(scope, receive, send):
        """
        This is a test method for me to have the ability to add asgi support
        """
        assert scope['type'] == 'http'

        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'text/plain'],
            ],
        })

        await send({
            'type': 'http.response.body',
            'body': b'Hello, world!',
        })
