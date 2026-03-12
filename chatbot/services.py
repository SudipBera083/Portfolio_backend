import re
from datetime import datetime


class PortfolioChatbotService:

    def __init__(self):

        self.responses = {

            "greeting": [
                "Hello 👋 I'm Sudip's AI assistant. How can I help you today?",
                "Hi there! I'm here to help you learn about Sudip's services and projects.",
                "Welcome! Feel free to ask about projects, skills, or how to collaborate."
            ],

            "services": """
Sudip provides professional development services including:

• Full-Stack Web Development (React + Django)
• Enterprise SaaS Architecture
• Oracle Cloud HCM / ERP Solutions
• AI-powered Applications
• API & Backend Engineering
• Cloud Integrations

If you have a project idea, I'd love to hear about it.
""",

            "skills": """
Sudip's core expertise includes:

• React / Next.js
• Django & Python
• Oracle Fusion Cloud HCM
• SQL / PL-SQL
• REST API Architecture
• AI & Automation Systems
• SaaS Platform Development
""",

            "experience": """
Sudip is currently working as a **Programmer Analyst at Cognizant** specializing in:

• Oracle Cloud HCM Technical Development
• BI Publisher Reporting
• Fast Formula
• HCM Extracts
• Cloud Integrations
• Enterprise HR systems
""",

            "projects": """
Sudip has built multiple production-ready systems including:

• AI SaaS platforms
• Enterprise HR automation tools
• Full-stack business applications
• Intelligent analytics dashboards

You can explore them in the **Projects section** of this portfolio.
""",

            "hire": """
Interested in working together? 🚀

You can:
• Use the **contact form**
• Connect via **LinkedIn**
• Send project details directly

Sudip typically responds within **24 hours**.
""",

            "pricing": """
Project pricing depends on scope, complexity, and timeline.

Typical engagements include:

• Full-stack web applications
• SaaS platform development
• Enterprise integrations
• AI-powered systems

Please share your project details so Sudip can provide an estimate.
""",

            "fallback": """
That's an interesting question!

You can ask me about:

• Sudip's services
• Technical skills
• Work experience
• Projects
• Hiring or collaboration

Or send a message through the **contact form**.
"""
        }

        self.intent_patterns = {

            "greeting": r"\b(hi|hello|hey|good morning|good evening)\b",

            "services": r"\b(service|offer|provide|solution|what do you do)\b",

            "skills": r"\b(skill|technology|tech stack|expertise)\b",

            "experience": r"\b(experience|work|company|cognizant|career)\b",

            "projects": r"\b(project|portfolio|built|work examples)\b",

            "hire": r"\b(hire|collaborate|work together|freelance|available)\b",

            "pricing": r"\b(price|cost|budget|rate|pricing)\b",
        }

    def detect_intent(self, message: str):

        message = message.lower()

        for intent, pattern in self.intent_patterns.items():

            if re.search(pattern, message):
                return intent

        return "fallback"

    def get_response(self, message: str):

        intent = self.detect_intent(message)

        response = self.responses.get(intent, self.responses["fallback"])

        return {
            "intent": intent,
            "response": response,
            "timestamp": datetime.utcnow().isoformat()
        }


chatbot_service = PortfolioChatbotService()