import json

from aws_cdk import core
from cdk_workshop.cdk_workshop_stack import CdkWorkshopStack

def get_template():
  app = core.App()
  CdkWorkshopStack(app, "cdk-workshop-dev")
  return json.dumps(app.synth().get_stack("cdk-workshop-dev").template)

def test_lambda_function_created():
  assert "AWS::Lambda::Function" in get_template()

def test_dynamodb_table_created():
  assert "AWS::DynamoDB::Table" in get_template()
