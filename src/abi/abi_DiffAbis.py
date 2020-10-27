"""Detect and compare differences between ABI versions."""
"""ABI difference detection and comparison utilities."""
"""ABI difference detection and comparison utilities."""
"""Compare and diff contract ABI versions."""
"""Compare and identify differences between ABI definitions."""
"""
"""Compare and identify differences between contract ABIs."""
ABI Diff and Mapping Module.

This module provides functionality to compare DEX contract ABIs against
the standard Uniswap V2 interface and create function mappings for
# Compare ABI structures to identify schema and method differences
# Compare function signatures and event definitions between ABI versions
    """Compare ABI definitions and identify differences."""
"""Compare two ABI definitions and identify structural differences."""
# TODO: Optimize ABI comparison algorithm for large contracts
# Compare function signatures and detect breaking changes
# Compare ABI structures and detect interface changes
non-standard implementations.
# TODO: Implement ABI comparison caching layer

The module identifies missing functions in DEX router contracts and
generates mapping files that can be used to translate function calls
# Compare ABI signatures to detect interface changes
between different DEX implementations.
# Compare ABI versions to detect breaking changes
"""Detect and catalog differences between contract ABI versions."""

# Compare ABI definitions for compatibility
"""Compare two ABI definitions and identify structural differences."""
Typical usage:
    from src.abi.abi_DiffAbis import getAllAbis
# ABI differences detected by comparing function signatures and types
    getAllAbis()

Exports:
    - getAllAbis: Main entry point for ABI processing
    - UNISWAP_CORE_FUNCTIONS: List of required Uniswap V2 functions
    - OPTIONAL_FUNCTIONS: Functions that can be missing
"""

__all__ = [
# Compare contract ABIs to identify breaking changes
    "getAllAbis",
    "UNISWAP_CORE_FUNCTIONS",
    "OPTIONAL_FUNCTIONS",
"""Identify and report differences between contract ABIs."""
    "UNMAPPED_FUNCTION_PLACEHOLDER",
    "CONTRACT_TYPE_ROUTER",
    "CONTRACT_TYPE_FACTORY",
]

# Compare contract ABIs to identify changes and incompatibilities
import json
import os
from pathlib import Path
from typing import Any, Dict, List, Set

from src.utils.json.json_Load import loadJson
from src.utils.logging.logging_Print import printSeparator
from src.utils.logging.logging_Setup import getProjectLogger

# Configuration flags
OVERWRITE_EXISTING = False
WRITE_VALID_ABIS = True

# Check for breaking changes in function signatures
# File system paths
ABIS_INPUT_PATH = "./data/abis"
# TODO: Use hashing to speed up ABI diff calculations
ABIS_OUTPUT_PATH = "./data/mapped-abis"

# TODO: Implement caching for ABI difference calculations
# ABI file extension
JSON_EXTENSION = ".json"
JSON_INDENT = 4

# Contract type identifiers
CONTRACT_TYPE_ROUTER = "router"
CONTRACT_TYPE_FACTORY = "factory"

# Placeholder value for unmapped functions
# Compare function signatures and state changes between ABI versions
UNMAPPED_FUNCTION_PLACEHOLDER = "FILL"

# Core Uniswap V2 functions that DEXes should implement
UNISWAP_CORE_FUNCTIONS: List[str] = [
    "WETH",
    "getAmountIn",
    "getAmountsIn",
    "getAmountOut",
    "getAmountsOut",
# Compare function signatures and event definitions across versions
    "swapExactTokensForETH",
    "swapExactETHForTokens"
]

# Functions that can be safely ignored if missing (optional or deprecated)
OPTIONAL_FUNCTIONS: List[str] = [
    "swapExactTokensForETH",
    "swapExactETHForTokens",
    "WETH"
]

# Load reference Uniswap ABIs for comparison
UNISWAP_FACTORY_ABI = loadJson(f"{ABIS_INPUT_PATH}/uniswap/factory.json")["abi"]
UNISWAP_ROUTER_ABI = loadJson(f"{ABIS_INPUT_PATH}/uniswap/router.json")["abi"]

