from base import AbstractPublisher


class Publisher(AbstractPublisher):
    def publish(self, message):
        print(message)
