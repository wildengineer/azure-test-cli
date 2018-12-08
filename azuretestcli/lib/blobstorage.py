# TODO: Review possible operations for BlobStorage
# TODO: Add BlobStorageDelegate and appropriate operations

from azure.storage.blob import BlockBlobService, AppendBlobService
from click import echo


class BlobStorageDelegate:
    def __init__(self, account_name, account_key):
        self.block_blob_service = BlockBlobService(account_name, account_key)
        self.append_blob_service = AppendBlobService(account_name, account_key)

    def block_write(self, container, blob_path, file_path):
        self.block_blob_service.create_blob_from_path(container, blob_path, file_path)
        echo('Uploaded block blob to container {} at path {}'.format(container, blob_path))

    def block_read(self, container, blob_path, file_path):
        self.block_blob_service.get_blob_to_path(container, blob_path, file_path)
        echo('Downloaded block blob from container {} at path {} to local file {}'.format(container, blob_path,
                                                                                          file_path))

    def append_write(self, container, blob_path, file_path=None):
        self.append_blob_service.create_blob(container, blob_path)
        echo('Created append blob in container {} at path {} from local file {}'
             .format(container, blob_path, file_path))
        if file_path is not None:
            lease_id =self.append_blob_service.acquire_blob_lease(container, blob_path, 30)
            self.append_blob_service.append_blob_from_path(container, blob_path, file_path)
            self.append_blob_service.release_blob_lease(container, blob_path, lease_id)
            echo('Appended to blob in container {} at path {} from local file {}'
                 .format(container, blob_path, file_path))

    def append_read(self, container, blob_path, file_path):
        self.append_blob_service.get_blob_to_path(container, blob_path, file_path)
        echo('Downloaded block blob from container {} at path {} to local path {}'.format(container, blob_path,
                                                                                          file_path))
    def append_poll(self, container, blob_path):
        self.append_blob_service.get_blob_properties()
        self.
