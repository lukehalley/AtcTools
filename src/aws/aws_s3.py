"""
AWS S3 Utilities Module.

This module provides helper functions for interacting with AWS S3,
including JSON upload, path checking, and listing stored objects.
"""

import json
import os
from typing import Any, Dict, List

import boto3
from botocore.errorfactory import ClientError

from src.utils.logging.logging_Setup import getProjectLogger

logger = getProjectLogger()

# Default JSON indent for S3 uploads
DEFAULT_JSON_INDENT = 4


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
        True if upload was successful, False otherwise.

    Note:
        Requires S3_BUCKET environment variable to be set.
    """
    s3 = boto3.client('s3')
    s3Bucket = os.getenv("S3_BUCKET")

    dataString = prepareJsonForS3(data=jsonData)

    result = s3.put_object(
        Body=dataString,
        Bucket=s3Bucket,
        Key=s3Path
    )

    upload_successful = result["ResponseMetadata"]["HTTPStatusCode"] == 200

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
    bucket_name = os.getenv("S3_BUCKET")
    s3_bucket = s3.Bucket(bucket_name)

    prefix = f'{networkName}/'
    filtered_objects = s3_bucket.objects.filter(Prefix=prefix)

    return [s3_object.key for s3_object in filtered_objects if s3_object.size]


