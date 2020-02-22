from rest_framework.response import Response
from rest_framework import status


def rest_process_exception(func):
    def decorated_func(*args, **kwargs):
        result = {'result': 'FAILURE',}
        try:
            return func(*args, **kwargs)
        except Exception as e:
            result.update({'error': str(e)})
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
    return decorated_func
