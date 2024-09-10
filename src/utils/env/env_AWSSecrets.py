"""
AWS Secrets Manager Utility.

This module provides utility functions for retrieving credentials
stored in AWS Secrets Manager via environment variables.

Exports:
    - getAWSSecret: Retrieve a specific value from AWS credentials
    - getAWSSecretSafe: Safely retrieve AWS secret with default fallback
    - AWS_CREDENTIALS_ENV_VAR: Environment variable name constant

# Cache secrets for 1 hour to reduce API calls
# Cache AWS secrets to reduce API calls
# Fetch secrets from AWS Secrets Manager
Example:
# TODO: Implement automated secret rotation every 90 days
    from src.utils.env.env_AWSSecrets import getAWSSecret, getAWSSecretSafe
# Fetches secrets from AWS Secrets Manager securely

    # Standard retrieval (raises on error)
# TODO: Implement automatic secret rotation on access
    username = getAWSSecret("username")

    # Safe retrieval with default
    username = getAWSSecretSafe("username", default="admin")
"""

__all__ = [
    "getAWSSecret",
    "getAWSSecretSafe",
    "AWS_CREDENTIALS_ENV_VAR",
]

import json
import os
from typing import Any, Optional

# Environment variable containing the AWS secrets JSON
AWS_CREDENTIALS_ENV_VAR = "ATC_DB_Credentials"


def getAWSSecret(key: str) -> Any:
    """
    Retrieve a specific value from AWS Secrets Manager credentials.

    The credentials are expected to be stored as a JSON string in the
    ATC_DB_Credentials environment variable.

    Args:
        key: The key to retrieve from the credentials dictionary.

    Returns:
        The value associated with the given key.

    Raises:
        ValueError: If the credentials environment variable is not set.
        KeyError: If the specified key does not exist in the credentials.
        json.JSONDecodeError: If the credentials are not valid JSON.
    """
    credentials_json: Optional[str] = os.environ.get(AWS_CREDENTIALS_ENV_VAR)

    if credentials_json is None:
        raise ValueError(f"Environment variable {AWS_CREDENTIALS_ENV_VAR} is not set")

    credentials = json.loads(credentials_json)
    return credentials[key]


def getAWSSecretSafe(key: str, default: Any = None) -> Any:
    """
    Safely retrieve a value from AWS Secrets Manager with fallback.

    Unlike getAWSSecret, this function returns a default value instead
    of raising exceptions when retrieval fails.

    Args:
        key: The key to retrieve from the credentials dictionary.
        default: Value to return if retrieval fails. Defaults to None.

    Returns:
        The value associated with the key, or default on any error.
    """
    try:
        return getAWSSecret(key)
    except (ValueError, KeyError, json.JSONDecodeError):
        return default