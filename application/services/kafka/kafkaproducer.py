from kafka import KafkaProducer
import json
import os

import logging
logger = logging.getLogger(__name__)


class Producer:
    def __init__(self, topic):
        self.producer = KafkaProducer(
            bootstrap_servers=os.environ['KAFKA_BOOTSTRAP_SERVERS'],
            client_id=os.environ['KAFKA_PRODUCER_CLIENT_ID'],
            sasl_mechanism=os.environ['KAFKA_SASL_MECHANISM'],
            security_protocol=os.environ['KAFKA_SECURITY_PROTOCOL'],
            sasl_plain_username=os.environ['KAFKA_SASL_PLAIN_USERNAME'],
            sasl_plain_password=os.environ['KAFKA_SASL_PLAIN_PASSWORD'],
            ssl_check_hostname=os.environ.get('KAFKA_SSL_CHECK_HOSTNAME', False),
            ssl_cafile=os.environ['KAFKA_SSL_CAFILE'],
            ssl_certfile=os.environ['KAFKA_SSL_CERTFILE'],
            ssl_keyfile=os.environ['KAFKA_SSL_KEYFILE'],
            ssl_password=os.environ['KAFKA_SSL_PASSWORD'],
            retries=5,
            value_serializer=lambda s: json.dumps(s).encode('utf-8'),
            # api_version=(2, 5, 0),
        )
        self.topic = topic

    def produce(self, key, value):
        try:
            self.producer.send(self.topic, key=key.encode(encoding='UTF-8'), value=value)
        except Exception as e:
            logger.exception("Exception occurred: {}".format(str(e)))

    def flush(self):
        self.producer.flush()
    
    def close(self):
        self.producer.close()
    