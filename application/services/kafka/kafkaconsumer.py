from kafka import KafkaConsumer
import json
import os


class Consumer:
    @staticmethod
    def get_consumer():
        consumer = KafkaConsumer(
            bootstrap_servers=os.environ['KAFKA_BOOTSTRAP_SERVERS'],
            client_id=os.environ['KAFKA_CONSUMER_CLIENT_ID'],
            group_id=os.environ['KAFKA_CONSUMER_GROUP_ID'],
            sasl_mechanism=os.environ['KAFKA_SASL_MECHANISM'],
            security_protocol=os.environ['KAFKA_SECURITY_PROTOCOL'],
            sasl_plain_username=os.environ['KAFKA_SASL_PLAIN_USERNAME'],
            sasl_plain_password=os.environ['KAFKA_SASL_PLAIN_PASSWORD'],
            ssl_check_hostname=os.environ.get('KAFKA_SSL_CHECK_HOSTNAME', False),
            ssl_cafile=os.environ['KAFKA_SSL_CAFILE'],
            ssl_certfile=os.environ['KAFKA_SSL_CERTFILE'],
            ssl_keyfile=os.environ['KAFKA_SSL_KEYFILE'],
            ssl_password=os.environ['KAFKA_SSL_PASSWORD'],
            auto_offset_reset='earliest',
            value_deserializer=lambda d: json.loads(d.decode('utf-8')),
        )
        return consumer
