from logging import basicConfig, getLogger, DEBUG, INFO

basicConfig()
LOGGER = getLogger('Game Logger')
LOGGER.setLevel(INFO)  # TODO: Make this configurable
