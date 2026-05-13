import logging
logger = logging.getLogger('example_logger')

logging.basicConfig(format='%(levelname)s-%(name)s - %(message)s')
logger.warning('This is a warning')
