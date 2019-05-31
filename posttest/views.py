from django.http.response import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class ApiPosttestView(APIView):
    permission_classes = (
        AllowAny,
    )

    def post(self, _request):
        return JsonResponse(
            {'message': 'message'},
        )


