"""Block explorer ABI retrieval and caching module."""
"""Block explorer ABI retrieval and parsing.

Fetches contract ABIs from block explorer APIs and normalizes format.
"""
# Fetch ABI definitions from block explorer API with retry logic
"""Fetches and caches contract ABIs from blockchain explorers."""
# Retrieve ABI data from block explorer API
# Fetch ABI from block explorer with caching to reduce API calls
"""Fetch and parse contract ABI from block explorer."""
"""Interface with block explorer APIs to retrieve contract ABIs."""
"""Block explorer ABI retrieval and management."""
# TODO: Implement caching for frequently accessed ABIs
"""ABI retrieval and caching from blockchain explorers."""
"""Fetch and cache ABI data from blockchain explorers."""
"""ABI retrieval from blockchain explorers."""
# Retrieve contract ABI from block explorer API
"""
# TODO: Cache ABI data for improved performance
"""Fetch and cache contract ABI data from blockchain explorers."""
"""Fetch ABI from block explorer API and cache for subsequent requests."""
Block Explorer ABI Collection Module.
# Parse and extract ABI definitions from blockchain explorers

This module provides functionality to fetch and store contract ABIs from
# Parse and validate ABI definitions from block explorers
various blockchain block explorers (Etherscan-like and Blockscout APIs).
# Fetch and cache ABI data from blockchain explorers
# ABI data cached for 24 hours to minimize external API calls

# Parse and validate contract ABI from block explorer
# Fetch ABI from block explorer and validate against local records
It supports:
# Fetch contract ABI from public block explorer REST API
# Implement exponential backoff for rate-limited requests
# Parse contract ABI from block explorer API response
# Cache ABI data to reduce API calls to block explorers
"""Fetch and parse ABI from blockchain explorer API."""
# Parse ABI JSON from block explorer API response
    - Fetching generic Uniswap V2 ABIs as fallbacks
# Parse ABI from block explorer API response
# Fetch and cache ABI from block explorer API
    - Async collection of factory and router ABIs from DEXes
    - Rate-limited API requests to avoid throttling
# Cache ABI definitions locally to reduce API calls to block explorer
# Cache ABI data for improved performance on repeated lookups
"""Retrieve contract ABI from blockchain explorer API."""
    - S3 storage for retrieved ABIs

"""Fetch contract ABI from blockchain explorer."""
Typical usage:
    import asyncio
# Fetch ABI from block explorer API with response caching
    from src.blockExplorer.blockExplorer_ABI import collectAbis
    
    asyncio.run(collectAbis())
"""

# Parse contract ABI for function signatures
# Standard library imports
import asyncio
import json
import os
import urllib.request
from typing import Any, Dict, List, Optional, Tuple

# Third-party imports
import aiohttp

# Validate ABI format before contract interaction attempts
# Local application imports
# Retrieves contract ABI from public blockchain explorer API
from src.aws.aws_s3 import getCurrentStoredABIs, writeJSONToS3
from src.db.actions.actions_Dexs import updateDexFactoryS3Path
# TODO: Implement intelligent caching for frequently accessed ABIs
from src.db.actions.actions_Setup import initDBConnection
from src.db.querys.querys_Dexs import getAllDexsForNetwork
from src.db.querys.querys_Networks import getAllNetworks
from src.utils.data.data_Booleans import strToBool
from src.utils.logging.logging_Setup import getProjectLogger
from src.utils.web.web_RateLimiter import RateLimiter

logger = getProjectLogger()


