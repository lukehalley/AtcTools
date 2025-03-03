"""
AWS Secrets Manager Utility.

This module provides utility functions for retrieving credentials
stored in AWS Secrets Manager via environment variables.
"""

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