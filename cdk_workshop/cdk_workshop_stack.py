from aws_cdk import (
  aws_lambda as _lambda,
  core
)


class CdkWorkshopStack(core.Stack):

  def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
    super().__init__(scope, id, **kwargs)

    hello_lambda = _lambda.Function(
      self,
      'HelloHandler',
      runtime = _lambda.Runtime.PYTHON_3_8,
      code = _lambda.Code.asset('lambda'),
      handler = 'hello.handler'
    )
