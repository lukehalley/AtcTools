"""
Environment Detection Module.

This module provides utility functions for detecting the runtime environment,
such as Docker containers, AWS, and headless mode.
"""

import os
from typing import Optional

from src.utils.data.data_Booleans import strToBool

# Environment variable names
ENV_RUNNING_IN_DOCKER = "RUNNING_IN_DOCKER"
ENV_AWS_DEFAULT_REGION = "AWS_DEFAULT_REGION"
ENV_FORCE_HEADLESS = "FORCE_HEADLESS"


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