import os
import sys

from deepdiff import DeepDiff
from src.utils.json.json_Load import loadJson
from src.utils.logging.logging_Print import printSeparator
from src.utils.logging.logging_Setup import getProjectLogger

abisPath = "./data/abis"

# Uniswap Factory
uniswapBaseFactory = loadJson(f"{abisPath}/IUniswapV2Factory.json")["abi"]
uniswapBaseFactoryFunctionNames = sorted([abiFunction["name"] for abiFunction in uniswapBaseFactory if "name" in abiFunction and "inputs" in abiFunction and "outputs" in abiFunction])
uniswapBaseFactoryFunctionInputs = [abiFunction["inputs"] for abiFunction in uniswapBaseFactory if "name" in abiFunction and "inputs" in abiFunction and "outputs" in abiFunction]
uniswapBaseFactoryFunctionOutputs = [abiFunction["outputs"] for abiFunction in uniswapBaseFactory if "name" in abiFunction and "inputs" in abiFunction and "outputs" in abiFunction]

# Uniswap Router
uniswapBaseRouter = loadJson(f"{abisPath}/IUniswapV2Router02.json")["abi"]
uniswapBaseRouterFunctionNames = sorted([abiFunction["name"] for abiFunction in uniswapBaseRouter if "name" in abiFunction and "inputs" in abiFunction and "outputs" in abiFunction])
uniswapBaseRouterFunctionInputs = [abiFunction["inputs"] for abiFunction in uniswapBaseRouter if "name" in abiFunction and "inputs" in abiFunction and "outputs" in abiFunction]
uniswapBaseRouterFunctionOutputs = [abiFunction["outputs"] for abiFunction in uniswapBaseRouter if "name" in abiFunction and "inputs" in abiFunction and "outputs" in abiFunction]

logger = getProjectLogger()

def getAllAbis():

    abiCount = 0
    goodAbis = abiCount
    badAbis = abiCount
    oppositeAbis = abiCount

    for folder, _, files in os.walk(abisPath):
        if folder != abisPath:
            for file in files:
                if file.endswith(".json"):

                    abiCount = abiCount + 1

                    abiNetwork = folder.split("/")[-2]
                    abiDex = folder.split("/")[-1]
                    abiType = file.split(".")[0]
                    currentAbi = loadJson(f"{folder}/{file}")

                    abiFunctions = sorted([abiFunction["name"] for abiFunction in currentAbi if
                                    "name" in abiFunction and "inputs" in abiFunction and "outputs" in abiFunction])

                    wrongAbiString = ""

                    if abiType == "factory":
                        missingFunctions = list(set(uniswapBaseFactoryFunctionNames) - set(abiFunctions))
                        amountOfMissingFunctions = len(missingFunctions)

                        diffToRouter = len(list(set(uniswapBaseRouterFunctionNames) - set(abiFunctions)))
                        isActuallyRouter = diffToRouter < amountOfMissingFunctions

                        if isActuallyRouter:
                            oppositeAbis = oppositeAbis + 1
                            wrongAbiString = "- Suspected To Actually Be Router ABI! 🤢"

                    elif abiType == "router":
                        missingFunctions = list(set(uniswapBaseRouterFunctionNames) - set(abiFunctions))

                        amountOfMissingFunctions = len(missingFunctions)

                        diffToFactory = len(list(set(uniswapBaseRouterFunctionNames) - set(abiFunctions)))
                        isActuallyFactory = diffToFactory < amountOfMissingFunctions

                        if isActuallyFactory:
                            oppositeAbis = oppositeAbis + 1
                            wrongAbiString = "- Suspected To Actually Be Factory ABI! 🤢"

                    else:
                        sys.exit(f"Bad Abi Type: {abiType}")

                    if missingFunctions:

                        printSeparator()
                        logger.info(f"[{abiNetwork.title()}] {abiDex.title()} {abiType.title()}")
                        printSeparator()

                        badAbis = badAbis + 1
                        logger.info(f"- Missing {missingFunctions} ⛔️")
                        if wrongAbiString:
                            logger.info(wrongAbiString)

                        printSeparator(True)
                    else:
                        goodAbis = goodAbis + 1
                        # logger.info(f"- Matches Uniswap {abiType.title()} ✅")



    printSeparator()
    logger.info(f"Total Abis:    [ {abiCount} ]")
    logger.info(f"Good Abis:     [ {goodAbis}/{abiCount} ]")
    logger.info(f"Bad Abis:      [ {badAbis}/{abiCount}  ]")
    logger.info(f"Opposite Abis: [ {oppositeAbis}/{abiCount}  ]")
    printSeparator()
