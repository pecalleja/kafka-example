import click


@click.group(help="Commands execution entry point")
@click.pass_context
def execute(ctx):
    ctx.ensure_object(dict)


@execute.command("publish", help="Publish message to kafka topic")
@click.argument("name")
def publish_message(name):
    from publisher import Publisher

    message = f"Hello {name} !"
    Publisher().publish(message)


@execute.command("subscribe", help="Subscribe to a kafka topic")
def raise_subscriber():
    from subscriber import Subscriber

    Subscriber().subscribe()


if __name__ == "__main__":
    execute()
