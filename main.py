import asyncio

from src.blockExplorer.blockExplorer_ABI import collectAbis
from src.utils.logging.logging_Setup import setupLogging

setupLogging()

asyncio.run(collectAbis())
