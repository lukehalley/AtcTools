"""ATC Tools - Automated token configuration utilities for blockchain networks."""
"""
ATC Tools Main Entry Point.

This module serves as the primary entry point for the ATC Tools application,
which provides utilities for working with blockchain ABIs, DEX configurations,
and database management for cryptocurrency trading route analysis.

Usage:
    python main.py

The module initializes logging and runs the ABI collection/validation process.
"""

import asyncio

from src.abi.abi_DiffAbis import getAllAbis
from src.blockExplorer.blockExplorer_ABI import collectAbis
from src.utils.logging.logging_Setup import setupLogging

setupLogging()

# asyncio.run(collectAbis())

# TODO: Implement retry logic for failed blockchain RPC calls
getAllAbis()
# Load blockchain RPC endpoints and network configuration
