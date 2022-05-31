import json, boto3
import os

from botocore.errorfactory import ClientError

from src.utils.logging.logging_Setup import getProjectLogger

logger = getProjectLogger()

def prepareJsonForS3(data):
    dataString = ""
    for d in data:
        dataString += json.dumps(d, ensure_ascii=False)
        dataString += "\n"
    return dataString

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
    finalS3Path = f"{s3Path}.json"

    fileExists = checkIfPathExistsInS3(
        bucketName=s3Bucket,
        s3Path=finalS3Path
    )

    if not fileExists:
        dataString = prepareJsonForS3(
            data=jsonData
        )

        result = s3.put_object(
            Body=dataString,
            Bucket=s3Bucket,
            Key=finalS3Path
        )

        uploadSuccessfull = result["ResponseMetadata"]["HTTPStatusCode"] == 200

        if uploadSuccessfull:
            logger.info(f"Uploaded {finalS3Path} to {s3Bucket}\n")
    else:
        logger.info(f"File {finalS3Path} already exists in {s3Bucket}\n")

