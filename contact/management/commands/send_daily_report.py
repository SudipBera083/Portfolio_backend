from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings

from chatbot.models import ChatMessage
from contact.models import ContactMessage


class Command(BaseCommand):
    help = "Send daily chatbot and contact report"

    def handle(self, *args, **kwargs):

        today = timezone.now().date()

        # Chatbot messages
        total_chat_messages = ChatMessage.objects.filter(
            created_at__date=today
        ).count()

        # Contact form submissions
        total_contacts = ContactMessage.objects.filter(
            created_at__date=today
        ).count()

        # Optional: list contacts
        contacts = ContactMessage.objects.filter(created_at__date=today)

        contact_details = "\n".join([
            f"- {c.name} | {c.email} | {c.subject}"
            for c in contacts
        ])

        subject = f"Daily Portfolio Report - {today}"

        message = f"""
Hello Sudip,

Here is your daily portfolio activity report.

Date: {today}

------------------------------
CHATBOT ACTIVITY
------------------------------
Total Messages Received: {total_chat_messages}

------------------------------
CONTACT FORM LEADS
------------------------------
Total Contact Requests: {total_contacts}

Contact Details:

{contact_details if contact_details else "No contacts today"}

------------------------------

Your Portfolio AI Assistant
"""

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            ["sudipbera083@gmail.com", "sudipberasrijitananda@gmail.com"],
            fail_silently=False,
        )

        self.stdout.write(self.style.SUCCESS("Daily report sent successfully"))