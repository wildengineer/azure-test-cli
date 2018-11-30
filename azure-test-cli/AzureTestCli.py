import click
import asyncio
from azure.eventhub.client import EventHubClient
from azure.eventhub import Offset, EventHubClientAsync, EventData


@click.group()
def cli():
    pass


@cli.group(help='Perform eventhub tests')
def eventhub():
    pass


@eventhub.command(name='send', help='Send messages to eventhub')
@click.option('--namespace', required=True, help='Name of event hub namespace')
@click.option('--name', required=True, help='Name of eventhub')
@click.option('--keyname', required=True, help='Name of eventhub SAS policy with listen rights')
@click.option('--keyval', required=True, help='Key value of eventhub SAS policy with listen rights')
@click.option('--message', required=True, help='Message to send. Must be in quotes')
@click.option('--repeat', type=int, default=1, help='Count of times to repeat the send of the message')
@click.pass_context
def eventhub_send(ctx, namespace, name, keyname, keyval, message, repeat):
    click.echo('Sending message...')
    client = EventHubClient(buildURL(namespace, name), debug=False, username=keyname, password=keyval)
    # TODO: Partition randomly in a range or use message bound partitioning
    sender = client.add_sender()
    client.run()
    try:
        count = 0
        while count < repeat:
            sender.send(EventData(message))
            click.echo('{} messages sent'.format(count+1))
            count += 1
    except:
        raise
    finally:
        client.stop()


@eventhub.command(name='receive', help='Receive messages from eventhub')
@click.option('--namespace', required=True, help='Name of event hub namespace')
@click.option('--name', required=True, help='Name of eventhub')
@click.option('--keyname', required=True, help='Name of eventhub SAS policy with listen rights')
@click.option('--keyval', required=True, help='Key value of eventhub SAS policy with listen rights')
@click.option('--consumergroup', required=True, help='Name of event hub consumer group')
@click.pass_context
def eventhub_input(ctx, namespace, name, keyname, keyval, consumergroup):
    click.echo("{} {} {} {} {}".format(namespace, name, keyname, keyval, consumergroup))
    OFFSET = Offset("-1")
    loop = asyncio.get_event_loop()
    client = EventHubClientAsync(buildURL(namespace, name), debug=False, username=keyname, password=keyval)
    info = client.get_eventhub_info()
    partitionIdList = info['partition_ids']
    click.echo("Reading from {} partitions.".format(len(partitionIdList)))
    tasks = [asyncio.ensure_future(pump(client, "{}".format(i), consumergroup, OFFSET)) for i in partitionIdList]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.run_until_complete(client.stop_async())
    loop.close()


async def pump(client, partition, consumergroup, offset):
    TIMEOUT = 30
    receiver = client.add_async_receiver(consumergroup, partition, offset, prefetch=5)
    await client.run_async()
    total = 0
    batch = await receiver.receive(timeout=TIMEOUT)
    while batch:
        for event_data in batch:
            last_offset = event_data.offset
            last_sn = event_data.sequence_number
            click.echo("Received: {}, {}".format(last_offset.value, last_sn))
            click.echo(event_data.body_as_str())
            total += 1
        batch = await receiver.receive(timeout=TIMEOUT)
    click.echo("Received {} messages from partition {}.".format(total, partition))


def buildURL(namespace, eventhubname):
    return "amqps://{}.servicebus.windows.net/{}".format(namespace, eventhubname)


# TODO - Add service bus send and receive sub-commands

# @cli.group(help='Perform servicebus tests')
# def servicebus():
#     pass
#
#
# @servicebus.command(name='send', help='')
# def service_bus_input():
#     click.echo('servicebus send')
#
#
# @servicebus.command(name='receive')
# def service_bus_input():
#     click.echo('servicebus send')


if __name__ == '__main__':
    cli()
