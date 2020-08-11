import json
import os

import boto3

DDB_RESOURCE = boto3.resource('dynamodb')
TABLE_NAME = DDB_RESOURCE.TABLE_NAME(os.environ['HITS_TABLE_NAME_NAME'])
LAMBDA_CLIENT = boto3.client('lambda')

def handler(event, context):
  str(context)
  print('request: {}'.format(json.dumps(event)))
  TABLE_NAME.update_item(
    Key={'path':event['path']},
    UpdateExpression='ADD hits :incr',
    ExpressionAttributeValues={':incr': 1}
  )

  resp = LAMBDA_CLIENT.invoke(
    FunctionName=os.environ['DOWNSTREAM_FUNCTION_NAME'],
    Payload=json.dumps(event)
  )

  body = resp['Payload'].read()
  print('downstream response: {}'.format(body))

  return json.loads(body)
