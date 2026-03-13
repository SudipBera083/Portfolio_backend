from django.core.management.base import BaseCommand
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone
from django.conf import settings

from chatbot.models import ChatMessage
from contact.models import ContactMessage
from analytics.models import Visitor


class Command(BaseCommand):

    help = "Send daily portfolio analytics report"

    def handle(self, *args, **kwargs):

        today = timezone.now().date()

        visitors = Visitor.objects.filter(
            visited_at__date=today
        ).values("session_id").distinct()

        total_visitors = visitors.count()

        chatbot_messages = ChatMessage.objects.filter(
            created_at__date=today
        ).count()

        contacts = ContactMessage.objects.filter(
            created_at__date=today
        )

        total_contacts = contacts.count()

        conversion_rate = 0
        if total_visitors > 0:
            conversion_rate = (total_contacts / total_visitors) * 100


        contact_rows = ""
        for c in contacts:
            contact_rows += f"""
            <tr>
                <td style="padding:8px;border-bottom:1px solid #eee;">{c.name}</td>
                <td style="padding:8px;border-bottom:1px solid #eee;">{c.email}</td>
                <td style="padding:8px;border-bottom:1px solid #eee;">{c.subject}</td>
            </tr>
            """


        html_message = f"""
        <html>
        <body style="font-family:Arial;background:#f5f7fb;padding:30px">

        <div style="max-width:650px;margin:auto;background:white;border-radius:10px;
        box-shadow:0 10px 30px rgba(0,0,0,0.1);overflow:hidden">

        <div style="background:linear-gradient(135deg,#00fff2,#b14cff);
        padding:20px;color:#030014">

        <h2 style="margin:0">Portfolio Analytics Report</h2>
        <p style="margin:0">Date: {today}</p>

        </div>

        <div style="padding:25px">

        <h3>Visitor Analytics</h3>

        <div style="background:#f7f9fc;padding:15px;border-radius:8px">
        <strong>Total Visitors:</strong> {total_visitors}
        </div>


        <h3 style="margin-top:25px">Chatbot Activity</h3>

        <div style="background:#f7f9fc;padding:15px;border-radius:8px">
        <strong>Total Chatbot Messages:</strong> {chatbot_messages}
        </div>


        <h3 style="margin-top:25px">Contact Form Leads</h3>

        <div style="background:#f7f9fc;padding:15px;border-radius:8px">
        <p><strong>Total Contact Requests:</strong> {total_contacts}</p>
        <p><strong>Conversion Rate:</strong> {conversion_rate:.2f}%</p>
        </div>


        <h3 style="margin-top:25px">Contact Details</h3>

        <table style="width:100%;border-collapse:collapse">

        <thead>
        <tr style="background:#f1f3f7;text-align:left">
        <th style="padding:10px">Name</th>
        <th style="padding:10px">Email</th>
        <th style="padding:10px">Subject</th>
        </tr>
        </thead>

        <tbody>
        {contact_rows if contact_rows else "<tr><td colspan='3' style='padding:10px'>No contacts today</td></tr>"}
        </tbody>

        </table>


        </div>

        <div style="background:#f5f7fb;padding:15px;text-align:center;font-size:12px;color:#777">
        Portfolio AI Assistant • Automated Daily Report
        </div>

        </div>

        </body>
        </html>
        """


        subject = f"Portfolio Analytics Report - {today}"


        email = EmailMultiAlternatives(
            subject,
            "Daily Portfolio Analytics Report",
            settings.DEFAULT_FROM_EMAIL,
            ["sudipbera083@gmail.com", "sudipberasrijitananda@gmail.com"],
        )

        email.attach_alternative(html_message, "text/html")
        email.send()

        self.stdout.write(self.style.SUCCESS("Professional analytics report sent"))