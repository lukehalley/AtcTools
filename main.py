import asyncio, time

from src.blockExplorer.blockExplorer_ABI import collectAbis
from src.utils.logging.logging_Setup import setupLogging

setupLogging()

start_time = time.time()

asyncio.run(collectAbis())
