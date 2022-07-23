import json
import os
import sys
from pathlib import Path

from src.utils.json.json_Load import loadJson
from src.utils.logging.logging_Print import printSeparator
from src.utils.logging.logging_Setup import getProjectLogger

overwrite = False
writeValidAbis = True

abisPath = "./data/abis"

functionsToFocusOn = ["WETH",
                      "getAmountIn",
                      "getAmountsIn",
                      "getAmountOut",
                      "getAmountsOut",
                      "swapExactTokensForETH",
                      "swapExactETHForTokens"]

functionsToIgnore = ["swapExactTokensForETH",
                     "swapExactETHForTokens",
                     "WETH"]

# Uniswap Factory
uniswapBaseFactory = loadJson(f"{abisPath}/uniswap/factory.json")["abi"]
# uniswapBaseFactoryFunctionNames = sorted(set([abiFunction["name"] for abiFunction in uniswapBaseFactory if "name" in abiFunction and abiFunction["name"]]) - set(functionsToFocusOn))
# uniswapBaseFactoryFunctionInputs = [abiFunction["inputs"][0] for abiFunction in uniswapBaseFactory if "inputs" in abiFunction and abiFunction["inputs"]]

# Uniswap Router
uniswapBaseRouter = loadJson(f"{abisPath}/uniswap/router.json")["abi"]
# uniswapBaseRouterFunctionNames = sorted(set([abiFunction["name"] for abiFunction in uniswapBaseRouter if "name" in abiFunction and abiFunction["name"]]) - set(functionsToFocusOn))
# uniswapBaseRouterFunctionInputs = [abiFunction["inputs"][0] for abiFunction in uniswapBaseRouter if "inputs" in abiFunction and abiFunction["inputs"]]

logger = getProjectLogger()


def getAllAbis():
    abiCount = 0
    goodAbis = abiCount
    badAbis = abiCount
    oppositeAbis = abiCount

    allAbis = os.walk(abisPath)

    for folder, _, files in allAbis:
        if folder != abisPath:
            for file in files:

                mappedAbiFolder = folder.replace("abis", "mapped-abis")
                mappedAbiPath = f"{mappedAbiFolder}/{file}"

                if not Path(mappedAbiPath).is_file():

                    amountOfMissingFunctions = 0
                    wrongAbiString = ""
                    finalAbi = {}
                    missingFunctions = []
                    presentFunctions = []
                    toMap = []

                    if file.endswith(".json"):

                        abiCount = abiCount + 1

                        abiNetwork = folder.split("/")[-2]
                        abiDex = folder.split("/")[-1]
                        abiType = file.split(".")[0]
                        currentAbi = loadJson(f"{folder}/{file}")

                        finalAbi["abi"] = currentAbi
                        finalAbi["mapping"] = {}

                        currentAbiFunctionNames = sorted(
                            [
                                abiFunction["name"] for abiFunction in currentAbi
                                if
                                "name" in abiFunction
                                and
                                abiFunction["name"]
                            ]
                        )

                        if abiType == "router":
                            # Check function names against standard uniswap Router ABI

                            missingFunctions = list(set(functionsToFocusOn) - set(currentAbiFunctionNames))
                            presentFunctions = list(set(functionsToFocusOn) - set(missingFunctions))
                            toMap = list(set(missingFunctions) - set(functionsToIgnore))
                            amountOfMissingFunctions = len(missingFunctions)

                        if missingFunctions:

                            printSeparator()
                            logger.info(f"[{abiNetwork.title()}] {abiDex.title()} {abiType.title()} ⛔")
                            printSeparator()

                            badAbis = badAbis + 1
                            logger.info(f"- Missing {amountOfMissingFunctions} Functions")
                            # logger.info(f"- Current Functions {currentAbiFunctionNames}️")
                            logger.info(f"- Functions To Map {missingFunctions}️")
                            if wrongAbiString:
                                logger.info(wrongAbiString)

                            for presentFunction in presentFunctions:
                                finalAbi["mapping"][presentFunction] = presentFunction

                            for missingFunction in missingFunctions:

                                if missingFunction in functionsToIgnore:
                                    finalAbi["mapping"][missingFunction] = None
                                else:
                                    finalAbi["mapping"][missingFunction] = "FILL"

                            printSeparator()

                        else:

                            goodAbis = goodAbis + 1

                            if abiType == "router":

                                for function in functionsToFocusOn:

                                    finalAbi["mapping"][function] = function

                            else:

                                for function in currentAbiFunctionNames:
                                    finalAbi["mapping"][function] = function

                            # printSeparator()
                            # logger.info(f"- Matches Uniswap {abiType.title()} ✅")
                            # printSeparator()


                    if missingFunctions or writeValidAbis:
                        if not Path(mappedAbiPath).is_file() or overwrite:
                            Path(mappedAbiFolder).mkdir(parents=True, exist_ok=True)
                            with open(f"{mappedAbiPath}", "w") as outfile:
                                json.dump(finalAbi, outfile, indent=4)
                            logger.info(f"- Wrote Mapped ABI To {mappedAbiPath} 📃")

                        printSeparator(True)

    printSeparator()
    logger.info(f"Total Abis:    [ {abiCount} ]")
    logger.info(f"Good Abis:     [ {goodAbis}/{abiCount} ]")
    logger.info(f"Bad Abis:      [ {badAbis}/{abiCount}  ]")
    printSeparator()
