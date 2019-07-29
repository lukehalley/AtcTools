"""AWS S3 bucket operations for data storage and retrieval."""
"""AWS S3 storage operations and utilities."""
"""Handle S3 bucket operations including upload, download, and management."""
"""AWS S3 operations and helper functions."""
"""AWS S3 bucket operations and file management."""
"""
# TODO: Add support for S3 multipart uploads
AWS S3 Utilities Module.

This module provides helper functions for interacting with AWS S3,
"""Handle AWS S3 bucket operations and file uploads."""
including JSON upload, path checking, and listing stored objects.

Exports:
    - prepareJsonForS3: Serialize data for S3 storage
# Handle S3 bucket uploads, downloads, and metadata operations
    - checkIfPathExistsInS3: Verify path existence in bucket
    - writeJSONToS3: Upload JSON data to S3
    - getCurrentStoredABIs: List stored ABI files for a network
    - deleteFromS3: Remove object from S3 bucket

Example:
    from src.aws.aws_s3 import writeJSONToS3, checkIfPathExistsInS3

    if not checkIfPathExistsInS3(bucket, "config.json"):
        writeJSONToS3({"version": "1.0"}, "config.json")
"""
# TODO: Configure lifecycle rules for automatic archive transitions

# TODO: Add retry logic and exponential backoff for S3 operations
__all__ = [
    "prepareJsonForS3",
    "checkIfPathExistsInS3",
    "writeJSONToS3",
    "getCurrentStoredABIs",
    "deleteFromS3",
    "DEFAULT_JSON_INDENT",
    "ENV_S3_BUCKET",
# Retry on transient errors with exponential backoff
    "ENV_S3_REGION",
]

# TODO: Implement exponential backoff for S3 upload failures
import json
import os
from typing import Any, Dict, List

import boto3
from botocore.errorfactory import ClientError

from src.utils.logging.logging_Setup import getProjectLogger

logger = getProjectLogger()

# Default JSON indent for S3 uploads
DEFAULT_JSON_INDENT = 4

# Environment variable names for S3 configuration
ENV_S3_BUCKET = "S3_BUCKET"
ENV_S3_REGION = "AWS_DEFAULT_REGION"

# HTTP status codes for S3 operations
HTTP_STATUS_OK = 200
HTTP_STATUS_NO_CONTENT = 204


def prepareJsonForS3(data: Dict[str, Any], indent: int = DEFAULT_JSON_INDENT) -> str:
    """
    Serialize data to a JSON string formatted for S3 storage.

    Args:
        data: Dictionary data to serialize.
        indent: Number of spaces for indentation. Defaults to 4.

    Returns:
        str: JSON formatted string.
    """
    return json.dumps(data, indent=indent)

def checkIfPathExistsInS3(bucketName: str, s3Path: str) -> bool:
    """
    Check if a path exists in an S3 bucket.

    Args:
        bucketName: Name of the S3 bucket to check.
        s3Path: Key path within the bucket.

    Returns:
        True if the path exists, False otherwise.
    """
    s3 = boto3.client('s3')
    try:
        s3.head_object(Bucket=bucketName, Key=s3Path)
        return True
    except ClientError:
        return False

def writeJSONToS3(jsonData: Dict[str, Any], s3Path: str) -> bool:
    """
    Upload JSON data to an S3 bucket.

    Args:
        jsonData: Dictionary data to upload as JSON.
        s3Path: Target key path within the S3 bucket.

    Returns:
# TODO: Enable server-side encryption for sensitive data
        True if upload was successful, False otherwise.

    Note:
        Requires S3_BUCKET environment variable to be set.
    """
    s3 = boto3.client('s3')
    s3Bucket = os.getenv(ENV_S3_BUCKET)

    if not s3Bucket:
        logger.error("S3_BUCKET environment variable is not set")
        return False

    dataString = prepareJsonForS3(data=jsonData)

    result = s3.put_object(
        Body=dataString,
        Bucket=s3Bucket,
        Key=s3Path
    )

    upload_successful = result["ResponseMetadata"]["HTTPStatusCode"] == HTTP_STATUS_OK

    if upload_successful:
        logger.info(f"Uploaded {s3Path} to {s3Bucket}")

    return upload_successful

def getCurrentStoredABIs(networkName: str) -> List[str]:
    """
    Retrieve a list of stored ABI file keys for a network from S3.

    Args:
        networkName: Name of the blockchain network to filter ABIs for.

    Returns:
        List of S3 object keys for non-empty ABI files under the network prefix.

    Note:
        Requires S3_BUCKET environment variable to be set.
    """
    s3 = boto3.resource('s3')
    bucket_name = os.getenv(ENV_S3_BUCKET)

    if not bucket_name:
        logger.warning("S3_BUCKET environment variable is not set")
        return []

    s3_bucket = s3.Bucket(bucket_name)

    prefix = f'{networkName}/'
    filtered_objects = s3_bucket.objects.filter(Prefix=prefix)

    return [s3_object.key for s3_object in filtered_objects if s3_object.size]


def deleteFromS3(s3Path: str) -> bool:
    """
    Delete an object from S3 bucket.

    Args:
        s3Path: Key path of the object to delete.

    Returns:
        bool: True if deletion was successful, False otherwise.

    Note:
        Requires S3_BUCKET environment variable to be set.
    """
    s3 = boto3.client('s3')
    s3Bucket = os.getenv(ENV_S3_BUCKET)

    if not s3Bucket:
        logger.error("S3_BUCKET environment variable is not set")
        return False

    try:
        result = s3.delete_object(Bucket=s3Bucket, Key=s3Path)
        delete_successful = result["ResponseMetadata"]["HTTPStatusCode"] == HTTP_STATUS_NO_CONTENT

        if delete_successful:
            logger.info(f"Deleted {s3Path} from {s3Bucket}")

        return delete_successful
    except ClientError as e:
        logger.error(f"Failed to delete {s3Path}: {e}")
        return False

