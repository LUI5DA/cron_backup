# This script back ups any given file or directory and stores it in a blob in azure
# This script needs the next arguments:
# - ofile: output file name without extension
# - ifolder: input directory to back up
# - bformat: backup format (zip, tar, gztar, bztar
# syntax: 
# python backup.py <ofile> <ifolder> <bformat>

import shutil
import sys

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, ContentSettings
from azure.core.exceptions import ResourceExistsError, ResourceNotFoundError
import os
from dotenv import load_dotenv
load_dotenv()



def make_backup(ofile, ifolder, bformat):
    """Compress the input file to the specified format into the output file"""
    try:
        shutil.make_archive(ofile, format=bformat, root_dir=ifolder)
    except: 
        print("Error creating archive with shutil")



def process_args():
    """Procesess the program arguments and passes them to the make_backup function"""
    if len(sys.argv) != 4:
        print("Error: invalid arguments.")
        print("Usage: python backup.py <ofile> <ifile> <bformat>")
        sys.exit(1)

    make_backup(sys.argv[1], sys.argv[2], sys.argv[3])





if __name__ == "__main__":
    process_args()

    # configuration for the connection with azure blob
    connection_string = BLOB_STORAGE_STRING
    container_name = CONTAINER_NAME
    blob_name = BLOB_NAME
    local_file_path = sys.argv[1] + sys.argv[3]
    



    
