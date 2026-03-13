import uuid
from .models import Visitor


class VisitorTrackingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        session_id = request.session.get("visitor_id")

        if not session_id:

            session_id = str(uuid.uuid4())
            request.session["visitor_id"] = session_id

            ip = request.META.get("REMOTE_ADDR")
            agent = request.META.get("HTTP_USER_AGENT", "")

            Visitor.objects.create(
                ip_address=ip,
                user_agent=agent,
                session_id=session_id
            )

        return self.get_response(request)