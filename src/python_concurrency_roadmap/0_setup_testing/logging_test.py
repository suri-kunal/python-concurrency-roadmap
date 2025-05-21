import logging
from another_module import func
from pathlib import Path, PurePath

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    filename = PurePath(*Path.cwd().parts[:3],'logs','app.log'),
    filemode = 'a'
)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    logger.debug("This is debug message")
    logger.info("This is info message")
    logger.warning("This is a warning")
    logger.error("This is error")
    logger.critical("This is critical")

    try:
        x = 1/0
    except Exception as e:
        logging.error("Failed to perform division",exc_info=True)

    func()