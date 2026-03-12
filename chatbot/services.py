def get_bot_response(message):

    message = message.lower()

    if "hire" in message or "project" in message:
        return "You can hire Sudip by contacting through the contact form or LinkedIn."

    if "skills" in message:
        return "Sudip specializes in React, Django, Oracle Cloud HCM, SQL, AI systems, and full-stack development."

    if "experience" in message:
        return "Sudip works as a Programmer Analyst at Cognizant with expertise in Oracle Cloud HCM and SaaS systems."

    if "contact" in message:
        return "You can contact Sudip using the contact form on this website."

    return "Thanks for your message! Sudip will respond soon."