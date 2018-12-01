from click import echo, option, group

from azuretestcli import EventHubDelegate
from azuretestcli import ServiceBusDelegate


@group()
def cli():
    pass


@cli.group(help='Perform eventhub tests')
def eventhub():
    pass


@eventhub.command(name='send', help='Send messages to eventhub')
@option('--namespace', required=True, help='Name of event hub namespace')
@option('--name', required=True, help='Name of eventhub')
@option('--sasname', required=True, help='Name of eventhub SAS policy with listen rights')
@option('--saskey', required=True, help='Key value of eventhub SAS policy with listen rights')
@option('--message', required=True, help='Message to send. Must be in quotes')
@option('--repeat', type=int, default=1, help='Count of times to repeat the send of the message')
def eventhub_send(namespace, name, sasname, saskey, message, repeat):
    echo('Sending message...')
    delegate = EventHubDelegate(namespace, name, sasname, saskey)
    delegate.send(message, repeat)


@eventhub.command(name='receive', help='Receive messages from eventhub')
@option('--namespace', required=True, help='Name of event hub namespace')
@option('--name', required=True, help='Name of eventhub')
@option('--sasname', required=True, help='Name of eventhub SAS policy with listen rights')
@option('--saskey', required=True, help='Key value of eventhub SAS policy with listen rights')
@option('--consumergroup', required=True, help='Name of event hub consumer group')
def eventhub_receive(namespace, name, sasname, saskey, consumergroup):
    delegate = EventHubDelegate(namespace, name, sasname, saskey)
    delegate.receive(consumergroup)


@cli.group(help='Perform servicebus tests')
def servicebus():
    pass


@servicebus.group(name='queue', help='Perform servicebus queue tests')
def servicebus_queue():
    pass


@servicebus_queue.command(name='send', help='Send messages onto servicebus queue')
@option('--namespace', required=True, help='Name of servicebus namespace')
@option('--name', required=True, help='Name of servicebus')
@option('--sasname', required=True, help='Name of servicebus SAS policy with send access')
@option('--saskey', required=True, help='Key value of servicebus SAS policy with send access')
@option('--message', required=True, help='Message to send. Must be in quotes')
@option('--repeat', type=int, default=1, help='Count of times to repeat the send of the message')
def servicebus_queue_send(namespace, name, sasname, saskey, message, repeat):
    delegate = ServiceBusDelegate(namespace, sasname, saskey)
    delegate.send_queue_message(name, message, repeat)


@servicebus_queue.command(name='receive')
@option('--namespace', required=True, help='Name of servicebus namespace')
@option('--name', required=True, help='Name of servicebus')
@option('--sasname', required=True, help='Name of servicebus SAS policy with listen access')
@option('--saskey', required=True, help='Key value of servicebus SAS policy with listen access')
def servicebus_queue_receive(namespace, name, sasname, saskey):
    delegate = ServiceBusDelegate(namespace, sasname, saskey)
    delegate.receive_queue_messages(name)


@servicebus.group(name='topic', help='Perform servicebus topic tests')
def servicebus_topic():
    pass


@servicebus_topic.command(name='send', help='Send messages onto servicebus topic')
@option('--namespace', required=True, help='Name of servicebus namespace')
@option('--name', required=True, help='Name of servicebus')
@option('--sasname', required=True, help='Name of servicebus SAS policy with send access')
@option('--saskey', required=True, help='Key value of servicebus SAS policy with send access')
@option('--message', required=True, help='Message to send. Must be in quotes')
@option('--repeat', type=int, default=1, help='Count of times to repeat the send of the message')
def servicebus_topic_send(namespace, name, sasname, saskey, message, repeat):
    delegate = ServiceBusDelegate(namespace, sasname, saskey)
    delegate.send_topic_message(name, message, repeat)


@servicebus_topic.command(name='receive')
@option('--namespace', required=True, help='Name of servicebus namespace')
@option('--name', required=True, help='Name of servicebus')
@option('--sasname', required=True, help='Name of servicebus SAS policy with listen access')
@option('--saskey', required=True, help='Key value of servicebus SAS policy with listen access')
def servicebus_topic_receive(namespace, name, sasname, saskey):
    delegate = ServiceBusDelegate(namespace, sasname, saskey)
    delegate.receive_topic_messages(name)


@cli.group(help='Perform blobstorage tests [NOT YET IMPLEMENTED]')
def blobstorage():
    pass


@blobstorage.group(help='Perform block blob tests [NOT YET IMPLEMENTED]')
def block():
    pass


@block.command(name='upload', help='Upload content to a block blob [NOT YET IMPLEMENTED]')
@option('--account', required=True, help='Name of blob account')
@option('--sasname', required=True, help='Name of SAS policy with send access')
@option('--saskey', required=True, help='Key value of SAS policy with send access')
@option('--path', required=True, help='Blob path of uploaded file')
@option('--content', required=True, help='Content to upload to path')
def servicebus_queue_send(namespace, name, sasname, saskey, message, repeat):
    raise NotImplementedError


@block.command(name='download', help='Download content from a block blob [NOT YET IMPLEMENTED]')
@option('--account', required=True, help='Name of servicebus namespace')
@option('--sasname', required=True, help='Name of servicebus SAS policy with listen access')
@option('--saskey', required=True, help='Key value of servicebus SAS policy with listen access')
@option('--path', required=True, help='Blob path')
def blob_block_download(account, name, sasname, saskey):
    raise NotImplementedError

if __name__ == '__main__':
    cli()
