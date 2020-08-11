#!/usr/bin/env python3

import os

from aws_cdk import core

from cdk_workshop.cdk_workshop_stack import CdkWorkshopStack


APP = core.App()
CdkWorkshopStack(APP, str("cdk-workshop-" + os.environ["STAGE"]), env={'region': 'eu-west-1'})

APP.synth()
