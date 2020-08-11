from aws_cdk import (
  aws_lambda as _lambda,
  aws_apigateway as apigw,
  core
)

from cdk_dynamo_table_viewer import TableViewer
from hit_counter import HitCounter


class CdkWorkshopStack(core.Stack):

  def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
    super().__init__(scope, id, **kwargs)

    hello_lambda = _lambda.Function(
      self,
      'HelloHandler',
      runtime = _lambda.Runtime.PYTHON_3_8,
      code = _lambda.Code.asset('lambda/hello'),
      handler = 'hello.handler'
    )

    hello_with_counter = HitCounter(
      self,
      'HitCounter',
      downstream=hello_lambda
    )

    hello_apigw = apigw.LambdaRestApi(
      self,
      'HelloRestApi',
      handler = hello_with_counter.handler
    )

    table_viewer = TableViewer(
      self,
      'TableViewer',
      title='Hello hits',
      table=hello_with_counter.table,
      sort_by='-hits'
    )
