# from src.cnnImageClssifier import logger
# from cnnImageClssifier import logger

# to check log info display this message in the terminal.
# logger.info("welcome to cnnImageClassifier!")
# logger.info("Data Deleted from Github Here, Restarting work!")

from cnnImageClssifier import logger
from cnnImageClssifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e