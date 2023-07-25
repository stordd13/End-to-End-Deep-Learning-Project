from ..config.configuration import ConfigurationManager
from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier import logger

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()
    

    STAGE_NAME = "Evaluation stage"

    if __name__ == "__main__":
        try:
            logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
            obj = EvaluationPipeline()
            obj.main()
            logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
        raise e