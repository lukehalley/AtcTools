import json, boto3
import os

from botocore.errorfactory import ClientError

from src.utils.logging.logging_Setup import getProjectLogger

logger = getProjectLogger()

def prepareJsonForS3(data):
    return json.dumps(data, indent=4)

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

    fileExists = checkIfPathExistsInS3(
        bucketName=s3Bucket,
        s3Path=s3Path
    )

    if not fileExists:
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
    else:
        logger.info(f"File {s3Path} already exists in {s3Bucket}\n")

    return fileUploaded

def getCurrentStoredABIs(networkName):

    s3 = boto3.resource('s3')
    s3Bucket = s3.Bucket(os.getenv("S3_BUCKET"))

    filteredObjects = s3Bucket.objects.filter(Prefix=f'{networkName}/')
    return [s3object.key for s3object in filteredObjects if s3object.size]


