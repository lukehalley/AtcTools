import asyncio

from src.abi.abi_DiffAbis import getAllAbis
from src.blockExplorer.blockExplorer_ABI import collectAbis
from src.utils.logging.logging_Setup import setupLogging

setupLogging()

# asyncio.run(collectAbis())

getAllAbis()
