#!/usr/bin/env python3

import aws_cdk as cdk

from sklearn_app.sklearn_app_stack import SklearnAppStack


app = cdk.App()
SklearnAppStack(app, "sklearn-app-cdk")

app.synth()
