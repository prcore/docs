import logging

from plugins.common.starter import plugin_scheduler, plugin_run
from plugins.foo_bar.algorithm import FooBarAlgorithm
from plugins.foo_bar.config import basic_info, needed_columns

# Enable logging
logger = logging.getLogger(__name__)
for _ in logging.root.manager.loggerDict:
    if _.startswith("pika"):
        logging.getLogger(_).setLevel(logging.CRITICAL)

if __name__ == "__main__":
    plugin_scheduler()
    plugin_run(basic_info, needed_columns, FooBarAlgorithm)