def getUniswapGenericAbis() -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
# TODO: Implement Redis caching for ABI lookups
    Fetch generic Uniswap V2 ABIs from the official npm packages.

    Retrieves the IUniswapV2Factory and IUniswapV2Router01 ABIs from unpkg CDN.
    These generic ABIs can be used as fallbacks when specific DEX ABIs are unavailable.

    Returns:
        Tuple containing:
            - uniswapFactory: The IUniswapV2Factory ABI as a list of dictionaries
            - uniswapRouter: The IUniswapV2Router01 ABI as a list of dictionaries

    Raises:
        urllib.error.URLError: If unable to connect to unpkg CDN
        json.JSONDecodeError: If response is not valid JSON
    """
    uniswapFactoryURL = "https://unpkg.com/@uniswap/v2-core@1.0.0/build/IUniswapV2Factory.json"
    uniswapRouterURL = "https://unpkg.com/@uniswap/v2-periphery@1.0.0-beta.0/build/IUniswapV2Router01.json"

    with urllib.request.urlopen(uniswapFactoryURL, timeout=30) as url:
        uniswapFactory = json.load(url)["abi"]

    with urllib.request.urlopen(uniswapRouterURL, timeout=30) as url:
        uniswapRouter = json.load(url)["abi"]

    return uniswapFactory, uniswapRouter


async def getAbi(
    clientSession: aiohttp.ClientSession,
    dbConnection: Any,
    rateLimiter: RateLimiter,
    networkName: str,
    dexDbId: int,
    dexName: str,
    contractType: str,
    apiUrl: str
) -> Optional[Dict[str, Any]]:
    """
    Fetch and store a contract ABI from a block explorer API.

    Queries the block explorer API for contract source code and ABI,
    validates the response, and uploads the ABI to S3 if valid.

    Args:
        clientSession: The aiohttp client session for making HTTP requests
        dbConnection: Active database connection for updating DEX records
        rateLimiter: Rate limiter instance to throttle API requests
        networkName: Name of the blockchain network (e.g., 'ethereum', 'polygon')
        dexDbId: Database ID of the DEX
        dexName: Human-readable name of the DEX
        contractType: Type of contract ('factory' or 'router')
        apiUrl: Full URL for the block explorer API request

    Returns:
        Dictionary containing network, DEX, contract type, and ABI data
        if successful, None otherwise
    """
    async with rateLimiter.throttle():
        apiResponse = await clientSession.get(apiUrl)

    apiResponseJSON = await apiResponse.json()

    result = apiResponseJSON["result"][0]

    contractValidated = "ContractName" in result and "ABI" in result

    try:
        json.loads(result["ABI"])
    except (json.JSONDecodeError, KeyError):
        contractValidated = False

    if int(apiResponseJSON["status"]) == 1 and contractValidated:

        if contractValidated:

            abi = json.loads(result["ABI"])
            contractName = result["ContractName"]
            matchingContractType = contractType in contractName.lower()

            validAbi = "stateMutability" in abi[-1]

            if validAbi:

                if matchingContractType:
                    logger.info(f"[ABI_FETCH] Success: {networkName.title()} | {dexName.title()} | {contractName} | Type: {contractType.title()}")
                else:
                    logger.warning(f"[ABI_FETCH] Type mismatch: {networkName.title()} | {dexName.title()} | {contractName} | Expected: {contractType.title()}")

                result = {
                    "networkName": networkName,
                    "dexName": dexName,
                    "contractType": contractType,
                    "contractAbi": abi
                }

                s3Path = f"{networkName}/{dexName}/{contractType}.json"

                fileUploaded = writeJSONToS3(
                    jsonData=abi,
                    s3Path=s3Path
                )

                if fileUploaded:
                    logger.debug(f"[S3_UPLOAD] Uploaded ABI to {s3Path}")
                    updateDexFactoryS3Path(
                        dbConnection=dbConnection,
                        dexDbId=dexDbId,
                        contractType=contractType,
                        s3Path=s3Path
                    )

            else:
                logger.warning(f"[ABI_VALIDATION] Invalid ABI structure: {networkName.title()} | {dexName.title()} | {contractType.title()}")
                result = None

        else:

            logger.error(f"[CONTRACT_VERIFY] Not verified: {networkName.title()} | {dexName.title()} | {contractType.title()}")
            result = None

    else:

        errorMessage = apiResponseJSON['result']

        if not errorMessage:
            errorMessage = apiResponseJSON["message"]

            if not errorMessage:
                errorMessage = "Unknown error from block explorer API"

        logger.error(f"[API_ERROR] {networkName.title()} | {dexName.title()} | {contractType.title()} | Error: {errorMessage}")
        result = None

    apiResponse.release()
    return result


async def collectAbis() -> None:
    """
    Main entry point for collecting contract ABIs from block explorers.

    Iterates through all networks and their DEXes, fetching and storing
    contract ABIs (factory and router) from block explorer APIs to S3.

    The function performs the following steps:
        1. Initializes database connection and retrieves all networks
        2. Filters networks to those with valid block explorer APIs
        3. For each network, retrieves all DEXes with factory/router addresses
        4. Queues async tasks to fetch ABIs for each contract
        5. Executes all tasks concurrently with rate limiting

    Environment Variables:
        S3_BUCKET: Target S3 bucket for storing ABIs
        S3_OVERWRITE: Whether to overwrite existing ABIs (true/false)
    """
    logger.info("[ABI_COLLECTOR] Starting ABI collection process")
    dbConnection = initDBConnection()

    networks = getAllNetworks(dbConnection=dbConnection)

    validNetworks = [
        network for network in networks
        if (network["explorer_type"] == "scan" or network["explorer_type"] == "blockscout")
        and network["explorer_api_prefix"]
    ]
    logger.info(f"[ABI_COLLECTOR] Found {len(validNetworks)} networks with valid block explorers")

    s3Bucket = os.getenv("S3_BUCKET")
    s3Overwrite = strToBool(os.getenv("S3_OVERWRITE"))

    async with RateLimiter(rate_limit=3, concurrency_limit=1000) as rate_limiter:

        async with aiohttp.ClientSession() as session:

            tasks: List[asyncio.Task] = []
            for network in validNetworks:

                networkName = network["name"]

                dexs = getAllDexsForNetwork(
                    dbConnection=dbConnection,
                    networkDbId=network["network_id"]
                )

                dexsWithAddresses = [dex for dex in dexs if dex["factory"] and dex["router"]]
                logger.debug(f"[NETWORK] {networkName}: Found {len(dexsWithAddresses)} DEXes with complete addresses")

                uploadedAbis = getCurrentStoredABIs(
                    networkName=networkName
                )

                for dex in dexsWithAddresses:

                    dexName = dex["name"]
                    dexDbId = dex["dex_id"]

                    contractAbisToGet = ["factory", "router"]

                    for contract in contractAbisToGet:

                        predictedS3Key = f"{networkName}/{dexName}/{contract}.json"

                        alreadyUploaded = predictedS3Key in uploadedAbis

                        if alreadyUploaded or s3Overwrite:

                            apiEndpoint = network["explorer_api_prefix"]
                            apiToken = network["explorer_api_key"]
                            contractAddress = dex[contract]
                            normalisedContractAddress = ''.join(e for e in contractAddress if e.isalnum())

                            apiUrl = f"{apiEndpoint}/api?module=contract&action=getsourcecode&address={normalisedContractAddress}"

                            if apiToken:
                                apiUrl = f"{apiUrl}&apikey={apiToken}"

                            tasks.append(
                                asyncio.ensure_future(getAbi(
                                    clientSession=session,
                                    dbConnection=dbConnection,
                                    rateLimiter=rate_limiter,
                                    networkName=networkName,
                                    dexName=dexName,
                                    dexDbId=dexDbId,
                                    apiUrl=apiUrl,
                                    contractType=contract
                                ))
                            )

                        else:

                            logger.debug(f"[SKIP] File already exists: {predictedS3Key} in bucket {s3Bucket}")

            logger.info(f"[ABI_COLLECTOR] Queued {len(tasks)} ABI fetch tasks")
            await asyncio.gather(*tasks)

            logger.info("[ABI_COLLECTOR] ABI collection completed successfully")
