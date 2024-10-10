# from src.cnnImageClssifier import logger
# from cnnImageClssifier import logger

# to check log info display this message in the terminal.
# logger.info("welcome to cnnImageClassifier!")
# logger.info("Data Deleted from Github Here, Restarting work!")

from cnnImageClssifier import logger
from cnnImageClssifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnImageClssifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline



STAGE_NAME = "Data Ingestion stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e