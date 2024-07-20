#!/usr/bin/env python3
import json
import boto3
from botocore.exceptions import ClientError
import logging
from os import environ
from http.client import responses
import traceback

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(environ['LOGLEVEL'] if 'LOGLEVEL' in environ.keys() else 'INFO')

if 'BOTOCORE_LOGLEVEL' in environ.keys():
    if environ['BOTOCORE_LOGLEVEL'] == 'DEBUG':
        logger.info('Setting boto3 logging to DEBUG')
        boto3.set_stream_logger('') # Log everything on boto3 messages to stdout
    else:
        logger.info('Setting boto3 logging to ' + environ['BOTOCORE_LOGLEVEL'])
        boto3.set_stream_logger(level=logging._nameToLevel[environ['BOTOCORE_LOGLEVEL']]) # Log boto3 messages that match BOTOCORE_LOGLEVEL to stdout

def lambda_handler(event, context):

    logger.info('Hello from EBS Detach!')

    logger.debug('Event - ' + str(event))
    logger.debug('Context - ' + str(context))

    body = {
        "message": "Hello from EBS Detach!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
