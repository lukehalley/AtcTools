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

def checkIfPathExistsInS3(bucketName, s3Path):
    s3 = boto3.client('s3')
    exists = False
    try:
        s3.head_object(Bucket=bucketName, Key=s3Path)
        exists = True
    except ClientError:
        pass
    return exists

def writeJSONToS3(jsonData, s3Path):

    s3 = boto3.client('s3')
    s3Bucket = os.getenv("S3_BUCKET")
    fileUploaded = False

    dataString = prepareJsonForS3(
        data=jsonData
    )

    result = s3.put_object(
        Body=dataString,
        Bucket=s3Bucket,
        Key=s3Path
    )

    uploadSuccessfull = result["ResponseMetadata"]["HTTPStatusCode"] == 200

    if uploadSuccessfull:
        logger.info(f"Uploaded {s3Path} to {s3Bucket}\n")
        fileUploaded = True

    return fileUploaded

def getCurrentStoredABIs(networkName):

    s3 = boto3.resource('s3')
    s3Bucket = s3.Bucket(os.getenv("S3_BUCKET"))

    filteredObjects = s3Bucket.objects.filter(Prefix=f'{networkName}/')
    return [s3object.key for s3object in filteredObjects if s3object.size]


