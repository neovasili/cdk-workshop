import json
import pytest

from aws_cdk import core
from cdk_workshop.cdk_workshop_stack import CdkWorkshopStack

@pytest.fixture(scope = 'module')
def global_data():
  app = core.App()
  CdkWorkshopStack(app, "cdk-workshop-dev")
  return {'template': json.dumps(app.synth().get_stack("cdk-workshop-dev").template)}

def test_lambda_restapi_created(global_data):
  assert "AWS::ApiGateway::RestApi" in global_data["template"]

def test_lambda_function_created(global_data):
  assert "AWS::Lambda::Function" in global_data["template"]

def test_dynamodb_table_created(global_data):
  assert "AWS::DynamoDB::Table" in global_data["template"]
