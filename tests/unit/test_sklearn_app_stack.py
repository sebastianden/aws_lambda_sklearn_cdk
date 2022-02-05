import aws_cdk as core
import aws_cdk.assertions as assertions
from sklearn_app.sklearn_app_stack import SklearnAppStack


def test_lambda_layer_created():
    app = core.App()
    stack = SklearnAppStack(app, "sklearn-app-cdk")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::Lambda::LayerVersion", 1)


def test_lambda_function_created():
    app = core.App()
    stack = SklearnAppStack(app, "sklearn-app-cdk")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::Lambda::Function", 1)


def test_api_gateway_created():
    app = core.App()
    stack = SklearnAppStack(app, "sklearn-app-cdk")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::ApiGateway::RestApi", 1)
