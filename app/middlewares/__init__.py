import inspect

from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

"""
Support following middleware syntax as bellow

async def middleware_func(request: Request, call_next):
    return await call_next(request)

class MiddlewareClass:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        await self.app(scope, receive, send)

class MiddlewareWithArgClass:
    def __init__(self, app: ASGIApp, argument: bool):
        self.app = app
        self.argument = argument

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        await self.app(scope, receive, send)

middlewares = [
    middleware_func,
    MiddlewareClass,
    [MiddlewareWithArgClass, {"argument": True}]
]
"""
middlewares = []


def setup_middlewares(app: FastAPI):
    for middleware in middlewares:
        if inspect.isfunction(middleware):
            app.add_middleware(BaseHTTPMiddleware, dispatch=middleware)
        elif inspect.isclass(middleware):
            app.add_middleware(middlewares)
        elif isinstance(middleware, list):
            arguments = middleware[1]
            middleware = middleware[0]
            app.add_middleware(middleware, **arguments)