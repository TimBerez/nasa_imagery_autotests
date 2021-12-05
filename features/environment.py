"""Before/after stuff."""

from core.core import AppConfig
from core.logger import Logger

logger = Logger()


def before_all(context):
    """These run before the whole shooting match."""

    logger.debug('Before all start.')
    context.app_config = AppConfig()
    logger.debug('Before all finish.')


def before_feature(context, feature):
    """These run before each feature file is exercised."""

    logger.debug('Before feature %s start.', feature)
    logger.debug('Before feature %s finish.', feature)


def before_scenario(context, scenario):
    """These run before each scenario is run."""

    logger.debug('Before scenario %s start.', scenario)

    context.scenario_log = Logger.add_temp_file_handler(logger)

    logger.debug('Before scenario %s finish.', scenario)


def before_step(context, step):
    """These run before every step."""

    logger.debug('Before step %s start.', step)

    logger.debug('Before step %s finish.', step)


def after_step(context, step):
    """These run after every step."""

    logger.debug('After step %s start.', step)

    logger.debug('After step %s finish.', step)


def after_scenario(context, scenario):
    """These run after each scenario is run."""

    logger.debug('After scenario %s start.', scenario)

    logger.debug('After scenario %s finish.', scenario)


def after_feature(context, feature):
    """These run after each feature file is exercised."""

    logger.debug('After feature %s start.', feature)

    logger.debug('After feature %s finish.', feature)


def after_all(context):
    """These run after the whole shooting match."""

    logger.debug('After all start.')
    logger.debug('After all finish.')
