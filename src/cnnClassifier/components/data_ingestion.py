import os 
import zipfile
import urllib.request as request
from cnnClassifier import logger
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier.utils.common import get_size
from pathlib import Path


class DataIngestion:
    def __init__(self,config : DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            try:
                filename, headers = request.urlretrieve(
                    url= self.config.source_url,
                    filename = self.config.local_data_file
                )
                logger.info(f"filename {filename} downloaded! with following info: \n {headers}")
            except Exception as e:
                logger.error(f" failed to download file:{e}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extract the zip file into the data directory
        Function returns None
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        print(f"Attempting to open file at {self.config.local_data_file}")  # Add debugging output

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            print("Successfully opened zip file")
            zip_ref.extractall(unzip_path)
            