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
def publish_message(ctx, name):
    from publisher import Publisher

    message = f"Hello {name} !"
    Publisher(configurator=ctx.obj.get("configurator")).publish(message)


@execute.command("subscribe", help="Subscribe to a kafka topic")
@click.pass_context
def raise_subscriber(ctx):
    from subscriber import Subscriber

    Subscriber(configurator=ctx.obj.get("configurator")).subscribe()


if __name__ == "__main__":
    execute()
