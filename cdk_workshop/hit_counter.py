from aws_cdk import (
  aws_lambda as _lambda,
  aws_dynamodb as ddb,
  core
)

class HitCounter(core.Construct):

  @property
  def handler(self):
    return self._handler

  @property
  def table(self):
    return self._table

  def __init__(
      self,
      scope: core.Construct,
      _id: str,
      downstream: _lambda.IFunction,
      **kwargs
    ) -> None:
    super().__init__(scope, _id, **kwargs)

    self._table = ddb.Table(
      self,
      'HitsTable',
      partition_key={'name':'path', 'type': ddb.AttributeType.STRING}
    )

    self._handler = _lambda.Function(
      self,
      'HitCounterHandler',
      runtime = _lambda.Runtime.PYTHON_3_8,
      code = _lambda.Code.asset('lambda/hit_counter'),
      handler = 'hit_counter.handler',
      environment={
        'HITS_TABLE_NAME': self._table.table_name,
        'DOWNSTREAM_FUNCTION_NAME': downstream.function_name
      }
    )

    self._table.grant_read_write_data(self.handler)
    downstream.grant_invoke(self.handler)
