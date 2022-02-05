from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    aws_apigateway as apigw,
)


class SklearnAppStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        sklearn_layer = lambda_.LayerVersion(
            self,
            "SklearnLambdaLayerCdk",
            code=lambda_.Code.from_asset("./lambda/layers/SklearnLayer.zip"),
            compatible_runtimes=[lambda_.Runtime.PYTHON_3_8],
        )

        lambda_function = lambda_.Function(
            self,
            "SklearnLambdaCdk",
            runtime=lambda_.Runtime.PYTHON_3_8,
            code=lambda_.Code.from_asset("./lambda/code"),
            handler="lambda_function.lambda_handler",
            layers=[sklearn_layer],
        )

        apigw.LambdaRestApi(
            self,
            "ApiGatewayCdk",
            handler=lambda_function,
        )
