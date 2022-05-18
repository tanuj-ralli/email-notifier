from .channels import Email


class NotificationFactory:
    @staticmethod
    def send_notification(notification_data):
        channel = notification_data.get('channel_type', None)
        if channel.lower() == "email":
            return Email(notification_data)
        return None
