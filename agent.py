import dotenv
from resend import Resend
from google.adk.agents import Agent

dotenv.load_dotenv()

def send_email(recipient: str, subject: str, body: str) -> str:
    """Sends an email using the Resend service.

    Args:
        recipient: The email address of the recipient.
        subject: The subject line of the email.
        body: The HTML or plain text body of the email.

    Returns:
        A string indicating the success or failure of the email attempt.
    """
    resend_api_key = os.getenv("RESEND_API_KEY")
    if not resend_api_key:
        return "Error: RESEND_API_KEY is not set in environment variables."

    try:
        resend_client = Resend(api_key=resend_api_key)
    except Exception as e:
        return f"Error initializing Resend client: {e}"

    sender_email = os.getenv("RESEND_FROM_EMAIL") 
    if not sender_email:
        return "Error: RESEND_FROM_EMAIL is not set. Please set a verified sender address."
        
    params = {
        "from": sender_email,
        "to": [recipient],
        "subject": subject,
        "html": body, # or use "text" for plain text
    }

    try:
        email = resend_client.emails.send(params)
        return f"Email sent successfully to {email['id']}."
    except Exception as e:

root_agent = Agent(
    name="hello",
    model="gemini-2.5-flash",
    instruction="You are an AI assistant designed to send emails.",
    tools=[send_email],
)
        return f"Error sending email: {e}"
