from sys import getsizeof
from models import Request
from json import dumps

class DummyStats(object):
    def process_response(self, request, response):
        Request.objects.create(meta=dumps(map(lambda x: (x[0], str(x[1])), request.META.items())),
                               path=request.get_full_path(),
                               ip=request.META.get("HTTP_X_REAL_IP", request.META.get("REMOTE_ADDR")),
                               response_code=response.status_code,
                               response_size=getsizeof(response.content))
        return response
