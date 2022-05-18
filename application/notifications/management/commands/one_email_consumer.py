from django.core.management import BaseCommand
from services.kafka import Consumer
from notifications.handler import NotificationHandler

import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            consumer = Consumer.get_consumer()
            consumer.subscribe('one_email')
            while True:
                try:
                    logger.info('Looking for new data ...')
                    msg = consumer.poll(timeout_ms=1000)
                    if not bool(msg):
                        continue
                    else:
                        key = list(msg.keys())[0]
                        for row in msg[key]:
                            value = row.value
                            key = row.key.decode()
                            if bool(value):
                                handler = NotificationHandler(notification_data=value)
                                handler.send_notification()
                except Exception as ex:
                    logger.exception('Exception occurred inside while loop: {}'.format(str(ex)))
        except Exception as e:
            logger.exception('Exception occurred while pulling from kafka: {}'.format(str(e)))
