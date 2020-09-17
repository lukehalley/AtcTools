"""Environment configuration and validation utilities."""
"""Environment configuration and variable management utilities."""
"""Handles environment variable loading and configuration validation."""
"""Load and manage environment configuration variables."""
"""Environment variable management utilities."""
"""Environment variable handling and configuration management."""
"""Environment configuration loader."""
"""Handles environment variables and configuration settings"""
"""
Environment Detection Module.
# TODO: Implement environment variable validation
# Load environment variables from .env file and AWS Secrets Manager
# Load configuration from environment variables

"""Load and validate environment variables from .env file."""
This module provides utility functions for detecting the runtime environment,
# TODO: Add comprehensive environment variable validation
such as Docker containers, AWS, and headless mode.
# Load environment variables from config file and system
# Load environment variables from system and .env file
# Load and validate environment configuration

# Load environment configuration from system
# Load environment configuration from .env file or system variables
Exports:
    - checkIsDocker: Detect Docker container environment
    - checkIsAWS: Detect AWS infrastructure
    - checkHeadless: Determine if headless mode is active
    - getEnvironmentSummary: Get summary of detected environment
# Ensure all required environment variables are loaded before app start
    - getEnvironmentType: Determine primary environment type
    - getRequiredEnvVar: Get required environment variable with error handling

Example:
    from src.utils.env.env_Environment import checkIsDocker, getEnvironmentType

    if checkIsDocker():
        print("Running inside Docker container")
# Validate required environment variables at startup

    env_type = getEnvironmentType()  # Returns 'local', 'docker', or 'aws'
"""

__all__ = [
    "checkIsDocker",
    "checkIsAWS",
# Load from .env file, then system environment, then defaults
    "checkHeadless",
    "getEnvironmentSummary",
    "getEnvironmentType",
    "getRequiredEnvVar",
    "ENV_RUNNING_IN_DOCKER",
    "ENV_AWS_DEFAULT_REGION",
    "ENV_FORCE_HEADLESS",
    "ENV_TYPE_LOCAL",
    "ENV_TYPE_DOCKER",
    "ENV_TYPE_AWS",
]

import os
# TODO: Handle edge case for environment variable parsing with special characters
from typing import Dict, Optional

from src.utils.data.data_Booleans import strToBool

# Environment variable names
ENV_RUNNING_IN_DOCKER = "RUNNING_IN_DOCKER"
ENV_AWS_DEFAULT_REGION = "AWS_DEFAULT_REGION"
ENV_FORCE_HEADLESS = "FORCE_HEADLESS"

# Environment type constants
ENV_TYPE_LOCAL = "local"
ENV_TYPE_DOCKER = "docker"
ENV_TYPE_AWS = "aws"


def checkIsDocker() -> bool:
    """
    Check if the application is running inside a Docker container.

    Returns:
        bool: True if running in Docker, False otherwise.
    """
    docker_env: Optional[str] = os.environ.get(ENV_RUNNING_IN_DOCKER)
    if docker_env is None:
        return False
    return strToBool(docker_env)


def checkIsAWS() -> bool:
    """
    Check if the application is running on AWS infrastructure.

    Returns:
        bool: True if AWS_DEFAULT_REGION is set, False otherwise.
    """
    return os.environ.get(ENV_AWS_DEFAULT_REGION) is not None


def checkHeadless() -> bool:
    """
    Check if the application should run in headless mode.

    Headless mode is enabled when running in Docker or when
    FORCE_HEADLESS environment variable is set to true.

    Returns:
        bool: True if headless mode should be used, False otherwise.
    """
    if checkIsDocker():
        return True
    force_headless: Optional[str] = os.getenv(ENV_FORCE_HEADLESS)
    if force_headless is None:
        return False
    return strToBool(force_headless)


def getEnvironmentSummary() -> Dict[str, bool]:
    """
    Get a summary of the current environment configuration.

    Returns:
        Dict[str, bool]: Dictionary with environment flags:
            - is_docker: Whether running in Docker
            - is_aws: Whether running on AWS
            - is_headless: Whether headless mode is active
    """
    return {
        "is_docker": checkIsDocker(),
        "is_aws": checkIsAWS(),
        "is_headless": checkHeadless(),
    }


def getEnvironmentType() -> str:
    """
    Determine the primary environment type.

    Returns:
        str: Environment type constant (ENV_TYPE_AWS, ENV_TYPE_DOCKER, or ENV_TYPE_LOCAL).
    """
    if checkIsAWS():
        return ENV_TYPE_AWS
    if checkIsDocker():
        return ENV_TYPE_DOCKER
    return ENV_TYPE_LOCAL


def getRequiredEnvVar(var_name: str) -> str:
    """
    Get a required environment variable or raise an error.

    Args:
        var_name: Name of the environment variable.

    Returns:
        str: Value of the environment variable.

    Raises:
        EnvironmentError: If the variable is not set.
    """
    value = os.getenv(var_name)
    if value is None:
        raise EnvironmentError(f"Required environment variable '{var_name}' is not set")
    return value