from click import option, group

from azuretestcli import EventHubDelegate
from azuretestcli import ServiceBusDelegate


@group()
def cli():
    pass


@cli.group(help='Perform eventhub tests')
def eventhub():
    pass


@eventhub.command(name='send', help='Send messages to eventhub')
@option('--eventhub_namespace', '-s', required=True, help='Name of event hub namespace')
@option('--eventhub_name', '-n', required=True, help='Name of eventhub')
@option('--eventhub_sas_name', '-p', required=True, help='Name of eventhub SAS policy with send rights')
@option('--eventhub_sas_key', '-k', required=True, help='Key value of eventhub SAS policy with send rights')
@option('--message', '-m', required=True, help='Message to send. Must be in quotes')
@option('--repeat', '-r', type=int, default=1, help='Count of times to repeat the send of the message')
def eventhub_send(eventhub_namespace, eventhub_name, eventhub_sas_name, eventhub_sas_key, message, repeat):
    delegate = EventHubDelegate(eventhub_namespace, eventhub_name, eventhub_sas_name, eventhub_sas_key)
    delegate.send(message, repeat)


@eventhub.command(name='receive', help='Receive messages from eventhub')
@option('--eventhub_namespace', '-s', required=True, help='Name of event hub namespace')
@option('--eventhub_name', '-n', required=True, help='Name of eventhub')
@option('--eventhub_sas_name', '-p', required=True, help='Name of eventhub SAS policy with listen rights')
@option('--eventhub_sas_key', '-k', required=True, help='Key value of eventhub SAS policy with listen rights')
@option('--consumer_group', '-c', required=True, help='Name of event hub consumer group')
def eventhub_receive(eventhub_namespace, eventhub_name, eventhub_sas_name, eventhub_sas_key, consumer_group):
    delegate = EventHubDelegate(eventhub_namespace, eventhub_name, eventhub_sas_name, eventhub_sas_key)
    delegate.receive(consumer_group)


@cli.group(help='Perform servicebus tests')
def servicebus():
    pass


@servicebus.group(name='queue', help='Perform servicebus queue tests')
def servicebus_queue():
    pass


@servicebus_queue.command(name='send', help='Send messages onto servicebus queue')
@option('--servicebus_namespace', '-s', required=True, help='Name of servicebus namespace')
@option('--servicebus_queue_name', '-n', required=True, help='Name of queue')
@option('--servicebus_sas_name', '-p', required=True, help='Name of servicebus SAS policy with send access')
@option('--servicebus_sas_key', '-k', required=True, help='Key value of servicebus SAS policy with send access')
@option('--message', '-m', required=True, help='Message to send. Must be in quotes')
@option('--repeat', '-r', type=int, default=1, help='Count of times to repeat the send of the message')
def servicebus_queue_send(servicebus_namespace, servicebus_queue_name, servicebus_sas_name, servicebus_sas_key,
                          message, repeat):
    delegate = ServiceBusDelegate(servicebus_namespace, servicebus_sas_name, servicebus_sas_key)
    delegate.send_queue_message(servicebus_queue_name, message, repeat)


@servicebus_queue.command(name='receive', help='Receive messages onto servicebus queue')
@option('--servicebus_namespace', '-s', required=True, help='Name of servicebus namespace')
@option('--servicebus_queue_name', '-n', required=True, help='Name of queue')
@option('--servicebus_sas_name', '-p', required=True, help='Name of servicebus SAS policy with listen access')
@option('--servicebus_sas_key', '-k', required=True, help='Key value of servicebus SAS policy with listen access')
def servicebus_queue_receive(servicebus_namespace, servicebus_queue_name, servicebus_sas_name, servicebus_sas_key):
    delegate = ServiceBusDelegate(servicebus_namespace, servicebus_sas_name, servicebus_sas_key)
    delegate.receive_queue_messages(servicebus_queue_name)


@servicebus.group(name='topic', help='Perform servicebus topic tests')
def servicebus_topic():
    pass


