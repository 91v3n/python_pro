import logging

FORMAT = '{levelname:<8} - {asctime} - {msg}'
fileHandler = logging.FileHandler(filename='logs.log', encoding='utf-8')
logging.basicConfig(level=logging.DEBUG, handlers={fileHandler}, format=FORMAT, style='{')
logger = logging.getLogger(__name__)
