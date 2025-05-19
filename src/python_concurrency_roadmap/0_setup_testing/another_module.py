import logging
from pathlib import Path, PurePath

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    filename = PurePath(*Path.cwd().parts[:3],'logs','app.log'),
    filemode = 'a'
)

logger = logging.getLogger(__name__)

def func():
    logger.debug("This is from func function")