@servicebus_topic.command(name='send', help='Send messages onto servicebus topic')
@option('--servicebus_namespace', '-s', required=True, help='Name of servicebus namespace')
@option('--servicebus_topic_name', '-n', required=True, help='Name of topic')
@option('--servicebus_sas_name', '-p', required=True, help='Name of servicebus SAS policy with send access')
@option('--servicebus_sas_key', '-k', required=True, help='Key value of servicebus SAS policy with send access')
@option('--message', '-m', required=True, help='Message to send. Must be in quotes')
@option('--repeat', '-r', type=int, default=1, help='Count of times to repeat the send of the message')
def servicebus_topic_send(servicebus_namespace, servicebus_topic_name, servicebus_sas_name, servicebus_sas_key,
                          message, repeat):
    delegate = ServiceBusDelegate(servicebus_namespace, servicebus_sas_name, servicebus_sas_key)
    delegate.send_topic_message(servicebus_topic_name, message, repeat)


@servicebus_topic.command(name='receive', help='Receive messages onto servicebus topic')
@option('--servicebus_namespace', '-s', required=True, help='Name of servicebus namespace')
@option('--servicebus_topic_name', '-n', required=True, help='Name of topic')
@option('--servicebus_sas_name', '-p', required=True, help='Name of servicebus SAS policy with listen access')
@option('--servicebus_sas_key', '-k', required=True, help='Key value of servicebus SAS policy with listen access')
def servicebus_topic_receive(servicebus_namespace, servicebus_topic_name, servicebus_sas_name, servicebus_sas_key):
    delegate = ServiceBusDelegate(servicebus_namespace, servicebus_sas_name, servicebus_sas_key)
    delegate.receive_topic_messages(servicebus_topic_name)


@cli.group(help='Perform blobstorage tests [NOT YET IMPLEMENTED]')
def blobstorage():
    pass


@blobstorage.command(name='download', help='Download content from a block blob [NOT YET IMPLEMENTED]')
@option('--blob_storage_account', '-a', required=True, help='Name of servicebus namespace')
@option('--blob_storage_sas_name', '-p', required=True, help='Name of servicebus SAS policy with read access')
@option('--blob_storage_sas_key', '-k', required=True, help='Key value of servicebus SAS policy with read access')
@option('--blob_storage_container', '-c', required=True, help='Blob container name')
@option('--path', required=True, help='Blob path')
def blobstorage_download(blob_storage_account, blob_storage_sas_name, blob_storage_sas_key, blob_storage_container, path):
    raise NotImplementedError


@blobstorage.group(help='Perform block blob tests [NOT YET IMPLEMENTED]')
def block():
    pass


@block.command(name='upload', help='Upload content to a block blob [NOT YET IMPLEMENTED]')
@option('--blob_storage_account', '-a', required=True, help='Name of blob account')
@option('--blob_storage_sas_name', '-p', required=True, help='Name of SAS policy with write access')
@option('--blob_storage_sas_key', '-k', required=True, help='Key value of SAS policy with write access')
@option('--blob_storage_container', '-c', required=True, help='Blob container name')
@option('--path', '-b', required=True, help='Blob path of uploaded file')
@option('--content', '-c', required=True, help='Content to upload to path')
def blobstorage_upload(blob_storage_account, blob_storage_sas_name, blob_storage_sas_key, blob_storage_container,
                       path, content):
    raise NotImplementedError


@blobstorage.group(help='Perform append blob tests [NOT YET IMPLEMENTED]')
def append():
    pass


@append.command(name='append', help='Upload content to a block blob [NOT YET IMPLEMENTED]')
@option('--blob_storage_account', '-a', required=True, help='Name of blob account')
@option('--blob_storage_sas_name', '-p', required=True, help='Name of SAS policy with write access')
@option('--blob_storage_sas_key', '-k', required=True, help='Key value of SAS policy with write access')
@option('--blob_storage_container', '-c', required=True, help='Blob container name')
@option('--path', '-b', required=True, help='Blob path of uploaded file')
@option('--content', '-c', required=True, help='Content to upload to path')
@option('--repeat', '-r', type=int, default=1, help='Count of times to repeat the append the content')
def blobstorage_append(blob_storage_account, blob_storage_sas_name, blob_storage_sas_key, blob_storage_container,
                       path, content, repeat):
    raise NotImplementedError


if __name__ == '__main__':
    cli()
