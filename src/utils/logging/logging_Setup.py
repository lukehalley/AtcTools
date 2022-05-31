import logging, os, sys

# Setup logger
def setupLogging():
    logger = logging.getLogger("atc-tools")

    log_format = '%(asctime)s | %(levelname)s | %(message)s'
    dateFormat = os.environ.get("DATE_FORMAT")

    logging.basicConfig(level=logging.INFO, format=log_format,
                        stream=sys.stdout, datefmt=dateFormat)

    return logger

# Get the project logger
def getProjectLogger():
    return logging.getLogger("atc-tools")
