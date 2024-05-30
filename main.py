from src.logger import logging
from src.exception import CustomException
from src.pipelines.stage_01_data_ingestion_pipeline import DataIngestionPipeline
from src.pipelines.stage_02_data_validation_pipeline import DataValidationPipeline
from src.pipelines.stage_03_data_transformation_pipeline import DataTransformationPipeline
from src.pipelines.stage_04_model_training_pipeline import ModelTrainerPipeline
import sys

STAGE_NAME = "Data Ingestion"

try:

    logging.info(f">>>>>>>>>> {STAGE_NAME} Started >>>>>>>>>>")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logging.info(f">>>>>>>>>> {STAGE_NAME} Ended >>>>>>>>>>")

except Exception as e:

    logging.info("Error Occure {}".format(e))
    raise CustomException(e,sys)


STAGE_NAME = "Data Validation"

try:
    logging.info(f">>>>>>>>>> {STAGE_NAME} Started >>>>>>>>>>")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logging.info(f">>>>>>>>>> {STAGE_NAME} Ended >>>>>>>>>>")

except Exception as e:

    logging.info("Error Occure {}".format(e))
    raise CustomException(e,sys)


STAGE_NAME = "Data Transformation"

try:
    logging.info(f">>>>>>>>>> {STAGE_NAME} Started >>>>>>>>>>")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logging.info(f">>>>>>>>>> {STAGE_NAME} Ended >>>>>>>>>>")

except Exception as e:

    logging.info("Error Occure {}".format(e))
    raise CustomException(e,sys)


STAGE_NAME = "Model Training"

try:
    logging.info(f">>>>>>>>>> {STAGE_NAME} Started >>>>>>>>>>")
    data_model_trainer = ModelTrainerPipeline()
    data_model_trainer.main()
    logging.info(f">>>>>>>>>> {STAGE_NAME} Ended >>>>>>>>>>")

except Exception as e:

    logging.info("Error Occure {}".format(e))
    raise CustomException(e,sys)


