import os
from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass


@dataclass
class BaseConfigurator:
    kafka_url: str = os.getenv("KAFKA_URL", default="localhost:9092")
    kafka_topic: str = os.getenv("KAFKA_TOPIC", default="hello")


class BaseKafkaClient:
    def __init__(self, configurator: BaseConfigurator):
        for attr, value in configurator.__dict__.items():
            setattr(self, attr, value)


class AbstractPublisher(BaseKafkaClient, ABC):
    @abstractmethod
    def publish(self, message: str):
        raise NotImplementedError


class AbstractSubscriber(BaseKafkaClient, ABC):
    @abstractmethod
    def subscribe(self):
        raise NotImplementedError
