from src.logging import logger
from src.exception.exception import ProjectException
import sys

from src.components.datatingstion import DataIngestion

from src.components.datatingstion import DataIngestionArtifact
from src.components.datatingstion import DataIngestionConfig


if __name__=="__main__":
    
    data_ingestion=DataIngestion()
    train_data, test_data = data_ingestion.initate_data_ingestion()
    




