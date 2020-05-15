from aws_cdk import core
from aws_cdk.aws_dynamodb import Table, Attribute, AttributeType
from aws_cdk.aws_lambda import Function, Runtime, Code


class BookshelfBackendStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        dyn_books = Table(self, 'dyn_books',
                          table_name="books",
                          partition_key=Attribute(
                              name="isbn",
                              type=AttributeType.STRING))

        dyn_users = Table(self, 'dyn_users',
                          table_name="users",
                          partition_key=Attribute(
                              name="user_id",
                              type=AttributeType.STRING))

        lba_graphql = Function(self, "lba_graphql",
                               function_name="graphql",
                               code=Code.asset("./source_code/lba_graphql"),
                               handler="lba_graphql.lambda_handler",
                               runtime=Runtime.PYTHON_3_7)

        dyn_books.grant_full_access(lba_graphql)
        dyn_users.grant_full_access(lba_graphql)