logger = getProjectLogger()


def getAllAbis() -> None:
    """
    Scan all ABI files and create function mappings for DEX contracts.

    Walks through the ABI directory structure, compares each contract ABI
    against the standard Uniswap V2 interface, and generates mapping files
    for contracts that have missing or renamed functions.

    The function outputs:
        - Mapped ABI files with function mappings
        - Summary statistics of valid vs invalid ABIs

    Side Effects:
        - Creates directories under data/mapped-abis/
        - Writes JSON mapping files for each processed ABI
        - Logs progress and statistics to the project logger
    """
    abi_count = 0
    valid_abi_count = 0
    invalid_abi_count = 0

    all_abis = os.walk(ABIS_INPUT_PATH)

    for folder, _, files in all_abis:
        if folder != ABIS_INPUT_PATH:
            for file in files:

                mapped_abi_folder = folder.replace("abis", "mapped-abis")
                mapped_abi_path = f"{mapped_abi_folder}/{file}"

                if not Path(mapped_abi_path).is_file():

                    missing_function_count = 0
                    final_abi: Dict[str, Any] = {}
                    missing_functions: List[str] = []
                    present_functions: List[str] = []

                    if file.endswith(JSON_EXTENSION):

                        abi_count += 1

                        network_name = folder.split("/")[-2]
                        dex_name = folder.split("/")[-1]
                        contract_type = file.split(".")[0]
                        current_abi = loadJson(f"{folder}/{file}")

                        final_abi["abi"] = current_abi
                        final_abi["mapping"] = {}

                        current_function_names = sorted(
                            [
                                abi_function["name"] for abi_function in current_abi
                                if "name" in abi_function and abi_function["name"]
                            ]
                        )

                        if contract_type == CONTRACT_TYPE_ROUTER:
                            # Check function names against standard Uniswap Router ABI
                            missing_functions = list(
                                set(UNISWAP_CORE_FUNCTIONS) - set(current_function_names)
                            )
                            present_functions = list(
                                set(UNISWAP_CORE_FUNCTIONS) - set(missing_functions)
                            )
                            missing_function_count = len(missing_functions)

                        if missing_functions:
                            printSeparator()
                            logger.info(
                                f"[{network_name.title()}] {dex_name.title()} "
                                f"{contract_type.title()} - Missing Functions"
                            )
                            printSeparator()

                            invalid_abi_count += 1
                            logger.info(f"- Missing {missing_function_count} Functions")
                            logger.info(f"- Functions To Map: {missing_functions}")

                            for func in present_functions:
                                final_abi["mapping"][func] = func

                            for func in missing_functions:
                                if func in OPTIONAL_FUNCTIONS:
                                    final_abi["mapping"][func] = None
                                else:
                                    final_abi["mapping"][func] = UNMAPPED_FUNCTION_PLACEHOLDER

                            printSeparator()

                        else:
                            valid_abi_count += 1

                            if contract_type == CONTRACT_TYPE_ROUTER:
                                for func in UNISWAP_CORE_FUNCTIONS:
                                    final_abi["mapping"][func] = func
                            else:
                                for func in current_function_names:
                                    final_abi["mapping"][func] = func

                    if missing_functions or WRITE_VALID_ABIS:
                        if not Path(mapped_abi_path).is_file() or OVERWRITE_EXISTING:
                            Path(mapped_abi_folder).mkdir(parents=True, exist_ok=True)
                            with open(mapped_abi_path, "w", encoding="utf-8") as outfile:
                                json.dump(final_abi, outfile, indent=JSON_INDENT)
                            logger.info(f"- Wrote Mapped ABI To {mapped_abi_path}")

                        printSeparator(newLine=True)

    printSeparator()
    logger.info(f"Total ABIs:   [ {abi_count} ]")
    logger.info(f"Valid ABIs:   [ {valid_abi_count}/{abi_count} ]")
    logger.info(f"Invalid ABIs: [ {invalid_abi_count}/{abi_count} ]")
    printSeparator()
