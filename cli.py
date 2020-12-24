import click


@click.group(help="Commands execution entry point")
@click.pass_context
def execute(ctx, **kwargs):
    from base import BaseConfigurator

    ctx.ensure_object(dict)
    ctx.obj["configurator"] = BaseConfigurator()


@execute.command("publish", help="Publish message to kafka topic")
@click.argument("name")
@click.pass_context
def publish(ctx, name):
    from publisher import Publisher

    message = f"Hello {name} !"
    Publisher(configurator=ctx.obj.get("configurator")).publish(message)


@execute.command("subscribe", help="Subscribe to a kafka topic")
@click.pass_context
def subscribe(ctx):
    from subscriber import Subscriber

    Subscriber(configurator=ctx.obj.get("configurator")).subscribe()


@execute.command("add_partition", help="Subscribe to a kafka topic")
@click.pass_context
def add_partition(ctx):
    from kafka import KafkaAdminClient
    from kafka.admin import NewPartitions

    configurator = ctx.obj.get("configurator")
    admin_client = KafkaAdminClient(bootstrap_servers=configurator.kafka_url)
    partitions = admin_client.describe_topics(
        topics=[configurator.kafka_topic]
    )[0].get("partitions")
    topic_partitions = {
        configurator.kafka_topic: NewPartitions(len(partitions) + 1)
    }
    admin_client.create_partitions(topic_partitions)
    new_partitions = admin_client.describe_topics(
        topics=[configurator.kafka_topic]
    )[0]
    print(new_partitions)


if __name__ == "__main__":
    execute()
