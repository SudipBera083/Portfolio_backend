from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services import get_bot_response


@api_view(["POST"])
def chat(request):

    message = request.data.get("message")

    response = get_bot_response(message)

    return Response({
        "reply": response
    })