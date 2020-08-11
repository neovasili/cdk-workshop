#!/usr/bin/env python3

import os

from aws_cdk import core

from cdk_workshop.cdk_workshop_stack import CdkWorkshopStack


app = core.App()
CdkWorkshopStack(app, str("cdk-workshop-" + os.environ["STAGE"]), env={'region': 'eu-west-1'})

app.synth()
