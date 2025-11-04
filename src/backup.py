# This script back ups any given file or directory and stores it in a blob in azure
# This script needs the next arguments:
# - ofile: output file name without extension
# - ifolder: input directory to back up
# - bformat: backup format (zip, tar, gztar, bztar
# syntax: 
# python backup.py <ofile> <ifolder> <bformat>

import shutil
import sys
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, ContentSettings
from azure.core.exceptions import ResourceExistsError, ResourceNotFoundError
from dotenv import load_dotenv



def make_backup(ofile, ifolder, bformat):
    """Compress the input file to the specified format into the output file"""
    try:
        shutil.make_archive(ofile, format=bformat, root_dir=ifolder)
    except: 
        print("Error creating archive with shutil")


def upload_backup(local_file, container_name, blob_name, blob_service_client):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    with open(local_file,"rb" ) as file:
        content_settings = ContentSettings(content_type="application/pdf",content_disposition='inline')
        blob_client.upload_blob(file, content_settings=content_settings, overwrite=True)
        print(f"File '{local_file}' Uploaded to Blob storage as '{blob_name}'.")



def process_args():
    """Procesess the program arguments and passes them to the make_backup function"""
    if len(sys.argv) != 4:
        print("Error: invalid arguments.")
        print("Usage: python backup.py <ofile> <ifile> <bformat>")
        sys.exit(1)

    make_backup(sys.argv[1], sys.argv[2], sys.argv[3])





if __name__ == "__main__":

    print("----------------------------------------------------------")
    print("Running backup script...")
    print("Python executable:", sys.executable)
    print("Current directory:", os.getcwd())

    process_args()

    # configuration for the connection with azure blob
    load_dotenv()
    connection_string = os.getenv("BLOB_STORAGE_STRING")
    container_name = os.getenv("CONTAINER_NAME")
    blob_name = os.getenv("BLOB_NAME")
    local_file_path = f"{sys.argv[1]}.{sys.argv[3]}"

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    try:
        container_client = blob_service_client.create_container(container_name)
        print(f"Container '{container_name}' created.")
    except ResourceExistsError:
        print(f"The container '{container_name}' already exists.")

    upload_backup(local_file_path, container_name, blob_name, blob_service_client)

    



    
