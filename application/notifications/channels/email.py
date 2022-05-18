from . import NotificationInterface

import logging
logger = logging.getLogger(__name__)


class Email(NotificationInterface):
    def __init__(self, data):
        self.data = data

    def generate_notification(self):
        # Create customised notification message in HTML

        # title = self.data.get('notification_title')
        # notification_description = self.data.get("notification_description")

        # We can also generalise the Notification Title/Description by having it in separate MessageDB where these two
        # will be mapped to a specific KEY.
        # So that email content is always customisable by Product and after getting KEY from service we will read that
        # message from MessageDB and will add required title/description to the email content.

        # Considering A/B testing, we can randomize the email content creation and with whatever method use,
        # we can save it in Email Model for testing later.

        email_content = ""
        # method can be "A" or "B" or "C"
        a_b_test_method_type = "A"
        return email_content, a_b_test_method_type

    # @retry_sending_email -> decorator which will try to send email with difference of 1 sec, 2 sec, 3 sec, 4 sec and
    # 5 sec when some exception occurs while sending the email.
    def send_notification(self, content, a_b_test_method_type):
        try:
            pass
            # Send notification using required library
            # In case we integrated multiple libraries to send email for any reason, then similarly we can create
            # interface for library function and use factory design pattern to send emails.

            # As sending email will be i/o based process and we are getting 10 email per second at max, we can use
            # multithreading to send the emails concurrently.

            # Save all details in Email Model with is_email_sent as 1 and result as success.

        except Exception as e:
            pass
            # Save all details in Email Model with is_email_sent as 0 and result as exception message.
        finally:
            return
