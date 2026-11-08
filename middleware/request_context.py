import time
import uuid
from starlette.middleware.base import BaseHTTPMiddleware


class RequestContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request_id = request.headers.get("x-request-id", str(uuid.uuid4()))
        request.state.request_id = request_id
        start = time.perf_counter()

        response = await call_next(request)

        response.headers["X-Request-ID"] = request_id
        response.headers["X-Process-Time-ms"] = f"{(time.perf_counter() - start) * 1000:.2f}"
        return response