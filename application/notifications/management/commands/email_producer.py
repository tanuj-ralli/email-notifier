from django.core.management import BaseCommand
from services.kafka import Producer
import datetime

import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            producer = Producer("one_email/bulk_email")
            # Main difference between one_email and bulk_email.
            # one_email - mail to be reached with in 20 seconds.
            # bulk_email - mail which can be bit delayed as well.
            payload = {
                'time': datetime.datetime.now().timestamp(),
                'service_name': 'SERVICE_NAME',
                'notification_type': 'INFO/WARNING/ERROR',
                'notification_title': 'EMAIL SUBJECT',
                'notification_description': 'EMAIL BODY',
                'to_email': '[abc@xyz.com]',
                'channel_type': 'email'
            }
            producer.produce(
                "Key",
                value=payload,
            )
            producer.flush()
            producer.close()
            logger.info('Successfully pushed to kafka')
        except Exception as e:
            logger.exception('Exception occurred while pushing to kafka: {}'.format(str(e)))
