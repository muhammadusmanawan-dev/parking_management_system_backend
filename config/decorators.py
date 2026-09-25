from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException


def handle_exceptions(view_function):
    @wraps(view_function)
    def wrapper(*args, **kwargs):
        try:
            return view_function(*args, **kwargs)

        except APIException:
            raise

        except ValueError as exc:
            return Response(
                {
                    "success": False,
                    "error": str(exc),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as exc:
            return Response(
                {
                    "success": False,
                    "error": str(exc),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    return wrapper
