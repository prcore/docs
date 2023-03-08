import logging
from typing import Any, Dict, List, Optional

from pandas import DataFrame

from plugins.common.algorithm import Algorithm

# Enable logging
logger = logging.getLogger(__name__)


class FooBarAlgorithm(Algorithm):
    def __init__(self, basic_info: Dict[str, Any], project_id: int, plugin_id: Optional[int] = None,
                 df: Optional[DataFrame] = None, model_name: str = None, treatment_definition: list = None):
        super().__init__(basic_info, project_id, plugin_id, df, model_name, treatment_definition)

    def preprocess(self) -> str:
        # Pre-process the data
        pass

    def train(self) -> str:
        # Train the model
        pass

    def predict(self, prefix: List[dict]) -> dict:
        # Predict the result by using the given prefix
        pass

    def predict_df(self, df: DataFrame) -> dict:
        # Predict the result using a DataFrame
        pass
