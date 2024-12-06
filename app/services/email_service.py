# email_service.py
from builtins import ValueError, dict, str
import logging
from settings.config import settings
from app.utils.smtp_connection import SMTPClient
from app.utils.template_manager import TemplateManager
from app.models.user_model import User


class EmailService:
    def __init__(self, template_manager: TemplateManager):
        self.smtp_client = SMTPClient(
            server=settings.smtp_server,
            port=settings.smtp_port,
            username=settings.smtp_username,
            password=settings.smtp_password
        )
        self.template_manager = template_manager
        self.logger = logging.getLogger(__name__)

    async def send_user_email(self, user_data: dict, email_type: str):
        """
        Sends an email to the user based on the email type and user data.

        Args:
            user_data (dict): Contains user details like name and email.
            email_type (str): Type of email to send (e.g., email_verification).

        Raises:
            ValueError: If the email type is invalid.
        """
        subject_map = {
            'email_verification': "Verify Your Account",
            'password_reset': "Password Reset Instructions",
            'account_locked': "Account Locked Notification"
        }

        if email_type not in subject_map:
            self.logger.error(f"Invalid email type: {email_type}")
            raise ValueError("Invalid email type")

        html_content = self.template_manager.render_template(
            email_type, **user_data)

        try:
            self.smtp_client.send_email(
                subject_map[email_type], html_content, user_data['email'])
            self.logger.info(
                f"Email sent successfully: {email_type} to {user_data['email']}")
        except Exception as e:
            self.logger.error(
                f"Failed to send email: {email_type} to {user_data['email']}. Error: {e}")
            raise

    async def send_verification_email(self, user: User):
        """
        Sends an account verification email to the user.

        Args:
            user (User): The user object containing user details.
        """
        verification_url = f"{settings.server_base_url}verify-email/{user.id}/{user.verification_token}"
        self.logger.info(
            f"Preparing verification email for user: {user.email}")
        await self.send_user_email({
            "name": user.first_name,
            "verification_url": verification_url,
            "email": user.email
        }, 'email_verification')
