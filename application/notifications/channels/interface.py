import abc


class NotificationInterface(abc.ABC):

    @abc.abstractmethod
    def __init__(self):
        self.django_obj = None

    @abc.abstractmethod
    def generate_notification(self):
        pass

    @abc.abstractmethod
    def send_notification(self, content, a_b_test_method_type):
        pass
