# CDK Python workshop

You should explore the contents of this project. It demonstrates a CDK app with an instance of a stack (`cdk_workshop_stack`)
which contains an Amazon SQS queue that is subscribed to an Amazon SNS topic.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project. The initialization process also creates
a virtualenv within this project, stored under the .env directory. To create the virtualenv
it assumes that there is a `python3` executable in your path with access to the `venv` package.
If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv
manually once the init process completes.

To manually create a virtualenv on MacOS and Linux:

```bash
python3 -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```bash
source .env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```bash
.env\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```bash
pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code. I have added a bash script to wrap the cdk command and add a stage parameter to the stack. So the command line sintax will be like this: `./cdk.sh <command> <stage>`. If stage is not specified, the `dev` stage is used by default.

```bash
./cdk.sh synth
```

You can now begin exploring the source code, contained in the hello directory.
There is also a very trivial test included that can be run like this:

```bash
pytest
```

To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

* `./cdk.sh ls`     list all stacks in the app
* `./cdk.sh synth`    emits the synthesized CloudFormation template
* `./cdk.sh deploy`   deploy this stack to your default AWS account/region
* `./cdk.sh diff`    compare deployed stack with current state
* `./cdk.sh docs`    open CDK documentation

Enjoy!

## References

* [https://cdkworkshop.com](https://cdkworkshop.com)
