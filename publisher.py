from kafka import KafkaProducer

from base import AbstractPublisher
from base import BaseConfigurator


class Publisher(AbstractPublisher):
    kafka_url: str
    kafka_topic: str

    def __init__(self, configurator: BaseConfigurator):
        super(Publisher, self).__init__(configurator)
        if not self.kafka_url or not self.kafka_topic:
            raise ValueError("Invalid kafka url or topic")
        self.producer = KafkaProducer(bootstrap_servers=self.kafka_url)

    def publish(self, message: str):
        print(message)
        self.producer.send(self.kafka_topic, value=message.encode("utf-8"))
