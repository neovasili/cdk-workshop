import json

def handler(event, context):
  print('request: {}'.format(json.dumps(event)))
  return {
    'statusCode': 200,
    'headers': {
      'Content-Type': 'application/json'
    },
    'body': json.dumps({"message": "Hello, CDK! You have hit {}".format(event['path'])})
  }
