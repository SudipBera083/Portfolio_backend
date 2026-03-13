from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings

from chatbot.models import ChatMessage
from contact.models import ContactMessage
from analytics.models import Visitor


class Command(BaseCommand):

    help = "Send daily analytics report for chatbot, contacts and visitors"

    def handle(self, *args, **kwargs):

        today = timezone.now().date()

        # ---------------------------
        # Daily Visitors
        # ---------------------------

        visitors = Visitor.objects.filter(
            visited_at__date=today
        ).values("session_id").distinct()

        total_visitors = visitors.count()

        # ---------------------------
        # Chatbot Messages
        # ---------------------------

        total_chat_messages = ChatMessage.objects.filter(
            created_at__date=today
        ).count()

        # ---------------------------
        # Contact Form Leads
        # ---------------------------

        contacts = ContactMessage.objects.filter(
            created_at__date=today
        )

        total_contacts = contacts.count()

        # ---------------------------
        # Conversion Rate
        # ---------------------------

        conversion_rate = 0

        if total_visitors > 0:
            conversion_rate = (total_contacts / total_visitors) * 100

        # ---------------------------
        # Contact Details
        # ---------------------------

        contact_details = "\n".join([
            f"- {c.name} | {c.email} | {c.subject}"
            for c in contacts
        ])

        if not contact_details:
            contact_details = "No contact submissions today."

        # ---------------------------
        # Email Content
        # ---------------------------

        subject = f"Daily Portfolio Analytics Report - {today}"

        message = f"""
Hello Sudip,

Here is your portfolio analytics report for today.

Date: {today}

----------------------------------------
VISITOR ANALYTICS
----------------------------------------

Total Visitors: {total_visitors}

----------------------------------------
CHATBOT ACTIVITY
----------------------------------------

Total Chatbot Messages: {total_chat_messages}

----------------------------------------
CONTACT FORM LEADS
----------------------------------------

Total Contact Requests: {total_contacts}

Conversion Rate: {conversion_rate:.2f} %

----------------------------------------
CONTACT DETAILS
----------------------------------------

{contact_details}

----------------------------------------

Regards,
Portfolio AI Assistant
"""

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            ["sudipbera083@gmail.com","sudipberasrijitananda@gmail.com"],
            fail_silently=False,
        )

        self.stdout.write(
            self.style.SUCCESS("Daily analytics report sent successfully")
        )