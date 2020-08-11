import setuptools


with open("README.md") as fp:
  LONG_DESCRIPTION = fp.read()


setuptools.setup(
  name="cdk_workshop",
  version="0.0.1",

  description="A sample CDK Python app",
  long_description=LONG_DESCRIPTION,
  long_description_content_type="text/markdown",

  author="Juan Manuel Ruiz Fernández",

  package_dir={"": "cdk_workshop"},
  packages=setuptools.find_packages(where="cdk_workshop"),

  install_requires=[
    "aws-cdk.core==1.57.0",
    "aws-cdk.aws_iam==1.57.0",
    "aws-cdk.aws_sqs==1.57.0",
    "aws-cdk.aws_sns==1.57.0",
    "aws-cdk.aws_sns_subscriptions==1.57.0",
    "aws-cdk.aws_s3==1.57.0",
    "aws-cdk.aws_lambda==1.57.0",
    "aws-cdk.aws_apigateway==1.57.0",
    "aws-cdk.aws_dynamodb==1.57.0",
    "cdk_dynamo_table_viewer==3.1.2",
  ],

  python_requires=">=3.6",

  classifiers=[
    "Development Status :: 4 - Beta",

    "Intended Audience :: Developers",

    "License :: OSI Approved :: Apache Software License",

    "Programming Language :: JavaScript",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",

    "Topic :: Software Development :: Code Generators",
    "Topic :: Utilities",

    "Typing :: Typed",
  ],
)
