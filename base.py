from abc import ABC
from abc import abstractmethod


class AbstractPublisher(ABC):
    @abstractmethod
    def publish(self, message: str):
        raise NotImplementedError


class AbstractSubscriber(ABC):
    @abstractmethod
    def subscribe(self):
        raise NotImplementedError
