from cnnClassifier.config.configuaration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger


STAGE_NAME = 'Date Ingestion Stage'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e



if __name__ == "__main__":
    try:
        logger.info(f'Running {STAGE_NAME}')
        pipeline = DataIngestionTrainingPipeline()
        pipeline.main()
        logger.info(f'{STAGE_NAME} completed successfully')
    except Exception as e:
        logger.exception(e)
        raise e




