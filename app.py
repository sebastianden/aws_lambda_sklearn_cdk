#!/usr/bin/env python3

import aws_cdk as cdk

from aws_lambda_sklearn_cdk.aws_lambda_sklearn_cdk_stack import AwsLambdaSklearnCdkStack


app = cdk.App()
AwsLambdaSklearnCdkStack(app, "aws-lambda-sklearn-cdk")

app.synth()
