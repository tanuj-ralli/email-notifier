from notifications.factory import NotificationFactory


class NotificationHandler:
    def __init__(self, notification_data):
        self.notification_data = notification_data

    def send_notification(self):
        channel = NotificationFactory.send_notification(self.notification_data)
        if channel is None:
            return "{} is not supported channel".format(self.notification_data.get('channel'))
        content, a_b_test_method_type = channel.generate_notification()
        return channel.send_notification(content, a_b_test_method_type)
