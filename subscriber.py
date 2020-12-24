from kafka import KafkaAdminClient
from kafka import KafkaConsumer
from kafka.admin import NewPartitions

from base import AbstractSubscriber
from base import BaseConfigurator


class Subscriber(AbstractSubscriber):
    kafka_url: str
    kafka_topic: str
    kafka_group: str = "default"

    def __init__(self, configurator: BaseConfigurator):
        super(Subscriber, self).__init__(configurator)
        if not self.kafka_url or not self.kafka_topic:
            raise ValueError("Invalid kafka url or topic")

        self.consumer = KafkaConsumer(
            self.kafka_topic,
            group_id=self.kafka_group,
            bootstrap_servers=[self.kafka_url],
            value_deserializer=lambda x: x.decode("utf-8"),
        )
        partitions = self.consumer.partitions_for_topic(self.kafka_topic)
        print(f"creating a new subscriber with: {partitions} partitions")

    def subscribe(self):
        for message in self.consumer:
            offset = getattr(message, "offset", None)
            partition = getattr(message, "partition", None)
            print(
                f"topic: {self.kafka_topic}, "
                f"partition: {partition}, "
                f"offset: {offset}, "
                f"message: {message.value}"
            )

    def __del__(self):
        print("deleting a subscriber")
        self.consumer.pause()
        self.consumer.unsubscribe()
