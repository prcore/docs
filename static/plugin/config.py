import logging
from typing import Any, Dict

from core.confs import config
from core.enums.definition import ColumnDefinition
from core.enums.plugin import PluginType

# Enable logging
logger = logging.getLogger(__name__)

# Pre-defined configuration
basic_info: Dict[str, Any] = {
    "id": config.APP_ID,
    "name": "Foo bar",
    "prescription_type": PluginType.NEXT_ACTIVITY,
    "description": "This is a foo bar plugin",
    "parameters": {},
    "needed_columns": [],
    "needed_info_for_training": [],
    "needed_info_for_prediction": [],
    "supported_encoding": []
}
