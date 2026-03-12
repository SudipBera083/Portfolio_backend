from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import chatbot_service


@api_view(["POST"])
def chat(request):

    user_message = request.data.get("message", "")

    result = chatbot_service.get_response(user_message)

    return Response({
        "reply": result["response"],
        "intent": result["intent"],
        "time": result["timestamp"]
    })