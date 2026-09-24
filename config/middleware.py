import time

from django.http import JsonResponse


class ExceptionHandlingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start_time = time.time()

        print(f"Request: {request.method} {request.path}")
        response = self.get_response(request)
        
        duration = time.time() - start_time

        print(
            f"Response: {response.status_code} "
            f"Time: {duration:.2f}s"
        )

        return response

    def process_exception(self, request, exception):
        print(f"Exception: {type(exception).__name__}: {exception}")

        return JsonResponse(
            {
                "success": False,
                "error": "An unexpected server error occurred.",
            },
            status=500,
        )
